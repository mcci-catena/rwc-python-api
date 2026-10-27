##############################################################################
# 
# Module: cRWCSerialSetup.py
#
# Description:
#     Performs serial and ethernet communication
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

# Built-in imports
import logging
import re
import socket
import sys
import time

# Lib imports
import serial

class RwcSerialSetup:
    '''
    This is a class file consists common attributes to access by 
    cRWC5020x library
    
    '''
    
    def __init__(self, port, addr = None):
        '''
        Class constructor contains the RWC5020A serial port/ Ethernet 
        settings

        * Baudrate - 115200
        * Bytesize - 8 bits
        * Parity - None
        * Stopbits - 1
        * Timeout - 15 s (CONF:RF:RX_FREQ takes about 5.5 s on v1.500)

        :param port: Serial port (E.g., COM3 or /dev/ttyS3) or UDP port
        :param addr: Ip Address (E.g., 192.168.0.33)
        
        '''
        self.myport = serial.Serial()
        self.myport.port = port
        self.myport.baudrate = 115200
        self.myport.bytesize = serial.EIGHTBITS
        self.myport.parity = serial.PARITY_NONE
        self.myport.stopbits = serial.STOPBITS_ONE
        self.myport.timeout = 15

        self.udpport = port
        self.udpipaddr = addr

        # Log through the "rwclib.cRWCSerialSetup" logger. The
        # application chooses handlers and levels; for example,
        # logging.basicConfig(level=logging.INFO) shows each command
        # and response.
        self.logger = logging.getLogger(__name__)

    def open_port(self):
        '''
        To open the serial or udp port

        :parameters: N/A
        
        '''
        if not self.udpipaddr:
            #open serial port
            if not self.myport.is_open:
                try:
                    self.myport.open()
                    if self.myport.is_open:
                        self.logger.info('%s Port opened',self.myport.port)
                        return True
                except Exception as err:
                    self.logger.error('Unable to open %s Port',
                                      self.myport.port
                                      )
                    sys.exit('ERROR: Can\'t open port')
        else:
            #open udp socket
            try:
                self.clientsock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM
                    )
                self.clientsock.settimeout(15)
                self.udpport = int(self.udpport)
                self.udpipaddr = str(self.udpipaddr)
                self.logger.info('%s connected',self.udpipaddr)
                return True
            except Exception as err:
                self.logger.error('Can\'t establish connection to {}:\n {}'
                                  .format(self.udpipaddr, err)
                                  )
                print('Can\'t establish connection: ',err)
                sys.exit('ERROR: Can\'t connect to {}'.format(self.udpipaddr))

    
    def transceive(self, rwccmd, sec = 0):
        '''
        Write the commands to the tester and return received response

        :param rwccmd: RWC5020A remote commands
        
        '''
        readResult = None

        if self.udpipaddr:
            sock = getattr(self, 'clientsock', None)
            isopen = sock is not None and sock.fileno() != -1
        else:
            isopen = self.myport.is_open
        if not isopen:
            raise Exception('Port not open: call open_port() first.')

        if not self.udpipaddr:
            if self.myport.in_waiting != 0:
                self.myport.reset_input_buffer()

            try:
                self.myport.write(rwccmd.encode())
                self.logger.info('Tx Command: {}'.format(rwccmd))
                time.sleep(sec)
                readResult = self.myport.readline()
                self.logger.info('Rx Response: {}'.format(readResult))
            except Exception as err:
                self.logger.error(
                    'Error Send/Receive in Serial Communication: {}'
                    .format(err))

        if self.udpport and self.udpipaddr:
            # Discard replies that arrived after an earlier call timed
            # out; otherwise each later call returns the previous one's
            # reply.
            self.clientsock.setblocking(False)
            try:
                while True:
                    stale, ip = self.clientsock.recvfrom(1024)
                    self.logger.warning('Discarded late response: {}'
                                        .format(stale))
            except (BlockingIOError, InterruptedError):
                pass
            finally:
                self.clientsock.settimeout(15)

            try:
                self.clientsock.sendto(
                    rwccmd.encode(),
                    (self.udpipaddr, self.udpport))
                self.logger.info('Tx Command: {}'.format(rwccmd))
                readResult, ip = self.clientsock.recvfrom(1024)
                self.logger.info('Rx Response: {}'.format(readResult))
            except Exception as err:
                self.logger.error(
                    'Error Send/Receive in IP Communication: {}'
                    .format(err))
        
        if readResult:
            result = readResult.decode()
            # READ:LINK:MSG? replies end with a NUL (firmware v1.500,
            # v1.604)
            result = re.sub('\r|\n', '', result).rstrip('\0')
            return result
        else:
            return None
    

    def close_port(self):
        '''
        To close the serial port

        :Parameters: N/A

        '''
        if not self.udpipaddr:
            if self.myport.is_open:
                self.myport.close()
                self.logger.info('%s port closed',self.myport.port)
                return True
            else:
                self.logger.error('Port is already closed')
                sys.exit('ERROR: Port is already closed')

        if self.udpport and self.udpipaddr:
            try:
                self.clientsock.close()
                self.logger.info('%s connection terminated',self.udpipaddr)
                return True
            except Exception as err:
                self.logger.error('Can\'t close connection: {}'.format(err))
                sys.exit('ERROR: Can\'t close connection')
