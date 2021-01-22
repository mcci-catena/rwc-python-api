# Script to perform EU certification 5.5 test

import os
import sys
import time
# sys.path.insert(0, os.path.abspath('..'))

from rwclib.cRWC5020x import RWCTesterApi

def debug(msg):
    print(msg, end='\n')
    return True

def err(msg):
    print(msg, end='\n')

def fatal(msg):
    err(msg)
    sys.exit(1)
    
def exec_link():
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
    result = ob.protocol_setdownlinkslot(slot)
    if result:
        if result == 'ACK':
            debug('Protocol Downlink Slot: {}'.format(slot))
        else:
            fatal('Configuring downlink slot failed\n')
    else:
        fatal('Tester returns none and connection timed-out\n')
    return True

def set_mactype():
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
    result = ob.link_setpayloadlength(1, length)
    if result:
        if result == 'ACK':
            debug('Set Bytes: {}'.format(length))
        else:
            fatal('Configuring bytes length failed\n')
    else:
        fatal('Tester returns none and connection timed-out\n')
    return True

def abnormal(mode):
    result = ob.link_setabnormal(mode)
    if result:
        if result == 'ACK':
            debug('Set Abnormal Mode: {}\n'.format(mode))
        else:
            fatal('Configuring abnormal mode failed\n')
    else:
        fatal('Tester returns none and connection timed-out\n')
    return True

def link_status():
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
                debug('Link status: In-active\n' \
                'Please make sure the link is active\nTrying again...\n')
                time.sleep(15)
            cnt = cnt + 1

    status = True if cnt < 2 and result == 'YES' else None

    if status:
        return True
    else:
        fatal('Link status: In-active\nTest failed\n')

def config_param(slot, num, maccmd):
    set_dlslot(slot)
    set_mactype()
    set_maccmdfield()
    set_numofcmd()
    instant_mac_cmd(num, maccmd)

def link_msg():
    msg = None
    while (msg is None or msg == 'NA'):
        msg = ob.link_readmsg()
        time.sleep(3)

    if msg and msg != 'NAK':
        return msg
    else:
        fatal('READ:LINK:MSG? - {}\n'.format(msg))

def send_mac():
    time.sleep(1)
    result = ob.link_sendmac()
    if result:
        if result == 'ACK':
            # debug('MAC Command Sent')
            pass
        else:
            fatal('Send MAC command failed\n')
    else:
        fatal('Tester returns none and connection timed-out\n')
    return True

def link_reset():
    result = ob.link_msgreset()
    if result:
        if result == 'ACK':
            # debug('Link message reset')
            pass
        else:
            fatal('Link message reset failed\n')
    else:
        fatal('Tester returns none and connection timed-out\n')
    return True

def link_test(req_num, req_cmd, resp_num, resp_cmd):
    cnt = 0
    while (cnt < 2):
        rcnt = 0
        send_mac()
        time.sleep(1)
        link_reset()

        while (rcnt < 2):
            msg = link_msg()
            msglist = msg.split('\t')
            if req_cmd in msglist[req_num]:
                print ('MAC Request: {}'.format(msglist[req_num]), end='\n')
                msg = link_msg()
                msglist = msg.split('\t')
                if resp_cmd in msglist[resp_num]:
                    print ('Response: {}'.format(msglist[resp_num]), end='\n\n')
                    return True
                else:
                    if rcnt < 1:
                        err('Invalid Response: {}\nTrying again...\n' \
                        .format(msglist[resp_num]))
                        time.sleep(3)
                        rcnt += 1
                    else:
                        err('Invalid Response: {}\nTest failed\n' \
                        .format(msglist[resp_num]))
                        return False
            else:
                # err('MAC Request fail: {} \n'.format(msglist[req_num]))
                rcnt += 1
        time.sleep(1)
        cnt += 1    

        
if __name__ == '__main__':

    ob = RWCTesterApi('5001', '192.168.0.33')    #For Ethernet communication

    # Open port
    ob.open_port()

    # Run Link
    exec_link()
    debug('Start EU Certification(5.5) Test\n')

    # Clear if old link messages
    clear_link()

    # Check link status
    link_status()

    # Send ACTIVATE_TM mac request
    debug('ACTIVATE-TM MAC CMD REQUEST\n')
    config_param('RX1', 1, 'ACTIVATE_TM')
    result = link_test(17, 'ActivateTM', 17, 'DlCounter')
    if bool(result) is False:
        fatal('ACTIVATE-TM MAC CMD REQUEST: Test Failed')

    # Send ECHO REQUEST mac command
    byte_len = 2

    while (byte_len < 19):
        debug('ECHO REQUEST MAC CMD REQUEST\n')
        set_echolen(byte_len)
        config_param('RX1', 1, 'ECHO_REQUEST_TM')
        result = link_test(17, 'EchoRequest', 17, 'EchoResponse')
        if bool(result) is False:
            fatal('ECHO REQUEST MAC CMD REQUEST (Bytes - {}): Test Failed' \
            .format(byte_len))
        byte_len += 1

    # Set abnormal mode
    mode = 'MIC_ERR'
    abnormal(mode)

    # Send ECHO REQUEST mac command
    debug('ECHO REQUEST MAC CMD REQUEST\n')
    config_param('RX1', 1, 'ECHO_REQUEST_TM')
    result = link_test(17, 'EchoRequest', 0, 'U') #To verify any UL Packet
    if bool(result) is False:
        fatal('ECHO REQUEST MAC CMD REQUEST (Abnormal mode - {}): Test Failed' \
        .format(mode))
    
    result = link_msg()
    msglist = result.split('\t')
    if msglist[17] == 'EchoResponse':
        fatal('Abnormal mode - {}: Test failed'.format(mode))
    else:
        print ('Response: {}'.format(msglist[17]), end = '\n\n')

    # SET LINK ABNORMAL PARAM
    mode = 'OFF'
    abnormal(mode)

    debug('EU Certification(5.5) Test Finished\nTest Result: PASS')
    
    ob.close_port()
