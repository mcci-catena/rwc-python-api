##############################################################################
# 
# Module: eucerttest_5_3_ethernet.py
#
# Description:
#     Script to perform EU certification 5.3 test through ethernet
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

import os, sys
import time

sys.path.insert(0, os.path.abspath('..'))

from rwclib.cRWC5020x import RWCTesterApi

def debug(msg):
    '''
    Display debug message
    '''
    print(msg, end='\n')
    return True

def err(msg):
    '''
    Display error message
    '''
    print(msg, end='\n')

def fatal(msg):
    '''
    Exit on error
    '''
    err(msg)
    print('\nTest Result: FAIL')
    sys.exit(1)
    
def exec_link():
    '''
    To start link test
    '''
    result = ob.link_run()
    if result:
        if result == 'ACK':
            debug('Link Status: Running\n')
        else:
            fatal('Link execution failed\n')
    else:
        fatal('Tester returns none and connection timed-out\n')
    return True

def clear_link():
    '''
    Clear existing link messages
    '''
    result = ob.link_clear()
    if result:
        if result == 'ACK':
            debug('Old link messages cleared\n')
        else:
            fatal('Clear link message failed\n')
    else:
        fatal('Tester returns none and connection timed-out\n')
    return True

def set_dlslot(slot):
    '''
    Configure downlink slot
    '''
    result = ob.protocol_setdownlinkslot(slot)
    if result:
        if result == 'ACK':
            debug('Protocol Downlink Slot: {}'.format(slot))
        else:
            fatal('Configuring downlink slot failed')
    else:
        fatal('Tester returns none and connection timed-out')
    return True

def set_mactype():
    '''
    Configure MAC command type
    '''
    mactype = 'UNCONFIRMED'
    result = ob.link_setmaccmdtype(mactype)
    if result:
        if result == 'ACK':
            debug('Link MAC Command Type: {}'.format(mactype))
        else:
            fatal('Configuring MAC command type failed\n')
    else:
        fatal('Tester returns none and connection timed-out\n')
    return True

def set_maccmdfield():
    '''
    Configure MAC command field
    '''
    maccmdfield = 'PAYLOAD'
    result = ob.link_setmaccmdfield(maccmdfield)
    if result:
        if result == 'ACK':
            debug('Link MAC Command Field: {}'.format(maccmdfield))
        else:
            fatal('Configuring MAC command field failed\n')
    else:
        fatal('Tester returns none and connection timed-out\n')
    return True

def set_numofcmd():
    '''
    Configure number of MAC command
    '''
    num = 1
    result = ob.link_setnumofmaccmd(num)
    if result:
        if result == 'ACK':
            debug('Link Number of Command: {}'.format(num))
        else:
            fatal('Configuring no. of commands failed\n')
    else:
        fatal('Tester returns none and connection timed-out\n')
    return True

def instant_mac_cmd(num, maccmd):
    '''
    Configure instant MAC command
    '''
    result = ob.link_setinstantmaccmd(num, maccmd)
    if result:
        if result == 'ACK':
            debug('Link Instant MAC Command: {}\n'.format(maccmd))
        else:
            fatal('Configuring instant MAC command failed\n')
    else:
        fatal('Tester returns none and connection timed-out\n')
    return True

def set_echolen(length):
    '''
    Configure payload length
    '''
    result = ob.link_setpayloadlength(1, length)
    if result:
        if result == 'ACK':
            debug('Set Bytes: {}'.format(length))
        else:
            fatal('Configuring bytes length failed\n')
    else:
        fatal('Tester returns none and connection timed-out\n')
    return True

def set_droffset(val):
    '''
    Configure RX1 data rate offset
    '''
    result = ob.protocol_setrx1_dr_offset(val)
    if result:
        if result == 'ACK':
            debug('Protocol RX1_DR_OFFSET value: {}'.format(val))
        else:
            fatal('Configuring RX1_DR_OFFSET failed\n')
    else:
        fatal('Tester returns none and connection timed-out\n')
    return True

def set_dr(val):
    '''
    Configure RX2 DR value
    '''
    result = ob.protocol_setrx2_dr(val)
    if result:
        if result == 'ACK':
            debug('Protocol RX2_DR value: {}\n'.format(val))
        else:
            fatal('Configuring RX2_DR failed\n')
    else:
        fatal('Tester returns none and connection timed-out\n')
    return True

def link_status():
    '''
    To check the status of link test
    '''
    cnt = 0
    while(cnt < 2):
        result = ob.link_getactivationstatus()
        if not result:
            fatal('Tester returns none and connection timed-out\n')

        if result == 'YES':
            debug('Link status: Active\n')
            return True
        else:
            if cnt == 0:
                debug('Link status: In-active\n' 
                'Please make sure the link is active\nTrying again...\n')
                time.sleep(15)
            cnt = cnt + 1

    status = True if cnt < 2 and result == 'YES' else None

    if status:
        return True
    else:
        fatal('Link status: In-active\n')

