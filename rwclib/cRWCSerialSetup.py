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
#     Released under the MIT license.
#
# Author:
#     Sivaprakash Veluthambi, MCCI   January, 2021
#
# Revision history:
#     V0.1.0 Thu Jan 14 2021 18:50:59 sivaprakash
#       Module created
#
##############################################################################

# Built-in imports
import logging
import os
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
        * Timeout - 30

        :param port: Serial port (E.g., COM3 or /dev/ttyS3) or UDP port
        :param addr: Ip Address (E.g., 192.168.0.33)
        
        '''
        self.myport = serial.Serial()
        self.myport.port = port
        self.myport.baudrate = 115200
        self.myport.bytesize = serial.EIGHTBITS
        self.myport.parity = serial.PARITY_NONE
        self.myport.stopbits = serial.STOPBITS_ONE
        self.myport.timeout = 5

        self.udpport = port
        self.udpipaddr = addr

        self.log_dir = os.path.join(os.path.normpath(
            os.getcwd() + os.sep + os.pardir), 'logs')
        self.log_fname = os.path.join(self.log_dir, 'rwcapi.log')
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(filename = self.log_fname,
                            format = '[%(asctime)s]: [%(name)s]: \
[%(levelname)s]: [%(funcName)s:%(lineno)d]: %(message)s')
        self.logger.setLevel(logging.DEBUG)

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
                self.clientsock.settimeout(5)
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

        if not self.udpipaddr:
            if not self.myport.in_waiting is 0:
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
            result = re.sub('\r|\n', '', result)
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
