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

import datetime
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from rwclib.cRWC5020x import RWCTesterApi
from rwclib.cRWCSerialSetup import RwcSerialSetup


class FakeTester:
    '''Records each command; answers version queries and the queries in
    answers, and ACKs the rest.'''

    def __init__(self, version):
        self.version = version
        self.answers = {}
        self.sent = []

    def transceive(self, api, cmd, sec = 0):
        if cmd == 'READ:SYSTEM:SW_VERSION?\n':
            return self.version
        if cmd in self.answers:
            return self.answers[cmd]
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
    rwc.fake.answers['READ:LINK:FOPTS_SIZE?\n'] = '2'
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


# step 4 of #18: commands added from the v1.500 manual

def test_new_choice_commands(rwc):
    rwc.rf_setedtmultichannel('64-CH')
    rwc.rf_getedtmultichannel()
    rwc.rf_setrxagc('ON')
    rwc.nst_tx_setimplicitheader('OFF')
    rwc.nst_rx_setimplicitheader('ON')
    rwc.nst_rx_setimplicitcr('4_8')
    rwc.protocol_setdownlinkdwelltime('400ms')
    rwc.protocol_setuplinkdwelltime('NO_LIMIT')
    assert sent(rwc) == ['CONF:RF:EDT_MULTI_CH 64-CH\n',
                         'READ:RF:EDT_MULTI_CH?\n',
                         'CONF:RF:RX_AGC ON\n',
                         'CONF:NST:TX:IMPLICIT_HEADER OFF\n',
                         'CONF:NST:RX:IMPLICIT_HEADER ON\n',
                         'CONF:NST:RX:IMPLICIT_CR 4_8\n',
                         'CONF:PROTOCOL:DL_DWELL_TIME 400ms\n',
                         'CONF:PROTOCOL:UL_DWELL_TIME NO_LIMIT\n']


def test_new_int_commands(rwc):
    rwc.nst_rx_setfcntavgn(10)
    rwc.nst_rx_setimplicitpayloadsize(0)
    rwc.link_setfoptspayloadsize(250)
    rwc.link_setfoptspayload('0x0001')
    rwc.sensitivity_getperresult(3)
    assert sent(rwc) == ['CONF:NST:RX:FCNT_AVG_N 10\n',
                         'CONF:NST:RX:IMPLICIT_PAYLOAD_SIZE 0\n',
                         'CONF:LINK:FOPTS_PAYLOAD_SIZE 250\n',
                         'CONF:LINK:FOPTS_PAYLOAD 0001\n',
                         'READ:SENSITIVITY:PER_RESULT? 3\n']


def test_genappkey(rwc):
    rwc.protocol_setgenappkey('0x' + '00' * 15 + '01')
    rwc.protocol_setgenappkey(1)
    assert sent(rwc) == ['CONF:PROTOCOL:GEN_APP_KEY ' + '00' * 15 + '01\n'] * 2
    with pytest.raises(Exception):
        rwc.protocol_setgenappkey('0x0001')


@pytest.mark.parametrize('call', [
    lambda r: r.rf_setedtmultichannel('12-CH'),
    lambda r: r.rf_setrxagc('AUTO'),
    lambda r: r.nst_rx_setfcntavgn(11),
    lambda r: r.nst_rx_setimplicitpayloadsize(256),
    lambda r: r.nst_rx_setimplicitcr('4_9'),
    lambda r: r.link_setfoptspayloadsize(251),
    lambda r: r.protocol_setdownlinkdwelltime('1s'),
    ])
def test_new_commands_out_of_range(rwc, call):
    with pytest.raises(Exception):
        call(rwc)
    assert sent(rwc) == []


