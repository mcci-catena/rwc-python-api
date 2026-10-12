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


# step 2 of #18: parameters and ranges

@pytest.mark.parametrize('name, sent_name', [
    ('AU_915', 'AU_915'), ('AU_921', 'AU_915'), ('KR_922', 'KR_920'),
    ('IN_866', 'IN_865'), ('RU_864', 'RU_864')])
def test_region(rwc, name, sent_name):
    rwc.protocol_setregion(name)
    assert sent(rwc) == ['CONF:PROTOCOL:REGION ' + sent_name + '\n']


def test_operator(rwc):
    rwc.protocol_setoperator('ICA')
    assert sent(rwc) == ['CONF:PROTOCOL:OPERATOR ICA\n']


@pytest.mark.parametrize('call', [
    lambda r: r.protocol_setregion('XX_000'),
    lambda r: r.protocol_setoperator('TTN'),
    lambda r: r.sensitivity_settargetpower(0.6),
    lambda r: r.power_setminyvalue(-81),
    lambda r: r.power_setminyvalue(31),
    lambda r: r.rf_settxpower(1),
    lambda r: r.link_setfopts(bytes(16)),
    lambda r: r.sensitivity_setpayload(bytes(129)),
    lambda r: r.link_setpayload(bytes(251)),
    lambda r: r.power_getavgdutpower_ch(96),
    ])
def test_out_of_range(rwc, call):
    with pytest.raises(Exception):
        call(rwc)
    assert sent(rwc) == []


def test_ranges_accepted(rwc):
    rwc.sensitivity_settargetpower(0.5)
    rwc.power_setminyvalue(-80)
    rwc.link_setfragemntpadding(0)
    rwc.rf_settxpower(0)
    rwc.nst_mfg_setinterval(0.01)
    assert sent(rwc) == ['CONF:SENSITIVITY:TARGET_PER 0.5\n',
                         'CONF:POWER:MIN_Y -80\n',
                         'CONF:LINK:FRAG_PADDING 0\n',
                         'CONF:RF:TX_POW 0\n',
                         'CONF:NST:MFG:PACKET_INTERVAL 0.01\n']


def test_payload_setters_keep_leading_zeros(rwc):
    rwc.link_setpayload('0x000102')
    rwc.link_setechopayload(1, bytes([0, 1, 2]))
    rwc.link_setfopts('0x0001')
    rwc.sensitivity_setpayload(bytes(range(16)))
    rwc.nst_mfg_setpayload('0x00ff')
    assert sent(rwc) == ['CONF:LINK:PAYLOAD 000102\n',
                         'CONF:LINK:ECHO_PAYLOAD 1 000102\n',
                         'CONF:LINK:FOPTS 0001\n',
                         'CONF:SENSITIVITY:PAYLOAD 000102030405060708090A0B0C0D0E0F\n',
                         'CONF:NST:MFG:PAYLOAD 00FF\n']


def test_power_per_channel(rwc):
    rwc.power_getnumofpkts_dut_ch(7)
    rwc.power_getavgdutpower_ch(8)
    rwc.power_getmindutpower_ch(63)
    assert sent(rwc) == ['READ:POWER:CH_7:NUM?\n',
                         'READ:POWER:CH:AVG? 8\n',
                         'READ:POWER:CH:MIN? 63\n']


@pytest.mark.parametrize('rwc', ['1.310'], indirect = True)
def test_power_per_channel_old_firmware(rwc):
    with pytest.raises(Exception, match = 'not supported'):
        rwc.power_getmaxdutpower_ch(8)


def test_hexparam_compatibility():
    from rwclib.cRWC5020x import _hexparam
    # v1.0.4 read strings as decimal, ints as numbers
    assert _hexparam('100', 8) == '64'
    assert _hexparam(100, 8) == '64'
    assert _hexparam(0x1234, 8) == '1234'
    # hex needs 0x, and keeps leading zero bytes
    assert _hexparam('0x000102', 8) == '000102'
    assert _hexparam('0xC194C1', 8) == 'C194C1'
    assert _hexparam(b'\x00\x01', 8) == '0001'
    for bad in ['C194C1', '0xzz', '', -1, None, 'x' * 3, '0x' + '00' * 9]:
        with pytest.raises(Exception):
            _hexparam(bad, 8)


def test_syncword(rwc):
    rwc.nst_tx_setsyncword('0xC194C1')
    rwc.nst_rx_setsyncword(0xC194C1)
    assert sent(rwc) == ['CONF:NST:TX:SYNC_WORD 0x0000000000C194C1\n',
                         'CONF:NST:RX:SYNC_WORD 0x0000000000C194C1\n']


# step 3 of #18: other defects

def test_sensitivity_rx2frequency(rwc):
    rwc.sensitivity_setrx2frequency(869.525)
    assert sent(rwc) == ['CONF:SENSITIVITY:RX2_FREQ 869.525000\n']
    with pytest.raises(Exception):
        rwc.sensitivity_setrx2frequency(869525000)


def test_channel_numbers(rwc):
    rwc.rf_getuplinkchannel()
    rwc.rf_getuplinkchannel(3)
    rwc.rf_getdownlinkchannel(1)
    rwc.rf_setuplinkchannel(868.1)
    rwc.rf_setuplinkchannel(867.1, 3)
    assert sent(rwc) == ['READ:RF:UL_CH?\n',
                         'READ:RF:UL_CH? 3\n',
                         'READ:RF:DL_CH? 1\n',
                         'CONF:RF:UL_CH 868.100000\n',
                         'CONF:RF:UL_CH 3 867.100000\n']


@pytest.mark.parametrize('version, ok', [
    ('1.150', True), ('1.210', True), ('1.215', True),
    ('1.220', False), ('1.500', False)])
def test_version_range_dut_type(monkeypatch, version, ok):
    # nst_tx_getduttype() is for firmware 1.150 up to 1.220
    fake = FakeTester(version)
    monkeypatch.setattr(RwcSerialSetup, 'transceive',
                        lambda api, cmd, sec = 0: fake.transceive(api, cmd, sec))
    api = RWCTesterApi('5001', '192.0.2.1')
    if ok:
        api.nst_tx_getduttype()
        assert fake.sent == ['READ:NST:TX:DUT_TYPE?\n']
    else:
        with pytest.raises(Exception, match = 'not supported'):
            api.nst_tx_getduttype()
        assert fake.sent == []


@pytest.mark.parametrize('rwc', ['1.160'], indirect = True)
def test_old_datarate_names(rwc):
    rwc.protocol_setrx2_dr('DR_3')
    assert sent(rwc) == ['CONF:PROTOCOL:RX2_DR DR_3\n']


@pytest.mark.parametrize('rwc', ['NAK'], indirect = True)
def test_float_version_sites_unreadable(rwc):
    with pytest.raises(Exception, match = 'Cannot read tester firmware version'):
        rwc.nst_tx_setinterval(1)
