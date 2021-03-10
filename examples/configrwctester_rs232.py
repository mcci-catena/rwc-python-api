##############################################################################
# 
# Module: configrwctester_rs232.py
#
# Description:
#     Script to perform link analyzer test by accessing RWC tester library
#     through RS232 serial communincation
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

import sys
import time
import os

sys.path.insert(0, os.path.abspath('..'))
from rwclib.cRWC5020x import RWCTesterApi

class LinkAnalyzerTest(RWCTesterApi):

    def __init__(self, port, addr = None):
        '''
        Opens port
        '''
        RWCTesterApi.__init__(self, port, addr)
        RWCTesterApi.open_port(self)
        
    def config_link_screen(self):
        '''
        Setting the test mode and sub screen
        '''
        screenparamdict = {'testmode' : 'EDT', 'submenu' : 'LINK'}

        print('Setting up Test Mode to EDT', end='\n')
        RWCTesterApi.set_mode(self, screenparamdict.get('testmode'))
        mymode = RWCTesterApi.query_mode(self)
        print('Test Mode: {}'.format(mymode), end='\n\n')
    
        RWCTesterApi.set_screen(self, screenparamdict.get('submenu'))


    def config_protocol(self):
        '''
        Configuring protocol parameters
        '''
        protocolparamdict = {'region' : 'IN_866', 'ver' : 'LoRaWAN1.0.2',
                         'class' : 'A', 'activation' : 'OTAA',
                         'setmode' : 'ON', 'appkey' : 0x01,
                         'chkeui' : 'NO'}

        print('Setting up PROTOCOL parameters', end='\n')
        RWCTesterApi.protocol_setregion(self, protocolparamdict.get('region'))
        myregion = RWCTesterApi.protocol_getregion(self)
        print('Protocol Region: {}'.format(myregion), end='\n')
    
        RWCTesterApi.protocol_setprotocolver(
            self, 
            protocolparamdict.get('ver'))
        myprotocolver = RWCTesterApi.protocol_getprotocolver(self)
        print('Protocol Version: {}'.format(myprotocolver), end='\n')
    
        RWCTesterApi.protocol_setclass(self, protocolparamdict.get('class'))
        myprotocolclass = RWCTesterApi.protocol_getclass(self)
        print('Protocol Class: {}'.format(myprotocolclass), end='\n')
    
        RWCTesterApi.protocol_setactivationprocedure(
            self, 
            protocolparamdict.get('activation'))
        myacttype = RWCTesterApi.protocol_getactivationprocedure(self)
        print('Protocol Activation Procedure: {}'.format(myacttype), end='\n')
    
        RWCTesterApi.protocol_settestmodeflag(
            self, 
            protocolparamdict.get('setmode'))
        mymodestat = RWCTesterApi.protocol_gettestmodeflag(self)
        print('Protocol Test Mode Status: {}'.format(mymodestat), end='\n')
    
        RWCTesterApi.protocol_setappkey(self, protocolparamdict.get('appkey'))
        myappkey = RWCTesterApi.protocol_getappkey(self)
        print('Protocol App Key: {}'.format(myappkey), end='\n')
    
        RWCTesterApi.protocol_seteuiflag(self, protocolparamdict.get('chkeui'))
        myeuiflag = RWCTesterApi.protocol_geteuiflag(self)
        print('Protocol EUI Check: {}'.format(myeuiflag), end='\n\n')

    def config_rf(self):
        '''
        Configuring RF Parameter settings
        '''
        rfparamdict = {'txpow' : -30, 'pathloss' : 0, 'freqoffset' : 0,
                   'timeoffset' : 0}

        print('Setting up RF parameters', end='\n')
        RWCTesterApi.rf_settxpower(self, rfparamdict.get('txpow'))
        mytxpow = RWCTesterApi.rf_gettxpower(self)
        print('RF Tx Power: {}'.format(mytxpow), end='\n')
    
        RWCTesterApi.rf_setpathloss(self, rfparamdict.get('pathloss'))
        mypathlossrng = RWCTesterApi.rf_getpathloss(self)
        print('RF Path Loss: {}'.format(mypathlossrng), end='\n')
    
        RWCTesterApi.rf_setfreqoffset(self, rfparamdict.get('freqoffset'))
        myrffreqoffset = RWCTesterApi.rf_getfreqoffset(self)
        print('RF Frequency Offset: {}'.format(myrffreqoffset), end='\n')
    
        RWCTesterApi.rf_settimeoffset(self, rfparamdict.get('timeoffset'))
        mytimeoffset = RWCTesterApi.rf_gettimeoffset(self)
        print('RF Time Offset: {}'.format(mytimeoffset), end='\n\n')

    def config_mac(self):
        '''
        Configuring MAC settings
        '''
        macparamdict = {
            'cmdno' : 2, 
            'mac' : {1 : 'DEV_STATUS', 2 : 'DUTY_CYCLE'},
            'mactype' : 'UNCONFIRMED', 
            'macfield' : 'PAYLOAD'}

        print('Setting up MAC parameters', end='\n')
        RWCTesterApi.link_setnumofmaccmd(self, macparamdict.get('cmdno'))
        mymaccmdno = RWCTesterApi.link_getnumofmaccmd(self)
        print('Number of MAC Command: {}'.format(mymaccmdno), end='\n')

        for key in macparamdict['mac']:
            RWCTesterApi.link_setinstantmaccmd(
                self, 
                key, 
                macparamdict['mac'][key])
            mymac = RWCTesterApi.link_getinstantmaccmd(self, key)
            print(
                'MAC DUT Command {} : {}'.format(key, macparamdict['mac'][key]), 
                end='\n')
    
        RWCTesterApi.link_setmaccmdtype(self, macparamdict.get('mactype'))
        mymactype = RWCTesterApi.link_getmaccmdtype(self)
        print('MAC Command Type : {}'.format(mymactype), end='\n')
    
        RWCTesterApi.link_setmaccmdfield(self, macparamdict.get('macfield'))
        mymacfield = RWCTesterApi.link_getmaccmdfield(self)
        print('MAC Command Field : {}'.format(mymacfield), end='\n\n')

    def exec_link(self):
        '''
        To start the link test
        '''
        print('Executing Link Analyzer Test', end='\n')
        time.sleep(1)
        result = RWCTesterApi.link_run(self)
        print(result, end='\n')

    def exec_mac(self):
        '''
        To send MAC command
        '''
        print('Executing MAC Command', end='\n')
        time.sleep(1)
        result = RWCTesterApi.link_sendmac(self)
        print(result, end='\n')

    def mv_submenu(self):
        '''
        To move between other sub menus
        '''
        submenudict = {
            'time' : 'POWER_TIME', 
            'channel' : 'POWER_CHANNEL', 
            'analyzer' : 'LINK'}
        RWCTesterApi.set_screen(self, submenudict.get('time'))
        RWCTesterApi.set_screen(self, submenudict.get('channel'))
        RWCTesterApi.set_screen(self, submenudict.get('analyzer'))

    def stop_link(self):
        '''
        Stop the test
        '''
        print('Stop Link Analyzer Test', end='\n')
        result = RWCTesterApi.link_stop(self)
        print(result, end='\n')

    def close(self):
        '''
        Closes the port
        '''
        RWCTesterApi.close_port(self)

if __name__ == '__main__':
    
    myobj = LinkAnalyzerTest('COM12')    # Change the serial port accordingly for RS232 communication
    myobj.config_link_screen()
    myobj.config_protocol()
    myobj.config_rf()
    myobj.config_mac()
    myobj.exec_link()
    myobj.exec_mac()
    myobj.exec_mac()
    myobj.mv_submenu()
    myobj.stop_link()
    myobj.close()