def test_option_queries(rwc):
    rwc.query_64choptinfo()
    rwc.query_aucertoptinfo()
    rwc.query_rucertoptinfo()
    rwc.query_ilcertoptinfo()
    rwc.query_eu433certoptinfo()
    assert sent(rwc) == ['READ:SYSTEM:OPTION_64_CH?\n',
                         'READ:SYSTEM:OPTION_CERTI_AU?\n',
                         'READ:SYSTEM:OPTION_CERTI_RU?\n',
                         'READ:SYSTEM:OPTION_CERTI_IL?\n',
                         'READ:SYSTEM:OPTION_CERTI_EU433?\n']


# step 5 of #18: firmware v1.604

def test_fopts_length_must_match_size(rwc):
    rwc.fake.answers['READ:LINK:FOPTS_SIZE?\n'] = '8'
    rwc.link_setfopts('0x0001020304050607')
    assert sent(rwc) == ['CONF:LINK:FOPTS 0001020304050607\n']
    # 1020304050607 decimal is 5 bytes; the tester would ACK it
    with pytest.raises(Exception):
        rwc.link_setfopts('0001020304050607')
    rwc.fake.answers['READ:LINK:FOPTS_SIZE?\n'] = 'NAK'
    with pytest.raises(Exception):
        rwc.link_setfopts('0x0001020304050607')
    assert sent(rwc) == ['CONF:LINK:FOPTS 0001020304050607\n']


@pytest.mark.parametrize('rwc', ['1.6040'], indirect = True)
def test_crc_split(rwc):
    rwc.nst_tx_setcr('4_6')
    rwc.nst_tx_setcrc('OFF')
    rwc.nst_tx_getcrc()
    rwc.nst_rx_setcrc('ON')
    rwc.nst_rx_getcrc()
    rwc.nst_mfg_setcrc('ON')
    rwc.nst_mfg_getcrc()
    rwc.nst_rx_setimplicitcrc('OFF')
    rwc.nst_rx_getimplicitcrc()
    assert sent(rwc) == ['CONF:NST:TX:CR 4_6\n',
                         'CONF:NST:TX:CRC OFF\n',
                         'READ:NST:TX:CRC?\n',
                         'CONF:NST:RX:CRC ON\n',
                         'READ:NST:RX:CRC?\n',
                         'CONF:NST:MFG:CRC ON\n',
                         'READ:NST:MFG:CRC?\n',
                         'CONF:NST:RX:IMPLICIT_CRC OFF\n',
                         'READ:NST:RX:IMPLICIT_CRC?\n']


@pytest.mark.parametrize('call', [
    lambda r: r.nst_tx_setcr('NO_CRC'),
    lambda r: r.nst_mfg_setcr('NO_CRC'),
    lambda r: r.nst_rx_setcr('4_5'),
    lambda r: r.nst_rx_setimplicitcr('NO_CRC'),
    lambda r: r.link_getadrchmask_optdr(1),
    lambda r: r.link_setadrchmask_optdr(1, 1),
    lambda r: r.query_ilcertoptinfo(),
    ])
@pytest.mark.parametrize('rwc', ['1.6040'], indirect = True)
def test_removed_in_1604(rwc, call):
    with pytest.raises(Exception, match = 'not supported'):
        call(rwc)
    assert sent(rwc) == []


@pytest.mark.parametrize('call', [
    lambda r: r.nst_tx_setcrc('ON'),
    lambda r: r.nst_rx_getimplicitcrc(),
    lambda r: r.nst_tx_setsf('SF5'),
    lambda r: r.nst_rx_setsf('SF6'),
    lambda r: r.nst_mfg_setsf('SF5'),
    lambda r: r.protocol_setrelaymode('ON'),
    lambda r: r.protocol_getrelaymode(),
    ])
def test_new_in_1520_or_later(rwc, call):
    with pytest.raises(Exception, match = 'not supported'):
        call(rwc)
    assert sent(rwc) == []


