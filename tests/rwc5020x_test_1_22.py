##############################################################################
# 
# Module: rwc5020x_test_1_22.py
#
# Description:
#     Unit test cases for sw version 1.222
#
# Copyright notice:
#     This file copyright (c) 2021 by
#
#         MCCI Corporation
#         3520 Krums Corners Road
#         Ithaca, NY  14850
#
#     See accompanying LICENSE file for copyright and license information.
#
# Author:
#     Sivaprakash Veluthambi, MCCI   January, 2021
#
##############################################################################

import os
import sys
import time
import unittest

import serial

sys.path.insert(0, os.path.abspath('..'))

from rwclib.cRWC5020x import RWCTesterApi

class RwcApiTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        port = myport
        addr = None
        self.rwctest = RWCTesterApi(port, addr)

    def test_atstart_openport(self):
        self.assertTrue(self.rwctest.open_port(), 'Failed to open the port')

    # Test cases for Common Command Methods
    def test_com_query_identification(self):
        self.assertEqual(self.rwctest.query_identification(), 'RWC5020A LoRaWAN Tester, Ver=1.222,SN=RWC50201760009 ')

    def test_com_reset(self):
        self.assertEqual(self.rwctest.reset(), 'ACK', 'Reset Operation Failed')

    # Test cases for System Configuration Command Methods
    def test_conf_setmode(self):
        self.assertEqual(self.rwctest.set_mode('EDT'), 'ACK', 'EDT change mode failed.')
        time.sleep(.5000)
        self.assertEqual(self.rwctest.query_mode(), 'EDT', 'Failed to get sub menu mode.')
        
        self.assertEqual(self.rwctest.set_mode('GWT'), 'ACK', 'GWT change mode failed.')
        time.sleep(.5000)
        self.assertEqual(self.rwctest.query_mode(), 'GWT', 'Failed to get sub menu mode.')
        
        self.assertEqual(self.rwctest.set_mode('NST_TX'), 'ACK', 'NST change mode failed.')
        time.sleep(.5000)
        self.assertEqual(self.rwctest.query_mode(), 'NST_TX', 'Failed to get sub menu mode.')

        self.assertEqual(self.rwctest.set_mode('NST_RX'), 'ACK', 'NST change mode failed.')
        time.sleep(.5000)
        self.assertEqual(self.rwctest.query_mode(), 'NST_RX', 'Failed to get sub menu mode.')

        self.assertEqual(self.rwctest.set_mode('NST_MFG'), 'ACK', 'NST change mode failed.')
        time.sleep(.5000)
        self.assertEqual(self.rwctest.query_mode(), 'NST_MFG', 'Failed to get sub menu mode.')

    def test_conf_remotelock(self):
        self.assertEqual(self.rwctest.set_remotelock('OFF'), 'ACK', 'Setting Remote Lock failed.')
        self.assertEqual(self.rwctest.query_remotelock(), 'OFF', 'Getting Remote Lock Status failed.')
        
        self.assertEqual(self.rwctest.set_remotelock('ON'), 'ACK', 'Setting Remote Lock failed.')
        self.assertEqual(self.rwctest.query_remotelock(), 'ON', 'Getting Remote Lock Status failed.')

    def test_conf_subscreen(self):
        self.assertEqual(self.rwctest.set_mode('EDT'), 'ACK', 'EDT change mode failed.')
        time.sleep(.5000)
        
        self.assertEqual(self.rwctest.set_screen('LINK'), 'ACK', 'Change sub menu mode failed.')
        time.sleep(.5000)

        self.assertEqual(self.rwctest.set_screen('POWER_TIME'), 'ACK', 'Change sub menu mode failed.')
        time.sleep(.5000)

        self.assertEqual(self.rwctest.set_screen('POWER_CHANNEL'), 'ACK', 'Change sub menu mode failed.')
        time.sleep(.5000)

        self.assertEqual(self.rwctest.set_screen('SENSITIVITY'), 'ACK', 'Change sub menu mode failed.')
        time.sleep(.5000)

        self.assertEqual(self.rwctest.set_mode('GWT'), 'ACK', 'GWT change mode failed.')
        time.sleep(.5000)

        self.assertEqual(self.rwctest.set_screen('LINK'), 'ACK', 'Change sub menu mode failed.')
        time.sleep(.5000)

        self.assertEqual(self.rwctest.set_screen('POWER_TIME'), 'ACK', 'Change sub menu mode failed.')
        time.sleep(.5000)

        self.assertEqual(self.rwctest.set_screen('POWER_CHANNEL'), 'ACK', 'Change sub menu mode failed.')
        time.sleep(.5000)

        self.assertEqual(self.rwctest.set_screen('SENSITIVITY'), 'ACK', 'Change sub menu mode failed.')
        time.sleep(.5000)

    # Test cases for RF Parameter Command Methods 
    def test_rffrequency(self):
        self.assertEqual(self.rwctest.rf_setfrequency('870'), 'ACK', 'Set RF Frequency Range failed.')
        self.assertEqual(self.rwctest.rf_getfrequency(), '870.000000', 'Get RF Frequency Range failed.')

    def test_rftxpower(self):
        self.assertEqual(self.rwctest.rf_settxpower('-50'), 'ACK', 'Set RF TX Power Range failed.')
        self.assertEqual(self.rwctest.rf_gettxpower(), '-50.0', 'Get RF TX Power Range failed.')

    def test_rfpathloss(self):
        self.assertEqual(self.rwctest.rf_setpathloss('40'), 'ACK', 'Set RF Path Loss Range failed.')
        self.assertEqual(self.rwctest.rf_getpathloss(), '40.0', 'Get RF Path Loss Range failed.')

    def test_rffrequencyoffset(self):
        self.assertEqual(self.rwctest.rf_setfreqoffset('110'), 'ACK', 'Set RF Frequency offset failed.')
        self.assertEqual(self.rwctest.rf_getfreqoffset(), '110.0', 'Get RF Frequency offset failed.')

    def test_rftimeoffset(self):
        self.assertEqual(self.rwctest.rf_settimeoffset('110'), 'ACK', 'Set RF Time offset failed.')
        self.assertEqual(self.rwctest.rf_gettimeoffset(), '110', 'Get RF Time offset failed.')

    def test_rfchannelmask(self):
        self.assertEqual(self.rwctest.set_mode('EDT'), 'ACK', 'GWT change mode failed.')
        self.assertEqual(self.rwctest.protocol_setregion('IN_866'), 'ACK', 'Set Region Failed')
        self.assertEqual(self.rwctest.rf_setchannelmask(0, 0x3F), 'ACK', 'Set RF Channel Mask failed.')
        self.assertEqual(self.rwctest.rf_getchannelmask(0), '0x3F', 'Read RF Channel Mask failed.')        

    def test_rfchannelgroup(self):
        self.assertEqual(self.rwctest.set_mode('EDT'), 'ACK', 'EDT change mode failed.')
        
        self.assertEqual(self.rwctest.protocol_setregion('US_915'), 'ACK', 'Set Region Failed')
        self.assertEqual(self.rwctest.rf_setchannelgroup(0), 'ACK', 'Set RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_getchannelgroup(), '00~07,64', 'Read RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_setchannelgroup(8), 'ACK', 'Set RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_getchannelgroup(), '08~15,65', 'Read RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_setchannelgroup(16), 'ACK', 'Set RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_getchannelgroup(), '16~23,66', 'Read RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_setchannelgroup(24), 'ACK', 'Set RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_getchannelgroup(), '24~31,67', 'Read RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_setchannelgroup(32), 'ACK', 'Set RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_getchannelgroup(), '32~39,68', 'Read RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_setchannelgroup(40), 'ACK', 'Set RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_getchannelgroup(), '40~47,69', 'Read RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_setchannelgroup(48), 'ACK', 'Set RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_getchannelgroup(), '48~55,70', 'Read RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_setchannelgroup(56), 'ACK', 'Set RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_getchannelgroup(), '56~63,71', 'Read RF Channel Group failed.')

        self.assertEqual(self.rwctest.protocol_setregion('AU_921'), 'ACK', 'Set Region Failed')
        self.assertEqual(self.rwctest.rf_setchannelgroup(0), 'ACK', 'Set RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_getchannelgroup(), '00~07,64', 'Read RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_setchannelgroup(8), 'ACK', 'Set RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_getchannelgroup(), '08~15,65', 'Read RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_setchannelgroup(16), 'ACK', 'Set RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_getchannelgroup(), '16~23,66', 'Read RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_setchannelgroup(24), 'ACK', 'Set RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_getchannelgroup(), '24~31,67', 'Read RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_setchannelgroup(32), 'ACK', 'Set RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_getchannelgroup(), '32~39,68', 'Read RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_setchannelgroup(40), 'ACK', 'Set RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_getchannelgroup(), '40~47,69', 'Read RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_setchannelgroup(48), 'ACK', 'Set RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_getchannelgroup(), '48~55,70', 'Read RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_setchannelgroup(56), 'ACK', 'Set RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_getchannelgroup(), '56~63,71', 'Read RF Channel Group failed.')

        self.assertEqual(self.rwctest.protocol_setregion('CN_470'), 'ACK', 'Set Region Failed')
        self.assertEqual(self.rwctest.rf_setchannelgroup(0), 'ACK', 'Set RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_getchannelgroup(), '00~07', 'Read RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_setchannelgroup(8), 'ACK', 'Set RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_getchannelgroup(), '08~15', 'Read RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_setchannelgroup(16), 'ACK', 'Set RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_getchannelgroup(), '16~23', 'Read RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_setchannelgroup(24), 'ACK', 'Set RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_getchannelgroup(), '24~31', 'Read RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_setchannelgroup(32), 'ACK', 'Set RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_getchannelgroup(), '32~39', 'Read RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_setchannelgroup(40), 'ACK', 'Set RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_getchannelgroup(), '40~47', 'Read RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_setchannelgroup(48), 'ACK', 'Set RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_getchannelgroup(), '48~55', 'Read RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_setchannelgroup(56), 'ACK', 'Set RF Channel Group failed.')
        self.assertEqual(self.rwctest.rf_getchannelgroup(), '56~63', 'Read RF Channel Group failed.')

    def test_rfpingfrequency(self):
        self.assertEqual(self.rwctest.rf_setpingfreq(865), 'ACK', 'Set RF ping frequency failed.')
        self.assertEqual(self.rwctest.rf_getpingfreq(), '865.000000', 'Read RF ping frequency failed.')

    def test_rfpingdatarate(self):
        self.assertEqual(self.rwctest.rf_setpingdr('DR0_SF12BW125'), 'ACK', 'Set RF ping DR failed.')
        self.assertEqual(self.rwctest.rf_getpingdr(), 'DR0_SF12BW125', 'Read RF ping DR failed.')

    def test_beaconfrequency(self):
        self.assertEqual(self.rwctest.rf_setbeaconfrequency(865), 'ACK', 'Set RF beacon frequency failed.')
        self.assertEqual(self.rwctest.rf_getbeaconfreq(), '865.000000', 'Read RF beacon frequency failed.')

    # Test Cases for Protocol Command Methods
    def test_protocolregion(self):
        regionlist = ['EU_868', 'EU_433', 'US_915', 'AU_921', 'CN_470', 'KR_922', 'AS_923', 'IN_866', 'RU_864']
        for region in regionlist:
            if region == 'EU_868':
                self.assertEqual(self.rwctest.protocol_setregion(region), 'ACK', 'Set Region Failed')
                self.assertEqual(self.rwctest.protocol_getregion(), 'EU_868', 'Failed to read region')
            if region == 'EU_433':
                self.assertEqual(self.rwctest.protocol_setregion(region), 'ACK', 'Set Region Failed')
                self.assertEqual(self.rwctest.protocol_getregion(), 'EU_433', 'Failed to read region')
            if region == 'US_915':
                self.assertEqual(self.rwctest.protocol_setregion(region), 'ACK', 'Set Region Failed')
                self.assertEqual(self.rwctest.protocol_getregion(), 'US_915', 'Failed to read region')
            if region == 'AU_921':
                self.assertEqual(self.rwctest.protocol_setregion(region), 'ACK', 'Set Region Failed')
                self.assertEqual(self.rwctest.protocol_getregion(), 'AU_915', 'Failed to read region')
            if region == 'CN_470':
                self.assertEqual(self.rwctest.protocol_setregion(region), 'ACK', 'Set Region Failed')
                self.assertEqual(self.rwctest.protocol_getregion(), 'CN_470', 'Failed to read region')
            if region == 'KR_922':
                self.assertEqual(self.rwctest.protocol_setregion(region), 'ACK', 'Set Region Failed')
                self.assertEqual(self.rwctest.protocol_getregion(), 'KR_920', 'Failed to read region')
            if region == 'AS_923':
                self.assertEqual(self.rwctest.protocol_setregion(region), 'ACK', 'Set Region Failed')
                self.assertEqual(self.rwctest.protocol_getregion(), 'AS_923', 'Failed to read region')
            if region == 'IN_866':
                self.assertEqual(self.rwctest.protocol_setregion(region), 'ACK', 'Set Region Failed')
                self.assertEqual(self.rwctest.protocol_getregion(), 'IN_865', 'Failed to read region')
            if region == 'RU_864':
                self.assertEqual(self.rwctest.protocol_setregion(region), 'ACK', 'Set Region Failed')
                self.assertEqual(self.rwctest.protocol_getregion(), 'RU_864', 'Failed to read region')
                
    def test_protocoloperator(self):
        operatorlist = ['LoRaWAN', 'PRIVATE', 'SKT']

        self.assertEqual(self.rwctest.protocol_setregion('KR_922'), 'ACK', 'Set Region Failed')
        
        for operator in operatorlist:
            if operator == 'LoRaWAN':
                self.assertEqual(self.rwctest.protocol_setoperator(operator), 'ACK', 'Set Operator Failed')
                self.assertEqual(self.rwctest.protocol_getoperator(), 'LoRaWAN', 'Failed to read operator')
            if operator == 'SKT':
                self.assertEqual(self.rwctest.protocol_setoperator(operator), 'ACK', 'Set Operator Failed')
                self.assertEqual(self.rwctest.protocol_getoperator(), 'SKT', 'Failed to read operator')

    def test_protocolclass(self):
        classlist = ['A', 'B', 'C']

        for classname in classlist:
            if classname == 'A':
                self.assertEqual(self.rwctest.protocol_setclass(classname), 'ACK', 'Set Class Failed')
                self.assertEqual(self.rwctest.protocol_getclass(), 'A', 'Failed to read class')
            if classname == 'B':
                self.assertEqual(self.rwctest.protocol_setclass(classname), 'ACK', 'Set Class Failed')
                self.assertEqual(self.rwctest.protocol_getclass(), 'B', 'Failed to read class')
            if classname == 'C':
                self.assertEqual(self.rwctest.protocol_setclass(classname), 'ACK', 'Set Class Failed')
                self.assertEqual(self.rwctest.protocol_getclass(), 'C', 'Failed to read class')

    def test_protocolactivationprocedure(self):
        activationlist = ['OTAA', 'ABP']

        for activationproc in activationlist:
            if activationproc == 'OTAA':
                self.assertEqual(self.rwctest.protocol_setactivationprocedure(activationproc), 'ACK', 'Set Activation procedure Failed')
                self.assertEqual(self.rwctest.protocol_getactivationprocedure(), 'OTAA', 'Failed to read activation procedure')
            if activationproc == 'ABP':
                self.assertEqual(self.rwctest.protocol_setactivationprocedure(activationproc), 'ACK', 'Set Activation procedure Failed')
                self.assertEqual(self.rwctest.protocol_getactivationprocedure(), 'ABP', 'Failed to read activation procedure')

    def test_protocoltestmodeflag(self):
        testmodelist = ['OFF', 'ON']

        for testmode in testmodelist:
            if testmode == 'OFF':
                self.assertEqual(self.rwctest.protocol_settestmodeflag(testmode), 'ACK', 'Set Test Mode Failed')
                self.assertEqual(self.rwctest.protocol_gettestmodeflag(), 'OFF', 'Failed to read test mode')
            if testmode == 'ON':
                self.assertEqual(self.rwctest.protocol_settestmodeflag(testmode), 'ACK', 'Set Test Mode Failed')
                self.assertEqual(self.rwctest.protocol_gettestmodeflag(), 'ON', 'Failed to read test mode')

    def test_protocolbeacontimeoffset(self):
        self.assertEqual(self.rwctest.protocol_setbeacontimeoffset(10), 'ACK', 'Set Beacon Time Offset Failed')
        self.assertEqual(self.rwctest.protocol_getbeacontimeoffset(), '10', 'Failed to read time offset value')

    def test_protocolappkey(self):
        self.assertEqual(self.rwctest.protocol_setappkey(255), 'ACK', 'Set Application Key Failed')
        self.assertEqual(self.rwctest.protocol_getappkey(), '0x000000000000000000000000000000ff', 'Failed to read application key')

    def test_protocolappsessionkey(self):
        self.assertEqual(self.rwctest.protocol_setappsessionkey(0x000000000000000000000000000000ff), 'ACK', 'Set Application Session Key Failed')
        self.assertEqual(self.rwctest.protocol_getappsessionkey(), '0x000000000000000000000000000000ff', 'Failed to read application session key')

    def test_protocolnwksessionkey(self):
        self.assertEqual(self.rwctest.protocol_setnwksessionkey(0x000000000000000000000000000000ff), 'ACK', 'Set Network Session Key Failed')
        self.assertEqual(self.rwctest.protocol_getnwksessionkey(), '0x000000000000000000000000000000ff', 'Failed to read network session key')

    def test_protocolseteuiflag(self):
        euiflaglist = ['NO', 'YES']

        for euiflag in euiflaglist:
            if euiflag == 'NO':
                self.assertEqual(self.rwctest.protocol_seteuiflag(euiflag), 'ACK', 'Set EUI Flag Failed')
                self.assertEqual(self.rwctest.protocol_geteuiflag(), 'NO', 'Failed to read EUI flag')
            if euiflag == 'YES':
                self.assertEqual(self.rwctest.protocol_seteuiflag(euiflag), 'ACK', 'Set EUI Flag Failed')
                self.assertEqual(self.rwctest.protocol_geteuiflag(), 'YES', 'Failed to read EUI flag')

    def test_protocoleuival(self):
        self.assertEqual(self.rwctest.protocol_seteuival(0x000000000000ffff), 'ACK', 'Set Device EUI Value Failed')
        self.assertEqual(self.rwctest.protocol_geteuival(), '0x000000000000ffff', 'Failed to read device EUI value')

    def test_protocolappeui(self):
        self.assertEqual(self.rwctest.protocol_setappeui(0x000000000000ffff), 'ACK', 'Set Application EUI Value Failed')
        self.assertEqual(self.rwctest.protocol_getappeui(), '0x000000000000ffff', 'Failed to read application EUI value')
    
    def test_protocoldevaddr(self):
        self.assertEqual(self.rwctest.protocol_setdevaddr(0x000000FF), 'ACK', 'Set Device Address Value Failed')
        self.assertEqual(self.rwctest.protocol_getdevaddr(), '0x000000FF', 'Failed to read device address value')

    def test_protocolnetid(self):
        self.assertEqual(self.rwctest.protocol_setnetid(0x00007F), 'ACK', 'Set NET ID Value Failed')
        self.assertEqual(self.rwctest.protocol_getnetid(), '0x00007F', 'Failed to read NET ID value')

    def test_protocolrecvdelay(self):
        self.assertEqual(self.rwctest.protocol_setrecvdelay('5'), 'ACK', 'Set RECEIVE_DELAY Value Failed')
        self.assertEqual(self.rwctest.protocol_getrecvdelay(), '5', 'Failed to read RECEIVE_DELAY value')

    def test_protocolperiodic_uplinkmsg(self):
        periodicuplinkmsglist = ['NONE', 'LINK_CHECK_REQ', 'CONFIRMED_UP', 'UNCONFIRMED_UP', 'DL_COUNTER']

        self.assertEqual(self.rwctest.set_mode('GWT'), 'ACK', 'GWT change mode failed.')
        time.sleep(.5000)

        for periodicuplinkmsg in periodicuplinkmsglist:
            if periodicuplinkmsg == 'NONE':
                self.assertEqual(self.rwctest.protocol_setperiodic_uplinkmsg(periodicuplinkmsg), 'ACK', 'Configuring Periodic Uplink Message Failed')
                self.assertEqual(self.rwctest.protocol_getperiodic_uplinkmsg(), 'NONE', 'Failed to Read Periodic Uplink Message')
            if periodicuplinkmsg == 'LINK_CHECK_REQ':
                self.assertEqual(self.rwctest.protocol_setperiodic_uplinkmsg(periodicuplinkmsg), 'ACK', 'Configuring Periodic Uplink Message Failed')
                self.assertEqual(self.rwctest.protocol_getperiodic_uplinkmsg(), 'LINK_CHECK_REQ', 'Failed to Read Periodic Uplink Message')
            if periodicuplinkmsg == 'CONFIRMED_UP':
                self.assertEqual(self.rwctest.protocol_setperiodic_uplinkmsg(periodicuplinkmsg), 'ACK', 'Configuring Periodic Uplink Message Failed')
                self.assertEqual(self.rwctest.protocol_getperiodic_uplinkmsg(), 'CONFIRMED_UP', 'Failed to Read Periodic Uplink Message')
            if periodicuplinkmsg == 'UNCONFIRMED_UP':
                self.assertEqual(self.rwctest.protocol_setperiodic_uplinkmsg(periodicuplinkmsg), 'ACK', 'Configuring Periodic Uplink Message Failed')
                self.assertEqual(self.rwctest.protocol_getperiodic_uplinkmsg(), 'UNCONFIRMED_UP', 'Failed to Read Periodic Uplink Message')
            if periodicuplinkmsg == 'DL_COUNTER':
                self.assertEqual(self.rwctest.protocol_setperiodic_uplinkmsg(periodicuplinkmsg), 'ACK', 'Configuring Periodic Uplink Message Failed')
                self.assertEqual(self.rwctest.protocol_getperiodic_uplinkmsg(), 'DL_COUNTER', 'Failed to Read Periodic Uplink Message')
    
    def test_protocolinterval(self):
        self.assertEqual(self.rwctest.protocol_setinterval('10'), 'ACK', 'Set Interval Failed')
        self.assertEqual(self.rwctest.protocol_getinterval(), '10', 'Failed to read interval value')

    def test_protocolframecnt(self):
        self.assertEqual(self.rwctest.protocol_setframecnt('300'), 'ACK', 'Set Frame Count Value Failed')
        self.assertEqual(self.rwctest.protocol_getframecnt(), '0x12C', 'Failed to read frame count value')

    def test_protocoladrflag(self):
        adrflaglist = ['OFF', 'ON']

        for adrflag in adrflaglist:
            if adrflag == 'OFF':
                self.assertEqual(self.rwctest.protocol_setadrflag(adrflag), 'ACK', 'Set ADR Flag Failed')
                self.assertEqual(self.rwctest.protocol_getadrflag(), 'OFF', 'Failed to read ADR flag')
            if adrflag == 'ON':
                self.assertEqual(self.rwctest.protocol_setadrflag(adrflag), 'ACK', 'Set ADR Flag Failed')
                self.assertEqual(self.rwctest.protocol_getadrflag(), 'ON', 'Failed to read ADR flag')

    def test_protocolyear(self):
        self.assertEqual(self.rwctest.protocol_setyear('2019'), 'ACK', 'Set Year Value Failed')
        self.assertEqual(self.rwctest.protocol_getyear(), '2019', 'Failed to read year value')

    def test_protocolmonth(self):
        self.assertEqual(self.rwctest.protocol_setmonth('12'), 'ACK', 'Set Month Value Failed')
        self.assertEqual(self.rwctest.protocol_getmonth(), '12', 'Failed to read month value')

    def test_protocolday(self):
        self.assertEqual(self.rwctest.protocol_setday('20'), 'ACK', 'Set Day Value Failed')
        self.assertEqual(self.rwctest.protocol_getday(), '20', 'Failed to read day value')

    def test_protocolhour(self):
        self.assertEqual(self.rwctest.protocol_sethour('12'), 'ACK', 'Set Hour Value Failed')
        self.assertEqual(self.rwctest.protocol_gethour(), '12', 'Failed to read hour value')

    def test_protocolminute(self):
        self.assertEqual(self.rwctest.protocol_setminute('30'), 'ACK', 'Set Minute Value Failed')
        self.assertEqual(self.rwctest.protocol_getminute(), '30', 'Failed to read minute value')

    def test_protocolsecond(self):
        self.assertEqual(self.rwctest.protocol_setsecond('45'), 'ACK', 'Set Second Value Failed')
        self.assertEqual(self.rwctest.protocol_getsecond(), '45', 'Failed to read second value')

    def test_protocollinkmargin(self):
        self.assertEqual(self.rwctest.protocol_setlinkmargin(10), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getlinkmargin(), '10', 'Failed to read')

    def test_protocolgatewaycntval(self):
        self.assertEqual(self.rwctest.protocol_setgatewaycntval(5), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getgatewaycntval(), '5', 'Failed to read')

    def test_protocolbatterystatusval(self):
        self.assertEqual(self.rwctest.protocol_setbatterystatusval(210), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getbatterystatusval(), '210', 'Failed to read')

    def test_protocolsnrmargin(self):
        self.assertEqual(self.rwctest.protocol_setsnrmargin('10'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getsnrmargin(), '10', 'Failed to read')

    def test_protocolnwktype(self):
        self.assertEqual(self.rwctest.protocol_setnwktype('PRIVATE'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getnwktype(), 'PRIVATE', 'Failed to read')
        time.sleep(.3000)
        self.assertEqual(self.rwctest.protocol_setnwktype('PUBLIC'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getnwktype(), 'PUBLIC', 'Failed to read')

    def test_protocoldownlinkslot(self):
        self.assertEqual(self.rwctest.set_mode('EDT'), 'ACK', 'EDT change mode failed.')
        time.sleep(.5000)
        self.assertEqual(self.rwctest.protocol_setdownlinkslot('RX1'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getdownlinkslot(), 'RX1', 'Failed to read')
        self.assertEqual(self.rwctest.protocol_setdownlinkslot('RX2'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getdownlinkslot(), 'RX2', 'Failed to read')
        self.assertEqual(self.rwctest.protocol_setclass('B'), 'ACK', 'Set Class Failed')
        self.assertEqual(self.rwctest.protocol_setdownlinkslot('PING'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getdownlinkslot(), 'PING', 'Failed to read')
        
        self.assertEqual(self.rwctest.set_mode('GWT'), 'ACK', 'GWT change mode failed.')
        time.sleep(.5000)
        self.assertEqual(self.rwctest.protocol_setdownlinkslot('RX1'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getdownlinkslot(), 'RX1', 'Failed to read')
        self.assertEqual(self.rwctest.protocol_setdownlinkslot('RX2'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getdownlinkslot(), 'RX2', 'Failed to read')

    def test_protocolmacresponsefield(self):
        self.assertEqual(self.rwctest.protocol_setmacresponsefield('PAYLOAD'), 'ACK', 'Set MAC response field type failed')
        self.assertEqual(self.rwctest.protocol_getmacresponsefield(), 'PAYLOAD', 'Reading MAC response field type failed')
        self.assertEqual(self.rwctest.protocol_setmacresponsefield('FOPTS'), 'ACK', 'Set MAC response field type failed')
        self.assertEqual(self.rwctest.protocol_getmacresponsefield(), 'FOPTS', 'Reading MAC response field type failed')

    def test_protocoluplinkdatarate(self):
        self.assertEqual(self.rwctest.protocol_setuplinkdatarate('DR0_SF12BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getuplinkdatarate(), 'DR0_SF12BW125', 'Failed to read')
        self.assertEqual(self.rwctest.protocol_setuplinkdatarate('DR1_SF11BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getuplinkdatarate(), 'DR1_SF11BW125', 'Failed to read')
        self.assertEqual(self.rwctest.protocol_setuplinkdatarate('DR2_SF10BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getuplinkdatarate(), 'DR2_SF10BW125', 'Failed to read')
        self.assertEqual(self.rwctest.protocol_setuplinkdatarate('DR3_SF9BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getuplinkdatarate(), 'DR3_SF9BW125', 'Failed to read')
        self.assertEqual(self.rwctest.protocol_setuplinkdatarate('DR4_SF8BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getuplinkdatarate(), 'DR4_SF8BW125', 'Failed to read')
        self.assertEqual(self.rwctest.protocol_setuplinkdatarate('DR5_SF7BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getuplinkdatarate(), 'DR5_SF7BW125', 'Failed to read')
        self.assertEqual(self.rwctest.protocol_setuplinkdatarate('DR6_SF7BW250'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getuplinkdatarate(), 'DR6_SF7BW250', 'Failed to read')
        self.assertEqual(self.rwctest.protocol_setuplinkdatarate('DR7_FSK50'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getuplinkdatarate(), 'DR7_FSK50', 'Failed to read')

    def test_protocolrx1_dr_offset(self):
        self.assertEqual(self.rwctest.protocol_setrx1_dr_offset(2), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getrx1_dr_offset(), '2', 'Failed to read')

    def test_protocolrx2_frequency(self):
        self.assertEqual(self.rwctest.protocol_setrx2_frequency(865), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getrx2_frequency(), '865.000000', 'Failed to read')

    def test_protocolrx2_dr(self):
        self.assertEqual(self.rwctest.protocol_setrx2_dr('DR0_SF12BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getrx2_dr(), 'DR0_SF12BW125', 'Failed to read')
        self.assertEqual(self.rwctest.protocol_setrx2_dr('DR1_SF11BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getrx2_dr(), 'DR1_SF11BW125', 'Failed to read')
        self.assertEqual(self.rwctest.protocol_setrx2_dr('DR2_SF10BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getrx2_dr(), 'DR2_SF10BW125', 'Failed to read')
        self.assertEqual(self.rwctest.protocol_setrx2_dr('DR3_SF9BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getrx2_dr(), 'DR3_SF9BW125', 'Failed to read')
        self.assertEqual(self.rwctest.protocol_setrx2_dr('DR4_SF8BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getrx2_dr(), 'DR4_SF8BW125', 'Failed to read')
        self.assertEqual(self.rwctest.protocol_setrx2_dr('DR5_SF7BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getrx2_dr(), 'DR5_SF7BW125', 'Failed to read')

    def test_protocolpingperiodicity(self):
        self.assertEqual(self.rwctest.protocol_setpingperiodicity(5), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getpingperiodicity(), '5', 'Failed to read')

    def test_protocolprotocolver(self):
        self.assertEqual(self.rwctest.protocol_setprotocolver('LoRaWAN1.0.2'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getprotocolver(), 'LoRaWAN1.0.2', 'Failed to read')
        self.assertEqual(self.rwctest.protocol_setprotocolver('LoRaWAN1.0.3'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getprotocolver(), 'LoRaWAN1.0.3', 'Failed to read')
        self.assertEqual(self.rwctest.protocol_setprotocolver('LoRaWAN1.1'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getprotocolver(), 'LoRaWAN1.1', 'Failed to read')

    def test_protocolnwkkey(self):
        self.assertEqual(self.rwctest.protocol_setprotocolver('LoRaWAN1.1'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_setnwkkey(0x000000000000000000000000000000ff), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getnwkkey(), '0x000000000000000000000000000000ff', 'Failed to read')

    def test_protocolfnwksintkey(self):
        self.assertEqual(self.rwctest.protocol_setprotocolver('LoRaWAN1.1'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_setfnwksintkey(0x000000000000000000000000000000ff), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getfnwksintkey(), '0x000000000000000000000000000000ff', 'Failed to read')

    def test_protocolsnwksintkey(self):
        self.assertEqual(self.rwctest.protocol_setprotocolver('LoRaWAN1.1'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_setsnwksintkey(0x000000000000000000000000000000ff), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getsnwksintkey(), '0x000000000000000000000000000000ff', 'Failed to read')

    def test_protocolnwksenckey(self):
        self.assertEqual(self.rwctest.protocol_setprotocolver('LoRaWAN1.1'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_setnwksenckey(0x000000000000000000000000000000ff), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getnwksenckey(), '0x000000000000000000000000000000ff', 'Failed to read')

    def test_protocoljoineuival(self):
        self.assertEqual(self.rwctest.protocol_setprotocolver('LoRaWAN1.1'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_setjoineuival(0x00000000000000ff), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getjoineuival(), '0x00000000000000ff', 'Failed to read')

    def test_protocolupdatenfcnt(self):
        self.assertEqual(self.rwctest.protocol_setprotocolver('LoRaWAN1.1'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_setnfcntval(5), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getnfcntval(), '0x5', 'Failed to read')

    def test_protocolupdateafcnt(self):
        self.assertEqual(self.rwctest.protocol_setprotocolver('LoRaWAN1.1'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_setafcntval(5), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getafcntval(), '0x5', 'Failed to read')

    def test_protocollatitude(self):
        self.assertEqual(self.rwctest.protocol_setclass('B'), 'ACK', 'Set Class Failed')
        self.assertEqual(self.rwctest.protocol_setlatitude(30), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getlatitude(), '30.000000', 'Failed to read')
    
    def test_protocollongitude(self):
        self.assertEqual(self.rwctest.protocol_setclass('B'), 'ACK', 'Set Class Failed')
        self.assertEqual(self.rwctest.protocol_setlongitude(120), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getlongitude(), '120.000000', 'Failed to read')
    
    def test_protocolsetedtperiodiclink(self):
        self.assertEqual(self.rwctest.set_mode('EDT'), 'ACK', 'EDT change mode failed.')
        self.assertEqual(self.rwctest.protocol_setclass('B'), 'ACK', 'Set Class Failed')
        self.assertEqual(self.rwctest.protocol_setedtperiodiclink('NONE'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getedtperiodiclink(), 'NONE', 'Failed to read')
        self.assertEqual(self.rwctest.protocol_setedtperiodiclink('CONFIRMED_DOWN'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getedtperiodiclink(), 'CONFIRMED_DOWN', 'Failed to read')
        self.assertEqual(self.rwctest.protocol_setedtperiodiclink('UNCONFIRMED_DOWN'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getedtperiodiclink(), 'UNCONFIRMED_DOWN', 'Failed to read')

    def test_protocolsetclaamode(self):
        self.assertEqual(self.rwctest.protocol_setclaamode('D'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getclaamode(), 'D', 'Failed to read')
        self.assertEqual(self.rwctest.protocol_setclaamode('E'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.protocol_getclaamode(), 'E', 'Failed to read')
    
    # Test Cases for Link Command Methods
    def test_linkmaccmdtype(self):
        self.assertEqual(self.rwctest.link_setmaccmdtype('UNCONFIRMED'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getmaccmdtype(), 'UNCONFIRMED', 'Failed to read')
        self.assertEqual(self.rwctest.link_setmaccmdtype('CONFIRMED'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getmaccmdtype(), 'CONFIRMED', 'Failed to read')

    def test_linkmacansto(self):
        self.assertEqual(self.rwctest.link_setmacanstimeout(60), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getmacanstimeout(), '60', 'Failed to read')

    def test_linkmaccmdfield(self):
        self.assertEqual(self.rwctest.link_setmaccmdfield('PAYLOAD'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getmaccmdfield(), 'PAYLOAD', 'Failed to read')
        self.assertEqual(self.rwctest.link_setmaccmdfield('FOPTS'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getmaccmdfield(), 'FOPTS', 'Failed to read')

    def test_linkinstantmaccmd(self):
        self.assertEqual(self.rwctest.set_mode('EDT'), 'ACK', 'EDT change mode failed.')
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'DEV_STATUS'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getinstantmaccmd(1), 'DEV_STATUS', 'Failed to read')
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'LINK_ADR'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getinstantmaccmd(1), 'LINK_ADR', 'Failed to read')
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'DUTY_CYCLE'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getinstantmaccmd(1), 'DUTY_CYCLE', 'Failed to read')
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'RX_PARAM_SETUP'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getinstantmaccmd(1), 'RX_PARAM_SETUP', 'Failed to read')
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'TX_PARAM_SETUP'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getinstantmaccmd(1), 'TX_PARAM_SETUP', 'Failed to read')
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'NEW_CHANNEL'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getinstantmaccmd(1), 'NEW_CHANNEL', 'Failed to read')
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'DL_CHANNEL'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getinstantmaccmd(1), 'DL_CHANNEL', 'Failed to read')
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'RX_TIMING_SETUP'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getinstantmaccmd(1), 'RX_TIMING_SETUP', 'Failed to read')
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'USER_DEFINED'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getinstantmaccmd(1), 'USER_DEFINED', 'Failed to read')
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'ACTIVATE_TM'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getinstantmaccmd(1), 'ACTIVATE_TM', 'Failed to read')
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'DEACTIVATE_TM'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getinstantmaccmd(1), 'DEACTIVATE_TM', 'Failed to read')
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'CONFIRMED_TM'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getinstantmaccmd(1), 'CONFIRMED_TM', 'Failed to read')
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'UNCONFIRMED_TM'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getinstantmaccmd(1), 'UNCONFIRMED_TM', 'Failed to read')
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'ECHO_REQUEST_TM'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getinstantmaccmd(1), 'ECHO_REQUEST_TM', 'Failed to read')
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'TRIGGER_JOIN_REQ_TM'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getinstantmaccmd(1), 'TRIGGER_JOIN_REQ_TM', 'Failed to read')
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'ENABLE_CW_MODE_TM'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getinstantmaccmd(1), 'ENABLE_CW_MODE_TM', 'Failed to read')
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'BEACON_FREQ'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getinstantmaccmd(1), 'BEACON_FREQ', 'Failed to read')
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'PING_SLOT_CH'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getinstantmaccmd(1), 'PING_SLOT_CH', 'Failed to read')
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'FORCE_REJOIN'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getinstantmaccmd(1), 'FORCE_REJOIN', 'Failed to read')
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'REJOIN_SETUP'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getinstantmaccmd(1), 'REJOIN_SETUP', 'Failed to read')
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'ADR_SETUP'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getinstantmaccmd(1), 'ADR_SETUP', 'Failed to read')
        
        self.assertEqual(self.rwctest.set_mode('GWT'), 'ACK', 'GWT change mode failed.')
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'LINK_CHECK'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getinstantmaccmd(1), 'LINK_CHECK', 'Failed to read')
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'DEVICE_TIME'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getinstantmaccmd(1), 'DEVICE_TIME', 'Failed to read')
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'DEVICE_MODE'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getinstantmaccmd(1), 'DEVICE_MODE', 'Failed to read')
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'RESET_IND'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getinstantmaccmd(1), 'RESET_IND', 'Failed to read')
        self.assertEqual(self.rwctest.set_mode('EDT'), 'ACK', 'EDT change mode failed.')

    def test_linkmic_errdisplay(self):
        self.assertEqual(self.rwctest.link_setmic_errdisplay('OFF'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getmic_errdisplay(), 'OFF', 'Failed to read')
        self.assertEqual(self.rwctest.link_setmic_errdisplay('ON'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getmic_errdisplay(), 'ON', 'Failed to read')

    def test_linkadr_drval(self):
        self.assertEqual(self.rwctest.link_setadr_drval(1, 'DR0_SF12BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getadr_drval(1), 'DR0_SF12BW125', 'Failed to read')
        self.assertEqual(self.rwctest.link_setadr_drval(1, 'DR1_SF11BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getadr_drval(1), 'DR1_SF11BW125', 'Failed to read')
        self.assertEqual(self.rwctest.link_setadr_drval(1, 'DR2_SF10BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getadr_drval(1), 'DR2_SF10BW125', 'Failed to read')
        self.assertEqual(self.rwctest.link_setadr_drval(1, 'DR3_SF9BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getadr_drval(1), 'DR3_SF9BW125', 'Failed to read')
        self.assertEqual(self.rwctest.link_setadr_drval(1, 'DR4_SF8BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getadr_drval(1), 'DR4_SF8BW125', 'Failed to read')
        self.assertEqual(self.rwctest.link_setadr_drval(1, 'DR5_SF7BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getadr_drval(1), 'DR5_SF7BW125', 'Failed to read')

    def test_linkadr_txpower(self):
        self.assertEqual(self.rwctest.link_setadr_txpower(1, 5), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getadr_txpower(1), '5', 'Failed to read')

    def test_linkadr_channelmask(self):
        self.assertEqual(self.rwctest.set_mode('EDT'), 'ACK', 'EDT change mode failed.')
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'LINK_ADR'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_setadr_channelmask(1, 1, 0x7), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getadr_channelmask(1, 1), '0x07', 'Failed to read')

    def test_linkadr_maskctrl(self):
       self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'LINK_ADR'), 'ACK', 'Set Operation Failed')
       self.assertEqual(self.rwctest.link_setadr_maskctrl(1, 1, 0xff), 'ACK', 'Set Operation Failed')
       self.assertEqual(self.rwctest.link_getadr_maskctrl(1, 1), '0xff', 'Failed to read')

    def test_linkadr_morechannelmask(self):
       self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'LINK_ADR'), 'ACK', 'Set Operation Failed')
       self.assertEqual(self.rwctest.link_setadr_morechannelmask('OFF'), 'ACK', 'Set Operation Failed')
       self.assertEqual(self.rwctest.link_getadr_morechannelmask(), 'OFF', 'Failed to read')
       self.assertEqual(self.rwctest.link_setadr_morechannelmask('ON'), 'ACK', 'Set Operation Failed')
       self.assertEqual(self.rwctest.link_getadr_morechannelmask(), 'ON', 'Failed to read')

    def test_linkadr_nbtrans(self):
        self.assertEqual(self.rwctest.link_setadr_nbtrans(1,5), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getadr_nbtrans(1), '5', 'Failed to read')

    def test_linkmaxdutycycle(self):
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'DUTY_CYCLE'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_setmaxdutycycle(1, 10), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getmaxdutycycle(1), '10', 'Failed to read')

    def test_linkmaxeirp(self):
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'TX_PARAM_SETUP'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_setmaxeirp(1, 8), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getmaxeirp(1), '8', 'Failed to read')
        self.assertEqual(self.rwctest.link_setmaxeirp(1, 10), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getmaxeirp(1), '10', 'Failed to read')
        self.assertEqual(self.rwctest.link_setmaxeirp(1, 12), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getmaxeirp(1), '12', 'Failed to read')
        self.assertEqual(self.rwctest.link_setmaxeirp(1, 13), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getmaxeirp(1), '13', 'Failed to read')
        self.assertEqual(self.rwctest.link_setmaxeirp(1, 14), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getmaxeirp(1), '14', 'Failed to read')
        self.assertEqual(self.rwctest.link_setmaxeirp(1, 16), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getmaxeirp(1), '16', 'Failed to read')
        self.assertEqual(self.rwctest.link_setmaxeirp(1, 18), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getmaxeirp(1), '18', 'Failed to read')
        self.assertEqual(self.rwctest.link_setmaxeirp(1, 20), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getmaxeirp(1), '20', 'Failed to read')
        self.assertEqual(self.rwctest.link_setmaxeirp(1, 21), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getmaxeirp(1), '21', 'Failed to read')
        self.assertEqual(self.rwctest.link_setmaxeirp(1, 24), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getmaxeirp(1), '24', 'Failed to read')
        self.assertEqual(self.rwctest.link_setmaxeirp(1, 26), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getmaxeirp(1), '26', 'Failed to read')
        self.assertEqual(self.rwctest.link_setmaxeirp(1, 27), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getmaxeirp(1), '27', 'Failed to read')
        self.assertEqual(self.rwctest.link_setmaxeirp(1, 29), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getmaxeirp(1), '29', 'Failed to read')
        self.assertEqual(self.rwctest.link_setmaxeirp(1, 30), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getmaxeirp(1), '30', 'Failed to read')
        self.assertEqual(self.rwctest.link_setmaxeirp(1, 33), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getmaxeirp(1), '33', 'Failed to read')
        self.assertEqual(self.rwctest.link_setmaxeirp(1, 36), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getmaxeirp(1), '36', 'Failed to read')

    def test_linkuplinkdwelltime(self):
        self.assertEqual(self.rwctest.link_setuplinkdwelltime(1, 'NO_LIMIT'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getuplinkdwelltime(1), 'NO_LIMIT', 'Failed to read')
        self.assertEqual(self.rwctest.link_setuplinkdwelltime(1, '400ms'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getuplinkdwelltime(1), '400ms', 'Failed to read')

    def test_linkdownlinkdwelltime(self):
        self.assertEqual(self.rwctest.set_mode('EDT'), 'ACK', 'EDT change mode failed.')
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1,'TX_PARAM_SETUP'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_setdownlinkdwelltime(1, 'NO_LIMIT'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getdownlinkdwelltime(1), 'NO_LIMIT', 'Failed to read')
        self.assertEqual(self.rwctest.link_setdownlinkdwelltime(1, '400ms'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getdownlinkdwelltime(1), '400ms', 'Failed to read')

    def test_linknewchannelmode(self):
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'NEW_CHANNEL'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_setnewchannelmode(1, 'CREATE'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getnewchannelmode(1), 'CREATE', 'Failed to read')
        self.assertEqual(self.rwctest.link_setnewchannelmode(1, 'DELETE'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getnewchannelmode(1), 'DELETE', 'Failed to read')

    def test_linknewchannelindex(self):
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'NEW_CHANNEL'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_setnewchannelindex(1, 1), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getnewchannelindex(1), '1', 'Failed to read')

    def test_linknewchannel_maxdr(self):
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'NEW_CHANNEL'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_setnewchannel_maxdr(1, 1), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getnewchannel_maxdr(1), '1', 'Failed to read')

    def test_linknewchannel_mindr(self):
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'NEW_CHANNEL'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_setnewchannel_mindr(1, 1), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getnewchannel_mindr(1), '1', 'Failed to read')

    def test_linknumofmaccmd(self):
        self.assertEqual(self.rwctest.link_setnumofmaccmd(2), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getnumofmaccmd(), '2', 'Failed to read')

    def test_linkdlchannelindex(self):
        self.assertEqual(self.rwctest.set_mode('EDT'), 'ACK', 'EDT change mode failed.')
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'DL_CHANNEL'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_setdlchannelindex(1, 1), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getdlchannelindex(1), '1', 'Failed to read')

    def test_linkdlchannelfrequency(self):
        self.assertEqual(self.rwctest.link_setdlchannelfrequency(1, 865), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getdlchannelfrequency(1), '865.000000', 'Failed to read')

    def test_linkfport(self):
        self.assertEqual(self.rwctest.link_setfport(30), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getfport(), '30', 'Failed to read')

    def test_linkpayloadsize(self):
        self.assertEqual(self.rwctest.link_setpayloadsize(16), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getpayloadsize(), '16', 'Failed to read')

    def test_linkbeaconfrequency(self):
        self.assertEqual(self.rwctest.set_mode('EDT'), 'ACK', 'EDT change mode failed.')
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'BEACON_FREQ'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_setbeaconfrequency(1, 865), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getbeaconfrequency(1), '865.000000', 'Failed to read')

    def test_linkpingdatarate(self):
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'PING_SLOT_CH'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_setpingdatarate(1, 'DR0_SF12BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getpingdatarate(1), 'DR0_SF12BW125', 'Failed to read')
        self.assertEqual(self.rwctest.link_setpingdatarate(1, 'DR1_SF11BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getpingdatarate(1), 'DR1_SF11BW125', 'Failed to read')
        self.assertEqual(self.rwctest.link_setpingdatarate(1, 'DR2_SF10BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getpingdatarate(1), 'DR2_SF10BW125', 'Failed to read')
        self.assertEqual(self.rwctest.link_setpingdatarate(1, 'DR3_SF9BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getpingdatarate(1), 'DR3_SF9BW125', 'Failed to read')
        self.assertEqual(self.rwctest.link_setpingdatarate(1, 'DR4_SF8BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getpingdatarate(1), 'DR4_SF8BW125', 'Failed to read')
        self.assertEqual(self.rwctest.link_setpingdatarate(1, 'DR5_SF7BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getpingdatarate(1), 'DR5_SF7BW125', 'Failed to read')

    def test_linkpingfrequency(self):
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'PING_SLOT_CH'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_setpingfrequency(1, 865), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getpingfrequency(1), '865.000000', 'Failed to read')

    def test_linkrx2datarate(self):
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'RX_PARAM_SETUP'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_setrx2datarate(1, 'DR0_SF12BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getrx2datarate(1), 'DR0_SF12BW125', 'Failed to read')
        self.assertEqual(self.rwctest.link_setrx2datarate(1, 'DR1_SF11BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getrx2datarate(1), 'DR1_SF11BW125', 'Failed to read')
        self.assertEqual(self.rwctest.link_setrx2datarate(1, 'DR2_SF10BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getrx2datarate(1), 'DR2_SF10BW125', 'Failed to read')
        self.assertEqual(self.rwctest.link_setrx2datarate(1, 'DR3_SF9BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getrx2datarate(1), 'DR3_SF9BW125', 'Failed to read')
        self.assertEqual(self.rwctest.link_setrx2datarate(1, 'DR4_SF8BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getrx2datarate(1), 'DR4_SF8BW125', 'Failed to read')
        self.assertEqual(self.rwctest.link_setrx2datarate(1, 'DR5_SF7BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getrx2datarate(1), 'DR5_SF7BW125', 'Failed to read')
        self.assertEqual(self.rwctest.link_setrx2datarate(1, 'DR6_SF7BW250'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getrx2datarate(1), 'DR6_SF7BW250', 'Failed to read')

    def test_linkrx2frequency(self):
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'RX_PARAM_SETUP'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_setrx2frequency(1, 865), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getrx2frequency(1), '865.000000', 'Failed to read')

    def test_linkreceivedelay(self):
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'RX_TIMING_SETUP'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_setreceivedelay(1, 5), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getreceivedelay(1), '5', 'Failed to read')

    def test_linkrx1droffset(self):
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'RX_PARAM_SETUP'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_setrx1droffset(1, 1), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getrx1droffset(1), '1', 'Failed to read')

    def test_linkrejoindatarate(self):
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'FORCE_REJOIN'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_setrejoindatarate(1, 'DR0_SF12BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getrejoindatarate(1), 'DR0_SF12BW125', 'Failed to read')
        self.assertEqual(self.rwctest.link_setrejoindatarate(1, 'DR1_SF11BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getrejoindatarate(1), 'DR1_SF11BW125', 'Failed to read')
        self.assertEqual(self.rwctest.link_setrejoindatarate(1, 'DR2_SF10BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getrejoindatarate(1), 'DR2_SF10BW125', 'Failed to read')
        self.assertEqual(self.rwctest.link_setrejoindatarate(1, 'DR3_SF9BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getrejoindatarate(1), 'DR3_SF9BW125', 'Failed to read')
        self.assertEqual(self.rwctest.link_setrejoindatarate(1, 'DR4_SF8BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getrejoindatarate(1), 'DR4_SF8BW125', 'Failed to read')
        self.assertEqual(self.rwctest.link_setrejoindatarate(1, 'DR5_SF7BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getrejoindatarate(1), 'DR5_SF7BW125', 'Failed to read')
        self.assertEqual(self.rwctest.link_setrejoindatarate(1, 'DR6_SF7BW250'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getrejoindatarate(1), 'DR6_SF7BW250', 'Failed to read')

    def test_linkrejointype(self):
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'FORCE_REJOIN'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_setrejointype(1, 'TYPE_0'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getrejointype(1), 'TYPE_0', 'Failed to read')
        self.assertEqual(self.rwctest.link_setrejointype(1, 'TYPE_2'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getrejointype(1), 'TYPE_2', 'Failed to read')

    def test_linkrejoinretry(self):
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'FORCE_REJOIN'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_setrejoinretry(1, 2), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getrejoinretry(1), '2', 'Failed to read')

    def test_linkrejoinperiod(self):
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'FORCE_REJOIN'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_setrejoinperiod(1, 2), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getrejoinperiod(1), '2', 'Failed to read')

    def test_linkrejoinmaxtime(self):
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'REJOIN_SETUP'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_setrejoinmaxtime(1, 10), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getrejoinmaxtime(1), '10', 'Failed to read')

    def test_linkrejoinmaxcnt(self):
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'REJOIN_SETUP'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_setrejoinmaxcnt(1, 10), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getrejoinmaxcnt(1), '10', 'Failed to read')

    def test_linkadrlimitexp(self):
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'ADR_SETUP'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_setadrlimitexp(1, 5), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getadrlimitexp(1), '5', 'Failed to read')

    def test_linkadrdelayexp(self):
        self.assertEqual(self.rwctest.set_mode('EDT'), 'ACK', 'EDT change mode failed.')
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'ADR_SETUP'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_setadrdelayexp(1, 5), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getadrdelayexp(1), '5', 'Failed to read')

    def test_linktimedisplay(self):
        self.assertEqual(self.rwctest.link_settimedisplay('OFF'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_gettimedisplay(), 'OFF', 'Failed to read')
        self.assertEqual(self.rwctest.link_settimedisplay('ON'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_gettimedisplay(), 'ON', 'Failed to read')

    def test_linkfcntdisplay(self):
        self.assertEqual(self.rwctest.link_setfcntdisplay('OFF'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getfcntdisplay(), 'OFF', 'Failed to read')
        self.assertEqual(self.rwctest.link_setfcntdisplay('ON'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getfcntdisplay(), 'ON', 'Failed to read')

    def test_linkadrdisplay(self):
        self.assertEqual(self.rwctest.link_setadrdisplay('OFF'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getadrdisplay(), 'OFF', 'Failed to read')
        self.assertEqual(self.rwctest.link_setadrdisplay('ON'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getadrdisplay(), 'ON', 'Failed to read')

    def test_linkackdisplay(self):
        self.assertEqual(self.rwctest.link_setackdisplay('OFF'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getackdisplay(), 'OFF', 'Failed to read')
        self.assertEqual(self.rwctest.link_setackdisplay('ON'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getackdisplay(), 'ON', 'Failed to read')

    def test_linkclassb_display(self):
        self.assertEqual(self.rwctest.link_setclassb_display('OFF'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getclassb_display(), 'OFF', 'Failed to read')
        self.assertEqual(self.rwctest.link_setclassb_display('ON'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getclassb_display(), 'ON', 'Failed to read')

    def test_linkportdisplay(self):
        self.assertEqual(self.rwctest.link_setportdisplay('OFF'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getportdisplay(), 'OFF', 'Failed to read')
        self.assertEqual(self.rwctest.link_setportdisplay('ON'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getportdisplay(), 'ON', 'Failed to read')

    def test_linkmsgtypedisplay(self):
        self.assertEqual(self.rwctest.link_setmsgtypedisplay('OFF'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getmsgtypedisplay(), 'OFF', 'Failed to read')
        self.assertEqual(self.rwctest.link_setmsgtypedisplay('ON'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getmsgtypedisplay(), 'ON', 'Failed to read')

    def test_linkpowerdisplay(self):
        self.assertEqual(self.rwctest.link_setpowerdisplay('OFF'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getpowerdisplay(), 'OFF', 'Failed to read')
        self.assertEqual(self.rwctest.link_setpowerdisplay('ON'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getpowerdisplay(), 'ON', 'Failed to read')

    def test_linkdrdisplay(self):
        self.assertEqual(self.rwctest.link_setdrdisplay('OFF'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getdrdisplay(), 'OFF', 'Failed to read')
        self.assertEqual(self.rwctest.link_setdrdisplay('ON'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getdrdisplay(), 'ON', 'Failed to read')

    def test_linkdelaydisplay(self):
        self.assertEqual(self.rwctest.link_setdelaydisplay('OFF'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getdelaydisplay(), 'OFF', 'Failed to read')
        self.assertEqual(self.rwctest.link_setdelaydisplay('ON'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getdelaydisplay(), 'ON', 'Failed to read')

    def test_linkadrackreq_display(self):
        self.assertEqual(self.rwctest.link_setadrackreq_display('OFF'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getadrackreq_display(), 'OFF', 'Failed to read')
        self.assertEqual(self.rwctest.link_setadrackreq_display('ON'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getadrackreq_display(), 'ON', 'Failed to read')

    def test_linkfpendingdisplay(self):
        self.assertEqual(self.rwctest.link_setfpendingdisplay('OFF'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getfpendingdisplay(), 'OFF', 'Failed to read')
        self.assertEqual(self.rwctest.link_setfpendingdisplay('ON'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getfpendingdisplay(), 'ON', 'Failed to read')

    def test_linkdwelldisplay(self):
        self.assertEqual(self.rwctest.link_setdwelldisplay('OFF'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getdwelldisplay(), 'OFF', 'Failed to read')
        self.assertEqual(self.rwctest.link_setdwelldisplay('ON'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getdwelldisplay(), 'ON', 'Failed to read')

    def test_linkpayloadlength(self):
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'ECHO_REQUEST_TM'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_setpayloadlength(1, 200), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getpayloadlength(1), '200', 'Failed to read')

    def test_linkechopayload(self):
        self.assertEqual(self.rwctest.link_setinstantmaccmd(1, 'ECHO_REQUEST_TM'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_setechopayload(1, 0x000102), 'ACK', 'Set Echo Payload Failed')
        self.assertEqual(self.rwctest.link_getechopayload(1), '000102', 'Set Echo Payload Failed')

    def test_linkcwtimeout(self):
        self.assertEqual(self.rwctest.link_setcwtimeout(1, 10), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getcwtimeout(1), '10', 'Failed to read')

    def test_linkcwfrequency(self):
        self.assertEqual(self.rwctest.link_setcwfrequency(1, 900), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getcwfrequency(1), '900.0000', 'Failed to read')

    def test_linkcwpower(self):
        self.assertEqual(self.rwctest.link_setcwpower(1, 25), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.link_getcwpower(1), '25', 'Failed to read')
    
    # Test Cases for Power Channel Command Methods
    def test_powscalemode(self):
        self.assertEqual(self.rwctest.power_setscalemode('AUTO'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.power_getscalemode(), 'AUTO', 'Failed to read')
        self.assertEqual(self.rwctest.power_setscalemode('MANUAL'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.power_getscalemode(), 'MANUAL', 'Failed to read')

    def test_powmaxyvalue(self):
        self.assertEqual(self.rwctest.power_setmaxyvalue(20), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.power_getmaxyvalue(), '20', 'Failed to read')

    def test_powminyvalue(self):
        self.assertEqual(self.rwctest.power_setminyvalue(-30), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.power_getminyvalue(), '-20', 'Failed to read')

    def test_powertargetchmask(self):
        self.assertEqual(self.rwctest.power_settargetchmask(0x00000000000000000000000000000001), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.power_gettargetchmask(), '0x01', 'Failed to read')

    def test_powermode(self):
        self.assertEqual(self.rwctest.power_setmode('SYNC_TO_LINK'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.power_getmode(), 'SYNC_TO_LINK', 'Failed to read')
        self.assertEqual(self.rwctest.power_setmode('SCENARIO'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.power_getmode(), 'SCENARIO', 'Failed to read')

    def test_powerscenario(self):
        self.assertEqual(self.rwctest.power_setscenario('NORMAL_UL'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.power_getscenario(), 'NORMAL_UL', 'Failed to read')
        self.assertEqual(self.rwctest.power_setscenario('CERTI_UL'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.power_getscenario(), 'CERTI_UL', 'Failed to read')
        self.assertEqual(self.rwctest.power_setscenario('CERTI_CW'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.power_getscenario(), 'CERTI_CW', 'Failed to read')

    def test_poweradr(self):
        self.assertEqual(self.rwctest.power_setadrpower(2), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.power_getadrpower(), '2', 'Failed to read')

    def test_poweruldatarate(self):
        self.assertEqual(self.rwctest.power_setuldatarate('DR0_SF12BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.power_getuldatarate(), 'DR0_SF12BW125', 'Failed to read')
        self.assertEqual(self.rwctest.power_setuldatarate('DR1_SF11BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.power_getuldatarate(), 'DR1_SF11BW125', 'Failed to read')
        self.assertEqual(self.rwctest.power_setuldatarate('DR2_SF10BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.power_getuldatarate(), 'DR2_SF10BW125', 'Failed to read')
        self.assertEqual(self.rwctest.power_setuldatarate('DR3_SF9BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.power_getuldatarate(), 'DR3_SF9BW125', 'Failed to read')
        self.assertEqual(self.rwctest.power_setuldatarate('DR4_SF8BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.power_getuldatarate(), 'DR4_SF8BW125', 'Failed to read')
        self.assertEqual(self.rwctest.power_setuldatarate('DR5_SF7BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.power_getuldatarate(), 'DR5_SF7BW125', 'Failed to read')
        self.assertEqual(self.rwctest.power_setuldatarate('DR6_SF7BW250'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.power_getuldatarate(), 'DR6_SF7BW250', 'Failed to read')
        self.assertEqual(self.rwctest.power_setuldatarate('DR7_FSK50'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.power_getuldatarate(), 'DR7_FSK50', 'Failed to read')

    def test_powerpacketnum(self):
        self.assertEqual(self.rwctest.power_setpacketnum(5), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.power_getpacketnum(), '5', 'Failed to read')

    # Test Cases for Sensitivity Command Methods
    def test_sensitivityopmode(self):
        self.assertEqual(self.rwctest.sensitivity_setopmode('CERTI_ECHO'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.sensitivity_getopmode(), 'CERTI_ECHO', 'Failed to read')
        self.assertEqual(self.rwctest.sensitivity_setopmode('NORMAL_UL'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.sensitivity_getopmode(), 'NORMAL_UL', 'Failed to read')

    def test_sensitivitypacketnum(self):
        self.assertEqual(self.rwctest.sensitivity_setpacketnum(100), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.sensitivity_getpacketnum(), '100', 'Failed to read')

    def test_sensitivitystartpower(self):
        self.assertEqual(self.rwctest.sensitivity_setstartpower(-40), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.sensitivity_getstartpower(), '-40.0', 'Failed to read')

    def test_sensitivitynumpower(self):
        self.assertEqual(self.rwctest.sensitivity_setnumpower(20), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.sensitivity_getnumpower(), '20', 'Failed to read')

    def test_sensitivitysteppower(self):
        self.assertEqual(self.rwctest.sensitivity_setsteppower(20), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.sensitivity_getsteppower(), '20.0', 'Failed to read')

    def test_sensitivitytargetpower(self):
        self.assertEqual(self.rwctest.sensitivity_settargetpower(0.1), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.sensitivity_gettargetpower(), '0.100', 'Failed to read')

    def test_sensitivitydownlinkslot(self):
        self.assertEqual(self.rwctest.set_mode('EDT'), 'ACK', 'EDT change mode failed.')
        self.assertEqual(self.rwctest.sensitivity_setdownlinkslot('RX1'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.sensitivity_getdownlinkslot(), 'RX1', 'Failed to read')
        self.assertEqual(self.rwctest.sensitivity_setdownlinkslot('RX2'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.sensitivity_getdownlinkslot(), 'RX2', 'Failed to read')
        self.assertEqual(self.rwctest.protocol_setclass('B'), 'ACK', 'Set Class Failed')
        self.assertEqual(self.rwctest.sensitivity_setdownlinkslot('PING'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.sensitivity_getdownlinkslot(), 'PING', 'Failed to read')

        self.assertEqual(self.rwctest.set_mode('GWT'), 'ACK', 'GWT change mode failed.')
        self.assertEqual(self.rwctest.sensitivity_setdownlinkslot('RX1'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.sensitivity_getdownlinkslot(), 'RX1', 'Failed to read')
        self.assertEqual(self.rwctest.sensitivity_setdownlinkslot('RX2'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.sensitivity_getdownlinkslot(), 'RX2', 'Failed to read')
        self.assertEqual(self.rwctest.sensitivity_setdownlinkslot('RX1&RX2'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.sensitivity_getdownlinkslot(), 'RX1&RX2', 'Failed to read')

    def test_sensitivitytargetdr(self):
        self.assertEqual(self.rwctest.sensitivity_settargetdr('DR0_SF12BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.sensitivity_gettargetdr(), 'DR0_SF12BW125', 'Failed to read')
        self.assertEqual(self.rwctest.sensitivity_settargetdr('DR1_SF11BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.sensitivity_gettargetdr(), 'DR1_SF11BW125', 'Failed to read')
        self.assertEqual(self.rwctest.sensitivity_settargetdr('DR2_SF10BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.sensitivity_gettargetdr(), 'DR2_SF10BW125', 'Failed to read')
        self.assertEqual(self.rwctest.sensitivity_settargetdr('DR3_SF9BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.sensitivity_gettargetdr(), 'DR3_SF9BW125', 'Failed to read')
        self.assertEqual(self.rwctest.sensitivity_settargetdr('DR4_SF8BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.sensitivity_gettargetdr(), 'DR4_SF8BW125', 'Failed to read')
        self.assertEqual(self.rwctest.sensitivity_settargetdr('DR5_SF7BW125'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.sensitivity_gettargetdr(), 'DR5_SF7BW125', 'Failed to read')

    def test_sensitivitytargetdlch(self):
        self.assertEqual(self.rwctest.sensitivity_settargetdlch(1, 900), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.sensitivity_gettargetdlch(1), '900.000000', 'Failed to read')
        
    def test_sensitivityfport(self):
        self.assertEqual(self.rwctest.sensitivity_setfport(200), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.sensitivity_getfport(), '200', 'Failed to read')

    def test_sensitivitypayloadsize(self):
        self.assertEqual(self.rwctest.sensitivity_setpayloadsize(16), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.sensitivity_getpayloadsize(), '16', 'Failed to read')
    
    # Test Cases for NST Command Methods
    def test_nsttx_repeatnum(self):
        self.assertEqual(self.rwctest.nst_tx_setrepeatnum(100), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_tx_getrepeatnum(), '100', 'Failed to read')

    def test_nsttx_mode(self):
        self.assertEqual(self.rwctest.nst_tx_setmode('LORA'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_tx_getmode(), 'LORA', 'Failed to read')
        self.assertEqual(self.rwctest.nst_tx_setmode('FSK'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_tx_getmode(), 'FSK', 'Failed to read')
        self.assertEqual(self.rwctest.nst_tx_setmode('CW'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_tx_getmode(), 'CW', 'Failed to read')

    def test_nsttx_interval(self):
        self.assertEqual(self.rwctest.nst_tx_setinterval(0.5), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_tx_getinterval(), '0.500', 'Failed to read')

    def test_nsttx_bw(self):
        self.assertEqual(self.rwctest.nst_tx_setbw(125), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_tx_getbw(), '125', 'Failed to read')

    def test_nsttx_sf(self):
        self.assertEqual(self.rwctest.nst_tx_setsf('SF7'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_tx_getsf(), 'SF7', 'Failed to read')
        self.assertEqual(self.rwctest.nst_tx_setsf('SF8'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_tx_getsf(), 'SF8', 'Failed to read')
        self.assertEqual(self.rwctest.nst_tx_setsf('SF9'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_tx_getsf(), 'SF9', 'Failed to read')
        self.assertEqual(self.rwctest.nst_tx_setsf('SF10'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_tx_getsf(), 'SF10', 'Failed to read')
        self.assertEqual(self.rwctest.nst_tx_setsf('SF11'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_tx_getsf(), 'SF11', 'Failed to read')
        self.assertEqual(self.rwctest.nst_tx_setsf('SF12'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_tx_getsf(), 'SF12', 'Failed to read')

    def test_nsttx_cr(self):
        self.assertEqual(self.rwctest.nst_tx_setcr('4_5'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_tx_getcr(), '4_5', 'Failed to read')
        self.assertEqual(self.rwctest.nst_tx_setcr('4_6'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_tx_getcr(), '4_6', 'Failed to read')
        self.assertEqual(self.rwctest.nst_tx_setcr('4_7'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_tx_getcr(), '4_7', 'Failed to read')
        self.assertEqual(self.rwctest.nst_tx_setcr('4_8'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_tx_getcr(), '4_8', 'Failed to read')
        self.assertEqual(self.rwctest.nst_tx_setcr('NO_CRC'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_tx_getcr(), 'NO_CRC', 'Failed to read')

    def test_nsttx_preamblesize(self):
        self.assertEqual(self.rwctest.nst_tx_setpreamblesize(2), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_tx_getpreamblesize(), '2', 'Failed to read')

    def test_nsttx_payloadsize(self):
        self.assertEqual(self.rwctest.nst_tx_setpayloadsize(16), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_tx_getpayloadsize(), '16', 'Failed to read')

    def test_nsttx_nwktype(self):
        self.assertEqual(self.rwctest.nst_tx_setnwktype('PRIVATE'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_tx_getnwktype(), 'PRIVATE', 'Failed to read')
        self.assertEqual(self.rwctest.nst_tx_setnwktype('PUBLIC'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_tx_getnwktype(), 'PUBLIC', 'Failed to read')

    def test_nstrx_mode(self):
        self.assertEqual(self.rwctest.nst_rx_setmode('LORA'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_rx_getmode(), 'LORA', 'Failed to read')
        self.assertEqual(self.rwctest.nst_rx_setmode('FSK'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_rx_getmode(), 'FSK', 'Failed to read')

    def test_nstrx_bw(self):
        self.assertEqual(self.rwctest.nst_rx_setbw(500), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_rx_getbw(), '500', 'Failed to read')
        self.assertEqual(self.rwctest.nst_rx_setbw(250), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_rx_getbw(), '250', 'Failed to read')
        self.assertEqual(self.rwctest.nst_rx_setbw(125), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_rx_getbw(), '125', 'Failed to read')

    def test_nstrx_sf(self):
        self.assertEqual(self.rwctest.nst_rx_setsf('SF7'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_rx_getsf(), 'SF7', 'Failed to read')
        self.assertEqual(self.rwctest.nst_rx_setsf('SF8'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_rx_getsf(), 'SF8', 'Failed to read')
        self.assertEqual(self.rwctest.nst_rx_setsf('SF9'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_rx_getsf(), 'SF9', 'Failed to read')
        self.assertEqual(self.rwctest.nst_rx_setsf('SF10'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_rx_getsf(), 'SF10', 'Failed to read')
        self.assertEqual(self.rwctest.nst_rx_setsf('SF11'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_rx_getsf(), 'SF11', 'Failed to read')
        self.assertEqual(self.rwctest.nst_rx_setsf('SF12'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_rx_getsf(), 'SF12', 'Failed to read')
        self.assertEqual(self.rwctest.nst_rx_setsf('ANY'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_rx_getsf(), 'ANY', 'Failed to read')

    def test_nstrx_nwktype(self):
        self.assertEqual(self.rwctest.nst_rx_setnwktype('PRIVATE'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_rx_getnwktype(), 'PRIVATE', 'Failed to read')
        self.assertEqual(self.rwctest.nst_rx_setnwktype('PUBLIC'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_rx_getnwktype(), 'PUBLIC', 'Failed to read')

    def test_nstmfg_timeout(self):
        self.assertEqual(self.rwctest.nst_mfg_settimeout(20), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_mfg_gettimeout(), '20', 'Failed to read')

    def test_nstmfg_mode(self):
        self.assertEqual(self.rwctest.nst_mfg_setmode('LORA'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_mfg_getmode(), 'LORA', 'Failed to read')
        self.assertEqual(self.rwctest.nst_mfg_setmode('FSK'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_mfg_getmode(), 'FSK', 'Failed to read')

    def test_nstmfg_interval(self):
        self.assertEqual(self.rwctest.nst_mfg_setinterval(0.1), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_mfg_getinterval(), '0.100', 'Failed to read')

    def test_nstmfg_bw(self):
        self.assertEqual(self.rwctest.nst_mfg_setbw(500), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_mfg_getbw(), '500', 'Failed to read')
        self.assertEqual(self.rwctest.nst_mfg_setbw(250), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_mfg_getbw(), '250', 'Failed to read')
        self.assertEqual(self.rwctest.nst_mfg_setbw(125), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_mfg_getbw(), '125', 'Failed to read')

    def test_nstmfg_sf(self):
        self.assertEqual(self.rwctest.nst_mfg_setsf('SF7'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_mfg_getsf(), 'SF7', 'Failed to read')
        self.assertEqual(self.rwctest.nst_mfg_setsf('SF8'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_mfg_getsf(), 'SF8', 'Failed to read')
        self.assertEqual(self.rwctest.nst_mfg_setsf('SF9'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_mfg_getsf(), 'SF9', 'Failed to read')
        self.assertEqual(self.rwctest.nst_mfg_setsf('SF10'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_mfg_getsf(), 'SF10', 'Failed to read')
        self.assertEqual(self.rwctest.nst_mfg_setsf('SF11'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_mfg_getsf(), 'SF11', 'Failed to read')
        self.assertEqual(self.rwctest.nst_mfg_setsf('SF12'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_mfg_getsf(), 'SF12', 'Failed to read')
        self.assertEqual(self.rwctest.nst_mfg_setsf('ANY'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_mfg_getsf(), 'ANY', 'Failed to read')

    def test_nstmfg_cr(self):
        self.assertEqual(self.rwctest.nst_mfg_setcr('4_5'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_mfg_getcr(), '4_5', 'Failed to read')
        self.assertEqual(self.rwctest.nst_mfg_setcr('4_6'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_mfg_getcr(), '4_6', 'Failed to read')
        self.assertEqual(self.rwctest.nst_mfg_setcr('4_7'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_mfg_getcr(), '4_7', 'Failed to read')
        self.assertEqual(self.rwctest.nst_mfg_setcr('4_8'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_mfg_getcr(), '4_8', 'Failed to read')
        self.assertEqual(self.rwctest.nst_mfg_setcr('NO_CRC'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_mfg_getcr(), 'NO_CRC', 'Failed to read')

    def test_nstmfg_payloadsize(self):
        self.assertEqual(self.rwctest.nst_mfg_setpayloadsize(16), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_mfg_getpayloadsize(), '16', 'Failed to read')

    def test_nstmfg_preamblesize(self):
        self.assertEqual(self.rwctest.nst_mfg_setpreamblesize(8), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_mfg_getpreamblesize(), '8', 'Failed to read')

    def test_nstmfg_repeatnum(self):
        self.assertEqual(self.rwctest.nst_mfg_setrepeatnum(10), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_mfg_getrepeatnum(), '10', 'Failed to read')

    def test_nstmfg_nwktype(self):
        self.assertEqual(self.rwctest.nst_mfg_setnwktype('PRIVATE'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_mfg_getnwktype(), 'PRIVATE', 'Failed to read')
        self.assertEqual(self.rwctest.nst_mfg_setnwktype('PUBLIC'), 'ACK', 'Set Operation Failed')
        self.assertEqual(self.rwctest.nst_mfg_getnwktype(), 'PUBLIC', 'Failed to read')

    # Test Cases for System Command Methods
    def test_querysysversion(self):
        self.assertEqual(self.rwctest.query_sysversion(), '1.222', 'Reading System Software Version Failed.')

    def test_sysreferenceclock(self):
        self.assertEqual(self.rwctest.sys_setreferenceclock('INT'), 'ACK', 'Setting System Reference Clock Failed.')
        self.assertEqual(self.rwctest.sys_getreferenceclock(), 'INT', 'Reading System Reference Clock Failed.')

        self.assertEqual(self.rwctest.sys_setreferenceclock('EXT'), 'ACK', 'Setting System Reference Clock Failed.')
        self.assertEqual(self.rwctest.sys_getreferenceclock(), 'EXT', 'Reading System Reference Clock Failed.')

    def test_sysserialnum(self):
        self.assertEqual(self.rwctest.query_sysserialnum(), '0x1760009', 'Reading System Serial Number Failed.')

    def test_sysgwtoptinfo(self):
        self.assertEqual(self.rwctest.query_gwtoptinfo(), 'ON', 'Reading System Software Option Info Failed.')

    def test_sysedtoptinfo(self):
        self.assertEqual(self.rwctest.query_edtoptinfo(), 'ON', 'Reading System Software Option Info Failed.')

    def test_sysnstoptinfo(self):
        self.assertEqual(self.rwctest.query_nstoptinfo(), 'ON', 'Reading System Software Option Info Failed.')

    def test_syseucertoptinfo(self):
        self.assertEqual(self.rwctest.query_eucertoptinfo(), 'ON', 'Reading System Software Option Info Failed.')

    def test_syssktcertoptinfo(self):
        self.assertEqual(self.rwctest.query_sktcertoptinfo(), 'ON', 'Reading System Software Option Info Failed.')

    def test_sysuscertoptinfo(self):
        self.assertEqual(self.rwctest.query_uscertoptinfo(), 'ON', 'Reading System Software Option Info Failed.')

    def test_sysascertoptinfo(self):
        self.assertEqual(self.rwctest.query_ascertoptinfo(), 'ON', 'Reading System Software Option Info Failed.')

    def test_syskrcertoptinfo(self):
        self.assertEqual(self.rwctest.query_krcertoptinfo(), 'ON', 'Reading System Software Option Info Failed.')
    
    @classmethod
    def tearDownClass(self):
        self.assertTrue(self.rwctest.close_port(), 'Failed to close the port')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        myport = sys.argv[1]
    else:
        sys.exit('ERROR: When passing command line argument.')
    del sys.argv[1:]
    unittest.main(verbosity=2)