def config_param(slot, num, maccmd):
    '''
    Configure parameters for EU test
    '''
    set_dlslot(slot)
    set_mactype()
    set_maccmdfield()
    set_numofcmd()
    instant_mac_cmd(num, maccmd)

def link_msg():
    '''
    To read the link message
    '''
    msg = None
    while (msg is None or msg == 'NA'):
        msg = ob.link_readmsg()
        time.sleep(3)

    if msg and msg != 'NAK':
        return msg
    else:
        fatal('READ:LINK:MSG? - {}\n'.format(msg))

def send_mac():
    '''
    To send a MAC command
    '''
    time.sleep(1)
    result = ob.link_sendmac()
    if result:
        if result == 'ACK':
            #debug('MAC Command Sent')
            pass
        else:
            fatal('Send MAC command failed\n')
    else:
        fatal('Tester returns none and connection timed-out\n')
    return True

def link_reset():
    '''
    Reset the link message
    '''
    result = ob.link_msgreset()
    if result:
        if result == 'ACK':
            #debug('Link message reset')
            pass
        else:
            fatal('Link message reset failed\n')
    else:
        fatal('Tester returns none and connection timed-out\n')
    return True

def link_test(num, req_cmd, resp_cmd):
    '''
    To perform link test
    '''
    cnt = 0
    while (cnt < 2):
        rcnt = 0
        send_mac()
        time.sleep(1)
        link_reset()

        while (rcnt < 2):
            msg = link_msg()
            msglist = msg.split('\t')
            if req_cmd in msglist[num]:
                print('MAC Request: {}'.format(msglist[num]), end='\n')
                msg = link_msg()
                msglist = msg.split('\t')
                if resp_cmd in msglist[num]:
                    print('Response: {}'.format(msglist[num]), end='\n\n')
                    return True
                else:
                    if rcnt < 1:
                        err('Invalid Response: {}\nTrying again...\n' \
                        .format(msglist[num]))
                        time.sleep(3)
                        rcnt += 1
                    else:
                        err('Invalid Response: {}\n'.format(msglist[num]))
                        return False
            else:
                #err('Invalid MAC Request : {} \n'.format(msglist[num]))
                rcnt += 1
        time.sleep(1)
        cnt += 1    

        
if __name__ == '__main__':

    ob = RWCTesterApi('5001', '192.168.0.33')    # For Ethernet communication

    # Open port
    ob.open_port()
    
    # Clear if old link messages
    clear_link()

    # Run Link
    exec_link()
    debug('Start EU Certification(5.3) Test\n')

    # Check link status
    link_status()

    # Send ACTIVATE_TM mac request
    debug('ACTIVATE-TM MAC CMD REQUEST\n')
    config_param('RX1', 1, 'ACTIVATE_TM')
    result = link_test(17, 'ActivateTM', 'DlCounter')
    if bool(result) is False:
        fatal('ACTIVATE-TM MAC CMD REQUEST: Test Failed\n')

    # Send TRIGGER_JOIN_REQ_TM mac request
    debug('TRIGGER JOIN MAC CMD REQUEST\n')
    set_droffset(2)
    set_dr('DR2_SF10BW125')
    config_param('RX1', 1, 'TRIGGER_JOIN_REQ_TM')
    result = link_test(17, 'TriggerJoinReq', 'Join-request')
    if bool(result) is False:
        fatal('TRIGGER JOIN MAC CMD REQUEST: Test Failed\n')

    # Check link status
    link_status()

    # Send ACTIVATE_TM mac request
    debug('ACTIVATE-TM MAC CMD REQUEST\n')
    config_param('RX1', 1, 'ACTIVATE_TM')
    result = link_test(17, 'ActivateTM', 'DlCounter')
    if bool(result) is False:
        fatal('ACTIVATE-TM MAC CMD REQUEST: Test Failed\n')

    # Send ECHO REQUEST mac command
    byte_len = 2

    debug('ECHO REQUEST MAC CMD REQUEST\n')
    set_echolen(byte_len)
    config_param('RX1', 1, 'ECHO_REQUEST_TM')
    result = link_test(17, 'EchoRequest', 'EchoResponse')
    if bool(result) is False:
        fatal('ECHO REQUEST MAC CMD REQUEST (Bytes - {}): Test Failed\n' \
        .format(byte_len))

    # Send ECHO REQUEST mac command
    debug('ECHO REQUEST MAC CMD REQUEST\n')
    set_echolen(byte_len)
    config_param('RX2', 1, 'ECHO_REQUEST_TM')
    result = link_test(17, 'EchoRequest', 'EchoResponse')
    if bool(result) is False:
        fatal('ECHO REQUEST MAC CMD REQUEST (Bytes - {}): Test Failed\n' \
        .format(byte_len))

    debug('EU Certification(5.3) Test Finished\nTest Result: PASS')
    
    ob.close_port()