@pytest.mark.parametrize('rwc', ['1.6040'], indirect = True)
def test_new_commands_1604(rwc):
    rwc.nst_tx_setsf('SF5')
    rwc.nst_rx_setsf('SF6')
    rwc.nst_mfg_setsf('ANY')
    rwc.rf_setedtmultichannel('16-CH')
    rwc.protocol_setrelaymode('OFF')
    rwc.protocol_getrelaymode()
    rwc.query_incertoptinfo()
    assert sent(rwc) == ['CONF:NST:TX:SF SF5\n',
                         'CONF:NST:RX:SF SF6\n',
                         'CONF:NST:MFG:SF ANY\n',
                         'CONF:RF:EDT_MULTI_CH 16-CH\n',
                         'CONF:PROTOCOL:RELAY_MODE OFF\n',
                         'READ:PROTOCOL:RELAY_MODE?\n',
                         'READ:SYSTEM:OPTION_CERTI_IN?\n']


def test_1500_keeps_old_forms(rwc):
    rwc.nst_tx_setcr('NO_CRC')
    rwc.nst_rx_setcr('4_5')
    rwc.link_getadrchmask_optdr(1)
    rwc.query_ilcertoptinfo()
    assert sent(rwc) == ['CONF:NST:TX:CR NO_CRC\n',
                         'CONF:NST:RX:CR 4_5\n',
                         'READ:LINK:ADR_CH_MASK_OPT? 1\n',
                         'READ:SYSTEM:OPTION_CERTI_IL?\n']


def test_settime(rwc):
    assert rwc.protocol_settime(datetime.datetime(2026, 10, 27, 0, 5, 9)) == 'ACK'
    assert sent(rwc) == ['CONF:PROTOCOL:YEAR 2026\n', 'CONF:PROTOCOL:MONTH 10\n',
                         'CONF:PROTOCOL:DAY 27\n', 'CONF:PROTOCOL:HOUR 0\n',
                         'CONF:PROTOCOL:MINUTE 5\n', 'CONF:PROTOCOL:SECOND 9\n']


def test_settime_converts_to_utc(rwc):
    est = datetime.timezone(datetime.timedelta(hours = -5))
    rwc.protocol_settime(datetime.datetime(2026, 12, 31, 20, 0, 0, tzinfo = est))
    assert sent(rwc)[:4] == ['CONF:PROTOCOL:YEAR 2027\n', 'CONF:PROTOCOL:MONTH 1\n',
                             'CONF:PROTOCOL:DAY 1\n', 'CONF:PROTOCOL:HOUR 1\n']


def test_settime_stops_at_nak(rwc, monkeypatch):
    monkeypatch.setattr(rwc, 'protocol_setmonth', lambda month: 'NAK')
    assert rwc.protocol_settime(datetime.datetime(2026, 10, 27)) == 'NAK'
    assert sent(rwc) == ['CONF:PROTOCOL:YEAR 2026\n']


def test_sethour_zero(rwc):
    rwc.protocol_sethour(0)
    assert sent(rwc) == ['CONF:PROTOCOL:HOUR 0\n']


@pytest.mark.parametrize('addr', [None, '192.0.2.1'])
def test_command_before_open_port(addr):
    api = RWCTesterApi('5001' if addr else '/dev/null', addr)
    with pytest.raises(Exception, match = 'open_port'):
        api.protocol_getyear()


def test_command_after_close_port():
    api = RWCTesterApi('5001', '192.0.2.1')
    api.open_port()
    api.close_port()
    with pytest.raises(Exception, match = 'open_port'):
        api.protocol_getyear()


def test_reply_nul_stripped():
    class Sock:
        '''Nothing waiting when transceive() drains stale replies; then
        one link message, as the tester sends it.'''
        replies = [None, b'U\t1\t40 01 00 \x00\r\n']
        def setblocking(self, flag): pass
        def settimeout(self, t): pass
        def fileno(self): return 3
        def sendto(self, data, addr): pass
        def recvfrom(self, n):
            reply = self.replies.pop(0)
            if reply is None:
                raise BlockingIOError
            return reply, None
    api = RWCTesterApi('5001', '192.0.2.1')
    api.clientsock = Sock()
    assert api.link_readmsg() == 'U\t1\t40 01 00 '
