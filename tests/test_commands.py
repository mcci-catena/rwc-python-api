##############################################################################
#
# Module: test_commands.py
#
# Description:
#     Offline tests: check the command strings that RWCTesterApi methods
#     send, with a stand-in for the transport. No tester needed:
#         python -m pytest tests/test_commands.py
#
# Copyright notice:
#     This file copyright (c) 2026 by
#
#         MCCI Corporation
#         3520 Krums Corners Road
#         Ithaca, NY  14850
#
#     See accompanying LICENSE file for copyright and license information.
#
##############################################################################

import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from rwclib.cRWC5020x import RWCTesterApi
from rwclib.cRWCSerialSetup import RwcSerialSetup


class FakeTester:
    '''Records each command; answers version queries and ACKs the rest.'''

    def __init__(self, version):
        self.version = version
        self.sent = []

    def transceive(self, api, cmd, sec = 0):
        if cmd == 'READ:SYSTEM:SW_VERSION?\n':
            return self.version
        self.sent.append(cmd)
        return 'ACK'


@pytest.fixture
def rwc(monkeypatch, request):
    fake = FakeTester(getattr(request, 'param', '1.500'))
    monkeypatch.setattr(RwcSerialSetup, 'transceive',
                        lambda api, cmd, sec = 0: fake.transceive(api, cmd, sec))
    api = RWCTesterApi('5001', '192.0.2.1')
    api.fake = fake
    return api


def sent(api):
    return api.fake.sent


def test_macsendresult(rwc):
    rwc.link_getmacsendresult(1)
    assert sent(rwc) == ['READ:LINK:MAC_SEND_RESULT? 1\n']


def test_nst_rx_polarity(rwc):
    rwc.nst_rx_settxpolarity('INVERSE')
    rwc.nst_rx_gettxpolarity()
    assert sent(rwc) == ['CONF:NST:RX:RX_POLARITY INVERSE\n',
                         'READ:NST:RX:RX_POLARITY?\n']


def test_nst_tx_getmode(rwc):
    rwc.nst_tx_getmode()
    assert sent(rwc) == ['READ:NST:TX:MODULATION?\n']


def test_adrchmask_opt(rwc):
    rwc.link_setadrchmask_optdr(0x01, 2)
    rwc.link_getadrchmask_optdr(2)
    rwc.link_getadrchmask_optdr()
    assert sent(rwc) == ['CONF:LINK:ADR_CH_MASK_OPT 2 0x1\n',
                         'READ:LINK:ADR_CH_MASK_OPT? 2\n',
                         'READ:LINK:ADR_CH_MASK_OPT? 1\n']


@pytest.mark.parametrize('rwc', ['1.160'], indirect = True)
def test_adrchmask_opt_old_firmware(rwc):
    rwc.link_setadrchmask_optdr(0x01)
    rwc.link_getadrchmask_optdr()
    assert sent(rwc) == ['CONF:LINK:ADR_CH_MASK_OPT_DR 0x1\n',
                         'READ:LINK:ADR_CH_MASK_OPT_DR?\n']


@pytest.mark.parametrize('call', [
    lambda r: r.protocol_setclaamode('D'),
    lambda r: r.protocol_getclaamode(),
    lambda r: r.link_setadr_morechannelmask('ON'),
    lambda r: r.link_getadr_morechannelmask(),
    lambda r: r.link_setadr_channelmask(2, 1, 0xFF),
    lambda r: r.link_getadr_channelmask(3, 1),
    lambda r: r.link_setadr_maskctrl(2, 1, 0),
    lambda r: r.link_getadr_maskctrl(3, 1),
    lambda r: r.link_setmulticastkey(1),
    ])
def test_deleted_commands_raise(rwc, call):
    with pytest.raises(Exception, match = 'not supported'):
        call(rwc)
    assert sent(rwc) == []


@pytest.mark.parametrize('rwc', ['1.310'], indirect = True)
def test_deleted_commands_on_old_firmware(rwc):
    rwc.protocol_getclaamode()
    rwc.link_getadr_channelmask(2, 1)
    rwc.link_setmulticastkey(1)
    assert sent(rwc) == ['READ:PROTOCOL:CLAA_MODE?\n',
                         'READ:LINK:ADR_CH_MASK2? 1\n',
                         'CONF:LINK:MC_KEY 0x1\n']


def test_adr_index1_unaffected(rwc):
    rwc.link_getadr_channelmask(1, 1)
    rwc.link_getadr_maskctrl(1, 1)
    assert sent(rwc) == ['READ:LINK:ADR_CH_MASK? 1\n',
                         'READ:LINK:ADR_MASK_CTRL? 1\n']


@pytest.mark.parametrize('rwc', ['NAK', None], indirect = True)
def test_version_unreadable(rwc):
    with pytest.raises(Exception, match = 'Cannot read tester firmware version'):
        rwc.protocol_getclaamode()
