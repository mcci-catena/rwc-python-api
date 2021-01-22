##############################################################################
# 
# Module: cRWC5020x.py
#
# Description:
#     Remote command methods for RWC5020x Tester
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
import sys
import time
import ipaddress

# Lib imports
import serial

from rwclib.cRWCSerialSetup import RwcSerialSetup

class RWCTesterApi(RwcSerialSetup):
    '''
    .. class:: RWCTesterApi

    This is class file to send commands and receive response from 
    RWC5020x LoRa Tester via RS232 Port.


    **Class Methods:**


    .. _commandlabel:
    '''

    def __init__(self, port, addr = None):
        '''
        Class constructor passes the received port to its base class 
        constructor

        :param port: Serial port (E.g., COM3 or /dev/ttyS3)
        '''
        RwcSerialSetup.__init__(self, port, addr)

    # Common Command Methods
    def query_identification(self):
        '''
        Identification query command

        :Parameters: N/A

        :return: Name, Version and Serial No. of the device; 
                 NAK on failure

        '''
        cmdIdn = '*IDN?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdIdn)
        return result

    def reset(self):
        '''
        Preset the equipment fully

        :Parameters: N/A

        :return: ACK on success, NAK on failure

        '''
        cmdRst = '*RST' + '\n'
        result = RwcSerialSetup.transceive(self, cmdRst)
        return result

    def save(self, index):
        '''
        Save the current parameters setting to memory

        :param value: setting value (1 ~ 10)

        :return: None

        '''
        saveindex = int(index)
        if saveindex >= 0 and saveindex <=9:
            cmdSaveIndex = str(saveindex)
            cmdSave = '*SAVE ' + cmdSaveIndex + '\n'
            result = RwcSerialSetup.transceive(self, cmdSave)
            return result
            
    def recall(self, index):
        '''
        Recall the saved parameters setting from memory

        :param value: setting value (1 ~ 10)

        :return: None


        .. _sysconflabel:
        '''
        recallindex = int(index)
        if recallindex >= 0 and recallindex <=9:
            cmdRecallIndex = str(recallindex)
            cmdRecall = '*SAVE ' + cmdRecallIndex + '\n'
            result = RwcSerialSetup.transceive(self, cmdRecall)
            return result
            
    # System Configuration Command Methods
    def set_mode(self, mode):
        '''
        Configure an operating mode (or Main Menu) of RWC5020A

        :param mode: Testing mode (EDT, GWT, NST)

        :return: ACK on success, NAK on failure

        '''
        cmdTestModeParam = mode
        if cmdTestModeParam == 'EDT':
            cmdTestMode = 'CONF:TESTER_MODE EDT' + '\n'
            result = RwcSerialSetup.transceive(self, cmdTestMode)
            return result
        elif cmdTestModeParam == 'GWT':
            cmdTestMode = 'CONF:TESTER_MODE GWT' + '\n'
            result = RwcSerialSetup.transceive(self, cmdTestMode)
            return result
        elif cmdTestModeParam == 'NST_TX':
            cmdTestMode = 'CONF:TESTER_MODE NST_TX' + '\n'
            result = RwcSerialSetup.transceive(self, cmdTestMode)
            return result
        elif cmdTestModeParam == 'NST_RX':
            cmdTestMode = 'CONF:TESTER_MODE NST_RX' + '\n'
            result = RwcSerialSetup.transceive(self, cmdTestMode)
            return result
        elif cmdTestModeParam == 'NST_MFG':
            cmdTestMode = 'CONF:TESTER_MODE NST_MFG' + '\n'
            result = RwcSerialSetup.transceive(self, cmdTestMode)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def query_mode(self):
        '''
        Read the operating mode (or Main Menu) of RWC5020A

        :Parameters: N/A (Query only)

        :return: It returns the operating mode; NAK on failure

        '''
        cmdGetMode = 'READ:TESTER_MODE?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMode)
        return result

    def set_remotelock(self, status):
        '''
        Lock the key input during Remote Control

        :param status: remote lock status (OFF, ON)

        :return: ACK on success, NAK on failure

        '''
        cmdLockStatusParam = status
        if cmdLockStatusParam == 'OFF':
            cmdRemoteLock = 'CONF:REMOTE:LOCK OFF' + '\n'
            result = RwcSerialSetup.transceive(self, cmdRemoteLock)
            return result
        elif cmdLockStatusParam == 'ON':
            cmdRemoteLock = 'CONF:REMOTE:LOCK ON' + '\n'
            result = RwcSerialSetup.transceive(self, cmdRemoteLock)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def query_remotelock(self):
        '''
        Unlock the key input during Remote Control

        :Parameters: N/A (Query only)

        :return: It returns the status of key input during remote 
                 control; NAK on failure

        '''
        cmdGetLockStatus = 'READ:REMOTE:LOCK?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetLockStatus)
        return result

    def set_screen(self, submenu):
        '''
        Configure a screen (or Sub Menu) of RWC5020A to move directly 
        to another sub menu

        :param submenu: sub menu type (LINK, POWER_TIME, POWER_CHANNEL, 
                        SENSITIVITY, REMOTE)

        :return: ACK on success, NAK on failure


        .. _rflabel:
        '''
        cmdSubmenuParam = submenu
        if cmdSubmenuParam == 'LINK':
            cmdMoveScreen = 'CONF:MOVE_SCREEN LINK' + '\n'
            result = RwcSerialSetup.transceive(self, cmdMoveScreen)
            return result
        elif cmdSubmenuParam == 'POWER_TIME':
            cmdMoveScreen = 'CONF:MOVE_SCREEN POWER_TIME' + '\n'
            result = RwcSerialSetup.transceive(self, cmdMoveScreen)
            return result
        elif cmdSubmenuParam == 'POWER_CHANNEL':
            cmdMoveScreen = 'CONF:MOVE_SCREEN POWER_CHANNEL' + '\n'
            result = RwcSerialSetup.transceive(self, cmdMoveScreen)
            return result
        elif cmdSubmenuParam == 'SENSITIVITY':
            cmdMoveScreen = 'CONF:MOVE_SCREEN SENSITIVITY' + '\n'
            result = RwcSerialSetup.transceive(self, cmdMoveScreen)
            return result
        elif cmdSubmenuParam == 'REMOTE':
            cmdMoveScreen = 'CONF:MOVE_SCREEN REMOTE' + '\n'
            result = RwcSerialSetup.transceive(self, cmdMoveScreen)
            return result
        else:
            raise Exception('Invalid parameter received.')

    #RF Parameter Command Methods
    def rf_setfrequency(self, freqrange):
        '''
        Configure CW frequency in MHz for non-signaling test

        :param freqrange: Frequency range (400~510, 862~960)

        :return: ACK on success, NAK on failure

        '''
        frequencynum = int(freqrange)
        if (frequencynum >= 400 
                and frequencynum <= 510) or (frequencynum >= 862 
                    and frequencynum <= 960):
            cmdFreqRange = str(frequencynum)
            cmdNstFrequency = 'CONF:RF:FREQ ' + cmdFreqRange + '\n'
            result = RwcSerialSetup.transceive(self, cmdNstFrequency)
            return result
        else:
            raise Exception('Invalid or Out of frequency range received.')

    def rf_getfrequency(self):
        '''
        Read CW frequency in MHz for non-signaling test

        :Parameters: Query only

        :return: It returns the frequency in MHz; NAK on failure

        '''
        cmdGetNstFrequency = 'READ:RF:FREQ?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetNstFrequency)
        return result

    def rf_settxfrequency(self, freqrange):
        '''
        Configure TX CW frequency in MHz for non-signaling test

        :param freqrange: Frequency range (400~510, 862~960)

        :return: ACK on success, NAK on failure

        '''
        txfrequencynum = int(freqrange)
        if (txfrequencynum >= 400 
                and txfrequencynum <= 510) or (txfrequencynum >= 862 
                    and txfrequencynum <= 960):
            cmdTxFreqRange = str(txfrequencynum)
            cmdNstTxFrequency = 'CONF:RF:TX_FREQ ' + cmdTxFreqRange + '\n'
            result = RwcSerialSetup.transceive(self, cmdNstTxFrequency)
            return result
        else:
            raise Exception('Invalid or Out of frequency range received.')

    def rf_gettxfrequency(self):
        '''
        Read TX CW frequency in MHz for non-signaling test

        :Parameters: Query only

        :return: It returns the frequency in MHz; NAK on failure

        '''
        cmdGetNstTxFrequency = 'READ:RF:TX_FREQ?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetNstTxFrequency)
        return result
    
    def rf_setrxfrequency(self, freqrange):
        '''
        Configure RX CW frequency in MHz for non-signaling test

        :param freqrange: Frequency range (400~510, 862~960)

        :return: ACK on success, NAK on failure

        '''
        rxfrequencynum = int(freqrange)
        if (rxfrequencynum >= 400 
                and rxfrequencynum <= 510) or (rxfrequencynum >= 862 
                    and rxfrequencynum <= 960):
            cmdRxFreqRange = str(rxfrequencynum)
            cmdNstRxFrequency = 'CONF:RF:RX_FREQ ' + cmdRxFreqRange + '\n'
            result = RwcSerialSetup.transceive(self, cmdNstRxFrequency)
            return result
        else:
            raise Exception('Invalid or Out of frequency range received.')

    def rf_getrxfrequency(self):
        '''
        Read RX CW frequency in MHz for non-signaling test

        :Parameters: Query only

        :return: It returns the frequency in MHz; NAK on failure

        '''
        cmdGetNstRxFrequency = 'READ:RF:RX_FREQ?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetNstRxFrequency)
        return result
    
    def rf_setmfgfrequency(self, freqrange):
        '''
        Configure MFG CW frequency in MHz for non-signaling test

        :param freqrange: Frequency range (400~510, 862~960)

        :return: ACK on success, NAK on failure

        '''
        mfgfrequencynum = int(freqrange)
        if (mfgfrequencynum >= 400 
                and mfgfrequencynum <= 510) or (mfgfrequencynum >= 862 
                    and mfgfrequencynum <= 960):
            cmdMfgFreqRange = str(mfgfrequencynum)
            cmdNstMfgFrequency = 'CONF:RF:MFG_FREQ ' + cmdMfgFreqRange + '\n'
            result = RwcSerialSetup.transceive(self, cmdNstMfgFrequency)
            return result
        else:
            raise Exception('Invalid or Out of frequency range received.')

    def rf_getmfgfrequency(self):
        '''
        Read MFG CW frequency in MHz for non-signaling test

        :Parameters: Query only

        :return: It returns the frequency in MHz; NAK on failure

        '''
        cmdGetNstMfgFrequency = 'READ:RF:MFG_FREQ?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetNstMfgFrequency)
        return result

    def rf_settxpower(self,txpow):
        '''
        Configure TX POWER in dBm

        :param txpow: TX Power value (-10 ~ -150)

        :return: ACK on success, NAK on failure

        '''
        txpownum = int(txpow)
        if (txpownum >= -150 and txpownum <= 10):
            cmdTxPowerRange = str(txpownum)
            cmdSetTxPower = 'CONF:RF:TX_POW ' + cmdTxPowerRange + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetTxPower)
            return result
        else:
            raise Exception('Invalid TX Power range received.')

    def rf_gettxpower(self):
        '''
        Read TX POWER in dBm

        :Parameters: N/A (Query only)

        :return: It returns the TX Power; NAK on failure

        '''
        cmdGetTxPower = 'READ:RF:TX_POW?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetTxPower)
        return result

    def rf_setpathloss(self, pathlossrng):
        '''
        Configure Path Loss in dB

        :param pathlossrng: Path loss range (0 ~ 50)

        :return: ACK on success, NAK on failure

        '''
        pathlossnum = int(pathlossrng)
        if (pathlossnum >= 0 and pathlossnum <= 50):
            cmdPathLossRange = str(pathlossnum)
            cmdSetPathLoss = 'CONF:RF:PATH_LOSS ' + cmdPathLossRange + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPathLoss)
            return result
        else:
            raise Exception('Invalid Path Loss range received.')

    def rf_getpathloss(self):
        '''
        Read Path Loss in dB

        :Parameters: N/A (Query only)

        :return: It returns the path loss in dB; NAK on failure

        '''
        cmdGetPathLoss = 'READ:RF:PATH_LOSS?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetPathLoss)
        return result

    def rf_setsysclkoffset(self, sysclkoffsetrng):
        '''
        Configure the system clock offset in ppm

        :param sysclkoffsetrng: Offset range (-100 ~ 100)

        :return: ACK on success, NAK on failure
        '''
        offsetnum = int(sysclkoffsetrng)
        if (offsetnum >= -100 and offsetnum <= 100):
            cmdOffsetRange = str(offsetnum)
            cmdSysclkOffset = 'CONF:RF:SYSCLK_OFFSET ' + cmdOffsetRange + '\n'
            result = RwcSerialSetup.transceive(self, cmdSysclkOffset)
            return result
        else:
            raise Exception('Invalid offset range received')

    def rf_getsysclkoffset(self):
        '''
        Read the system clock offset in ppm

        :Parameters: N/A (Query only)

        :return: It returns the system clock offset value; 
                 NAK on failure
        '''
        cmdGetSysclkOffset = 'READ:RF:SYSCLK_OFFSET?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetSysclkOffset)
        return result

    def rf_setfreqoffset(self, freqoffsetrng):
        '''
        Configure the frequency offset in ppm

        :param freqoffsetrng: Frequency range (-1000 ~ 1000)

        :return: ACK on success, NAK on failure

        '''
        freqoffnum = int(freqoffsetrng)
        if (freqoffnum >= -1000 and freqoffnum <= 1000):
            cmdFreqOffsetRange = str(freqoffnum)
            cmdSetFreqOffset = 'CONF:RF:FREQ_OFFSET ' \
                                + cmdFreqOffsetRange \
                                + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetFreqOffset)
            return result
        else:
            raise Exception('Invalid Frequency Offset range received.')

    def rf_getfreqoffset(self):
        '''
        Read the frequency offset in ppm

        :Parameters: N/A (Query only)

        :return: It returns the frequency offset value; NAK on failure

        '''
        cmdGetFreqOffset = 'READ:RF:FREQ_OFFSET?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetFreqOffset)
        return result

    def rf_settimeoffset(self, timeoffsetrng):
        '''
        Configure the time offset in us

        :param timeoffsetrng: Time offset range (-1000 ~ 1000)

        :return: ACK on success, NAK on failure

        '''
        timeoffnum = int(timeoffsetrng)
        if (timeoffnum >= -1000 and timeoffnum <= 1000):
            cmdTimeOffsetRange = str(timeoffnum)
            cmdSetTimeOffset = 'CONF:RF:TIME_OFFSET ' \
                                + cmdTimeOffsetRange \
                                + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetTimeOffset)
            return result
        else:
            raise Exception('Invalid Time Offset range received.')

    def rf_gettimeoffset(self):
        '''
        Read the time offset in us

        :Parameters: N/A (Query only)

        :return: It returns the time offset value; NAK on failure

        '''
        cmdGetTimeOffset = 'READ:RF:TIME_OFFSET?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetTimeOffset)
        return result

    def rf_setchannelmask(self, chindexrange, chmaskrange):
        '''
        Configure the channel mask of channel index 0 in both EDT and 
        GWT mode

        :param chindexrange: Channel index (0 - 5)
        :param chmaskrange: Channel Mask (For EDT 0x00 ~ 0xFF, 
                            For GWT 0x00 ~ 0xFFFF(US/AU/CN), 
                            read-only (others))

        :return: ACK on success, NAK on failure

        '''
        chindexnum = int(chindexrange)
        chmasknum = int(chmaskrange)

        if (chindexnum >= 0 and chindexnum <= 5):
            cmdChIndexrange = str(chindexnum)
            if (chmasknum >= 0 and chmasknum <= 65535):
                cmdChMaskRange = hex(chmasknum)
                cmdSetChMask = 'CONF:RF:CH_MASK_' \
                                + cmdChIndexrange \
                                + ' ' \
                                + cmdChMaskRange \
                                + '\n'
                result = RwcSerialSetup.transceive(self, cmdSetChMask)
                return result
            else:
                raise Exception('Invalid Channel Mask range received.')
        else:
            raise Exception('Invalid Channel Index received.')

    def rf_getchannelmask(self, chindexrange):
        '''
        Read the channel mask of channel index 0 in both EDT and 
        GWT mode

        :param chindexrange: Channel index (0 - 5)

        :return: It returns the channel mask with respect to the 
                 channel index; NAK on failure

        '''
        chindexnum = int(chindexrange)
        if (chindexnum >=0 and chindexnum <= 5):
            cmdChIndexrange = str(chindexnum)
            cmdGetChMask = 'READ:RF:CH_MASK_' + cmdChIndexrange + '?' + '\n'
            result = RwcSerialSetup.transceive(self, cmdGetChMask)
            return result
        else:
            raise Exception('Invalid Channel Index received.')

    def rf_setchannelgroup(self, chgrouprange):
        '''
        Configure the channel group 
        (only applicable to US/AU/CN in EDT mode)

        :param: For US/AU, 
                00 ~ 07, 08 ~ 15, 16 ~ 23, 
                24 ~ 31, ... , 48 ~ 55, 56 ~ 63,
                For CN, 
                00 ~ 07, 08 ~ 15, 16 ~ 23, 
                24 ~ 31, ... , 80 ~ 87, 88 ~ 95

        :return: ACK on success, NAK on failure

        '''
        chgroupnum = int(chgrouprange)
        chregion = self.protocol_getregion()
        if (chregion == 'US_915' 
            or chregion == 'AU_915' or chregion == 'CN_470'):
            if chgroupnum == 0:
                if chregion == 'CN_470':
                    cmdSetChGroup = 'CONF:RF:CH_GROUP 00~07' + '\n'
                else:
                    cmdSetChGroup = 'CONF:RF:CH_GROUP 00~07,64' + '\n'
                result = RwcSerialSetup.transceive(self, cmdSetChGroup)
                return result
            elif chgroupnum == 8:
                if chregion == 'CN_470':
                    cmdSetChGroup = 'CONF:RF:CH_GROUP 08~15' + '\n'
                else:
                    cmdSetChGroup = 'CONF:RF:CH_GROUP 08~15,65' + '\n'
                result = RwcSerialSetup.transceive(self, cmdSetChGroup)
                return result
            elif chgroupnum == 16:
                if chregion == 'CN_470':
                    cmdSetChGroup = 'CONF:RF:CH_GROUP 16~23' + '\n'
                else:
                    cmdSetChGroup = 'CONF:RF:CH_GROUP 16~23,66' + '\n'
                result = RwcSerialSetup.transceive(self, cmdSetChGroup)
                return result
            elif chgroupnum == 24:
                if chregion == 'CN_470':
                    cmdSetChGroup = 'CONF:RF:CH_GROUP 24~31' + '\n'
                else:
                    cmdSetChGroup = 'CONF:RF:CH_GROUP 24~31,67' + '\n'
                result = RwcSerialSetup.transceive(self, cmdSetChGroup)
                return result
            elif chgroupnum == 32:
                if chregion == 'CN_470':
                    cmdSetChGroup = 'CONF:RF:CH_GROUP 32~39' + '\n'
                else:
                    cmdSetChGroup = 'CONF:RF:CH_GROUP 32~39,68' + '\n'
                result = RwcSerialSetup.transceive(self, cmdSetChGroup)
                return result
            elif chgroupnum == 40:
                if chregion == 'CN_470':
                    cmdSetChGroup = 'CONF:RF:CH_GROUP 40~47' + '\n'
                else:
                    cmdSetChGroup = 'CONF:RF:CH_GROUP 40~47,69' + '\n'
                result = RwcSerialSetup.transceive(self, cmdSetChGroup)
                return result
            elif chgroupnum == 48:
                if chregion == 'CN_470':
                    cmdSetChGroup = 'CONF:RF:CH_GROUP 48~55' + '\n'
                else:
                    cmdSetChGroup = 'CONF:RF:CH_GROUP 48~55,70' + '\n'
                result = RwcSerialSetup.transceive(self, cmdSetChGroup)
                return result
            elif chgroupnum == 56:
                if chregion == 'CN_470':
                    cmdSetChGroup = 'CONF:RF:CH_GROUP 56~63' + '\n'
                else:
                    cmdSetChGroup = 'CONF:RF:CH_GROUP 56~63,71' + '\n'
                result = RwcSerialSetup.transceive(self, cmdSetChGroup)
                return result
            elif chgroupnum == 64:
                if chregion == 'CN_470':
                    cmdSetChGroup = 'CONF:RF:CH_GROUP 64~71' + '\n'
                else:
                    raise Exception('Invalid Channel Group Region received.')
                result = RwcSerialSetup.transceive(self, cmdSetChGroup)
                return result
            elif chgroupnum == 72:
                if chregion == 'CN_470':
                    cmdSetChGroup = 'CONF:RF:CH_GROUP 72~79' + '\n'
                else:
                    raise Exception('Invalid Channel Group Region received.')
                result = RwcSerialSetup.transceive(self, cmdSetChGroup)
                return result
            elif chgroupnum == 80:
                if chregion == 'CN_470':
                    cmdSetChGroup = 'CONF:RF:CH_GROUP 80~87' + '\n'
                else:
                    raise Exception('Invalid Channel Group Region received.')
                result = RwcSerialSetup.transceive(self, cmdSetChGroup)
                return result
            elif chgroupnum == 88:
                if chregion == 'CN_470':
                    cmdSetChGroup = 'CONF:RF:CH_GROUP 88~95' + '\n'
                else:
                    raise Exception('Invalid Channel Group Region received.')
                result = RwcSerialSetup.transceive(self, cmdSetChGroup)
                return result
            else:
                raise Exception('Invalid Channel Group Parameter received.')
        else:
            raise Exception('Invalid Channel Group Region received.')

    def rf_getchannelgroup(self):
        '''
        Read the channel group 
        (only applicable to US/AU/CN in EDT mode)

        :Parameters: N/A (Query only)

        :return: It returns the channel group of US/AU/CN region; 
                 NAK on failure

        '''
        cmdGetChGroup = 'READ:RF:CH_GROUP?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetChGroup)
        return result

    def rf_setuplinkchannel(self, ulchfreqrange):
        '''
        Write uplink Channel n frequency in MHz;

        For EDT param=3 (EU868, IN) param=4 (EU433, KR, AS)
        For GWT all channels frequencies are editable

        :param ulchfreqrange: Frequency range (400~510, 862~960)

        :return: ACK on success, NAK on failure

        '''
        freqnum = int(ulchfreqrange)
        if (freqnum >= 400 and freqnum <= 510
        ) or (freqnum >= 862 and freqnum <= 960):
            cmdUlChFreqRange = str(freqnum)
            cmdSetUplinkChannel = 'CONF:RF:UL_CH ' + cmdUlChFreqRange + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetUplinkChannel)
            return result
        else:
            raise Exception('Invalid Uplink Channel Freq range received.')

    def rf_getuplinkchannel(self):
        '''
        Read Uplink Channel n frequency in MHz

        * param=0,1,...,71 (US/AU)
        * param=0,1,...,95 (CN)
        * param=0,1,...,7 (others)

        :Parameters: N/A (Query only)

        :return: -

        '''
        cmdGetUplinkChannel = 'READ:RF:UL_CH?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetUplinkChannel)
        return result

    def rf_getdownlinkchannel(self):
        '''
        Read Downlink Channel n frequency in MHz

        * param=0,1,...,47 (CN)
        * param=0,1,...,7 (others)

        :Parameters: N/A (Query only)

        :return: -

        '''
        cmdGetDownlinklinkChannel = 'READ:RF:DL_CH?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetDownlinklinkChannel)
        return result

    def rf_setpingfreq(self, freqrange):
        '''
        Configure the frequency of ping channel

        :param freqrange: Frequency range (400~510, 862~960)

        :return: ACK on success, NAK on failure

        '''
        pingfrequencynum = int(freqrange)
        if (pingfrequencynum >= 400 
                and pingfrequencynum <= 510) or (pingfrequencynum >= 862 
                    and pingfrequencynum <= 960):
            cmdPingFreqRange = str(pingfrequencynum)
            cmdNstPingFrequency = 'CONF:RF:PING_FREQ ' \
                                    + cmdPingFreqRange \
                                    + '\n'
            result = RwcSerialSetup.transceive(self, cmdNstPingFrequency)
            return result
        else:
            raise Exception('Invalid or Out of frequency range received.')

    def rf_getpingfreq(self):
        '''
        Read the frequency of ping channel

        :Parameters: N/A (Query only)

        :return: It returns the frequency of ping channel; NAK on failure

        '''
        cmdGetPingFreq = 'READ:RF:PING_FREQ?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetPingFreq)
        return result

    def rf_setpingdr(self, drvalue):
        '''
        Configure the data rate of ping channel

        :param drvalue: DR0_SF12BW125, DR1_SF11BW125, DR2_SF10BW125, 
                        DR3_SF9BW125, DR4_SF8BW125, DR5_SF7BW125, 
                        DR6_SF7BW250, DR7_FSK50

        :return: ACK on success, NAK on failure
        
        '''
        drvallist = [
            'DR0_SF12BW125',
            'DR1_SF11BW125',
            'DR2_SF10BW125',
            'DR3_SF9BW125',
            'DR4_SF8BW125',
            'DR5_SF7BW125',
            'DR6_SF7BW250',
            'DR7_FSK50']
        if drvalue in drvallist:
            cmdSetPingDr = 'CONF:RF:PING_DR ' + drvalue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPingDr)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def rf_getpingdr(self):
        '''
        Read the data rate of ping channel

        :Parameters: N/A (Query only)

        :return: It returns the data rate of ping channel; 
                 NAK on failure

        '''
        cmdGetPingDr = 'READ:RF:PING_DR?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetPingDr)
        return result

    def rf_setbeaconfrequency(self, freqrange):
        '''
        Configure the frequency of beacon

        :param freqrange: Frequency range (400~510, 862~960)

        :return: ACK on success, NAK on failure

        '''
        bcnfrequencynum = int(freqrange)
        if (bcnfrequencynum >= 400 
                and bcnfrequencynum <= 510) or (bcnfrequencynum >= 862 
                    and bcnfrequencynum <= 960):
            cmdBcnFreqRange = str(bcnfrequencynum)
            cmdNstBcnFrequency = 'CONF:RF:BEACON_FREQ ' \
                                    + cmdBcnFreqRange \
                                    + '\n'
            result = RwcSerialSetup.transceive(self, cmdNstBcnFrequency)
            return result
        else:
            raise Exception('Invalid or Out of frequency range received.')

    def rf_getbeaconfreq(self):
        '''
        Read the frequency of beacon

        :Parameters: N/A (Query only)

        :return: It returns the frequency of beacon; NAK on failure

        '''
        cmdGetBeaconFreq = 'READ:RF:BEACON_FREQ?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetBeaconFreq)
        return result

    def rf_setbeacondr(self, drvalue):
        '''
        Configure the data rate of beacon

        :param drvalue: DR0_SF12BW125, DR1_SF11BW125, DR2_SF10BW125, 
                        DR3_SF9BW125, DR4_SF8BW125, DR5_SF7BW125, 
                        DR6_SF7BW250, DR7_FSK50

        :return: ACK on success, NAK on failure
        
        '''
        drvallist = [
            'DR0_SF12BW125',
            'DR1_SF11BW125',
            'DR2_SF10BW125',
            'DR3_SF9BW125',
            'DR4_SF8BW125',
            'DR5_SF7BW125',
            'DR6_SF7BW250',
            'DR7_FSK50']
        if drvalue in drvallist:
            cmdSetBeaconDr = 'CONF:RF:BEACON_DR ' + drvalue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetBeaconDr)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def rf_getbeacondr(self):
        '''
        Read the data rate of beacon

        :Parameters: N/A (Query only)

        :return: It returns the data rate of beacon; NAK on failure

        '''
        cmdGetBeaconDr = 'READ:RF:BEACON_DR?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetBeaconDr)
        return result

    def rf_setchannelmode(self, mode):
        '''
        Configure the channel mode (only applicable to CN in ICA mode)

        :param mode: Channel mode (INTER_FREQ, SAME_FREQ)

        :return: ACK on success, NAK on failure

        '''
        cmdRfChannelMode = mode
        if cmdRfChannelMode == 'INTER_FREQ':
            cmdSetChMode = 'CONF:RF:ICA_CH_MODE INTER_FREQ' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetChMode)
            return result
        elif cmdRfChannelMode == 'SAME_FREQ':
            cmdSetChMode = 'CONF:RF:ICA_CH_MODE SAME_FREQ' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetChMode)
            return result
        else:
            raise Exception('Invalid Channel Mode Parameter passed.')

    def rf_getchannelmode(self):
        '''
        Read the channel mode (only applicable to CN in ICA mode)

        :Parameters: N/A (Query only)

        :return: It returns the channel mode; NAK on failure 
        '''
        cmdGetChMode = 'READ:RF:ICA_CH_MODE?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetChMode)
        return result

    def rf_setchannelmode_as923(self, mode):
        '''
        Configure the channel mode (only applicable to AS923 region)

        :param mode: Channel mode (AS920-923, AS923-925)

        :return: ACK on success, NAK on failure

        '''
        chModeList = ['AS920-923', 'AS923-925']
        cmdSupportedVersion = [
            '1.200', '1.203', '1.204', '1.206', 
            '1.210', '1.220', '1.221', '1.222']
        verStatus = self.validate_sys_swversion(cmdSupportedVersion)

        if verStatus and mode in chModeList:
            cmdSetAsChMode = 'CONF:RF:AS923_CH_MODE ' + mode + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetAsChMode)
            return result
        else:
            raise Exception('Invalid Channel Mode Parameter passed.')

    def rf_getchannelmode_as923(self):
        '''
        Read the channel mode (only applicable to AS923 region)

        :Parameters: N/A (Query only)

        :return: It returns the channel mode; NAK on failure 
        '''
        cmdSupportedVersion = [
            '1.200', '1.203', '1.204', '1.206', 
            '1.210', '1.220', '1.221', '1.222']
        verStatus = self.validate_sys_swversion(cmdSupportedVersion)

        if verStatus:
            cmdGetChModeAs = 'READ:RF:AS923_CH_MODE?' + '\n'
            result = RwcSerialSetup.transceive(self, cmdGetChModeAs)
            return result

    def rf_setchannelgroup_as923(self, mode):
        '''
        Configure the channel group (only applicable to AS923 region)

        :param mode: Channel group (AS_923-1, AS_923-2, AS_923-3)

        :return: ACK on success, NAK on failure

        '''
        cmdAsChannelGroup = mode
        if cmdAsChannelGroup == 'AS_923-1':
            cmdSetAsChGroup = 'CONF:RF:AS923_CH_GROUP AS_923-1' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetAsChGroup)
            return result
        elif cmdAsChannelGroup == 'AS_923-2':
            cmdSetAsChGroup = 'CONF:RF:AS923_CH_GROUP AS_923-2' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetAsChGroup)
            return result
        elif cmdAsChannelGroup == 'AS_923-3':
            cmdSetAsChGroup = 'CONF:RF:AS923_CH_GROUP AS_923-3' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetAsChGroup)
            return result
        else:
            raise Exception('Invalid Channel Group Parameter passed.')

    def rf_getchannelgroup_as923(self):
        '''
        Read the channel group (only applicable to AS923 region)

        :Parameters: N/A (Query only)

        :return: It returns the channel mode; NAK on failure 
        '''
        cmdGetChGroupAs = 'READ:RF:AS923_CH_GROUP?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetChGroupAs)
        return result

    def rf_setfreqoffset_as923(self, freqoffsetrng):
        '''
        Configure the frequency offset for channel group 
        (only applicable to AS923 region)

        :param freqoffsetrng: Offset range (-100 ~ 100)

        :return: ACK on success, NAK on failure

        '''
        offsetnum = int(freqoffsetrng)
        if (offsetnum >= -100 and offsetnum <= 100):
            cmdOffsetRange = str(offsetnum)
            cmdFreqOffset = 'CONF:RF:AS923_FREQ_OFFSET ' \
                                + cmdOffsetRange \
                                + '\n'
            result = RwcSerialSetup.transceive(self, cmdFreqOffset)
            return result
        else:
            raise Exception('Invalid offset range received')

    def rf_getfreqoffset_as923(self):
        '''
        Read the frequency offset for channel group 
        (only applicable to AS923 region)

        :Parameters: N/A (Query only)

        :return: It returns the frequency offset value of AS923 
                 channel group; NAK on failure

        '''
        cmdGetFreqOffset = 'READ:RF:AS923_FREQ_OFFSET?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetFreqOffset)
        return result

    def rf_setchplan_cn470(self, planType):
        '''
        Configure the channel plan (only applicable to CN470 region)

        :param planType: 20M_A, 20M_B, 26M_A, 26M_B

        :return: ACK on success, NAK on failure
        
        '''
        planTypelist = ['20M_A', '20M_B', '26M_A', '26M_B']
        if planType in planTypelist:
            cmdSetChPlan = 'CONF:RF:CN470_CH_PLAN ' + planType + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetChPlan)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def rf_getchplan_cn470(self):
        '''
        Read the channel plan (only applicable to CN470 region)

        :Parameters: N/A (Query only)

        :return: It returns the channel plan of CN470 region; 
                 NAK on failure

        '''
        cmdGetChPlan = 'READ:RF:CN470_CH_PLAN?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetChPlan)
        return result

    def rf_getmeasuredfreq(self):
        '''
        Read currently measured CW frequency value

        :Parameters: N/A (Query only)

        :return: It returns the channel mode; NAK on failure 
        '''
        cmdGetMeasuredFreq = 'READ:RF:MEASURED_FREQ?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMeasuredFreq)
        return result
    
    def rf_getmeasuredfreq_max(self):
        '''
        Read maximum value of measured CW frequency value

        :Parameters: N/A (Query only)

        :return: It returns the channel mode; NAK on failure 
        '''
        cmdGetMeasuredFreqMax = 'READ:RF:MEASURED_FREQ_MAX?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMeasuredFreqMax)
        return result

    def rf_getmeasuredfreq_avg(self):
        '''
        Read average value of measured CW frequency value

        :Parameters: N/A (Query only)

        :return: It returns the channel mode; NAK on failure 
        '''
        cmdGetMeasuredFreqAvg = 'READ:RF:MEASURED_FREQ_AVG?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMeasuredFreqAvg)
        return result

    def rf_getmeasuredfreq_min(self):
        '''
        Read minimum value of measured CW frequency value

        :Parameters: N/A (Query only)

        :return: It returns the channel mode; NAK on failure


        .. _protocollabel: 
        '''
        cmdGetMeasuredFreqMin = 'READ:RF:MEASURED_FREQ_MIN?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMeasuredFreqMin)
        return result

    #Protocol Command Methods
    def protocol_setregion(self, region):
        '''
        Configure an operating Region of RWC5020A

        :param region: EU_868, EU_433, US_915, AU_921, CN_470, KR_922, 
                       AS_923, IN_866

        :return: ACK on success, NAK on failure
        
        '''
        cmdRegion = region
        if cmdRegion == 'EU_868':
            cmdSetRegion = 'CONF:PROTOCOL:REGION EU_868' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRegion)
            return result
        elif cmdRegion == 'EU_433':
            cmdSetRegion = 'CONF:PROTOCOL:REGION EU_433' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRegion)
            return result
        elif cmdRegion == 'US_915':
            cmdSetRegion = 'CONF:PROTOCOL:REGION US_915' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRegion)
            return result
        elif cmdRegion == 'AU_921':
            cmdSetRegion = 'CONF:PROTOCOL:REGION AU_921' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRegion)
            return result
        elif cmdRegion == 'CN_470':
            cmdSetRegion = 'CONF:PROTOCOL:REGION CN_470' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRegion)
            return result
        elif cmdRegion == 'KR_922':
            cmdSetRegion = 'CONF:PROTOCOL:REGION KR_922' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRegion)
            return result
        elif cmdRegion == 'AS_923':
            cmdSetRegion = 'CONF:PROTOCOL:REGION AS_923' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRegion)
            return result
        elif cmdRegion == 'IN_866':
            cmdSetRegion = 'CONF:PROTOCOL:REGION IN_866' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRegion)
            return result
        elif cmdRegion == 'RU_864':
            cmdSetRegion = 'CONF:PROTOCOL:REGION RU_864' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRegion)
            return result
        else:
            raise Exception('Invalid parameter received.')          

    def protocol_getregion(self):
        '''
        Read an operating Region of RWC5020A

        :param: Query only

        :return: It returns the protocol region; NAK on failure

        '''
        cmdGetRegion = 'READ:PROTOCOL:REGION?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetRegion)
        return result

    def protocol_setoperator(self, serviceop):
        '''
        Configure the LoRa service operator in case of KR_922

        :param serviceop: LoRaWAN, SKT

        :return: ACK on success, NAK on failure
        
        '''
        cmdServiceOperator = serviceop
        if cmdServiceOperator == 'LoRaWAN':
            cmdSetOperator = 'CONF:PROTOCOL:OPERATOR LoRaWAN' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetOperator)
            return result
        elif cmdServiceOperator == 'SKT':
            cmdSetOperator = 'CONF:PROTOCOL:OPERATOR SKT' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetOperator)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getoperator(self):
        '''
        Read the LoRa service operator in case of KR_922

        :param: Query only

        :return: It returns the service operator name; NAK on failure
        
        '''
        cmdGetOperator = 'READ:PROTOCOL:OPERATOR?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetOperator)
        return result

    def protocol_setclass(self, classtype):
        '''
        Configure the class of LoRa device

        :param classtype: A, B, C

        :return: ACK on success, NAK on failure
        
        '''
        cmdClassType = classtype
        if cmdClassType == 'A':
            cmdSetClass = 'CONF:PROTOCOL:CLASS A' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetClass)
            return result
        elif cmdClassType == 'B':
            cmdSetClass = 'CONF:PROTOCOL:CLASS B' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetClass)
            return result
        elif cmdClassType == 'C':
            cmdSetClass = 'CONF:PROTOCOL:CLASS C' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetClass)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getclass(self):
        '''
        Read the class of LoRa device

        :param: Query only

        :return: It returns the class type; NAK on failure
        
        '''
        cmdGetClass = 'READ:PROTOCOL:CLASS?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetClass)
        return result

    def protocol_setactivationprocedure(self, activation):
        '''
        Configure the activation procedure

        :param activation: OTAA, ABP

        :return: ACK on success, NAK on failure
   
        '''
        cmdActivationProcedure = activation
        if cmdActivationProcedure == 'OTAA':
            cmdSetActivationProcedure = 'CONF:PROTOCOL:ACTIVATION OTAA' + '\n'
            result = RwcSerialSetup.transceive(
                self, 
                cmdSetActivationProcedure)
            return result
        elif cmdActivationProcedure == 'ABP':
            cmdSetActivationProcedure = 'CONF:PROTOCOL:ACTIVATION ABP' + '\n'
            result = RwcSerialSetup.transceive(
                self, 
                cmdSetActivationProcedure)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getactivationprocedure(self):
        '''
        Read the activation procedure

        :param: Query only

        :return: It returns the activation procedure type; NAK on failure
        
        '''
        cmdGetActivationProcedure = 'READ:PROTOCOL:ACTIVATION?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetActivationProcedure)
        return result

    def protocol_settestmodeflag(self, mode):
        '''
        Configure the flag whether to send the ActivateTestMode command 
        after activation

        :param mode: OFF, ON

        :return: ACK on success, NAK on failure
        
        '''
        cmdMode = mode
        if cmdMode == 'OFF':
            cmdSetTestModeFlag = 'CONF:PROTOCOL:SET_TEST_MODE OFF' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetTestModeFlag)
            return result
        elif cmdMode == 'ON':
            cmdSetTestModeFlag = 'CONF:PROTOCOL:SET_TEST_MODE ON' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetTestModeFlag)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_gettestmodeflag(self):
        '''
        Read the flag whether to send the ActivateTestMode command 
        after activation

        :param: Query only

        :return: It returns the flag status either ON or OFF; 
                 NAK on failure
        
        '''
        cmdGetTestModeFlag = 'READ:PROTOCOL:SET_TEST_MODE?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetTestModeFlag)
        return result

    def protocol_setbeacontimeoffset(self, value):
        '''
        Configure the beacon time offset

        :param value: -1000 ~ 1000 ms

        :return: ACK on success, NAK on failure
        
        '''
        cmdValue = int(value)
        if cmdValue >= -1000 and cmdValue <= 1000:
            cmdTimeOffsetValue = str(cmdValue)
            cmdSetBeaconTimeOffset = 'CONF:PROTOCOL:BEACON_TIME_OFFSET ' \
                                        + cmdTimeOffsetValue \
                                        + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetBeaconTimeOffset)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getbeacontimeoffset(self):
        '''
        Read the beacon time offset

        :param: Query only

        :return: It returns the beacon time offset; NAK on failure
        
        '''
        cmdGetBeaconTimeOffset = 'READ:PROTOCOL:BEACON_TIME_OFFSET?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetBeaconTimeOffset)
        return result

    def protocol_setappkey(self, value):
        '''
        Configure Application Key

        :param value: 128-bit HEX value

        :return: ACK on success, NAK on failure
        
        '''
        cmdValue = int(value)
        if (cmdValue >= 0 and cmdValue <= 2**128 - 1):
            cmdHexValue = hex(cmdValue)
            cmdSetAppKey = 'CONF:PROTOCOL:APP_KEY ' + cmdHexValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetAppKey)
            return result
        else:
            raise Exception('Invalid parameter received.')
    
    def protocol_getappkey(self):
        '''
        Read Application Key

        :param: Query only

        :return: It returns the application key; NAK on failure
        
        '''
        cmdGetAppKey = 'READ:PROTOCOL:APP_KEY?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetAppKey)
        return result

    def protocol_getrealappkey(self):
        '''
        Read the Real Application Key

        :param: Query only

        :return: It returns the real application key; NAK on failure
        
        '''
        cmdGetRealKey = 'READ:PROTOCOL:REAL_KEY?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetRealKey)
        return result

    def protocol_setappsessionkey(self, value):
        '''
        Configure Application Session Key

        :param value: 128-bit HEX value

        :return: ACK on success, NAK on failure
        
        '''
        cmdValue = int(value)
        if (cmdValue >= 0 and cmdValue <= 2**128 - 1):
            cmdHexValue = hex(cmdValue)
            cmdSetAppSessionKey = 'CONF:PROTOCOL:APPS_KEY ' \
            + cmdHexValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetAppSessionKey)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getappsessionkey(self):
        '''
        Read Application Session Key

        :param: Query only

        :return: It returns the read application session key; 
                 NAK on failure
        
        '''
        cmdGetAppSessionKey = 'READ:PROTOCOL:APPS_KEY?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetAppSessionKey)
        return result

    def protocol_setnwksessionkey(self, value):
        '''
        Configure Network Session Key

        :param value: 128-bit HEX value

        :return: ACK on success, NAK on failure
        
        '''
        cmdValue = int(value)
        if (cmdValue >= 0 and cmdValue <= 2**128 - 1):
            cmdHexValue = hex(cmdValue)
            cmdSetNwkSessionKey = 'CONF:PROTOCOL:NWKS_KEY ' \
            + cmdHexValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetNwkSessionKey)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getnwksessionkey(self):
        '''
        Read Network Session Key

        :param: Query only

        :return: It returns the network session key; NAK on failure
        
        '''
        cmdGetNwkSessionKey = 'READ:PROTOCOL:NWKS_KEY?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetNwkSessionKey)
        return result

    def protocol_seteuiflag(self, euiflag):
        '''
        Configure a flag whether to check DUT's EUI value for activation

        :param euiflag: NO, YES

        :return: ACK on success, NAK on failure
        
        '''
        cmdEuiFlag = euiflag
        if cmdEuiFlag == 'NO':
            cmdSetEuiFlag = 'CONF:PROTOCOL:CHECK_EUI NO' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetEuiFlag)
            return result
        elif cmdEuiFlag == 'YES':
            cmdSetEuiFlag = 'CONF:PROTOCOL:CHECK_EUI YES' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetEuiFlag)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_geteuiflag(self):
        '''
        Read a flag whether to check DUT's EUI value for activation

        :param: Query only

        :return: It returns the flag status; NAK on failure
        
        '''
        cmdGetEuiFlag = 'READ:PROTOCOL:CHECK_EUI?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetEuiFlag)
        return result

    def protocol_seteuival(self, value):
        '''
        Configure Device EUI value

        :param value: 64-bit HEX value

        :return: ACK on success, NAK on failure
        
        '''
        cmdValue = int(value)
        if (cmdValue >= 0 and cmdValue <= 2**64 - 1):
            cmdHexValue = hex(cmdValue)
            cmdSetEuiVal = 'CONF:PROTOCOL:DEV_EUI ' + cmdHexValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetEuiVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_geteuival(self):
        '''
        Read Device EUI value

        :param: Query only

        :return: It returns the device EUI value; NAK on failure
        
        '''
        cmdGetEuiVal = 'READ:PROTOCOL:DEV_EUI?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetEuiVal)
        return result

    def protocol_setappeui(self, value):
        '''
        Configure Application EUI value

        :param value: 64-bit HEX value

        :return: ACK on success, NAK on failure
        
        '''
        cmdValue = int(value)
        if (cmdValue >= 0 and cmdValue <= 2**64 - 1):
            cmdHexValue = hex(cmdValue)
            cmdSetAppEuiVal = 'CONF:PROTOCOL:APP_EUI ' + cmdHexValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetAppEuiVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getappeui(self):
        '''
        Read Application EUI value

        :param: Query only

        :return: It returns the application EUI value; NAK on failure
        
        '''
        cmdGetAppEuiVal = 'READ:PROTOCOL:APP_EUI?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetAppEuiVal)
        return result

    def protocol_setdevaddr(self, addrval):
        '''
        Configure Device Address value

        :param addrval: 0 ~ 0xFFFFFFFF

        :return: ACK on success, NAK on failure
        
        '''
        cmdValue = int(addrval)
        if (cmdValue >= 0 and cmdValue <= 2**32 - 1):
            cmdAddrValue = hex(cmdValue)
            cmdSetAddrVal = 'CONF:PROTOCOL:DEV_ADDR ' + cmdAddrValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetAddrVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getdevaddr(self):
        '''
        Read Device Address value

        :param: Query only

        :return: It returns the device address value; NAK on failure
        
        '''
        cmdGetAddrVal = 'READ:PROTOCOL:DEV_ADDR?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetAddrVal)
        return result

    def protocol_setnetid(self, netidval):
        '''
        Configure NET ID value

        :param netidval: 0 ~ 0X7F

        :return: ACK on success, NAK on failure
        
        '''
        cmdValue = int(netidval)
        if (cmdValue >= 0 and cmdValue <= 127):
            cmdNetIdvalue = str(cmdValue)
            cmdSetNetIdVal = 'CONF:PROTOCOL:NET_ID ' + cmdNetIdvalue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetNetIdVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getnetid(self):
        '''
        Read NET ID value

        :param: Query only

        :return: It returns the net id value; NAK on failure
        
        '''
        cmdGetNetIdVal = 'READ:PROTOCOL:NET_ID?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetNetIdVal)
        return result

    def protocol_setrecvdelay(self, delayval):
        '''
        Configure RECEIVE_DELAY value in sec

        :param delayval: 1 ~ 10

        :return: ACK on success, NAK on failure
        
        '''
        delaynum = int(delayval)
        if delaynum >= 1 and delaynum <= 10:
            cmdRecvDelayVal = str(delaynum)
            cmdSetRecvDelayVal = 'CONF:PROTOCOL:RECEIVE_DELAY ' \
                                    + cmdRecvDelayVal \
                                    + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRecvDelayVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getrecvdelay(self):
        '''
        Read RECEIVE_DELAY value in sec

        :param: Query only

        :return: It returns the receive delay in seconds; NAK on failure
        
        '''
        cmdGetRecvDelayVal = 'READ:PROTOCOL:RECEIVE_DELAY?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetRecvDelayVal)
        return result

    def protocol_setperiodic_uplinkmsg(self, peruplinkmsg):
        '''
        Configure the Periodic Uplink message in GWT

        :param peruplinkmsg: NONE, LINK_CHECK_REQ, CONFIRMED_UP, 
                             UNCONFIRMRED_UP, DL_COUNTER

        :return: ACK on success, NAK on failure
        
        '''
        cmdPeriodicUplinkMsg = peruplinkmsg
        if cmdPeriodicUplinkMsg == 'NONE':
            cmdSetPeriodicUplinkMsg = 'CONF:PROTOCOL:PERIODIC_UPLINK NONE' \
                                        + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPeriodicUplinkMsg)
            return result
        elif cmdPeriodicUplinkMsg == 'LINK_CHECK_REQ':
            cmdSetPeriodicUplinkMsg = 'CONF:PROTOCOL:PERIODIC_UPLINK LINK_CHECK_REQ' \
                                        + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPeriodicUplinkMsg)
            return result
        elif cmdPeriodicUplinkMsg == 'CONFIRMED_UP':
            cmdSetPeriodicUplinkMsg = 'CONF:PROTOCOL:PERIODIC_UPLINK CONFIRMED_UP' \
                                        + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPeriodicUplinkMsg)
            return result
        elif cmdPeriodicUplinkMsg == 'UNCONFIRMED_UP':
            cmdSetPeriodicUplinkMsg = 'CONF:PROTOCOL:PERIODIC_UPLINK UNCONFIRMED_UP' \
                                        + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPeriodicUplinkMsg)
            return result
        elif cmdPeriodicUplinkMsg == 'DL_COUNTER':
            cmdSetPeriodicUplinkMsg = 'CONF:PROTOCOL:PERIODIC_UPLINK DL_COUNTER' \
                                        + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPeriodicUplinkMsg)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getperiodic_uplinkmsg(self):
        '''
        Read the Periodic Uplink message in GWT

        :param: Query only

        :return: It returns the periodic uplink message; 
                 NAK on failure
        
        '''
        cmdGetPeriodicUplinkMsg = 'READ:PROTOCOL:PERIODIC_UPLINK?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetPeriodicUplinkMsg)
        return result

    def protocol_setinterval(self, interval):
        '''
        Configure the interval in sec between Uplink message defined 
        by Periodic uplink

        :param interval: 3 ~ 60

        :return: ACK on success, NAK on failure
        
        '''
        intervalnum = int(interval)
        if intervalnum >= 3 and intervalnum <= 60:
            cmdInterval = str(intervalnum)
            cmdSetInterval = 'CONF:PROTOCOL:INTERVAL ' + cmdInterval + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetInterval)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getinterval(self):
        '''
        Read the interval in sec between Uplink message defined by 
        Periodic uplink

        :param: Query only

        :return: It returns the interval in seconds; NAK on failure
        
        '''
        cmdGetInterval = 'READ:PROTOCOL:INTERVAL?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetInterval)
        return result

    def protocol_setframecnt(self, fcnt):
        '''
        Configure an frame count value

        :param fcnt: 0 ~ 65535

        :return: ACK on success, NAK on failure
        
        '''
        fcntnum = int(fcnt)
        if fcntnum >= 0 and fcntnum <= 65535:
            cmdFrameCnt = str(fcntnum)
            cmdSetFrameCnt = 'CONF:PROTOCOL:UPDATE_FCNT ' + cmdFrameCnt + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetFrameCnt)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getframecnt(self):
        '''
        Read the frame count value

        :param: Query only

        :return: It returns the frame count value; NAK on failure
        
        '''
        cmdGetFrameCnt = 'READ:PROTOCOL:UPDATE_FCNT?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetFrameCnt)
        return result

    def protocol_setadrflag(self, adrflag):
        '''
        Configure a flag of ADR support

        :param adrflag: OFF, ON

        :return: ACK on success, NAK on failure
        
        '''
        cmdAdrFlag = adrflag
        if cmdAdrFlag == 'OFF':
            cmdSetAdrFlag = 'CONF:PROTOCOL:ADR OFF' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetAdrFlag)
            return result
        elif cmdAdrFlag == 'ON':
            cmdSetAdrFlag = 'CONF:PROTOCOL:ADR ON' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetAdrFlag)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getadrflag(self):
        '''
        Read the flag of ADR support

        :param: Query only

        :return: It returns the flag status either ON or OFF; 
                 NAK on failure
        
        '''
        cmdGetAdrFlag = 'READ:PROTOCOL:ADR?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetAdrFlag)
        return result

    def protocol_setyear(self, year):
        '''
        Configure the year value for TIME information

        :param year: 2000 ~ 2100

        :return: ACK on success, NAK on failure
        
        '''
        yearnum = int(year)
        if yearnum >= 2000 and yearnum <= 2100:
            cmdYear = str(yearnum)
            cmdSetYear = 'CONF:PROTOCOL:YEAR ' + cmdYear + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetYear)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getyear(self):
        '''
        Read the year value for TIME information

        :param: Query only

        :return: Return year; NAK on failure
        
        '''
        cmdGetYear = 'READ:PROTOCOL:YEAR?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetYear)
        return result

    def protocol_setmonth(self, month):
        '''
        Configure the month value for TIME information

        :param month: 1 ~ 12

        :return: ACK on success, NAK on failure
        
        '''
        monthnum = int(month)
        if monthnum >= 1 and monthnum <= 12:
            cmdMonth = str(monthnum)
            cmdSetMonth = 'CONF:PROTOCOL:MONTH ' + cmdMonth + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMonth)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getmonth(self):
        '''
        Read the month value for TIME information

        :param: Query only

        :return: Return month; NAK on failure
        
        '''
        cmdGetMonth = 'READ:PROTOCOL:MONTH?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMonth)
        return result

    def protocol_setday(self, day):
        '''
        Configure the day value for TIME information

        :param day: 1 ~ 31

        :return: ACK on success, NAK on failure
        
        '''
        daynum = int(day)
        if daynum >= 1 and daynum <= 31:
            cmdDay = str(daynum)
            cmdSetDay = 'CONF:PROTOCOL:DAY ' + cmdDay + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetDay)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getday(self):
        '''
        Read the day value for TIME information

        :param: Query only

        :return: Return day; NAK on failure
        
        '''
        cmdGetDay = 'READ:PROTOCOL:DAY?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetDay)
        return result

    def protocol_sethour(self, hour):
        '''
        Configure the hour value for TIME information

        :param hour: 1 ~ 23

        :return: ACK on success, NAK on failure
        
        '''
        hournum = int(hour)
        if hournum >= 1 and hournum <= 23:
            cmdHour = str(hournum)
            cmdSetHour = 'CONF:PROTOCOL:HOUR ' + cmdHour + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetHour)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_gethour(self):
        '''
        Read the hour value for TIME information

        :param: Query only

        :return: Return hour; NAK on failure
        
        '''
        cmdGetHour = 'READ:PROTOCOL:HOUR?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetHour)
        return result

    def protocol_setminute(self, minute):
        '''
        Configure the minute value for TIME information

        :param minute: 0 ~ 59

        :return: ACK on success, NAK on failure
        
        '''
        minutenum = int(minute)
        if minutenum >= 0 and minutenum <= 59:
            cmdMinute = str(minutenum)
            cmdSetMinute = 'CONF:PROTOCOL:MINUTE ' + cmdMinute + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMinute)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getminute(self):
        '''
        Read the minute value for TIME information

        :param: Query only

        :return: Return minute; NAK on failure
        
        '''
        cmdGetMinute = 'READ:PROTOCOL:MINUTE?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMinute)
        return result

    def protocol_setsecond(self, second):
        '''
        Configure the second value for TIME information

        :param: 0 ~ 59

        :return: ACK on success, NAK on failure
        
        '''
        secondnum = int(second)
        if secondnum >= 0 and secondnum <= 59:
            cmdSecond = str(secondnum)
            cmdSetSecond = 'CONF:PROTOCOL:SECOND ' + cmdSecond + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetSecond)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getsecond(self):
        '''
        Read the second value for TIME information

        :param: Query only

        :return: Return seconds; NAK on failure
        
        '''
        cmdGetSecond = 'READ:PROTOCOL:SECOND?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetSecond)
        return result

    def protocol_setlinkmargin(self, linkmargin):
        '''
        Configure the link margin value in dB for LinkCheckAns

        :param linkmargin: 0 ~ 254

        :return: ACK on success, NAK on failure
        
        '''
        linkmarginnum = int(linkmargin)
        if linkmarginnum >= 0 and linkmarginnum <= 254:
            cmdLinkMargin = str(linkmarginnum)
            cmdSetLinkMargin = 'CONF:PROTOCOL:LINK_MARGIN ' \
                                + cmdLinkMargin \
                                + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetLinkMargin)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getlinkmargin(self):
        '''
        Read the link margin value in dB for LinkCheckAns

        :param: Query only

        :return: It returns the link margin value; NAK on failure
        
        '''
        cmdGetLinkMargin = 'READ:PROTOCOL:LINK_MARGIN?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetLinkMargin)
        return result

    def protocol_setgatewaycntval(self, gwcnt):
        '''
        Configure the gateway count value for LinkCheckAns

        :param gwcnt: 0 ~ 255

        :return: ACK on success, NAK on failure
        
        '''
        gwcntnum = int(gwcnt)
        if gwcntnum >= 0 and gwcntnum <= 255:
            cmdGatewayCnt = str(gwcntnum)
            cmdSetGatewayCnt = 'CONF:PROTOCOL:GATEWAY_CNT ' \
                                + cmdGatewayCnt \
                                + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetGatewayCnt)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getgatewaycntval(self):
        '''
        Read the gateway count value for LinkCheckAns

        :param: Query only

        :return: It returns the gateway count value; NAK on failure
        
        '''
        cmdGetGatewayCnt = 'READ:PROTOCOL:GATEWAY_CNT?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetGatewayCnt)
        return result

    def protocol_setbatterystatusval(self, batterystat):
        '''
        Configure the battery status value for DevStatusAns

        :param batterystat: 0 ~ 255

        :return: ACK on success, NAK on failure
        
        '''
        batterystatnum = int(batterystat)
        if batterystatnum >= 0 and batterystatnum <= 255:
            cmdBatteryStatusVal = str(batterystatnum)
            cmdSetBatteryStatusVal = 'CONF:PROTOCOL:BATTERY ' \
                                        + cmdBatteryStatusVal \
                                        + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetBatteryStatusVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getbatterystatusval(self):
        '''
        Read the battery status value for DevStatusAns

        :param: Query only

        :return: It returns the battery status value; NAK on failure
        
        '''
        cmdGetBatteryStatusVal = 'READ:PROTOCOL:BATTERY?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetBatteryStatusVal)
        return result

    def protocol_setsnrmargin(self, snrval):
        '''
        Configure the SNR margin value in dB for DevStatusAns

        :param snrval: -32 ~ 31

        :return: ACK on success, NAK on failure
        
        '''
        snrnum = int(snrval)
        if snrnum >= -32 and snrnum <= 31:
            cmdSnrMarginVal = str(snrnum)
            cmdSetSnrMarginVal = 'CONF:PROTOCOL:SNR_MARGIN ' \
                                    + cmdSnrMarginVal \
                                    + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetSnrMarginVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getsnrmargin(self):
        '''
        Read the SNR margin value in dB for DevStatusAns

        :param: Query only

        :return: It returns the SNR margin value; NAK on failure
        
        '''
        cmdGetSnrMarginVal = 'READ:PROTOCOL:SNR_MARGIN?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetSnrMarginVal)
        return result
    
    def protocol_getactivationstatus(self):
        '''
        Read the status of activation procedure

        :param: Query only

        :return: It returns activation procedure status; NAK on failure
        
        '''
        cmdGetActivationStatus = 'READ:PROTOCOL:ACTIVATION_STATUS?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetActivationStatus)
        return result

    def protocol_setnwktype(self, nwktype):
        '''
        Configure the sync word in LoRa modulation:
        * 0x12 for private network
        * 0x34 for public network

        :param nwktype: PRIVATE, PUBLIC

        :return: ACK on success, NAK on failure
        
        '''
        cmdNetworkType = nwktype
        if cmdNetworkType == 'PRIVATE':
            cmdSetNetworkType = 'CONF:PROTOCOL:NETWORK PRIVATE' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetNetworkType)
            return result
        elif cmdNetworkType == 'PUBLIC':
            cmdSetNetworkType = 'CONF:PROTOCOL:NETWORK PUBLIC' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetNetworkType)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getnwktype(self):
        '''
        Read the sync word in LoRa modulation:
        * 0x12 for private network
        * 0x34 for public network

        :param: Query only

        :return: It returns the network type; NAK on failure
        
        '''
        cmdGetNetworkType = 'READ:PROTOCOL:NETWORK?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetNetworkType)
        return result

    def protocol_setdownlinkslot(self, slotval):
        '''
        Configure the selection of downlink slot (RX window)

        :param slotval: For EDT, RX1, RX2, PING(Class B), 
                        For GWT, RX1, RX2, RX1&RX2

        :return: ACK on success, NAK on failure
        
        '''
        cmdSlotValue = str(slotval)
        if cmdSlotValue == 'RX1':
            cmdSetDownlinkSlot = 'CONF:PROTOCOL:DOWNLINK_SLOT RX1' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetDownlinkSlot)
            return result
        elif cmdSlotValue == 'RX2':
            cmdSetDownlinkSlot = 'CONF:PROTOCOL:DOWNLINK_SLOT RX2' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetDownlinkSlot)
            return result
        elif cmdSlotValue == 'RX1&RX2':
            cmdSetDownlinkSlot = 'CONF:PROTOCOL:DOWNLINK_SLOT RX1&RX2' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetDownlinkSlot)
            return result
        elif cmdSlotValue == 'PING':
            cmdSetDownlinkSlot = 'CONF:PROTOCOL:DOWNLINK_SLOT PING' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetDownlinkSlot)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getdownlinkslot(self):
        '''
        Read the selection of downlink slot (RX window)

        :param: Query only

        :return: It returns the selected downlink slot; NAK on failure
        
        '''
        cmdGetDownlinkSlot = 'READ:PROTOCOL:DOWNLINK_SLOT?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetDownlinkSlot)
        return result

    def protocol_setmacresponsefield(self, fieldType):
        '''
        Configure the selection of MAC response field type

        :param fieldType: PAYLOAD, FOPTS

        :return: ACK on success, NAK on failure
        
        '''
        fieldTypelist = ['PAYLOAD', 'FOPTS']
        if fieldType in fieldTypelist:
            cmdSetMACRespField = 'CONF:PROTOCOL:MAC_RSP_FIELD ' \
                                    + fieldType \
                                    + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMACRespField)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getmacresponsefield(self):
        '''
        Read the selection of MAC response field type

        :Parameters: N/A (Query only)

        :return: It returns the MAC response field type; NAK on failure

        '''
        cmdGetMACRespField = 'READ:PROTOCOL:MAC_RSP_FIELD?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMACRespField)
        return result

    def protocol_setuplinkdatarate(self, dr):
        '''
        Configure Data Rate of Uplink in GWT mode

        :param dr: For S/W Version 1.150 and 1.160:
                   DR_0, DR_1, DR_2, DR_3, DR_4, DR_5, DR_6, DR_7

                   For S/W Version 1.170 - 1.305:
                   DR0_SF12BW125, DR1_SF11BW125, DR2_SF10BW125, 
                   DR3_SF9BW125, DR4_SF8BW125, DR5_SF7BW125, 
                   DR6_SF7BW250, DR7_FSK50

        :return: ACK on success, NAK on failure
        
        '''
        verList1 = ['1.150', '1.160']
        verList2 = [
            '1.170', '1.200', '1.203', 
            '1.204', '1.206', '1.210', 
            '1.220', '1.221', '1.222', 
            '1.300', '1.305']
        drList1 = [
            'DR_0', 'DR_1', 'DR_2', 'DR_3', 
            'DR_4', 'DR_5', 'DR_6', 'DR_7']
        drList2 = [
            'DR0_SF12BW125', 'DR1_SF11BW125', 
            'DR2_SF10BW125', 'DR3_SF9BW125', 
            'DR4_SF8BW125', 'DR5_SF7BW125', 
            'DR6_SF7BW250', 'DR7_FSK50']
        swVersion = self.query_sysversion()

        if swVersion in verList1 and dr in drList1:
            cmdSetUplinkDr = 'CONF:PROTOCOL:UPLINK_DR ' + dr + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetUplinkDr)
            return result
        elif swVersion in verList2 and dr in drList2:
            cmdSetUplinkDr = 'CONF:PROTOCOL:UPLINK_DR ' + dr + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetUplinkDr)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getuplinkdatarate(self):
        '''
        Read Data Rate of Uplink in GWT mode

        :param: Query only

        :return: It returns the uplink data rate; NAK on failure
        
        '''
        cmdGetUplinkDatarate = 'READ:PROTOCOL:UPLINK_DR?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetUplinkDatarate)
        return result

    def protocol_setrx1_dr_offset(self, rx1droffsetval):
        '''
        Configure RX1_DR_OFFSET value for RXParamSetupReq

        :param rx1droffsetval: 0 ~ 7

        :return: ACK on success, NAK on failure
        
        '''
        if rx1droffsetval >= 0 and rx1droffsetval <= 7:
            cmdRx1DrOffsetVal = str(rx1droffsetval)
            cmdSetRx1DrOffsetVal = 'CONF:PROTOCOL:RX1_DR_OFFSET ' \
                                    + cmdRx1DrOffsetVal \
                                    + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRx1DrOffsetVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getrx1_dr_offset(self):
        '''
        Read RX1_DR_OFFSET value for RXParamSetupReq

        :param: Query only

        :return: It returns RX1_DR_OFFSET value; NAK on failure
        
        '''
        cmdGetRx1DrOffsetVal = 'READ:PROTOCOL:RX1_DR_OFFSET?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetRx1DrOffsetVal)
        return result

    def protocol_setrx2_frequency(self, rx2freq):
        '''
        Configure RX2_FREQ value in MHz for RXParamSetupReq

        :param rx2freq: 400~510, 862~960

        :return: ACK on success, NAK on failure
        
        '''
        if (rx2freq >= 400 
                and rx2freq <= 510) or (rx2freq >= 862 
                    and rx2freq <= 960):
            cmdRx2Frequency = str(rx2freq)
            cmdSetRx2FrequencyVal = 'CONF:PROTOCOL:RX2_FREQ ' \
                                        + cmdRx2Frequency \
                                        + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRx2FrequencyVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getrx2_frequency(self):
        '''
        Read RX2_FREQ value in MHz for RXParamSetupReq

        :param: Query only

        :return: It returns the RX2_FREQ value; NAK on failure
        
        '''
        cmdGetRx2FrequencyVal = 'READ:PROTOCOL:RX2_FREQ?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetRx2FrequencyVal)
        return result

    def protocol_setrx2_dr(self, dr):
        '''
        Configure RX2_DR value for RXParamSetupReq

        :param dr: For S/W Version 1.150 and 1.160:
                   DR_0, DR_1, DR_2, DR_3, DR_4, DR_5, DR_6, DR_7
                   
                   For S/W Version 1.170 - 1.305:
                   DR0_SF12BW125, DR1_SF11BW125, DR2_SF10BW125, 
                   DR3_SF9BW125, DR4_SF8BW125, DR5_SF7BW125, 
                   DR6_SF7BW250, DR7_FSK50

        :return: ACK on success, NAK on failure
        
        '''
        verList1 = ['1.150', '1.160']
        verList2 = [
            '1.170', '1.200', '1.203', '1.204', 
            '1.206', '1.210', '1.220', '1.221', 
            '1.222', '1.300', '1.305']
        drList1 = [
            'DR_0', 'DR_1', 'DR_2', 'DR_3', 
            'DR_4', 'DR_5', 'DR_6', 'DR_7']
        drList2 = [
            'DR0_SF12BW125', 'DR1_SF11BW125', 
            'DR2_SF10BW125', 'DR3_SF9BW125', 
            'DR4_SF8BW125', 'DR5_SF7BW125', 
            'DR6_SF7BW250', 'DR7_FSK50']
        swVersion = self.query_sysversion()

        if swVersion in verList1 and dr in drList1:
            cmdSetRx2Dr = 'CONF:PROTOCOL:RX2_DR ' + dr + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRx2Dr)
            return result
        elif swVersion in verList2 and dr in drList2:
            cmdSetRx2Dr = 'CONF:PROTOCOL:RX2_DR ' + dr + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRx2Dr)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getrx2_dr(self):
        '''
        Read RX2_DR value for RXParamSetupReq

        :param: Query only

        :return: It returns the RX2 Data rate value; NAK on failure
        
        '''
        cmdGetRx2DrVal = 'READ:PROTOCOL:RX2_DR?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetRx2DrVal)
        return result

    def protocol_setpingperiodicity(self, period):
        '''
        Configure the periodicity of Ping for Class B

        :param period: 0 ~ 7

        :return: ACK on success, NAK on failure
        
        '''
        if period >= 0 and period <= 7:
            cmdPingPeriodicity = str(period)
            cmdSetPingPeriodicityVal = 'CONF:PROTOCOL:PING_PERIODICITY ' \
                                        + cmdPingPeriodicity \
                                        + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPingPeriodicityVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getpingperiodicity(self):
        '''
        Read the periodicity of Ping for Class B

        :param: Query only

        :return: It returns the ping periodicity value; NAK on failure
        
        '''
        cmdGetPingPeriodicity = 'READ:PROTOCOL:PING_PERIODICITY?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetPingPeriodicity)
        return result

    def protocol_setprotocolver(self, version):
        '''
        Configure the protocol version of LoRaWAN

        :param version: LoRaWAN1.0.2, LoRaWAN 1.0.3, LoRaWAN1.1

        :return: ACK on success, NAK on failure
        
        '''
        cmdProtocolVersion = version
        if cmdProtocolVersion == 'LoRaWAN1.0.2':
            cmdSetProtocolVersion = 'CONF:PROTOCOL:PROTOCOL_VER LoRaWAN1.0.2' \
                                        + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetProtocolVersion)
            return result
        elif cmdProtocolVersion == 'LoRaWAN1.0.3':
            cmdSetProtocolVersion = 'CONF:PROTOCOL:PROTOCOL_VER LoRaWAN1.0.3' \
                                        + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetProtocolVersion)
            return result
        elif cmdProtocolVersion == 'LoRaWAN1.1':
            cmdSetProtocolVersion = 'CONF:PROTOCOL:PROTOCOL_VER LoRaWAN1.1' \
                                        + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetProtocolVersion)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getprotocolver(self):
        '''
        Read the protocol version of LoRaWAN

        :param: Query only

        :return: It returns the LoRaWAN protocol version; 
                 NAK on failure
        
        '''
        cmdGetProtocolVersion = 'READ:PROTOCOL:PROTOCOL_VER?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetProtocolVersion)
        return result

    def protocol_setnwkkey(self, value):
        '''
        Configure the NwkKey value (LoRaWAN V1.1 only)

        :param value: 128-bit HEX value

        :return: ACK on success, NAK on failure
        
        '''
        cmdValue = int(value)
        if (cmdValue >= 0 and cmdValue <= 2**128 - 1):
            cmdHexValue = hex(cmdValue)
            cmdSetNwkKeyVal = 'CONF:PROTOCOL:NWK_KEY ' + cmdHexValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetNwkKeyVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getnwkkey(self):
        '''
        Read the NwkKey value (LoRaWAN V1.1 only)

        :param: Query only

        :return: It returns the network key value; NAK on failure
        
        '''
        cmdGetNwkKey = 'READ:PROTOCOL:NWK_KEY?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetNwkKey)
        return result

    def protocol_setfnwksintkey(self, value):
        '''
        Configure the FNwkSIntKey value (LoRaWAN V1.1 only)

        :param value: 128-bit HEX value

        :return: ACK on success, NAK on failure
        
        '''
        cmdValue = int(value)
        if (cmdValue >= 0 and cmdValue <= 2**128 - 1):
            cmdHexValue = hex(cmdValue)
            cmdSetFNwkSKeyVal = 'CONF:PROTOCOL:FNWKS_IKEY ' \
                                    + cmdHexValue \
                                    + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetFNwkSKeyVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getfnwksintkey(self):
        '''
        Read the FNwkSIntKey value (LoRaWAN V1.1 only)

        :param: Query only

        :return: It returns FNwkSIntKey value; NAK on failure
        
        '''
        cmdGetFNwkSKey = 'READ:PROTOCOL:FNWKS_IKEY?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetFNwkSKey)
        return result

    def protocol_setsnwksintkey(self, value):
        '''
        Configure the SNwkSIntKey value (LoRaWAN V1.1 only)

        :param value: 128-bit HEX value

        :return: ACK on success, NAK on failure
        
        '''
        cmdValue = int(value)
        if (cmdValue >= 0 and cmdValue <= 2**128 - 1):
            cmdHexValue = hex(cmdValue)
            cmdSetSNwkSKeyVal = 'CONF:PROTOCOL:SNWKS_IKEY ' \
                                    + cmdHexValue \
                                    + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetSNwkSKeyVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getsnwksintkey(self):
        '''
        Read the SNwkSIntKey value (LoRaWAN V1.1 only)

        :param: Query only

        :return: It returns SNwkSIntKey value; NAK on failure
        
        '''
        cmdGetSNwkSKey = 'READ:PROTOCOL:SNWKS_IKEY?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetSNwkSKey)
        return result

    def protocol_setnwksenckey(self, value):
        '''
        Configure the NwkSEncKey value (LoRaWAN V1.1 only)

        :param value: 128-bit HEX value

        :return: ACK on success, NAK on failure
        
        '''
        cmdValue = int(value)
        if (cmdValue >= 0 and cmdValue <= 2**128 - 1):
            cmdHexValue = hex(cmdValue)
            cmdSetNwkSEncKeyVal = 'CONF:PROTOCOL:NWKS_EKEY ' \
                                    + cmdHexValue \
                                    + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetNwkSEncKeyVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getnwksenckey(self):
        '''
        Read the NwkSEncKey value (LoRaWAN V1.1 only)

        :param: Query only

        :return: It returns NwkSEncKey value; NAK on failure
        
        '''
        cmdGetNwkSEncKey = 'READ:PROTOCOL:NWKS_EKEY?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetNwkSEncKey)
        return result

    def protocol_setjoineuival(self, value):
        '''
        Configure the JoinEUI value (LoRaWAN V1.1 only)

        :param value: 64-bit HEX value

        :return: ACK on success, NAK on failure
        
        '''
        cmdValue = int(value)
        if (cmdValue >= 0 and cmdValue <= 2**64 - 1):
            cmdHexValue = hex(cmdValue)
            cmdSetJoinEuiVal = 'CONF:PROTOCOL:JOIN_EUI ' + cmdHexValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetJoinEuiVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getjoineuival(self):
        '''
        Read the JoinEUI value (LoRaWAN V1.1 only)

        :param: Query only

        :return: It returns the JoinEUI value; NAK on failure
        
        '''
        cmdGetJoinEuiVal = 'READ:PROTOCOL:JOIN_EUI?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetJoinEuiVal)
        return result

    def protocol_setnfcntval(self, nfcnt):
        '''
        Configure the NFCnt Value (LoRaWAN V1.1 only)

        :param nfcnt: 0 ~ 65535

        :return: ACK on success, NAK on failure
        
        '''
        if nfcnt >= 0 and nfcnt <= 65535:
            cmdNfCnt = str(nfcnt)
            cmdSetNfCntVal = 'CONF:PROTOCOL:UPDATE_NFCNT ' + cmdNfCnt + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetNfCntVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getnfcntval(self):
        '''
        Read the NFCnt Value (LoRaWAN V1.1 only)

        :param: Query only

        :return: It returns the NFCnt value; NAK on failure
        
        '''
        cmdGetNfCnt = 'READ:PROTOCOL:UPDATE_NFCNT?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetNfCnt)
        return result

    def protocol_setafcntval(self, afcnt):
        '''
        Configure the AFCnt Value (LoRaWAN V1.1 only)

        :param: 0 ~ 65535

        :return: ACK on success, NAK on failure
        
        '''
        if afcnt >= 0 and afcnt <= 65535:
            cmdAfCnt = str(afcnt)
            cmdSetAfCntVal = 'CONF:PROTOCOL:UPDATE_AFCNT ' + cmdAfCnt + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetAfCntVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getafcntval(self):
        '''
        Read the AFCnt Value (LoRaWAN V1.1 only)

        :param: Query only

        :return: It returns the AFCnt value; NAK on failure
        
        '''
        cmdGetAfCnt = 'READ:PROTOCOL:UPDATE_AFCNT?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetAfCnt)
        return result

    def protocol_getdownlinkdwelltime(self):
        '''
        Read the downlink dwell time in GWT mode

        :param: Query only

        :return: -
        
        '''
        cmdGetDownlinkDwellTime = 'READ:PROTOCOL:DL_DWELL_TIME?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetDownlinkDwellTime)
        return result

    def protocol_getuplinkdwelltime(self):
        '''
        Read the uplink dwell time in GWT mode

        :param: Query only

        :return: -
        
        '''
        cmdGetUplinkDwellTime = 'READ:PROTOCOL:UL_DWELL_TIME?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetUplinkDwellTime)
        return result

    def protocol_setlatitude(self, lat):
        '''
        Configure the latitude value in Beacon frame for Class B

        :param lat: -90 ~ 90

        :return: ACK on success, NAK on failure
        
        '''
        if lat >= -90 and lat <= 90:
            cmdLatitude = str(lat)
            cmdLatitudeVal = 'CONF:PROTOCOL:LATITUDE ' + cmdLatitude + '\n'
            result = RwcSerialSetup.transceive(self, cmdLatitudeVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getlatitude(self):
        '''
        Read the latitude value in Beacon frame for Class B

        :param: Query only

        :return: It returns the latitude value; NAK on failure
        
        '''
        cmdGetLatitude = 'READ:PROTOCOL:LATITUDE?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetLatitude)
        return result

    def protocol_setlongitude(self, long):
        '''
        Configure the longitude value in Beacon frame for Class B

        :param long: -180 ~ 180

        :return: ACK on success, NAK on failure
        
        '''
        if long >= -180 and long <= 180:
            cmdLongitude = str(long)
            cmdLongitudeVal = 'CONF:PROTOCOL:LONGITUDE ' + cmdLongitude + '\n'
            result = RwcSerialSetup.transceive(self, cmdLongitudeVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getlongitude(self):
        '''
        Read the longitude value in Beacon frame for Class B

        :param: Query only

        :return: It returns the longitude value; NAK on failure
        
        '''
        cmdGetLongitude = 'READ:PROTOCOL:LONGITUDE?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetLongitude)
        return result

    def protocol_setduttype(self, duttype):
        '''
        Configure the type of DUT, which determines whether the frame 
        is for uplink or downlink. (Supported version: v1.15 - v1.21)

        :param duttype: END_DEVICE, GATEWAY

        :return: ACK on success, NAK on failure
        
        '''
        dutTypeList = ['END_DEVICE', 'GATEWAY']
        cmdSupportedVersion = [
            '1.150', '1.160', '1.170', '1.200', 
            '1.203', '1.204', '1.206', '1.210']
        verStatus = self.validate_sys_swversion(cmdSupportedVersion)

        if verStatus and duttype in dutTypeList:
            cmdSetDutType = 'CONF:PROTOCOL:DUT_TYPE ' + duttype + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetDutType)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getduttype(self):
        '''
        Read the type of DUT, which determines whether the frame is for 
        uplink or downlink. (Supported version: v1.15 - v1.21)

        :param: Query only

        :return: It returns the DUT type; NAK on failure
        
        '''
        cmdSupportedVersion = [
            '1.150', '1.160', '1.170', '1.200', 
            '1.204', '1.203', '1.206', '1.210']
        verStatus = self.validate_sys_swversion(cmdSupportedVersion)

        if verStatus:
            cmdGetDutType = 'READ:PROTOCOL:DUT_TYPE?' + '\n'
            result = RwcSerialSetup.transceive(self, cmdGetDutType)
            return result

    def protocol_setmacformatflag(self, macformatflag):
        '''
        Configure the flag whether to use MAC protocol parameters in 
        LoRa test frame in NST mode (Supported version: v1.15 - v1.17)

        :param macformatflag: OFF, ON

        :return: ACK on success, NAK on failure
        
        '''
        macFormatFlagList = ['OFF', 'ON']
        cmdSupportedVersion = ['1.150', '1.160', '1.170']
        verStatus = self.validate_sys_swversion(cmdSupportedVersion)

        if verStatus and macformatflag in macFormatFlagList:
            cmdSetMacFormatFlag = 'CONF:PROTOCOL:MAC_FORMAT ' \
                                    + macformatflag \
                                    + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMacFormatFlag)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getmacformatflag(self):
        '''
        Read the flag whether to use MAC protocol parameters in LoRa 
        test frame in NST mode (Supported version: v1.15 - v1.17)

        :param: Query only

        :return: It returns the flag status; NAK on failure
        
        '''
        cmdSupportedVersion = ['1.150', '1.160', '1.170']
        verStatus = self.validate_sys_swversion(cmdSupportedVersion)
        if verStatus:
            cmdGetMacFormatFlag = 'READ:PROTOCOL:MAC_FORMAT?' + '\n'
            result = RwcSerialSetup.transceive(self, cmdGetMacFormatFlag)
            return result

    def protocol_setnstfcnt(self, nstfcnt):
        '''
        Configure the FCnt field of LoRa test frame in NST mode 
        (Supported version: v1.15 - v1.17)

        :param nstfcnt: 0 ~ 65535

        :return: ACK on success, NAK on failure
        
        '''
        cmdSupportedVersion = ['1.150', '1.160', '1.170']
        verStatus = self.validate_sys_swversion(cmdSupportedVersion)

        if verStatus and (nstfcnt >= 0 and nstfcnt <= 65535):
            cmdNstFCnt = str(nstfcnt)
            cmdSetNstFCntVal = 'CONF:PROTOCOL:FCNT ' + cmdNstFCnt + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetNstFCntVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getnstfcnt(self):
        '''
        Read the FCnt field of LoRa test frame in NST mode 
        (Supported version: v1.15 - v1.17)

        :param: Query only

        :return: It returns the FCnt value; NAK on failure
        
        '''
        cmdSupportedVersion = ['1.150', '1.160', '1.170']
        verStatus = self.validate_sys_swversion(cmdSupportedVersion)

        if verStatus:
            cmdGetNstFcnt = 'READ:PROTOCOL:FCNT?' + '\n'
            result = RwcSerialSetup.transceive(self, cmdGetNstFcnt)
            return result

    def protocol_setnstfcntmode(self, fcntmode):
        '''
        Configure the operation mode of FCnt field of LoRa test frame 
        in NST mode (Supported version: v1.15 - v1.17)

        :param fcntmode: FIXED, INCREASING

        :return: ACK on success, NAK on failure
        
        '''
        fcntModeList = ['FIXED', 'INCREASING']
        cmdSupportedVersion = ['1.150', '1.160', '1.170']
        verStatus = self.validate_sys_swversion(cmdSupportedVersion)

        if verStatus and fcntmode in fcntModeList:
            cmdSetFcntMode = 'CONF:PROTOCOL:FCNT_MODE ' + fcntmode + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetFcntMode)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getnstfcntmode(self):
        '''
        Read the operation mode of FCnt field of LoRa test frame in 
        NST mode (Supported version: v1.15 - v1.17)

        :param: Query only

        :return: It returns the FCnt mode; NAK on failure
        
        '''
        cmdSupportedVersion = ['1.150', '1.160', '1.170']
        verStatus = self.validate_sys_swversion(cmdSupportedVersion)

        if verStatus:
            cmdGetNstFcntMode = 'READ:PROTOCOL:FCNT_MODE?' + '\n'
            result = RwcSerialSetup.transceive(self, cmdGetNstFcntMode)
            return result

    def protocol_setnstack(self, nstack):
        '''
        Configure the ACK field of LoRa test frame in NST mode 
        (Supported version: v1.15 - v1.21)

        :param nstack: OFF, ON

        :return: ACK on success, NAK on failure
        
        '''
        nstAckList = ['OFF', 'ON']
        cmdSupportedVersion = ['1.150', '1.160', '1.170']
        verStatus = self.validate_sys_swversion(cmdSupportedVersion)

        if verStatus and nstack in nstAckList:
            cmdSetNstAck = 'CONF:PROTOCOL:ACK ' + nstack + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetNstAck)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getnstack(self):
        '''
        Read the ACK field of LoRa test frame in NST mode 
        (Supported version: v1.15 - v1.17)

        :param: Query only

        :return: It returns the NST ACK status; NAK on failure
        
        '''
        cmdSupportedVersion = ['1.150', '1.160', '1.170']
        verStatus = self.validate_sys_swversion(cmdSupportedVersion)

        if verStatus:
            cmdGetNstAck = 'READ:PROTOCOL:ACK?' + '\n'
            result = RwcSerialSetup.transceive(self, cmdGetNstAck)
            return result

    def protocol_setnst_adrackreq(self, adrackreq):
        '''
        Configure the ADRACKReq field of LoRa test frame in NST mode 
        (Supported version: v1.15 - v1.17)

        :param adrackreq: OFF, ON

        :return: ACK on success, NAK on failure
        
        '''
        adrAckReqList = ['OFF', 'ON']
        cmdSupportedVersion = ['1.150', '1.160', '1.170']
        verStatus = self.validate_sys_swversion(cmdSupportedVersion)

        if verStatus and adrackreq in adrAckReqList:
            cmdSetAdrAckReq = 'CONF:PROTOCOL:ADR_ACK_REQ ' + adrackreq + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetAdrAckReq)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getnst_adrackreq(self):
        '''
        Read the ADRACKReq field of LoRa test frame in NST mode 
        (Supported version: v1.15 - v1.17)

        :param: Query only

        :return: It returns the ADRACKReq status; NAK on failure
        
        '''
        cmdSupportedVersion = ['1.150', '1.160', '1.170']
        verStatus = self.validate_sys_swversion(cmdSupportedVersion)

        if verStatus:
            cmdGetNstAdrAckReq = 'READ:PROTOCOL:ADR_ACK_REQ?' + '\n'
            result = RwcSerialSetup.transceive(self, cmdGetNstAdrAckReq)
            return result

    def protocol_setnstfpending(self, fpending):
        '''
        Configure the FPending field of LoRa test frame in NST mode 
        (Supported version: v1.15 - v1.17)

        :param fpending: OFF, ON

        :return: ACK on success, NAK on failure
        
        '''
        fpendingList = ['OFF', 'ON']
        cmdSupportedVersion = ['1.150', '1.160', '1.170']
        verStatus = self.validate_sys_swversion(cmdSupportedVersion)

        if verStatus and fpending in fpendingList:
            cmdSetNstFpending = 'CONF:PROTOCOL:FPENDING ' + fpending + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetNstFpending)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getnstfpending(self):
        '''
        Read the FPending field of LoRa test frame in NST mode 
        (Supported version: v1.15 - v1.17)

        :param: Query only

        :return: It returns the NST Fpending status; NAK on failure
        
        '''
        cmdSupportedVersion = ['1.150', '1.160', '1.170']
        verStatus = self.validate_sys_swversion(cmdSupportedVersion)

        if verStatus:
            cmdGetNstFpending = 'READ:PROTOCOL:FPENDING?' + '\n'
            result = RwcSerialSetup.transceive(self, cmdGetNstFpending)
            return result

    def protocol_setedtperiodiclink(self, periodicdownlink):
        '''
        Configure the Periodic Downlink mode for class B in EDT

        :param periodicdownlink: NONE, CONFIRMED_DOWN, UNCONFIRMED_DOWN

        :return: ACK on success, NAK on failure
        
        '''
        cmdEdtPeriodicDownlink = periodicdownlink
        if cmdEdtPeriodicDownlink == 'NONE':
            cmdSetEdtPeriodicDownlink = 'CONF:PROTOCOL:PERIODIC_DOWNLINK NONE' \
                                            + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetEdtPeriodicDownlink)
            return result
        elif cmdEdtPeriodicDownlink == 'CONFIRMED_DOWN':
            cmdSetEdtPeriodicDownlink = 'CONF:PROTOCOL:PERIODIC_DOWNLINK CONFIRMED_DOWN' \
                                            + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetEdtPeriodicDownlink)
            return result
        elif cmdEdtPeriodicDownlink == 'UNCONFIRMED_DOWN':
            cmdSetEdtPeriodicDownlink = 'CONF:PROTOCOL:PERIODIC_DOWNLINK UNCONFIRMED_DOWN' \
                                            + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetEdtPeriodicDownlink)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getedtperiodiclink(self):
        '''
        Read the Periodic Downlink mode for class B in EDT

        :param: Query only

        :return: It returns the periodic downlink mode for class B; 
                 NAK on failure
        
        '''
        cmdGetEdtPeriodicDownlink = 'READ:PROTOCOL:PERIODIC_DOWNLINK?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetEdtPeriodicDownlink)
        return result

    def protocol_setclaamode(self, claamode):
        '''
        Configure the CLAA mode

        :param claamode: D, E

        :return: ACK on success, NAK on failure
        
        '''
        cmdClaaMode = claamode
        if cmdClaaMode == 'D':
            cmdSetClaaMode = 'CONF:PROTOCOL:CLAA_MODE D' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetClaaMode)
            return result
        elif cmdClaaMode == 'E':
            cmdSetClaaMode = 'CONF:PROTOCOL:CLAA_MODE E' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetClaaMode)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getclaamode(self):
        '''
        Read the CLAA mode

        :param: Query only

        :return: It returns CLAA mode; NAK on failure

        '''
        cmdGetClaaMode = 'READ:PROTOCOL:CLAA_MODE?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetClaaMode)
        return result

    def protocol_setnwkid(self, value):
        '''
        Configure the Network id

        :param value: 0 ~ 0x7F

        :return: ACK on success, NAK on failure
        
        '''
        cmdValue = int(value)
        if (cmdValue >= 0 and cmdValue <= 2**7 - 1):
            cmdHexValue = hex(cmdValue)
            cmdSetNwkId = 'CONF:PROTOCOL:NWK_ID ' + cmdHexValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetNwkId)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getnwkid(self):
        '''
        Read the Network id

        :param: Query only

        :return: It returns the network id; NAK on failure
        
        '''
        cmdGetNwkId = 'READ:PROTOCOL:NWK_ID?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetNwkId)
        return result

    def protocol_setnetidmsb(self, value):
        '''
        Configure the MSB of net id

        :param value: 0 ~ 0x1FFFF

        :return: ACK on success, NAK on failure
        
        '''
        cmdValue = int(value)
        if (cmdValue >= 0 and cmdValue <= 2**17 - 1):
            cmdHexValue = hex(cmdValue)
            cmdSetNetIdMsb = 'CONF:PROTOCOL:NET_ID_MSB ' + cmdHexValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetNetIdMsb)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getnetidmsb(self):
        '''
        Read the MSB of net id

        :param: Query only

        :return: It returns the MSB of net id; NAK on failure
        
        '''
        cmdGetNetIdMsb = 'READ:PROTOCOL:NET_ID_MSB?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetNetIdMsb)
        return result

    def protocol_setnwkaddr(self, value):
        '''
        Configure the Network Address

        :param value: 0 ~ 0x1FFFFFF

        :return: ACK on success, NAK on failure
        
        '''
        cmdValue = int(value)
        if (cmdValue >= 0 and cmdValue <= 2**25 - 1):
            cmdHexValue = hex(cmdValue)
            cmdSetNwkAddr = 'CONF:PROTOCOL:NWK_ADDR ' + cmdHexValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetNwkAddr)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getnwkaddr(self):
        '''
        Read the Network Address

        :param: Query only

        :return: It returns the network address; NAK on failure
        
        '''
        cmdGetNwkAddr = 'READ:PROTOCOL:NWK_ADDR?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetNwkAddr)
        return result

    def protocol_setpingtimeoffset(self, value):
        '''
        Configure the Ping time offset

        :param value: -1000 ~ 1000 ms

        :return: ACK on success, NAK on failure
        
        '''
        if value >= -1000 and value <= 1000:
            cmdParam = str(value)
            cmdSetPingTimeOffset = 'CONF:PROTOCOL:PING_TIME_OFFSET ' \
                                    + cmdParam \
                                    + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPingTimeOffset)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def protocol_getpingtimeoffset(self):
        '''
        Read the Ping time offset

        :param: Query only

        :return: It returns the Ping time offset value; NAK on failure

        '''
        cmdGetPingTimeOffset = 'READ:PROTOCOL:PING_TIME_OFFSET?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetPingTimeOffset)
        return result

    def protocol_setmacrspslot(self, slotvalue):
        '''
        Config the MAC Response slot in GWT

        :param: RX1, RX2

        :return: ACK on success, NAK on failure
        
        '''
        slotlist = ['RX1', 'RX2']
        if slotvalue in slotlist:
            cmdSetMacRspSlot = 'CONF:PROTOCOL:MAC_RSP_SLOT ' \
                                + slotvalue \
                                + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMacRspSlot)
            return result
        else:
            raise Exception('Invalid Mac Slot received.')

    def protocol_getmacrspslot(self):
        '''
        Read the MAC Response slot in GWT

        :param: Query only

        :return: It returns the MAC Response slot value; NAK on failure

        
        .. _linklabel:
        '''
        cmdGetMacRspSlot = 'READ:PROTOCOL:MAC_RSP_SLOT?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMacRspSlot)
        return result

    #Link Command Methods
    def link_run(self):
        '''
        Start link creation

        :Parameters: N/A

        :return: None
        
        '''
        cmdLinkStart = 'EXEC:LINK:RUN' + '\n'
        result = RwcSerialSetup.transceive(self, cmdLinkStart)
        return result

    def link_stop(self):
        '''
        Stop the current link

        :Parameters: N/A

        :return: None
        
        '''
        cmdLinkStop = 'EXEC:LINK:STOP' + '\n'
        result = RwcSerialSetup.transceive(self, cmdLinkStop)
        return result

    def link_status(self):
        '''
        Read link running status

        :Parameters: N/A

        :return: It will return RUNNING or STOPPED
        
        '''
        cmdLinkStatus = 'READ:LINK:STATUS?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdLinkStatus)
        return result

    def link_clear(self):
        '''
        Clear the list of link messages and measured power data

        :Parameters: N/A

        :return: None
        
        '''
        cmdLinkClear = 'EXEC:LINK:CLEAR' + '\n'
        result = RwcSerialSetup.transceive(self, cmdLinkClear)
        return result

    def link_getactivationstatus(self):
        '''
        Read the status of activation procedure

        :Parameters: Query only

        :return: It returns the activation procedure status; 
                 NAK on failure
        
        '''
        cmdGetActivationStatus = 'READ:LINK:ACTIVATION_STATUS?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetActivationStatus)
        return result

    def link_getinfo(self):
        '''
        Read the link information messages

        :Parameters: Query only

        :return: It returns the link information; NAK on failure
        
        '''
        cmdGetInfoMsg = 'READ:INFO_MSG?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetInfoMsg)
        return result

    def link_msgreset(self):
        '''
        It sets Read link message pointer current position

        :Parameters: N/A

        :return: None
        
        '''
        cmdLinkMsgReset = 'EXEC:LINK:MSG_RESET' + '\n'
        result = RwcSerialSetup.transceive(self, cmdLinkMsgReset)
        return result

    def link_readmsg(self):
        '''
        Read the link messages with detailed information

        :Parameters: Query only

        :return: It returns the link message information; NAK on failure
        
        '''
        cmdGetReadMsg = 'READ:LINK:MSG?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetReadMsg)
        return result

    def link_sendmac(self):
        '''
        Force RWC5020A to send the defined MAC command

        :Parameters: N/A

        :return: ACK on success, NAK on failure
        
        '''
        cmdLinkSendMac = 'EXEC:LINK:MAC_SEND' + '\n'
        result = RwcSerialSetup.transceive(self, cmdLinkSendMac, 3)
        return result

    def link_setmaccmdtype(self, cmdtype):
        '''
        Configure the message type of MAC Command to send to the DUT

        :param cmdtype: UNCONFIRMED, CONFIRMED

        :return: ACK on success, NAK on failure
        
        '''
        cmdMactype = cmdtype
        if cmdMactype == 'UNCONFIRMED':
            cmdSetMactype = 'CONF:LINK:MAC_CMD_TYPE UNCONFIRMED' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMactype)
            return result
        elif cmdMactype == 'CONFIRMED':
            cmdSetMactype = 'CONF:LINK:MAC_CMD_TYPE CONFIRMED' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMactype)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getmaccmdtype(self):
        '''
        Read the message type of MAC Command to send to the DUT

        :param: Query only

        :return: It returns MAC Command Type; NAK on failure
        
        '''
        cmdGetMacType = 'READ:LINK:MAC_CMD_TYPE?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMacType)
        return result

    def link_setmacanstimeout(self, value):
        '''
        Configure the time out of MAC Answer after sending MAC Command

        :param value: 1 ~ 100

        :return: ACK on success, NAK on failure
        
        '''
        
        if (value >= 1) and (value <= 100):
            cmdValue = str(value)
            cmdSetMacAnsTo = 'CONF:LINK:MAC_ANS_TO ' + cmdValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMacAnsTo)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getmacanstimeout(self):
        '''
        Read the time out of MAC Answer after sending MAC Command

        :param: Query only

        :return: It returns time out of MAC Answer; NAK on failure
        
        '''
        cmdGetMacAnsTo = 'READ:LINK:MAC_ANS_TO?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMacAnsTo)
        return result

    def link_setmaccmdfield(self, cmdfield):
        '''
        Configure the field where MAC Command is sent

        :param cmdfield: PAYLOAD, FOPTS

        :return: ACK on success, NAK on failure
        
        '''
        cmdMacField = cmdfield
        if cmdMacField == 'PAYLOAD':
            cmdSetMacField = 'CONF:LINK:MAC_CMD_FIELD PAYLOAD' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMacField)
            return result
        elif cmdMacField == 'FOPTS':
            cmdSetMacField = 'CONF:LINK:MAC_CMD_FIELD FOPTS' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMacField)
            return result
        elif cmdMacField == 'FOPTION':
            cmdSetMacField = 'CONF:LINK:MAC_CMD_FIELD FOPTS' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMacField)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getmaccmdfield(self):
        '''
        Read the field where MAC Command is sent

        :param: Query only

        :return: It returns the MAC Command field; NAK on failure
        
        '''
        cmdGetMacField = 'READ:LINK:MAC_CMD_FIELD?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMacField)
        return result

    def link_setinstantmaccmd(self, macnum, dutcmd):
        '''
        Configure the MAC Command to send to the DUT

        :param macnum: MAC Command Number
        :param dutcmd: For EDT, DEV_STATUS, LINK_ADR, DUTY_CYCLE, 
                       RX_PARAM_SETUP, TX_PARAM_SETUP, NEW_CHANNEL, 
                       DL_CHANNEL, RX_TIMING_SETUP, USER_DEFINED, 
                       ACTIVATE_TM, DEACTIVATE_TM, CONFIRMED_TM,
                       UNCONFIRMED_TM, ECHO_REQUEST_TM, 
                       TRIGGER_JOIN_REQ_TM, ENABLE_CW_MODE_TM, 
                       BEACON_FREQ, PING_SLOT_CH, 
                       FORCE_REJOIN, REJOIN_SETUP, ADR_SETUP

                       For GWT, LINK_CHECK, DEVICE_TIME, DEVICE_MODE, 
                       RESET_IND

        :return: ACK on success, NAK on failure
                
        '''
        cmdMacDut = str(dutcmd)
        cmdMacNum = str(macnum)
        
        if cmdMacDut == 'DEV_STATUS':
            cmdSetMacDut = 'CONF:LINK:INSTANT_MAC_CMD ' \
                            + cmdMacNum \
                            + ' DEV_STATUS' \
                            + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMacDut)
            return result
        elif cmdMacDut == 'LINK_ADR':
            cmdSetMacDut = 'CONF:LINK:INSTANT_MAC_CMD ' \
                            + cmdMacNum \
                            + ' LINK_ADR' \
                            + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMacDut)
            return result
        elif cmdMacDut == 'DUTY_CYCLE':
            cmdSetMacDut = 'CONF:LINK:INSTANT_MAC_CMD ' \
                            + cmdMacNum \
                            + ' DUTY_CYCLE' \
                            + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMacDut)
            return result
        elif cmdMacDut == 'RX_PARAM_SETUP':
            cmdSetMacDut = 'CONF:LINK:INSTANT_MAC_CMD ' \
                            + cmdMacNum \
                            + ' RX_PARAM_SETUP' \
                            + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMacDut)
            return result
        elif cmdMacDut == 'TX_PARAM_SETUP':
            cmdSetMacDut = 'CONF:LINK:INSTANT_MAC_CMD ' \
                            + cmdMacNum \
                            + ' TX_PARAM_SETUP' \
                            + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMacDut)
            return result
        elif cmdMacDut == 'NEW_CHANNEL':
            cmdSetMacDut = 'CONF:LINK:INSTANT_MAC_CMD ' \
                            + cmdMacNum \
                            + ' NEW_CHANNEL' \
                            + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMacDut)
            return result
        elif cmdMacDut == 'DL_CHANNEL':
            cmdSetMacDut = 'CONF:LINK:INSTANT_MAC_CMD ' \
                            + cmdMacNum \
                            + ' DL_CHANNEL' \
                            + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMacDut)
            return result
        elif cmdMacDut == 'RX_TIMING_SETUP':
            cmdSetMacDut = 'CONF:LINK:INSTANT_MAC_CMD ' \
                            + cmdMacNum \
                            + ' RX_TIMING_SETUP' \
                            + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMacDut)
            return result
        elif cmdMacDut == 'USER_DEFINED':
            cmdSetMacDut = 'CONF:LINK:INSTANT_MAC_CMD ' \
                            + cmdMacNum \
                            + ' USER_DEFINED' \
                            + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMacDut)
            return result
        elif cmdMacDut == 'ACTIVATE_TM':
            cmdSetMacDut = 'CONF:LINK:INSTANT_MAC_CMD ' \
                            + cmdMacNum \
                            + ' ACTIVATE_TM' \
                            + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMacDut)
            return result
        elif cmdMacDut == 'DEACTIVATE_TM':
            cmdSetMacDut = 'CONF:LINK:INSTANT_MAC_CMD ' \
                            + cmdMacNum \
                            + ' DEACTIVATE_TM' \
                            + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMacDut)
            return result
        elif cmdMacDut == 'CONFIRMED_TM':
            cmdSetMacDut = 'CONF:LINK:INSTANT_MAC_CMD ' \
                            + cmdMacNum \
                            + ' CONFIRMED_TM' \
                            + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMacDut)
            return result
        elif cmdMacDut == 'UNCONFIRMED_TM':
            cmdSetMacDut = 'CONF:LINK:INSTANT_MAC_CMD ' \
                            + cmdMacNum \
                            + ' UNCONFIRMED_TM' \
                            + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMacDut)
            return result
        elif cmdMacDut == 'ECHO_REQUEST_TM':
            cmdSetMacDut = 'CONF:LINK:INSTANT_MAC_CMD ' \
                            + cmdMacNum \
                            + ' ECHO_REQUEST_TM' \
                            + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMacDut)
            return result
        elif cmdMacDut == 'TRIGGER_JOIN_REQ_TM':
            cmdSetMacDut = 'CONF:LINK:INSTANT_MAC_CMD ' \
                            + cmdMacNum \
                            + ' TRIGGER_JOIN_REQ_TM' \
                            + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMacDut)
            return result
        elif cmdMacDut == 'ENABLE_CW_MODE_TM':
            cmdSetMacDut = 'CONF:LINK:INSTANT_MAC_CMD ' \
                            + cmdMacNum \
                            + ' ENABLE_CW_MODE_TM' \
                            + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMacDut)
            return result
        elif cmdMacDut == 'BEACON_FREQ':
            cmdSetMacDut = 'CONF:LINK:INSTANT_MAC_CMD ' \
                            + cmdMacNum \
                            + ' BEACON_FREQ' \
                            + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMacDut)
            return result
        elif cmdMacDut == 'PING_SLOT_CH':
            cmdSetMacDut = 'CONF:LINK:INSTANT_MAC_CMD ' \
                            + cmdMacNum \
                            + ' PING_SLOT_CH' \
                            + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMacDut)
            return result
        elif cmdMacDut == 'FORCE_REJOIN':
            cmdSetMacDut = 'CONF:LINK:INSTANT_MAC_CMD ' \
                            + cmdMacNum \
                            + ' FORCE_REJOIN' \
                            + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMacDut)
            return result
        elif cmdMacDut == 'REJOIN_SETUP':
            cmdSetMacDut = 'CONF:LINK:INSTANT_MAC_CMD ' \
                            + cmdMacNum \
                            + ' REJOIN_SETUP' \
                            + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMacDut)
            return result
        elif cmdMacDut == 'ADR_SETUP':
            cmdSetMacDut = 'CONF:LINK:INSTANT_MAC_CMD ' \
                            + cmdMacNum \
                            + ' ADR_SETUP' \
                            + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMacDut)
            return result
        elif cmdMacDut == 'LINK_CHECK':
            cmdSetMacDut = 'CONF:LINK:INSTANT_MAC_CMD ' \
                            + cmdMacNum \
                            + ' LINK_CHECK' \
                            + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMacDut)
            return result
        elif cmdMacDut == 'DEVICE_TIME':
            cmdSetMacDut = 'CONF:LINK:INSTANT_MAC_CMD ' \
                            + cmdMacNum \
                            + ' DEVICE_TIME' \
                            + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMacDut)
            return result
        elif cmdMacDut == 'DEVICE_MODE':
            cmdSetMacDut = 'CONF:LINK:INSTANT_MAC_CMD ' \
                            + cmdMacNum \
                            + ' DEVICE_MODE' \
                            + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMacDut)
            return result
        elif cmdMacDut == 'RESET_IND':
            cmdSetMacDut = 'CONF:LINK:INSTANT_MAC_CMD ' \
                            + cmdMacNum \
                            + ' RESET_IND' \
                            + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMacDut)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getinstantmaccmd(self, macnum):
        '''
        Read the MAC Command to send to the DUT

        :param macnum: MAC Command Number

        :return: It returns the MAC Command mode; NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        cmdGetInstantMac = 'READ:LINK:INSTANT_MAC_CMD? ' + cmdMacNum + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetInstantMac)
        return result

    def link_setmic_errdisplay(self, errdispflag):
        '''
        Configure the flag whether to display erroneous messages in 
        link Analyzer

        :param errdispflag: OFF, ON

        :return: ACK on success, NAK on failure
        
        '''
        cmdMicErrDisplay = errdispflag
        if cmdMicErrDisplay == 'OFF':
            cmdSetMicErrDisplay = 'CONF:LINK:MIC_ERR_DISPLAY OFF' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMicErrDisplay)
            return result
        elif cmdMicErrDisplay == 'ON':
            cmdSetMicErrDisplay = 'CONF:LINK:MIC_ERR_DISPLAY ON' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMicErrDisplay)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getmic_errdisplay(self):
        '''
        Read the flag whether to display erroneous messages in 
        link Analyzer

        :param: Query only

        :return: It returns the flag status; NAK on failure
        
        '''
        cmdGetMicErrDisplay = 'READ:LINK:MIC_ERR_DISPLAY?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMicErrDisplay)
        return result

    def link_setadr_drval(self, macnum, drval):
        '''
        Configure DR value for LinkADRReq

        :param macnum: MAC Command Number
        :param drval: DR0_SF12BW125, DR1_SF11BW125, DR2_SF10BW125, 
                      DR3_SF9BW125, DR4_SF8BW125, DR5_SF7BW125, 
                      DR6_SF7BW250, DR7_FSK50

        :return: ACK on success, NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        cmdVersion = self.query_sysversion()
        numVersion = float(cmdVersion)
        lowVersionDrvallist = [0, 1, 2, 3, 4, 5, 6, 7]
        drvallist = [
            'DR0_SF12BW125', 
            'DR1_SF11BW125', 
            'DR2_SF10BW125', 
            'DR3_SF9BW125', 
            'DR4_SF8BW125', 
            'DR5_SF7BW125', 
            'DR6_SF7BW250', 
            'DR7_FSK50']
        
        if (cmdVersion == '1.150' 
                or cmdVersion == '1.160') and (int(drval) 
                    in lowVersionDrvallist):
            cmdDrVal = str(drval)
            cmdSetAdrDrVal = 'CONF:LINK:ADR_DR ' \
                                + cmdMacNum \
                                + ' ' \
                                + cmdDrVal \
                                + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetAdrDrVal)
            return result
        elif numVersion > 1.160 and drval in drvallist:
            cmdDrVal = str(drval)
            cmdSetAdrDrVal = 'CONF:LINK:ADR_DR ' \
                                + cmdMacNum \
                                + ' ' \
                                + cmdDrVal \
                                + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetAdrDrVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getadr_drval(self, macnum):
        '''
        Read DR value for LinkADRReq

        :param macnum: MAC Command Number

        :return: It returns the data rate value; NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        cmdGetAdrDrVal = 'READ:LINK:ADR_DR? ' + cmdMacNum + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetAdrDrVal)
        return result

    def link_setadr_txpower(self, macnum, txpowval):
        '''
        Configure TX power value for LinkADRReq

        :param macnum: MAC Command Number
        :param txpowval: 0 ~ 7

        :return: ACK on success, NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        if txpowval >= 0 and txpowval <= 7:
            cmdTxPowVal = str(txpowval)
            cmdSetTxPowVal = 'CONF:LINK:ADR_TXPOW ' \
                                + cmdMacNum \
                                + ' ' \
                                + cmdTxPowVal \
                                + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetTxPowVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getadr_txpower(self, macnum):
        '''
        Read TX power value for LinkADRReq

        :param macnum: MAC Command Number

        :return: it returns the TX power value; NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        cmdGetTxPowVal = 'READ:LINK:ADR_TXPOW? ' + cmdMacNum + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetTxPowVal)
        return result

    def link_setadr_channelmask(self, index, macnum, value):
        '''
        Configure CH_MASK value for LinkADRReq

        :param index: 1 - 3
        :param macnum: MAC Command Number
        :param value: 0x00 ~ 0xFF

        :return: ACK on success, NAK on failure
        
        '''
        cmdValue = int(value)
        cmdMacNum = str(macnum)
        cmdIndex = int(index)
        if cmdIndex == 1:
            if (cmdValue >= 0 and cmdValue <= 2**8 - 1):
                cmdHexValue = hex(cmdValue)
                cmdSetAdrChMask = 'CONF:LINK:ADR_CH_MASK ' \
                                    + cmdMacNum + ' ' \
                                    + cmdHexValue + '\n'
                result = RwcSerialSetup.transceive(self, cmdSetAdrChMask)
                return result
            else:
                raise Exception('Invalid parameter received.')
        elif (cmdIndex > 1 and cmdIndex <= 3):
            if (cmdValue >= 0 and cmdValue <= 2**8 - 1):
                cmdHexValue = hex(cmdValue)
                cmdSetAdrChMask = 'CONF:LINK:ADR_CH_MASK' \
                                    + str(cmdIndex) + ' ' \
                                    + cmdMacNum + ' ' \
                                    + cmdHexValue + '\n'
                result = RwcSerialSetup.transceive(self, cmdSetAdrChMask)
                return result
            else:
                raise Exception('Invalid parameter received.')
        else:
            raise Exception('Invalid parameter received.')

    def link_getadr_channelmask(self, index, macnum):
        '''
        Read CH_MASK value for LinkADRReq

        :param index: 1 - 3
        :param macnum: MAC Command Number

        :return: It returns channel mask value; NAK on failure
        
        '''
        cmdIndex = int(index)
        cmdMacNum = str(macnum)
        if cmdIndex == 1:
            cmdGetAdrChMask = 'READ:LINK:ADR_CH_MASK? ' + cmdMacNum + '\n'
            result = RwcSerialSetup.transceive(self, cmdGetAdrChMask)
            return result
        elif (cmdIndex > 1 and cmdIndex <= 3):
            cmdGetAdrChMask = 'READ:LINK:ADR_CH_MASK' \
            + str(cmdIndex) + '? '  + cmdMacNum + '\n'
            result = RwcSerialSetup.transceive(self, cmdGetAdrChMask)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_setadr_maskctrl(self, index, macnum, value):
        '''
        Configure MASK_CTRL value for LinkADRReq

        :param index: 1 - 3
        :param macnum: MAC Command Number
        :param value: 0x00 ~ 0xFF

        :return: ACK on success, NAK on failure
        
        '''
        cmdValue = int(value)
        cmdMacNum = str(macnum)
        cmdIndex = int(index)
        if cmdIndex == 1:
            if (cmdValue >= 0 and cmdValue <= 2**8 - 1):
                cmdHexValue = hex(cmdValue)
                cmdSetAdrMaskCtrl = 'CONF:LINK:ADR_MASK_CTRL ' \
                                        + cmdMacNum + ' ' \
                                        + cmdHexValue + '\n'
                result = RwcSerialSetup.transceive(self, cmdSetAdrMaskCtrl)
                return result
            else:
                raise Exception('Invalid parameter received.')
        elif (cmdIndex > 1 and cmdIndex <= 3):
            if (cmdValue >= 0 and cmdValue <= 2**8 - 1):
                cmdHexValue = hex(cmdValue)
                cmdSetAdrMaskCtrl = 'CONF:LINK:ADR_MASK' \
                                        + str(cmdIndex) + '_CTRL ' \
                                        + cmdMacNum + ' ' \
                                        + cmdHexValue + '\n'
                result = RwcSerialSetup.transceive(self, cmdSetAdrMaskCtrl)
                return result
            else:
                raise Exception('Invalid parameter received.')
        else:
            raise Exception('Invalid parameter received.')

    def link_getadr_maskctrl(self, index, macnum):
        '''
        Read MASK_CTRL value for LinkADRReq

        :param index: 1 - 3
        :param macnum: MAC Command Number

        :return: It returns mask control value; NAK on failure
        
        '''
        cmdIndex = int(index)
        cmdMacNum = str(macnum)
        if cmdIndex == 1:
            cmdGetAdrMaskCtrl = 'READ:LINK:ADR_MASK_CTRL? ' + cmdMacNum + '\n'
            result = RwcSerialSetup.transceive(self, cmdGetAdrMaskCtrl)
            return result
        elif (cmdIndex > 1 and cmdIndex <= 3):
            cmdGetAdrMaskCtrl = 'READ:LINK:ADR_MASK' \
                                    + str(cmdIndex) + '_CTRL? ' \
                                    + cmdMacNum + '\n'
            result = RwcSerialSetup.transceive(self, cmdGetAdrMaskCtrl)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_setadr_morechannelmask(self, chmaskval):
        '''
        Configure ADD_MORE_CH_MASK value for LinkADRReq for 
        CLAA mode only

        :param chmaskval: OFF, ON

        :return: ACK on success, NAK on failure
        
        '''
        cmdMoreChannelMask = chmaskval
        if cmdMoreChannelMask == 'OFF':
            cmdSetMoreChannelMask = 'CONF:LINK:ADR_MORE_CH_MASK OFF' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMoreChannelMask)
            return result
        elif cmdMoreChannelMask == 'ON':
            cmdSetMoreChannelMask = 'CONF:LINK:ADR_MORE_CH_MASK ON' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMoreChannelMask)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getadr_morechannelmask(self):
        '''
        Read ADD_MORE_CH_MASK value for LinkADRReq for CLAA mode only

        :param: Query only

        :return: It returns ADR_MORE_CH_MASK value; NAK on failure
        
        '''
        cmdGetMoreChannelMask = 'READ:LINK:ADR_MORE_CH_MASK?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMoreChannelMask)
        return result

    def link_setadrchmask_optdr(self, value):
        '''
        Configure CH_MASK value for optional DR for LinkADRReq

        :param value: 0x01 ~ 0x80

        :return: ACK on success, NAK on failure

        '''
        cmdValue = int(value)
        if (cmdValue >= 1 and cmdValue <= 2**7):
            cmdHexValue = hex(cmdValue)
            cmdSetAdrChMaskOptDr = 'CONF:LINK:ADR_CH_MASK_OPT_DR ' \
            + cmdHexValue \
            + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetAdrChMaskOptDr)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getadrchmask_optdr(self):
        '''
        Read CH_MASK value for optional DR for LinkADRReq

        :parameters: N/A (Query only)

        :return: It returns CH_MASK value; NAK on failure

        '''
        cmdGetAdrChMaskOptDr = 'READ:LINK:ADR_CH_MASK_OPT_DR?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetAdrChMaskOptDr)
        return result

    def link_setadr_nbtrans(self, macnum, nbtransval):
        '''
        Configure NbTrans value for LinkADRReq

        :param macnum: MAC Command Number
        :param nbtransval: 0 ~ 15

        :return: ACK on success, NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        if nbtransval >= 0 and nbtransval <= 15:
            cmdNbTransVal = str(nbtransval)
            cmdSetNbTransVal = 'CONF:LINK:ADR_NB_TRANS ' \
                                    + cmdMacNum + ' ' \
                                    + cmdNbTransVal + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetNbTransVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getadr_nbtrans(self, macnum):
        '''
        Read NbTrans value for LinkADRReq

        :param macnum: MAC Command Number

        :return: It returns nbtrans value; NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        cmdGetNbTransVal = 'READ:LINK:ADR_NB_TRANS? '  + cmdMacNum + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetNbTransVal)
        return result

    def link_setmaxdutycycle(self, macnum, dutycycleval):
        '''
        Configure the maximum duty cycle value for DutyCycleReq

        :param macnum: MAC Command Number
        :param dutycycleval: 0 ~ 15

        :return: ACK on success, NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        if dutycycleval >= 0 and dutycycleval <= 15:
            cmdMaxDutyCycleVal = str(dutycycleval)
            cmdSetMaxDutyCycleVal = 'CONF:LINK:MAX_DUTY_CYCLE ' \
                                        + cmdMacNum + ' ' \
                                        + cmdMaxDutyCycleVal + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMaxDutyCycleVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getmaxdutycycle(self, macnum):
        '''
        Read the maximum duty cycle value for DutyCycleReq

        :param macnum: MAC Command Number

        :return: It returns max DUT cycle value; NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        cmdGetMaxDutyCycleVal = 'READ:LINK:MAX_DUTY_CYCLE? ' \
        + cmdMacNum + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMaxDutyCycleVal)
        return result

    def link_setmaxeirp(self, macnum, value):
        '''
        Configure the maximum EIRP value in dBm for TXParamSetupReq

        :param macnum: MAC Command Number
        :param value: 8, 10, 12, 13, 14, 16, 18, 20, 21, 24, 26, 27, 29, 
                      30, 33, 36

        :return: ACK on success, NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        eirplist = [
            8, 10, 12, 13, 
            14, 16, 18, 20, 
            21, 24, 26, 27, 
            29, 30, 33, 36]
        cmdValue = int(value)

        if cmdValue in eirplist:
            cmdEirpValue = str(cmdValue)
            cmdSetMaxEirpVal = 'CONF:LINK:MAX_EIRP ' \
                                + cmdMacNum + ' ' \
                                + cmdEirpValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMaxEirpVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getmaxeirp(self, macnum):
        '''
        Read the maximum EIRP value in dBm for TXParamSetupReq

        :param macnum: MAC Command Number

        :return: It returns max EIRP value; NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        cmdGetMaxEirpVal = 'READ:LINK:MAX_EIRP? ' + cmdMacNum + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMaxEirpVal)
        return result

    def link_setuplinkdwelltime(self, macnum, dwelltimeval):
        '''
        Configure the uplink dwell time value in dBm for TXParamSetupReq

        :param macnum: MAC Command Number
        :param dwelltimeval: NO_LIMIT, 400ms

        :return: ACK on success, NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        cmdUlDwellTimeVal = dwelltimeval
        if cmdUlDwellTimeVal == 'NO_LIMIT':
            cmdSetUlDwellTimeVal = 'CONF:LINK:UL_DWELL_TIME ' \
                                    + cmdMacNum \
                                    + ' NO_LIMIT' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetUlDwellTimeVal)
            return result
        elif cmdUlDwellTimeVal == '400ms':
            cmdSetUlDwellTimeVal = 'CONF:LINK:UL_DWELL_TIME ' \
                                    + cmdMacNum \
                                    + ' 400ms' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetUlDwellTimeVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getuplinkdwelltime(self, macnum):
        '''
        Read the uplink dwell time value in dBm for TXParamSetupReq

        :param macnum: MAC Command Number

        :return: -
        
        '''
        cmdMacNum = str(macnum)
        cmdGetUlDwellTimeVal = 'READ:LINK:UL_DWELL_TIME? ' + cmdMacNum + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetUlDwellTimeVal)
        return result

    def link_setdownlinkdwelltime(self, macnum, dwelltimeval):
        '''
        Configure the downlink dwell value in dBm for TXParamSetupReq

        :param macnum: MAC Command Number
        :param dwelltimeval: NO_LIMIT, 400ms

        :return: ACK on success, NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        cmdDlDwellTimeVal = dwelltimeval
        if cmdDlDwellTimeVal == 'NO_LIMIT':
            cmdSetDlDwellTimeVal = 'CONF:LINK:DL_DWELL_TIME ' \
                                    + cmdMacNum \
                                    + ' NO_LIMIT' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetDlDwellTimeVal)
            return result
        elif cmdDlDwellTimeVal == '400ms':
            cmdSetDlDwellTimeVal = 'CONF:LINK:DL_DWELL_TIME ' \
                                    + cmdMacNum \
                                    + ' 400ms' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetDlDwellTimeVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getdownlinkdwelltime(self, macnum):
        '''
        Read the downlink dwell value in dBm for TXParamSetupReq

        :param macnum: MAC Command Number

        :return: -
        
        '''
        cmdMacNum = str(macnum)
        cmdGetDlDwellTimeVal = 'READ:LINK:DL_DWELL_TIME? ' + cmdMacNum + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetDlDwellTimeVal)
        return result

    def link_setnewchannelmode(self, macnum, mode):
        '''
        Configure the mode for NewChannelReq

        :param macnum: MAC Command Number
        :param mode: CREATE, DELETE

        :return: ACK on success, NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        cmdNewChMode = mode
        if cmdNewChMode == 'CREATE':
            cmdSetNewChMode = 'CONF:LINK:NEW_CH_MODE ' \
                                + cmdMacNum \
                                + ' CREATE' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetNewChMode)
            return result
        elif cmdNewChMode == 'DELETE':
            cmdSetNewChMode = 'CONF:LINK:NEW_CH_MODE ' \
                                + cmdMacNum \
                                + ' DELETE' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetNewChMode)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getnewchannelmode(self, macnum):
        '''
        Read the mode for NewChannelReq

        :param macnum: MAC Command Number

        :return: It returns the channel mode; NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        cmdGetNewChMode = 'READ:LINK:NEW_CH_MODE? ' + cmdMacNum + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetNewChMode)
        return result

    def link_setnewchannelindex(self, chindex, macnum):
        '''
        Configure the channel index for NewChannelReq

        :param chindex: 0 ~ 7
        :param macnum: MAC Command Number

        :return: ACK on success, NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        if chindex >= 0 and chindex <= 7:
            cmdNewChannelIndex = str(chindex)
            cmdSetNewChannelIndexVal = 'CONF:LINK:NEW_CH_INDEX ' \
                                        + cmdMacNum + ' ' \
                                        + cmdNewChannelIndex + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetNewChannelIndexVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getnewchannelindex(self, macnum):
        '''
        Read the channel index for NewChannelReq

        :param macnum: MAC Command Number

        :return: It returns the channel index; NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        cmdGetNewChannelIndexVal = 'READ:LINK:NEW_CH_INDEX? ' \
                                    + cmdMacNum + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetNewChannelIndexVal)
        return result

    def link_setnewchannel_maxdr(self, macnum, drval):
        '''
        Configure the maximum DR for NewChannelReq

        :param macnum: MAC Command Number
        :param drval: 0 ~ 7

        :return: ACK on success, NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        if drval >= 0 and drval <= 7:
            cmdNewChannelMaxDr = str(drval)
            cmdSetNewChannelMaxDrVal = 'CONF:LINK:NEW_CH_MAX_DR ' \
                                        + cmdMacNum + ' ' \
                                        + cmdNewChannelMaxDr + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetNewChannelMaxDrVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getnewchannel_maxdr(self, macnum):
        '''
        Read the maximum DR for NewChannelReq

        :param macnum: MAC Command Number

        :return: It returns the maximum data rate; NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        cmdGetNewChannelMaxDrVal = 'READ:LINK:NEW_CH_MAX_DR? ' \
                                    + cmdMacNum + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetNewChannelMaxDrVal)
        return result

    def link_setnewchannel_mindr(self, macnum, drval):
        '''
        Configure the minimum DR for NewChannelReq

        :param macnum: MAC Command Number
        :param drval: 0 ~ 7

        :return: ACK on success, NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        if drval >= 0 and drval <= 7:
            cmdNewChannelMinDr = str(drval)
            cmdSetNewChannelMinDrVal = 'CONF:LINK:NEW_CH_MIN_DR ' \
                                        + cmdMacNum + ' ' \
                                        + cmdNewChannelMinDr + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetNewChannelMinDrVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getnewchannel_mindr(self, macnum):
        '''
        Read the minimum DR for NewChannelReq

        :param macnum: MAC Command Number

        :return: It returns the minimum data rate; NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        cmdGetNewChannelMinDrVal = 'READ:LINK:NEW_CH_MIN_DR? ' \
                                    + cmdMacNum + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetNewChannelMinDrVal)
        return result

    def link_setnumofmaccmd(self, num):
        '''
        Configure the number of MAC commands to be sent in a single frame

        :param num: 1 ~ 3

        :return: ACK on success, NAK on failure
        
        '''
        if num >= 1 and num <= 3:
            cmdNum = str(num)
            cmdSetNum = 'CONF:LINK:NUM_OF_CMD ' + cmdNum + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetNum)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getnumofmaccmd(self):
        '''
        Read the number of MAC commands to be sent in a single frame

        :param: Query only

        :return: It returns the number of mac commands; NAK on failure
        
        '''
        cmdGetNum = 'READ:LINK:NUM_OF_CMD?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetNum)
        return result
    
    def link_setdlchannelindex(self, macnum, chindex):
        '''
        Configure the channel index for DIChannelReq

        :param macnum: MAC Command Number
        :param chindex: 0 ~ 7

        :return: ACK on success, NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        if chindex >= 0 and chindex <= 7:
            cmdDlChannelIndex = str(chindex)
            cmdSetDlChannelIndexVal = 'CONF:LINK:DL_CH_INDEX ' \
                                        + cmdMacNum + ' ' \
                                        + cmdDlChannelIndex + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetDlChannelIndexVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getdlchannelindex(self, macnum):
        '''
        Read the channel index for DIChannelReq

        :param macnum: MAC Command Number

        :return: It returns the channel index; NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        cmdGetChannelIndex = 'READ:LINK:DL_CH_INDEX? ' + cmdMacNum + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetChannelIndex)
        return result

    def link_setdlchannelfrequency(self, macnum, chfreq):
        '''
        Configure the channel frequency for DIChannelReq

        :param macnum: MAC Command Number
        :param chfreq: 400 ~ 510, 862 ~ 960 MHz

        :return: ACK on success, NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        if (chfreq >= 400 
                and chfreq <= 510) or (chfreq >= 862 
                    and chfreq <= 960):
            cmdDlChannelFrequency = str(chfreq)
            cmdSetDlChannelFrequencyVal = 'CONF:LINK:DL_CH_FREQ ' \
                                            + cmdMacNum + ' ' \
                                            + cmdDlChannelFrequency + '\n'
            result = RwcSerialSetup.transceive(
                self, 
                cmdSetDlChannelFrequencyVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getdlchannelfrequency(self, macnum):
        '''
        Read the channel frequency for DIChannelReq

        :param macnum: MAC Command Number

        :return: It returns the channel frequency; NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        cmdGetChannelFrequency = 'READ:LINK:DL_CH_FREQ? ' + cmdMacNum + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetChannelFrequency)
        return result

    def link_setpayloadtype(self, payloadtype):
        '''
        Configure the message type of user-defined MAC command
        (Supported version: v1.15)

        :param payloadtype: 0000_0000, 1111_1111, 1111_0000, 
                            1010_1010, PRBS, USER

        :return: ACK on success, NAK on failure

        '''
        payloadTypeList = [
            '0000_0000', '1111_1111', 
            '1111_0000', '1010_1010', 
            'PRBS', 'USER']
        cmdSupportedVersion = ['1.150']
        verStatus = self.validate_sys_swversion(cmdSupportedVersion)

        if verStatus and payloadtype in payloadTypeList:
            cmdSetPayloadType = 'CONF:LINK:PAYLOAD_TYPE ' + payloadtype + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPayloadType)
            return result
        else:
            raise Exception('Invalid link payload type parameter received')

    def link_getpayloadtype(self):
        '''
        Read the message type of user-defined MAC command
        (Supported version: v1.15)

        :param: Query only

        :return: It returns link payload type; NAK on failure

        '''
        cmdSupportedVersion = ['1.150']
        verStatus = self.validate_sys_swversion(cmdSupportedVersion)
        if verStatus:
            cmdGetPayloadType = 'READ:LINK:PAYLOAD_TYPE?' + '\n'
            result = RwcSerialSetup.transceive(self, cmdGetPayloadType)
            return result

    def link_setfport(self, fport):
        '''
        Configure the FPORT of user-defined MAC command

        :param fport: 1 ~ 255

        :return: ACK on success, NAK on failure
        
        '''
        if fport >= 1 and fport <= 255:
            cmdFport = str(fport)
            cmdSetFport = 'CONF:LINK:FPORT ' + cmdFport + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetFport)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getfport(self):
        '''
        Read the FPORT of user-defined MAC command

        :param: Query only

        :return: It returns the fport value; NAK on failure
        
        '''
        cmdGetFport = 'READ:LINK:FPORT?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetFport)
        return result

    def link_setpayloadsize(self, length):
        '''
        Configure the Message length in byte of user-defined 
        MAC command

        :param length: 1 ~ 128

        :return: ACK on success, NAK on failure
        
        '''
        if length >= 1 and length <= 128:
            cmdMsgLength = str(length)
            cmdSetMsgLength = 'CONF:LINK:PAYLOAD_SIZE ' + cmdMsgLength + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMsgLength)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getpayloadsize(self):
        '''
        Read the Message length in byte of user-defined MAC command

        :param: Query only

        :return: It returns the payload size; NAK on failure
        
        '''
        cmdGetMsgLength = 'READ:LINK:PAYLOAD_SIZE?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMsgLength)
        return result

    def link_setpayload(self, value):
        '''
        Configure the Message data of user-defined MAC command

        :param value: 250-byte HEX value

        :return: ACK on success, NAK on failure
        
        '''
        cmdValue = int(value)
        if (cmdValue >= 0 and cmdValue <= 2**250 -1) :
            cmdHexValue = hex(cmdValue)
            cmdSetPayload = 'CONF:LINK:PAYLOAD ' + cmdHexValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPayload)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getpayload(self):
        '''
        Read the Message data of user-defined MAC command

        :param: Query only

        :return: It returns the payload data; NAK on failure
        
        '''
        cmdGetMsgData = 'READ:LINK:PAYLOAD?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMsgData)
        return result

    def link_setfoptssize(self, length):
        '''
        Configure the Message length in byte of user-defined 
        FOpts field

        :param length: 1 ~ 15

        :return: ACK on success, NAK on failure
        
        '''
        if length >= 1 and length <= 15:
            cmdMsgLength = str(length)
            cmdSetMsgLength = 'CONF:LINK:FOPTS_SIZE ' + cmdMsgLength + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMsgLength)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getfoptssize(self):
        '''
        Read the Message length in byte of user-defined FOpts field

        :param: Query only

        :return: It returns the FOpts size; NAK on failure
        
        '''
        cmdGetMsgLength = 'READ:LINK:FOPTS_SIZE?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMsgLength)
        return result

    def link_setfopts(self, value):
        '''
        Configure the Message data of user-defined FOpts field

        :param value: 15-byte HEX value

        :return: ACK on success, NAK on failure
        
        '''
        cmdValue = int(value)
        if (cmdValue >= 0 and cmdValue <= 2**15 -1) :
            cmdHexValue = hex(cmdValue)
            cmdSetFOpts = 'CONF:LINK:FOPTS ' + cmdHexValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetFOpts)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getfopts(self):
        '''
        Read the Message data of user-defined FOpts field

        :param: Query only

        :return: It returns the FOpts data; NAK on failure
        
        '''
        cmdGetMsgData = 'READ:LINK:FOPTS?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMsgData)
        return result

    def link_setbeaconfrequency(self, *args):
        '''
        Configure the frequency value of Beacon frame

        :param *args: For version below 1.17
                      only frequency required (0, 862 ~ 960 MHz)

                      For version 1.17 and above:
                      first parameter should be a MAC command number,
                      second parameter should be frequency 
                      (0, 862 ~ 960 MHz)

        :return: ACK on success, NAK on failure
        
        '''
        if len(args) == 1 and (args[0] == 0 
                or (args[0] >= 862 and args[0] <= 960)):
            cmdFreq = str(args[0])
            cmdSetBeaconFrequencyVal = 'CONF:LINK:BEACON_FREQ ' \
                                        + cmdFreq + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetBeaconFrequencyVal)
            return result
        elif len(args) == 2 and (args[1] >= 400 
                and args[1] <= 510) or (args[1] >= 862 and args[1] <= 960):
            cmdMacNum = str(args[0])
            cmdBeaconFrequency = str(args[1])
            cmdSetBeaconFrequencyVal = 'CONF:LINK:BEACON_FREQ ' \
                                        + cmdMacNum + ' ' \
                                        + cmdBeaconFrequency + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetBeaconFrequencyVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getbeaconfrequency(self, *args):
        '''
        Read the frequency value of Beacon frame

        :param *args: MAC Command Number required if version 1.17 and 
                      above otherwise parameter not required

        :return: It returns the frequency value; NAK on failure
        
        '''
        if len(args) == 0:
            cmdGetBeaconFrequency = 'READ:LINK:BEACON_FREQ?' + '\n'
            result = RwcSerialSetup.transceive(self, cmdGetBeaconFrequency)
            return result
        elif len(args) == 1:
            cmdMacNum = str(args[0])
            cmdGetBeaconFrequency = 'READ:LINK:BEACON_FREQ? ' \
                                        + cmdMacNum + '\n'
            result = RwcSerialSetup.transceive(self, cmdGetBeaconFrequency)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_setbeacondatarate(self, framedr):
        '''
        Configure the data rate of Beacon frame 
        (RWC supported version: v1.15 and v1.16)

        :param framedr: DR_0 ~ DR_6

        :return: ACK on success, NAK on failure
        
        '''
        cmdSupportedVersion = ['1.150', '1.160']
        frameDrList = [
            'DR_0', 'DR_1', 
            'DR_2', 'DR_3', 
            'DR_4', 'DR_5', 
            'DR_6']
        verStatus = self.validate_sys_swversion(cmdSupportedVersion)

        if verStatus and framedr in frameDrList:
            cmdSetFrameDr = 'CONF:LINK:BEACON_DR ' + framedr + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetFrameDr)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getbeacondatarate(self):
        '''
        Read the data rate of Beacon frame 
        (RWC supported version: v1.15 and v1.16)

        :param: Query only

        :return: It returns the data rate; NAK on failure

        '''
        cmdSupportedVersion = ['1.150', '1.160']
        verStatus = self.validate_sys_swversion(cmdSupportedVersion)

        if verStatus:
            cmdGetBeaconDr = 'READ:LINK:BEACON_DR?' + '\n'
            result = RwcSerialSetup.transceive(self, cmdGetBeaconDr)
            return result

    def link_setpingdatarate(self, *args):
        '''
        Configure the index of the Data Rate used for ping-slot 
        downlinks for PingSlotChannelReq (above v1.160)

        :param *args: For version below 1.17
                      only datarate required

                      For version 1.17 and above:
                      first parameter should be a MAC command number,
                      second parameter should be datarate

                      (DR0_SF12BW125, DR1_SF11BW125, 
                       DR2_SF10BW125, DR3_SF9BW125, 
                       DR4_SF8BW125, DR5_SF7BW125, 
                       DR6_SF7BW250, DR7_FSK50)

        :return: ACK on success, NAK on failure
        
        '''
        drList = [
            'DR0_SF12BW125', 'DR1_SF11BW125', 
            'DR2_SF10BW125', 'DR3_SF9BW125', 
            'DR4_SF8BW125', 'DR5_SF7BW125', 
            'DR6_SF7BW250', 'DR7_FSK50']

        if len(args) == 1 and args[0] in drList:
            cmdDr = str(args[0])
            cmdSetPingDr = 'CONF:LINK:PING_DR ' \
                            + cmdDr + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPingDr)
            return result
        elif len(args) == 2 and args[1] in drList:
            cmdMacNum = str(args[0])
            cmdDr = str(args[1])
            cmdSetPingDr = 'CONF:LINK:PING_DR ' \
                            + cmdMacNum + ' ' \
                            + cmdDr + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPingDr)
            return result
        else:
            raise Exception('Invalid parameter received.')
    
    def link_getpingdatarate(self, *args):
        '''
        Read the index of the Data Rate used for ping-slot downlinks 
        for PingSlotChannelReq (above v1.160)

        :param *args: MAC Command Number required if version is 1.17 
                      and above otherwise parameter not required

        :return: It returns the data rate; NAK on failure
        
        '''
        if len(args) == 0:
            cmdGetPingDr = 'READ:LINK:PING_DR?' + '\n'
            result = RwcSerialSetup.transceive(self, cmdGetPingDr)
            return result
        elif len(args) == 1:
            cmdMacNum = str(args[0])
            cmdGetPingDr = 'READ:LINK:PING_DR? ' + cmdMacNum + '\n'
            result = RwcSerialSetup.transceive(self, cmdGetPingDr)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_setpingfrequency(self, *args):
        '''
        Configure the frequency used for ping-slot downlinks 
        for PingSlotChannelReq

        :param *args: For version below 1.17
                      only frequency required 
                      (400 ~ 510, 862 ~ 960 MHz)

                      For version 1.17 and above:
                      first parameter should be a MAC command number,
                      second parameter should be frequency 
                      (400 ~ 510, 862 ~ 960 MHz)

        :return: ACK on success, NAK on failure
        
        '''
        if len(args) == 1 and (args[0] == 0 
                or (args[0] >= 862 and args[0] <= 960)):
            cmdFreq = str(args[0])
            cmdSetPingFrequencyVal = 'CONF:LINK:PING_FREQ ' \
                                        + cmdFreq + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPingFrequencyVal)
            return result
        elif len(args) == 2 and (args[1] >= 400 
                and args[1] <= 510) or (args[1] >= 862 
                    and args[1] <= 960):
            cmdMacNum = str(args[0])
            cmdPingFrequency = str(args[1])
            cmdSetPingFrequencyVal = 'CONF:LINK:PING_FREQ ' \
                                        + cmdMacNum + ' ' \
                                        + cmdPingFrequency + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPingFrequencyVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getpingfrequency(self, *args):
        '''
        Read the frequency used for ping-slot downlinks 
        for PingSlotChannelReq

        :param *args: MAC Command Number required if version is 1.17 
                      and above otherwise parameter not required

        :return: It returns the frequency value; NAK on failure
        
        '''
        if len(args) == 0:
            cmdGetPingFreq = 'READ:LINK:PING_FREQ?' + '\n'
            result = RwcSerialSetup.transceive(self, cmdGetPingFreq)
            return result
        elif len(args) == 1:
            cmdMacNum = str(args[0])
            cmdGetPingFreq = 'READ:LINK:PING_FREQ? ' + cmdMacNum + '\n'
            result = RwcSerialSetup.transceive(self, cmdGetPingFreq)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_setrx2datarate(self, macnum, datarate):
        '''
        Configure the Data Rate used for RX2 channel

        :param macnum: MAC Command Number
        :param datarate: DR0_SF12BW125, DR1_SF11BW125, 
                         DR2_SF10BW125, DR3_SF9BW125, 
                         DR4_SF8BW125, DR5_SF7BW125, 
                         DR6_SF7BW250, DR7_FSK50

        :return: ACK on success, NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        cmdRx2Dr = datarate
        if cmdRx2Dr == 'DR0_SF12BW125':
            cmdSetRx2Dr = 'CONF:LINK:RX2_DR ' \
                            + cmdMacNum + ' DR0_SF12BW125' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRx2Dr)
            return result
        elif cmdRx2Dr == 'DR1_SF11BW125':
            cmdSetRx2Dr = 'CONF:LINK:RX2_DR ' \
                            + cmdMacNum + ' DR1_SF11BW125' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRx2Dr)
            return result
        elif cmdRx2Dr == 'DR2_SF10BW125':
            cmdSetRx2Dr = 'CONF:LINK:RX2_DR ' \
                            + cmdMacNum + ' DR2_SF10BW125' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRx2Dr)
            return result
        elif cmdRx2Dr == 'DR3_SF9BW125':
            cmdSetRx2Dr = 'CONF:LINK:RX2_DR ' \
                            + cmdMacNum + ' DR3_SF9BW125' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRx2Dr)
            return result
        elif cmdRx2Dr == 'DR4_SF8BW125':
            cmdSetRx2Dr = 'CONF:LINK:RX2_DR ' \
                            + cmdMacNum + ' DR4_SF8BW125' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRx2Dr)
            return result
        elif cmdRx2Dr == 'DR5_SF7BW125':
            cmdSetRx2Dr = 'CONF:LINK:RX2_DR ' \
                            + cmdMacNum + ' DR5_SF7BW125' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRx2Dr)
            return result
        elif cmdRx2Dr == 'DR6_SF7BW250':
            cmdSetRx2Dr = 'CONF:LINK:RX2_DR ' \
                            + cmdMacNum + ' DR6_SF7BW250' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRx2Dr)
            return result
        elif cmdRx2Dr == 'DR7_FSK50':
            cmdSetRx2Dr = 'CONF:LINK:RX2_DR ' \
                            + cmdMacNum + ' DR7_FSK50' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRx2Dr)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getrx2datarate(self, macnum):
        '''
        Read the Data Rate used for the RX2 channel

        :param macnum: MAC Command Number

        :return: It returns the data rate value; NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        cmdGetRx2Dr = 'READ:LINK:RX2_DR? ' + cmdMacNum + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetRx2Dr)
        return result

    def link_setrx2frequency(self, macnum, freq):
        '''
        Configure the frequency used for RX2 channel

        :param freq: 400 ~ 510, 862 ~ 960 MHz

        :return: ACK on success, NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        if (freq >= 400 
                and freq <= 510) or (freq >= 862 
                    and freq <= 960):
            cmdRx2Frequency = str(freq)
            cmdSetRx2FrequencyVal = 'CONF:LINK:RX2_FREQ ' \
                                        + cmdMacNum + ' ' \
                                        + cmdRx2Frequency + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRx2FrequencyVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getrx2frequency(self, macnum):
        '''
        Read the frequency used for RX2 channel

        :param macnum: MAC Command Number

        :return: It returns the RX2 channel frequency value; 
                 NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        cmdGetRx2Freq = 'READ:LINK:RX2_FREQ? ' + cmdMacNum + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetRx2Freq)
        return result

    def link_setreceivedelay(self, macnum, value):
        '''
        Configure the receive delay

        :param value: 1 ~ 10

        :return: ACK on success, NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        if (value >= 1 and value <= 10):
            cmdDelayValue = str(value)
            cmdSetReceiveDelayVal = 'CONF:LINK:RECEIVE_DELAY ' \
                                        + cmdMacNum + ' ' \
                                        + cmdDelayValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetReceiveDelayVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getreceivedelay(self, macnum):
        '''
        Read the receive delay

        :param macnum: MAC Command Number

        :return: It returns link receive delay value; NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        cmdGetReceiveDelayValue = 'READ:LINK:RECEIVE_DELAY? ' \
                                    + cmdMacNum + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetReceiveDelayValue)
        return result

    def link_setrx1droffset(self, macnum, value):
        '''
        Configure the RX1 DR Offset

        :param value: 0 ~ 7

        :return: ACK on success, NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        if (value >= 0 and value <= 7):
            cmdOffsetValue = str(value)
            cmdSetRx1DrOffsetVal = 'CONF:LINK:RX1_DR_OFFSET ' \
                                    + cmdMacNum + ' ' \
                                    + cmdOffsetValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRx1DrOffsetVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getrx1droffset(self, macnum):
        '''
        Read the RX1 DR Offset

        :param macnum: MAC Command Number

        :return: It returns RX1 DR Offset value; NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        cmdGetRx1DrOffsetValue = 'READ:LINK:RX1_DR_OFFSET? ' \
                                    + cmdMacNum + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetRx1DrOffsetValue)
        return result

    def link_setrejoindatarate(self, macnum, datarate):
        '''
        Configure the Data Rate value for ForceRejoinReq

        :param macnum: MAC Command Number
        :param datarate: DR0_SF12BW125, DR1_SF11BW125, 
                         DR2_SF10BW125, DR3_SF9BW125, 
                         DR4_SF8BW125, DR5_SF7BW125, 
                         DR6_SF7BW250, DR7_FSK50

        :return: ACK on success, NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        lowVersionDrList = [
            'DR_0', 'DR_1', 
            'DR_2', 'DR_3', 
            'DR_4', 'DR_5', 
            'DR_6']
        drList = [
            'DR0_SF12BW125', 'DR1_SF11BW125', 
            'DR2_SF10BW125', 'DR3_SF9BW125', 
            'DR4_SF8BW125', 'DR5_SF7BW125', 
            'DR6_SF7BW250', 'DR7_FSK50']
        cmdVersion = self.query_sysversion()
        numVersion = float(cmdVersion)
        
        if numVersion < 1.170 and datarate in lowVersionDrList:
            cmdSetRejoinDr = 'CONF:LINK:REJOIN_DR ' \
                                + cmdMacNum + ' ' \
                                + datarate + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRejoinDr)
            return result
        elif numVersion > 1.160 and datarate in drList:
            cmdSetRejoinDr = 'CONF:LINK:REJOIN_DR ' \
                                + cmdMacNum + ' ' \
                                + datarate + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRejoinDr)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getrejoindatarate(self, macnum):
        '''
        Read the Data Rate value for ForceRejoinReq

        :param macnum: MAC Command Number

        :return: It returns the data rate value; NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        cmdGetRejoinDr = 'READ:LINK:REJOIN_DR? ' + cmdMacNum + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetRejoinDr)
        return result
    
    def link_setrejointype(self, macnum, rejointype):
        '''
        Configure the RejoinType value for ForceRejoinReq

        :param macnum: MAC Command Number
        :param rejointype: TYPE_0, TYPE_2

        :return: ACK on success, NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        cmdRejoinType = rejointype
        if cmdRejoinType == 'TYPE_0':
            cmdSetRejoinType = 'CONF:LINK:REJOIN_TYPE ' \
                                + cmdMacNum + ' TYPE_0' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRejoinType)
            return result
        elif cmdRejoinType == 'TYPE_2':
            cmdSetRejoinType = 'CONF:LINK:REJOIN_TYPE ' \
                                + cmdMacNum + ' TYPE_2' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRejoinType)
            return result
        else:
            raise Exception('Invalid parameter received.')
    
    def link_getrejointype(self, macnum):
        '''
        Read the RejoinType value for ForceRejoinReq

        :param macnum: MAC Command Number

        :return: It returns the RejoinType value; NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        cmdGetRejoinType = 'READ:LINK:REJOIN_TYPE? ' + cmdMacNum + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetRejoinType)
        return result
    
    def link_setrejoinretry(self, macnum, retryval):
        '''
        Configure the Max_Retries value for ForceRejoinReq

        :param macnum: MAC Command Number
        :param retryval: 0 ~ 7

        :return: ACK on success, NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        if retryval >= 0 and retryval <= 7:
            cmdRejoinRetryVal = str(retryval)
            cmdSetRejoinRetryVal = 'CONF:LINK:REJOIN_RETRY ' \
                                    + cmdMacNum + ' ' \
                                    + cmdRejoinRetryVal + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRejoinRetryVal)
            return result
        else:
            raise Exception('Invalid parameter received.')
    
    def link_getrejoinretry(self, macnum):
        '''
        Read the Max_Retries value for ForceRejoinReq

        :param macnum: MAC Command Number

        :return: It returns rejoin entry value; NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        cmdGetRejoinRetryVal = 'READ:LINK:REJOIN_RETRY? ' + cmdMacNum + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetRejoinRetryVal)
        return result
    
    def link_setrejoinperiod(self, macnum, period):
        '''
        Configure the Period value for ForceRejoinReq

        :param macnum: MAC Command Number
        :param period: 0 ~ 7

        :return: ACK on success, NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        if period >= 0 and period <= 7:
            cmdRejoinPeriodVal = str(period)
            cmdSetRejoinPeriodVal = 'CONF:LINK:REJOIN_PERIOD ' \
                                        + cmdMacNum + ' ' \
                                        + cmdRejoinPeriodVal + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRejoinPeriodVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getrejoinperiod(self, macnum):
        '''
        Read the Period value for ForceRejoinReq

        :param macnum: MAC Command Number

        :return: It returns rejoin period value; NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        cmdGetRejoinPeriodVal = 'READ:LINK:REJOIN_PERIOD? ' + cmdMacNum + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetRejoinPeriodVal)
        return result

    def link_setrejoinmaxtime(self, macnum, maxtimeval):
        '''
        Configure the MaxTimeN value for RejoinParamSetupReq

        :param macnum: MAC Command Number
        :param maxtimeval: 0 ~ 15

        :return: ACK on success, NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        if maxtimeval >= 0 and maxtimeval <= 15:
            cmdRejoinMaxTimeVal = str(maxtimeval)
            cmdSetRejoinMaxTimeVal = 'CONF:LINK:REJOIN_MAX_TIME_N ' \
                                        + cmdMacNum + ' ' \
                                        + cmdRejoinMaxTimeVal + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRejoinMaxTimeVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getrejoinmaxtime(self, macnum):
        '''
        Read the MaxTimeN value for RejoinParamSetupReq

        :param macnum: MAC Command Number

        :return: It returns rejoin max time value; NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        cmdGetRejoinMaxTimeVal = 'READ:LINK:REJOIN_MAX_TIME_N? ' \
                                    + cmdMacNum + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetRejoinMaxTimeVal)
        return result

    def link_setrejoinmaxcnt(self, macnum, maxcnt):
        '''
        Configure the MaxCountN value for RejoinParamSetupReq

        :param macnum: MAC Command Number
        :param maxcnt: 0 ~ 15

        :return: ACK on success, NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        if maxcnt >= 0 and maxcnt <= 15:
            cmdRejoinMaxCntVal = str(maxcnt)
            cmdSetRejoinMaxCntVal = 'CONF:LINK:REJOIN_MAX_CNT_N ' \
                                        + cmdMacNum + ' ' \
                                        + cmdRejoinMaxCntVal + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRejoinMaxCntVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getrejoinmaxcnt(self, macnum):
        '''
        Read the MaxCountN value for RejoinParamSetupReq

        :param macnum: MAC Command Number

        :return: It returns rejoin max count value; NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        cmdGetRejoinMaxCntVal = 'READ:LINK:REJOIN_MAX_CNT_N? ' \
                                    + cmdMacNum + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetRejoinMaxCntVal)
        return result

    def link_setadrlimitexp(self, macnum, limit):
        '''
        Configure the Limit_exp value for ADRParamSetupReq 
        (ADR_ACK_LIMIT=2^Limit_exp)

        :param macnum: MAC Command Number
        :param limit: 0 ~ 15

        :return: ACK on success, NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        if limit >= 0 and limit <= 15:
            cmdAdrLimitExpVal = str(limit)
            cmdSetAdrLimitExpVal = 'CONF:LINK:ADR_LIMIT_EXP ' \
                                    + cmdMacNum + ' ' \
                                    + cmdAdrLimitExpVal + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetAdrLimitExpVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getadrlimitexp(self, macnum):
        '''
        Read the Limit_exp value for ADRParamSetupReq 
        (ADR_ACK_LIMIT=2^Limit_exp)

        :param macnum: MAC Command Number

        :return: It returns the Limit_exp value; NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        cmdGetAdrLimitExpVal = 'READ:LINK:ADR_LIMIT_EXP? ' + cmdMacNum + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetAdrLimitExpVal)
        return result

    def link_setadrdelayexp(self, macnum, delay):
        '''
        Configure the Delay_exp value for ADRParamSetupReq 
        (ADR_ACK_DELAY=2^Delay_exp)

        :param macnum: MAC Command Number
        :param delay: 0 ~ 15

        :return: ACK on success, NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        if delay >= 0 and delay <= 15:
            cmdAdrDelayExpVal = str(delay)
            cmdSetAdrDelayExpVal = 'CONF:LINK:ADR_DELAY_EXP ' \
                                    + cmdMacNum + ' ' \
                                    + cmdAdrDelayExpVal + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetAdrDelayExpVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getadrdelayexp(self, macnum):
        '''
        Read the Delay_exp value for ADRParamSetupReq 
        (ADR_ACK_DELAY=2^Delay_exp)

        :param macnum: MAC Command Number

        :return: It returns the delay_exp value; NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        cmdGetAdrDelayExpVal = 'READ:LINK:ADR_DELAY_EXP? ' + cmdMacNum + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetAdrDelayExpVal)
        return result

    def link_settimedisplay(self, flag):
        '''
        Configure the flag whether to display Time parameter in 
        Link Analyzer screen

        :param flag: OFF, ON

        :return: ACK on success, NAK on failure
        
        '''
        cmdTimeDisplay = flag
        if cmdTimeDisplay == 'OFF':
            cmdSetTimeDisplay = 'CONF:LINK:TIME_DISPLAY OFF' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetTimeDisplay)
            return result
        elif cmdTimeDisplay == 'ON':
            cmdSetTimeDisplay = 'CONF:LINK:TIME_DISPLAY ON' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetTimeDisplay)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_gettimedisplay(self):
        '''
        Read the flag whether to display Time parameter in Link 
        Analyzer screen

        :param: Query only

        :return: It returns the flag status; NAK on failure
        
        '''
        cmdGetTimeDisplay = 'READ:LINK:TIME_DISPLAY?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetTimeDisplay)
        return result

    def link_setfcntdisplay(self, flag):
        '''
        Configure the flag whether to display FCnt field in Link 
        Analyzer screen

        :param flag: OFF, ON

        :return: ACK on success, NAK on failure
        
        '''
        cmdFcntDisplay = flag
        if cmdFcntDisplay == 'OFF':
            cmdSetFcntDisplay = 'CONF:LINK:FCNT_DISPLAY OFF' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetFcntDisplay)
            return result
        elif cmdFcntDisplay == 'ON':
            cmdSetFcntDisplay = 'CONF:LINK:FCNT_DISPLAY ON' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetFcntDisplay)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getfcntdisplay(self):
        '''
        Read the flag whether to display FCnt field in Link 
        Analyzer screen

        :param: Query only

        :return: It returns the flag status; NAK on failure
        
        '''
        cmdGetFcntDisplay = 'READ:LINK:FCNT_DISPLAY?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetFcntDisplay)
        return result

    def link_setadrdisplay(self, flag):
        '''
        Configure the flag whether to display ADR field in Link 
        Analyzer screen

        :param flag: OFF, ON

        :return: ACK on success, NAK on failure
        
        '''
        cmdAdrDisplay = flag
        if cmdAdrDisplay == 'OFF':
            cmdSetAdrDisplay = 'CONF:LINK:ADR_DISPLAY OFF' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetAdrDisplay)
            return result
        elif cmdAdrDisplay == 'ON':
            cmdSetAdrDisplay = 'CONF:LINK:ADR_DISPLAY ON' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetAdrDisplay)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getadrdisplay(self):
        '''
        Read the flag whether to display ADR field in Link 
        Analyzer screen

        :param: Query only

        :return: It returns the flag status; NAK on failure
        
        '''
        cmdGetAdrDisplay = 'READ:LINK:ADR_DISPLAY?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetAdrDisplay)
        return result

    def link_setackdisplay(self, flag):
        '''
        Configure the flag whether to display ACK field in Link 
        Analyzer screen

        :param flag: OFF, ON

        :return: ACK on success, NAK on failure
        
        '''
        cmdAckDisplay = flag
        if cmdAckDisplay == 'OFF':
            cmdSetAckDisplay = 'CONF:LINK:ACK_DISPLAY OFF' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetAckDisplay)
            return result
        elif cmdAckDisplay == 'ON':
            cmdSetAckDisplay = 'CONF:LINK:ACK_DISPLAY ON' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetAckDisplay)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getackdisplay(self):
        '''
        Read the flag whether to display ACK field in Link 
        Analyzer screen

        :param: Query only

        :return: It returns the flag status; NAK on failure
        
        '''
        cmdGetAckDisplay = 'READ:LINK:ACK_DISPLAY?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetAckDisplay)
        return result

    def link_setclassb_display(self, flag):
        '''
        Configure the flag whether to display Class B field in Link 
        Analyzer screen

        :param flag: OFF, ON

        :return: ACK on success, NAK on failure
        
        '''
        cmdClassbDisplay = flag
        if cmdClassbDisplay == 'OFF':
            cmdSetClassbDisplay = 'CONF:LINK:CLASS_B_DISPLAY OFF' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetClassbDisplay)
            return result
        elif cmdClassbDisplay == 'ON':
            cmdSetClassbDisplay = 'CONF:LINK:CLASS_B_DISPLAY ON' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetClassbDisplay)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getclassb_display(self):
        '''
        Read the flag whether to display Class B field in Link 
        Analyzer screen

        :param: Query only

        :return: It returns the flag status; NAK on failure
        
        '''
        cmdGetClassbDisplay = 'READ:LINK:CLASS_B_DISPLAY?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetClassbDisplay)
        return result
    
    def link_setportdisplay(self, flag):
        '''
        Configure the flag whether to display FPort field in Link 
        Analyzer screen

        :param flag: OFF, ON

        :return: ACK on success, NAK on failure
        
        '''
        cmdPortDisplay = flag
        if cmdPortDisplay == 'OFF':
            cmdSetPortDisplay = 'CONF:LINK:PORT_DISPLAY OFF' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPortDisplay)
            return result
        elif cmdPortDisplay == 'ON':
            cmdSetPortDisplay = 'CONF:LINK:PORT_DISPLAY ON' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPortDisplay)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getportdisplay(self):
        '''
        Read the flag whether to display FPort field in Link 
        Analyzer screen

        :param: Query only

        :return: It returns the flag status; NAK on failure
        
        '''
        cmdGetPortDisplay = 'READ:LINK:PORT_DISPLAY?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetPortDisplay)
        return result

    def link_setmsgtypedisplay(self, flag):
        '''
        Configure the flag whether to display Message type field in 
        Link Analyzer screen

        :param flag: OFF, ON

        :return: ACK on success, NAK on failure
        
        '''
        cmdMsgtypeDisplay = flag
        if cmdMsgtypeDisplay == 'OFF':
            cmdSetMsgtypeDisplay = 'CONF:LINK:MSG_TYPE_DISPLAY OFF' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMsgtypeDisplay)
            return result
        elif cmdMsgtypeDisplay == 'ON':
            cmdSetMsgtypeDisplay = 'CONF:LINK:MSG_TYPE_DISPLAY ON' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMsgtypeDisplay)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getmsgtypedisplay(self):
        '''
        Read the flag whether to display Message type field in Link 
        Analyzer screen

        :param: Query only

        :return: It returns the flag status; NAK on failure
        
        '''
        cmdGetMsgtypeDisplay = 'READ:LINK:MSG_TYPE_DISPLAY?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMsgtypeDisplay)
        return result

    def link_setpowerdisplay(self, flag):
        '''
        Configure the flag whether to display the measured power in Link 
        Analyzer screen

        :param flag: OFF, ON

        :return: ACK on success, NAK on failure
        
        '''
        cmdPowDisplay = flag
        if cmdPowDisplay == 'OFF':
            cmdSetPowDisplay = 'CONF:LINK:POW_DISPLAY OFF' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPowDisplay)
            return result
        elif cmdPowDisplay == 'ON':
            cmdSetPowDisplay = 'CONF:LINK:POW_DISPLAY ON' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPowDisplay)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getpowerdisplay(self):
        '''
        Read the flag whether to display the measured power in Link 
        Analyzer screen

        :param: Query only

        :return: It returns the flag status; NAK on failure
        
        '''
        cmdGetPowDisplay = 'READ:LINK:POW_DISPLAY?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetPowDisplay)
        return result

    def link_setdrdisplay(self, flag):
        '''
        Configure the flag whether to display DR value in Link 
        Analyzer screen

        :param flag: OFF, ON

        :return: ACK on success, NAK on failure
        
        '''
        cmdDrDisplay = flag
        if cmdDrDisplay == 'OFF':
            cmdSetDrDisplay = 'CONF:LINK:DR_DISPLAY OFF' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetDrDisplay)
            return result
        elif cmdDrDisplay == 'ON':
            cmdSetDrDisplay = 'CONF:LINK:DR_DISPLAY ON' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetDrDisplay)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getdrdisplay(self):
        '''
        Read the flag whether to display DR value in Link 
        Analyzer screen

        :param: Query only

        :return: It returns the flag status; NAK on failure
        
        '''
        cmdGetDrDisplay = 'READ:LINK:DR_DISPLAY?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetDrDisplay)
        return result

    def link_setdelaydisplay(self, flag):
        '''
        Configure the flag whether to display RxDelay value in Link 
        Analyzer screen

        :param flag: OFF, ON

        :return: ACK on success, NAK on failure
        
        '''
        cmdDelayDisplay = flag
        if cmdDelayDisplay == 'OFF':
            cmdSetDelayDisplay = 'CONF:LINK:DELAY_DISPLAY OFF' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetDelayDisplay)
            return result
        elif cmdDelayDisplay == 'ON':
            cmdSetDelayDisplay = 'CONF:LINK:DELAY_DISPLAY ON' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetDelayDisplay)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getdelaydisplay(self):
        '''
        Read the flag whether to display RxDelay value in Link Analyzer screen

        :param: Query only

        :return: It returns the flag status; NAK on failure
        
        '''
        cmdGetDelayDisplay = 'READ:LINK:DELAY_DISPLAY?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetDelayDisplay)
        return result

    def link_setadrackreq_display(self, flag):
        '''
        Configure the flag whether to display ADRACKReq field in Link 
        Analyzer screen

        :param flag: OFF, ON

        :return: ACK on success, NAK on failure
        
        '''
        cmdAdrackreqDisplay = flag
        if cmdAdrackreqDisplay == 'OFF':
            cmdSetAdrackreqDisplay = 'CONF:LINK:ADRACKREQ_DISPLAY OFF' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetAdrackreqDisplay)
            return result
        elif cmdAdrackreqDisplay == 'ON':
            cmdSetAdrackreqDisplay = 'CONF:LINK:ADRACKREQ_DISPLAY ON' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetAdrackreqDisplay)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getadrackreq_display(self):
        '''
        Read the flag whether to display ADRACKReq field in Link 
        Analyzer screen

        :param: Query only

        :return: It returns the flag status; NAK on failure
        
        '''
        cmdGetAdrackreqDisplay = 'READ:LINK:ADRACKREQ_DISPLAY?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetAdrackreqDisplay)
        return result

    def link_setfpendingdisplay(self, flag):
        '''
        Configure the flag whether to display FPending field in Link 
        Analyzer screen

        :param flag: OFF, ON

        :return: ACK on success, NAK on failure
        
        '''
        cmdFpendingDisplay = flag
        if cmdFpendingDisplay == 'OFF':
            cmdSetFpendingDisplay = 'CONF:LINK:FPENDING_DISPLAY OFF' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetFpendingDisplay)
            return result
        elif cmdFpendingDisplay == 'ON':
            cmdSetFpendingDisplay = 'CONF:LINK:FPENDING_DISPLAY ON' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetFpendingDisplay)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getfpendingdisplay(self):
        '''
        Read the flag whether to display FPending field in Link 
        Analyzer screen

        :param: Query only

        :return: It returns the flag status; NAK on failure
        
        '''
        cmdGetFpendingDisplay = 'READ:LINK:FPENDING_DISPLAY?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetFpendingDisplay)
        return result

    def link_setdwelldisplay(self, flag):
        '''
        Configure the flag whether to display dwell time field in Link 
        Analyzer screen

        :param flag: OFF, ON

        :return: ACK on success, NAK on failure
        
        '''
        cmdDwellDisplay = flag
        if cmdDwellDisplay == 'OFF':
            cmdSetDwellDisplay = 'CONF:LINK:DWELL_DISPLAY OFF' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetDwellDisplay)
            return result
        elif cmdDwellDisplay == 'ON':
            cmdSetDwellDisplay = 'CONF:LINK:DWELL_DISPLAY ON' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetDwellDisplay)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getdwelldisplay(self):
        '''
        Read the flag whether to display dwell time field in Link 
        Analyzer screen

        :param: Query only

        :return: It returns the flag status; NAK on failure
        
        '''
        cmdGetDwellDisplay = 'READ:LINK:DWELL_DISPLAY?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetDwellDisplay)
        return result

    def link_setpayloadlength(self, *args):
        '''
        Configure the length of payload in bytes in EchoRequest Command

        :param *args: For version below 1.17
                      only length required 
                      (1 ~ 242)

                      For version 1.17 and above:
                      first parameter should be a MAC command number,
                      second parameter should be length 
                      (1 ~ 242)

        :return: ACK on success, NAK on failure
        
        '''
        if len(args) == 1 and args[0] >= 1 and args[0] <= 242:
            cmdEchoLen = str(args[0])
            cmdSetEchoLen = 'CONF:LINK:ECHO_LEN ' \
            + cmdEchoLen + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetEchoLen)
            return result
        if len(args) ==2 and args[1] >= 1 and args[1] <= 242:
            cmdMacNum = str(args[0])
            cmdEchoLen = str(args[1])
            cmdSetEchoLen = 'CONF:LINK:ECHO_LEN ' \
            + cmdMacNum + ' ' + cmdEchoLen + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetEchoLen)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getpayloadlength(self, *args):
        '''
        Read the length of payload in bytes in EchoRequest Command

        :param *args: MAC Command Number if version is 1.17 and
                      above, otherwise parameter not required 

        :return: It returns the payload length; NAK on failure
        
        '''
        if len(args) == 0:
            cmdGetEchoLen = 'READ:LINK:ECHO_LEN?' + '\n'
            result = RwcSerialSetup.transceive(self, cmdGetEchoLen)
            return result
        elif len(args) == 1:
            cmdMacNum = str(args[0])
            cmdGetEchoLen = 'READ:LINK:ECHO_LEN? ' + cmdMacNum + '\n'
            result = RwcSerialSetup.transceive(self, cmdGetEchoLen)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_setechopayload(self, macnum, value):
        '''
        Configure the Message data of echo request command

        :param value: 250-byte HEX value

        :return: ACK on success, NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        cmdValue = int(value)
        if (cmdValue >= 0 and cmdValue <= 2**250 -1) :
            cmdHexValue = hex(cmdValue)
            cmdSetEchoPayload = 'CONF:LINK:ECHO_PAYLOAD ' \
                                    + cmdMacNum + ' ' \
                                    + cmdHexValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetEchoPayload)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getechopayload(self, macnum):
        '''
        Read the Message data of echo request command

        :param: Query only

        :return: It returns the payload data; NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        cmdGetMsgData = 'READ:LINK:ECHO_PAYLOAD? ' + cmdMacNum + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMsgData)
        return result

    def link_setcwtimeout(self, *args):
        '''
        Configure the timeout of CW transmission in Enable Continuous 
        Wave Mode command

        :param *args: For version below 1.17
                      only time required 
                      (1 ~ 255)

                      For version 1.17 and above:
                      first parameter should be a MAC command number,
                      second parameter should be time 
                      (1 ~ 255)

        :return: ACK on success, NAK on failure
        
        '''
        if len(args) == 1 and args[0] >= 1 and args[0] <= 255:
            cmdCwTimeout = str(args[0])
            cmdSetCwTimeout = 'CONF:LINK:CW_TIMEOUT ' \
                                + cmdCwTimeout + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetCwTimeout)
            return result
        elif len(args) == 2 and args[1] >= 1 and args[1] <= 255:
            cmdMacNum = str(args[0])
            cmdCwTimeout = str(args[1])
            cmdSetCwTimeout = 'CONF:LINK:CW_TIMEOUT ' \
                                + cmdMacNum + ' ' \
                                + cmdCwTimeout + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetCwTimeout)
            return result
        else:
            raise Exception('Invalid parameter received.')
    
    def link_getcwtimeout(self, *args):
        '''
        Read the timeout of CW transmission in Enable Continuous 
        Wave Mode command

        :param *args: MAC Command Number if version is 1.17 and
                      above, otherwise parameter not required 

        :return: It returns the CW timeout value; NAK on failure
        
        '''
        if len(args) == 0:
            cmdGetCwTimeout = 'READ:LINK:CW_TIMEOUT?' + '\n'
        elif len(args) == 1:
            cmdMacNum = str(args[0])
            cmdGetCwTimeout = 'READ:LINK:CW_TIMEOUT? ' + cmdMacNum + '\n'
        else:
            raise Exception('Invalid parameter received.')

        result = RwcSerialSetup.transceive(self, cmdGetCwTimeout)
        return result
    
    def link_setcwfrequency(self, *args):
        '''
        Configure the frequency of CW signal in Enable Continuous Wave 
        Mode command

        :param *args: For version below 1.17
                      only frequency required 
                      (400 ~ 510 MHz, 862 ~ 960 MHz)

                      For version 1.17 and above:
                      first parameter should be a MAC command number,
                      second parameter should be frequency 
                      (400 ~ 510 MHz, 862 ~ 960 MHz)

        :return: ACK on success, NAK on failure
        
        '''
        if len(args) == 1 and (args[0] >= 400 
                and args[0] <= 510) or (args[0] >= 862 
                    and args[0] <= 960):
            cmdCwFreq = str(args[0])
            cmdSetCwFreq = 'CONF:LINK:CW_FREQ ' \
                            + cmdCwFreq + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetCwFreq)
            return result
        elif len(args) == 2 and (args[1] >= 400 
                and args[1] <= 510) or (args[1] >= 862 
                    and args[1] <= 960):
            cmdMacNum = str(args[0])
            cmdCwFreq = str(args[1])
            cmdSetCwFreq = 'CONF:LINK:CW_FREQ ' \
                            + cmdMacNum + ' ' \
                            + cmdCwFreq + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetCwFreq)
            return result
        else:
            raise Exception('Invalid parameter received.')
    
    def link_getcwfrequency(self, *args):
        '''
        Read the frequency of CW signal in Enable Continuous 
        Wave Mode command

        :param *args: MAC Command Number if version is 1.17 and
                      above, otherwise parameter not required 

        :return: It returns the CW frequency value; NAK on failure
        
        '''
        if len(args) == 0:
            cmdGetCwFrequency = 'READ:LINK:CW_FREQ?' + '\n'
        elif len(args) == 1:
            cmdMacNum = str(args[0])
            cmdGetCwFrequency = 'READ:LINK:CW_FREQ? ' + cmdMacNum + '\n'
        else:
            raise Exception('Invalid parameter received.')
        
        result = RwcSerialSetup.transceive(self, cmdGetCwFrequency)
        return result
    
    def link_setcwpower(self, *args):
        '''
        Configure the power of CW signal in dBm in Enable Continuous Wave 
        Mode command

        :param *args: For version below 1.17
                      only power required 
                      (0 ~ 40)

                      For version 1.17 and above:
                      first parameter should be a MAC command number,
                      second parameter should be power 
                      (0 ~ 40)

        :return: ACK on success, NAK on failure
        
        '''
        if len(args) == 1 and args[0] >= 0 and args[0] <= 40:
            cmdCwPow = str(args[0])
            cmdSetCwPow = 'CONF:LINK:CW_POW ' \
                            + cmdCwPow + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetCwPow)
            return result
        elif len(args) == 2 and args[1] >= 0 and args[1] <= 40:
            cmdMacNum = str(args[0])
            cmdCwPow = str(args[1])
            cmdSetCwPow = 'CONF:LINK:CW_POW ' \
                            + cmdMacNum + ' ' \
                            + cmdCwPow + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetCwPow)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getcwpower(self, *args):
        '''
        Read the power of CW signal in dBm in Enable Continuous Wave 
        Mode command

        :param *args: MAC Command Number if version is 1.17 and
                      above, otherwise parameter not required 

        :return: It returns the CW power value; NAK on failure

        '''
        if len(args) == 0:
            cmdGetCwPow = 'READ:LINK:CW_POW?' + '\n'
        elif len(args) == 1:
            cmdMacNum = str(args[0])
            cmdGetCwPow = 'READ:LINK:CW_POW? ' + cmdMacNum + '\n'
        else:
            raise Exception('Invalid parameter received.')

        result = RwcSerialSetup.transceive(self, cmdGetCwPow)
        return result

    def link_setmacinterval(self, interval):
        '''
        Configure the minimum MAC command interval in sec. This 
        parameter is used for Periodic Downlink in Class B & C

        :param interval: 5 - 60

        :return: ACK on success, NAK on failure

        '''
        if interval >= 5 and interval <= 60:
            cmdInterval = str(interval)
            cmdSetMacInterval = 'CONF:LINK:MAC_INTERVAL ' + cmdInterval + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMacInterval)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getmacinterval(self):
        '''
        Read the minimum MAC command interval in sec.

        :Parameters: N/A (Query only)

        :return: It returns the interval in seconds; NAK on failure
        
        '''
        cmdGetMacInterval = 'READ:LINK:MAC_INTERVAL?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMacInterval)
        return result

    def link_setabnormal(self, value):
        '''
        Config the abnormal behavior of RWC5020A.
        For Example, RWC5020A sends packets with artificially generated 
        MIC Error Packets if it is set as MIC_ERR

        :param value: OFF, MIC_ERR, NO_RSP, INVALID_CMD

        :return: ACK on success, NAK on failure
        
        '''
        abnormalparamlist = [
            'OFF', 
            'MIC_ERR', 
            'NO_RSP', 
            'INVALID_CMD']
        if value in abnormalparamlist:
            cmdSetAbnormal = 'CONF:LINK:ABNORMAL ' + value + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetAbnormal)
            return result
        else:
            raise Exception('Invalid abnormal parameter received.')

    def link_getabnormal(self):
        '''
        Read the abnormal behavior of RWC5020A.

        :param: Query only

        :return: It returns the link abnormal message; NAK on failure
        
        '''
        cmdGetAbnormalValue = 'READ:LINK:ABNORMAL?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetAbnormalValue)
        return result

    def link_getmacsendresult(self, macnum):
        '''
        Read MAC response information after sending MAC command. 
        For multi-mac response, it requires MAC_NUM parameter

        :param macnum: MAC Command Number

        :return: MAC response; NAK on failure
        
        '''
        cmdMacNum = str(macnum)
        cmdGetMacSendResult = 'READ:LINK:MAC_SENDL_RESULT? ' \
                                + cmdMacNum + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMacSendResult)
        return result

    def link_getmacsendstatus(self):
        '''
        Read MAC command sending status. There are five status defined 
        (IDLE, STARTED, SCHEDULED, GOT_RSP, TIMEOUT). 
        Refer to following fig.

        :Parameters: N/A (Query only)

        :return: MAC Command status; NAK on failure

        '''
        cmdGetMacSendStatus = 'READ:LINK:MAC_SEND_STATUS?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMacSendStatus)
        return result
    
    def link_getdutycycle(self):
        '''
        Read duty cycle value displayed on Link Analyzer

        :Parameters: N/A (Query only)

        :return: Duty cycle value; NAK on failure

        '''
        cmdGetDutyCycleVal = 'READ:LINK:DUTY_CYCLE?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetDutyCycleVal)
        return result

    def link_setmalfunction(self, value):
        '''
        To configure malfunction activation

        :param value: ON, OFF

        :return: ACK on success, NAK on failure

        '''
        cmdValue = value
        if (cmdValue == 'ON' or cmdValue == 'OFF'):
            cmdSetMalfunction = 'CONF:LINK:MALFUNCTION ' + cmdValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMalfunction)
            return result
        else:
            raise Exception('Invalid malfunction parameter received.')

    def link_getmalfunction(self):
        '''
        To read malfunction activation

        :Parameters: N/A (Query only)

        :return: link malfunction status; NAK on failure

        '''
        cmdGetMalfunction = 'READ:LINK:MALFUNCTION?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMalfunction)
        return result

    def link_setmicerror(self, value):
        '''
        To configure Mic Error activation for malfunction testing

        :param value: ON, OFF

        :return: ACK on success, NAK on failure

        '''
        cmdValue = value
        if (cmdValue == 'ON' or cmdValue == 'OFF'):
            cmdSetMicError = 'CONF:LINK:MIC_ERROR ' + cmdValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMicError)
            return result
        else:
            raise Exception('Invalid MIC Error parameter received.')

    def link_getmicerror(self):
        '''
        To read Mic Error activation for malfunction testing

        :Parameters: N/A (Query only)

        :return: link mic error activation status; NAK on failure

        '''
        cmdGetMicError = 'READ:LINK:MIC_ERROR?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMicError)
        return result

    def link_setmhdrerror(self, value):
        '''
        To configure MAC Header Error activation for malfunction 
        testing

        :param value: ON, OFF

        :return: ACK on success, NAK on failure

        '''
        cmdValue = value
        if (cmdValue == 'ON' or cmdValue == 'OFF'):
            cmdSetMACError = 'CONF:LINK:MHDR_ERROR ' + cmdValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMACError)
            return result
        else:
            raise Exception('Invalid MAC Error parameter received.')

    def link_getmhdrerror(self):
        '''
        To read MAC header Error activation for malfunction testing

        :Parameters: N/A (Query only)

        :return: link MAC error activation status; NAK on failure

        '''
        cmdGetMACError = 'READ:LINK:MHDR_ERROR?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMACError)
        return result

    def link_setxormhdr(self, value):
        '''
        To configure exclusive OR for value for MAC header

        :param value: 8-bit Hex Value

        :return: ACK on success, NAK on failure

        '''
        cmdValue = int(value)
        if (cmdValue >= 0 and cmdValue <= 2**8 - 1):
            cmdHexValue = hex(cmdValue)
            cmdXorMHDR = 'CONF:LINK:XOR_MHDR ' + cmdHexValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdXorMHDR)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getxormhdr(self):
        '''
        To read exclusive OR for value for MAC header

        :Parameters: N/A (Query only)

        :return: link XOR MAC header value; NAK on failure

        '''
        cmdGetXorMHDR = 'READ:LINK:XOR_MHDR?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetXorMHDR)
        return result

    def link_setfhdrerror(self, value):
        '''
        To configure Frame Header Error activation for malfunction 
        testing

        :param value: ON, OFF

        :return: ACK on success, NAK on failure

        '''
        cmdValue = value
        if (cmdValue == 'ON' or cmdValue == 'OFF'):
            cmdSetFrameError = 'CONF:LINK:FHDR_ERROR ' + cmdValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetFrameError)
            return result
        else:
            raise Exception('Invalid FHDR Error parameter received.')

    def link_getfhdrerror(self):
        '''
        To read frame header Error activation for malfunction testing

        :Parameters: N/A (Query only)

        :return: link frame error activation status; NAK on failure

        '''
        cmdGetFrameError = 'READ:LINK:FHDR_ERROR?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetFrameError)
        return result

    def link_setxorfhdr(self, value):
        '''
        To configure exclusive OR for value for Frame header

        :param value: 56-bit Hex Value

        :return: ACK on success, NAK on failure

        '''
        cmdValue = int(value)
        if (cmdValue >= 0 and cmdValue <= 2**56 - 1):
            cmdHexValue = hex(cmdValue)
            cmdXorFHDR = 'CONF:LINK:XOR_FHDR ' + cmdHexValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdXorFHDR)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def link_getxorfhdr(self):
        '''
        To read exclusive OR for value for Frame header

        :Parameters: N/A (Query only)

        :return: link XOR Frame header value; NAK on failure

        '''
        cmdGetXorFHDR = 'READ:LINK:XOR_FHDR?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetXorFHDR)
        return result

    def link_getfuotafilelength(self):
        '''
        To read the length of FUOTA binary file

        :Parameters: N/A (Query only)

        :return: FUOTA binary file length; NAK on failure

        '''
        cmdGetFUOTAFileLen = 'READ:LINK:FUOTA_FILE_LEN?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetFUOTAFileLen)
        return result

    def link_getfuotafilename(self):
        '''
        To read the name of FUOTA binary file

        :Parameters: N/A (Query only)

        :return: name of the FUOTA binary file; NAK on failure

        '''
        cmdGetFUOTAFileName = 'READ:LINK:FUOTA_FILE_NAME?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetFUOTAFileName)
        return result

    def link_setfragmentindex(self, indexval):
        '''
        To configure fragment index for application layer

        :param indexval: 0 - 3

        :return: ACK on success, NAK on failure

        '''
        if indexval >= 0 and indexval <= 3:
            cmdIndexVal = str(indexval)
            cmdSetFragIndex = 'CONF:LINK:FRAG_INDEX ' + cmdIndexVal + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetFragIndex)
            return result
        else:
            raise Exception('Invalid fragment index parameter received.')

    def link_setfragmentsize(self, fragsize):
        '''
        To configure fragment size for application layer

        :param fragsize: 1 - 255

        :return: ACK on success, NAK on failure

        '''
        if fragsize >= 1 and fragsize <= 255:
            cmdFragSize= str(fragsize)
            cmdSetFragSize = 'CONF:LINK:FRAG_SIZE ' + cmdFragSize + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetFragSize)
            return result
        else:
            raise Exception('Invalid fragment size parameter received.')

    def link_setnumberoffragment(self, fragnum):
        '''
        To configure number of fragment for application layer

        :param fragnum: 1 - 65535

        :return: ACK on success, NAK on failure

        '''
        if fragnum >= 1 and fragnum <= 65535:
            cmdFragNum= str(fragnum)
            cmdSetFragNum = 'CONF:LINK:NB_FRAG ' + cmdFragNum + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetFragNum)
            return result
        else:
            raise Exception('Invalid fragment number parameter received.')

    def link_setfragemntpadding(self, paddingval):
        '''
        To configure fragment padding for application layer

        :param paddingval: 1 - 255

        :return: ACK on success, NAK on failure

        '''
        if paddingval >= 1 and paddingval <= 255:
            cmdPaddingval= str(paddingval)
            cmdSetFragPadding = 'CONF:LINK:FRAG_PADDING ' \
                                    + cmdPaddingval + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetFragPadding)
            return result
        else:
            raise Exception('Invalid fragment padding parameter received.')

    def link_setfragmentdescriptor(self, descval):
        '''
        To configure fragment descriptor for application layer

        :param descval: 0x0 - 0xFFFFFFFF

        :return: ACK on success, NAK on failure

        '''
        cmdDescVal = int(descval)
        if (cmdDescVal >= 0 and cmdDescVal <= 2**32 - 1):
            cmdHexValue = hex(cmdDescVal)
            cmdSetFragDesc = 'CONF:LINK:FRAG_DESCRIPTOR ' + cmdHexValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetFragDesc)
            return result
        else:
            raise Exception('Invalid Fragment descriptor parameter received.')

    def link_setfragmentalgorithm(self, algoval):
        '''
        To configure fragment algorithm for application layer

        :param algoval: 0 - 7

        :return: ACK on success, NAK on failure

        '''
        if algoval >= 0 and algoval <= 7:
            cmdAlgoVal= str(algoval)
            cmdSetFragAlgo = 'CONF:LINK:FRAG_ALGO ' + cmdAlgoVal + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetFragAlgo)
            return result
        else:
            raise Exception('Invalid fragment algorithm parameter received.')

    def link_getfragmentprocessingstatus(self):
        '''
        To read the status of fragment progressing for 
        application layer

        :Parameters: NA (Query only)

        :return: It returns fragment progressing status, NAK on failure

        '''
        cmdGetFragProcessStatus = 'READ:LINK:FRAG_PROGRESS?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetFragProcessStatus)
        return result

    def link_setmulticastkey(self, value):
        '''
        To configure multicast key value for application layer

        :param value: 128-bit Hex value

        :return: ACK on success, NAK on failure

        '''
        cmdValue = int(value)
        if (cmdValue >= 0 and cmdValue <= 2**128 - 1):
            cmdHexValue = hex(cmdValue)
            cmdSetMcKey = 'CONF:LINK:MC_KEY ' + cmdHexValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMcKey)
            return result
        else:
            raise Exception('Invalid Multicast key parameter received.')

    def link_setmulticastgroupid(self, groupid):
        '''
        To configure multicast group id for application layer

        :param groupid: 0 - 3

        :return: ACK on success, NAK on failure

        '''
        if groupid >= 0 and groupid <= 3:
            cmdGroupId= str(groupid)
            cmdSetMcGroupId = 'CONF:LINK:MC_GROUP_ID ' + cmdGroupId + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMcGroupId)
            return result
        else:
            raise Exception('Invalid Multicast Group ID parameter received.')

    def link_setmulticastaddress(self, mcaddrval):
        '''
        To configure multicast address for application layer

        :param mcaddrval: 0x0 - 0xFFFFFFFF

        :return: ACK on success, NAK on failure

        '''
        cmdMcAddrVal = int(mcaddrval)
        if (cmdMcAddrVal >= 0 and cmdMcAddrVal <= 2**32 - 1):
            cmdHexValue = hex(cmdMcAddrVal)
            cmdSetMcAddrval = 'CONF:LINK:MC_ADDR ' + cmdHexValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMcAddrval)
            return result
        else:
            raise Exception('Invalid Multicast address parameter received.')

    def link_setmulticastfrequency(self, freqval):
        '''
        To configure multicast frequency for application layer

        :param freqval: 400 - 510, 862 - 960 MHz

        :return: ACK on success, NAK on failure

        '''
        if (freqval >= 400 and freqval <= 510) or (freqval >= 862 
                and freqval <= 960):
            cmdFreq= str(freqval)
            cmdSetMcFreq = 'CONF:LINK:MC_FREQ ' + cmdFreq + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMcFreq)
            return result
        else:
            raise Exception('Invalid Multicast Frequency parameter received.')

    def link_setmulticastdr(self, drval):
        '''
        To configure multicast data rate for application layer

        :param drval: 'DR0_SF12BW125', 'DR1_SF11BW125', 
                      'DR2_SF10BW125', 'DR3_SF9BW125', 
                      'DR4_SF8BW125', 'DR5_SF7BW125', 
                      'DR6_SF7BW250', 'DR7_FSK50'

        :return: ACK on success, NAK on failure

        '''
        drlist = [
            'DR0_SF12BW125', 
            'DR1_SF11BW125', 
            'DR2_SF10BW125',
            'DR3_SF9BW125', 
            'DR4_SF8BW125', 
            'DR5_SF7BW125', 
            'DR6_SF7BW250', 
            'DR7_FSK50']
        if drval in drlist:
            cmdSetMcDr = 'CONF:LINK:MC_DR ' + drval + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMcDr)
            return result
        else:
            raise Exception('Invalid multicast data rate Parameter received.')

    def link_setmulticastoption(self, optval):
        '''
        To configure multicast option for application layer

        :param optval: 0 - 1

        :return: ACK on success, NAK on failure

        '''
        if optval == 0 or optval == 1:
            cmdOptVal= str(optval)
            cmdSetMcOption = 'CONF:LINK:MC_OPTION ' + cmdOptVal + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMcOption)
            return result
        else:
            raise Exception('Invalid Multicast option parameter received.')

    def link_setmulticastinterval(self, interval):
        '''
        To configure multicast interval between multicast packets 
        for application layer

        :param interval: 1 - 10000

        :return: ACK on success, NAK on failure

        '''
        if interval >= 1 and interval <= 10000:
            cmdInterval= str(interval)
            cmdSetMcInterval = 'CONF:LINK:MC_INTERVAL ' + cmdInterval + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMcInterval)
            return result
        else:
            raise Exception('Invalid Multicast Interval parameter received.')

    def link_setfirmwarereboottimemode(self, mode):
        '''
        To configure firmware management reboot time mode for 
        application layer

        :param mode: TIME, ASAP, CANCEL

        :return: ACK on success, NAK on failure
        
        '''
        reboottimemodelist = ['TIME', 'ASAP', 'CANCEL']
        if mode in reboottimemodelist:
            cmdSetFMRebootTimeMode = 'CONF:LINK:FM_REBOOT_TIME_MODE ' \
                                        + mode + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetFMRebootTimeMode)
            return result
        else:
            raise Exception('Invalid firmware reboot time mode ' \
                            'Parameter received.')

    def link_setfirmwarerebootyear(self, yearval):
        '''
        To configure firmware management reboot time (year) for 
        application layer

        :param yearval: 1900 - 2300

        :return: ACK on success, NAK on failure

        '''
        if yearval >= 1900 and yearval <= 2300:
            cmdYearVal= str(yearval)
            cmdSetFMRebootYear = 'CONF:LINK:FM_REBOOT_YEAR ' \
                                    + cmdYearVal + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetFMRebootYear)
            return result
        else:
            raise Exception('Invalid reboot year parameter received.')

    def link_setfirmwarerebootmonth(self, monthval):
        '''
        To configure firmware management reboot time (month) for 
        application layer

        :param monthval: 1 - 12

        :return: ACK on success, NAK on failure

        '''
        if monthval >= 1 and monthval <= 12:
            cmdMonthVal= str(monthval)
            cmdSetFMRebootMonth = 'CONF:LINK:FM_REBOOT_MONTH ' \
                                    + cmdMonthVal + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetFMRebootMonth)
            return result
        else:
            raise Exception('Invalid reboot month parameter received.')

    def link_setfirmwarerebootday(self, dayval):
        '''
        To configure firmware management reboot time (day) for 
        application layer

        :param dayval: 1 - 31

        :return: ACK on success, NAK on failure

        '''
        if dayval >= 1 and dayval <= 31:
            cmdDayVal= str(dayval)
            cmdSetFMRebootDay = 'CONF:LINK:FM_REBOOT_DAY ' + cmdDayVal + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetFMRebootDay)
            return result
        else:
            raise Exception('Invalid reboot day parameter received.')

    def link_setfirmwarereboothour(self, hourval):
        '''
        To configure firmware management reboot time (hour) for 
        application layer

        :param hourval: 0 - 23

        :return: ACK on success, NAK on failure

        '''
        if hourval >= 0 and hourval <= 23:
            cmdHourVal= str(hourval)
            cmdSetFMRebootHour = 'CONF:LINK:FM_REBOOT_HOUR ' \
                                    + cmdHourVal + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetFMRebootHour)
            return result
        else:
            raise Exception('Invalid reboot hour parameter received.')

    def link_setfirmwarerebootminute(self, minval):
        '''
        To configure firmware management reboot time (minute) for 
        application layer

        :param minval: 0 - 59

        :return: ACK on success, NAK on failure

        '''
        if minval >= 0 and minval <= 59:
            cmdMinVal= str(minval)
            cmdSetFMRebootMinute = 'CONF:LINK:FM_REBOOT_MINUTE ' \
                                    + cmdMinVal + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetFMRebootMinute)
            return result
        else:
            raise Exception('Invalid reboot minute parameter received.')

    def link_setfirmwarerebootsecond(self, secval):
        '''
        To configure firmware management reboot time (second) for 
        application layer

        :param secval: 0 - 59

        :return: ACK on success, NAK on failure

        '''
        if secval >= 0 and secval <= 59:
            cmdSecVal= str(secval)
            cmdSetFMRebootSecond = 'CONF:LINK:FM_REBOOT_SECOND ' \
                                    + cmdSecVal + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetFMRebootSecond)
            return result
        else:
            raise Exception('Invalid reboot second parameter received.')

    def link_setfirmwarerebootcountdownval(self, cdval):
        '''
        To configure firmware management reboot count down value for 
        application layer

        :param cdval: 0x0 - 0xFFFFFF

        :return: ACK on success, NAK on failure

        '''
        cmdCdVal = int(cdval)
        if (cmdCdVal >= 0 and cmdCdVal <= 2**24 - 1):
            cmdHexValue = hex(cmdCdVal)
            cmdSetFmCdVal = 'CONF:LINK:FM_REBOOT_CD ' + cmdHexValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetFmCdVal)
            return result
        else:
            raise Exception('Invalid reboot countdown parameter received.')

    def link_setnextfirmwareversion(self, nextfmver):
        '''
        To configure next firmware version of firmware management for 
        application layer

        :param nextfmver: 0x0 - 0xFFFFFFFF

        :return: ACK on success, NAK on failure

        '''
        cmdNxtFmVerVal = int(nextfmver)
        if (cmdNxtFmVerVal >= 0 and cmdNxtFmVerVal <= 2**32 - 1):
            cmdHexValue = hex(cmdNxtFmVerVal)
            cmdSetNextFmVerVal = 'CONF:LINK:FM_NEXT_FW_VER ' \
                                    + cmdHexValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetNextFmVerVal)
            return result
        else:
            raise Exception('Invalid next firmware version ' \
                            'parameter received.')

    def link_deletefirmwareversion(self, delfmver):
        '''
        To configure delete firmware version of firmware management 
        for application layer

        :param delfmver: 0x0 - 0xFFFFFFFF

        :return: ACK on success, NAK on failure

        '''
        cmdDelFmVerVal = int(delfmver)
        if (cmdDelFmVerVal >= 0 and cmdDelFmVerVal <= 2**32 - 1):
            cmdHexValue = hex(cmdDelFmVerVal)
            cmdSetDelFmVerVal = 'CONF:LINK:FM_DEL_FW_VER ' \
                                    + cmdHexValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetDelFmVerVal)
            return result
        else:
            raise Exception('Invalid delete firmware version ' \
                            'parameter received.')

    def link_setapptimeperiod(self, timeperiodval):
        '''
        To configure the application layer time request period

        :param timeperiodval: 0 - 15

        :return: ACK on success, NAK on failure

        '''
        if timeperiodval >= 0 and timeperiodval <= 15:
            cmdTimePeriodVal = str(timeperiodval)
            cmdSetAppTimePeriod = 'CONF:LINK:APP_TIME_PERIOD ' \
                                    + cmdTimePeriodVal + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetAppTimePeriod)
            return result
        else:
            raise Exception('Invalid time request period parameter received.')

    def link_setapptimetransnumber(self, timesynctransnumber):
        '''
        To configure the number of transfers for time synchronization 
        application layer

        :param timesynctransnumber: 0 - 7

        :return: ACK on success, NAK on failure
 

        .. _powerlabel:
        '''
        if timesynctransnumber >= 0 and timesynctransnumber <= 7:
            cmdTimeSyncTransVal = str(timesynctransnumber)
            cmdSetAppTimeSyncTransNo = 'CONF:LINK:APP_TIME_NB_TRANS ' \
                                        + cmdTimeSyncTransVal + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetAppTimeSyncTransNo)
            return result
        else:
            raise Exception('Invalid time sync transfer number ' \
                            'parameter received.')

    #Power Command Methods
    def power_setscalemode(self, mode):
        '''
        Configure the scaling mode of Y-axis

        :param mode: AUTO, MANUAL

        :return: ACK on success, NAK on failure
        
        '''
        cmdScalingMode = mode
        if cmdScalingMode == 'AUTO':
            cmdSetScalingMode = 'CONF:POWER:SCALE AUTO' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetScalingMode)
            return result
        elif cmdScalingMode == 'MANUAL':
            cmdSetScalingMode = 'CONF:POWER:SCALE MANUAL' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetScalingMode)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def power_getscalemode(self):
        '''
        Read the scaling mode of Y-axis

        :Parameters: Query only

        :return: It returns the scaling mode; NAK on failure
        
        '''
        cmdGetScalingMode = 'READ:POWER:SCALE?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetScalingMode)
        return result

    def power_setmaxyvalue(self, maxval):
        '''
        Configure the maximum value of Y-axis

        :param maxval: 40 ~ -60

        :return: ACK on success, NAK on failure
        
        '''
        maxnum = int(maxval)
        if maxnum >= -60 and maxnum <= 40:
            cmdMaxVal = str(maxnum)
            cmdSetMaxVal = 'CONF:POWER:MAX_Y ' + cmdMaxVal + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMaxVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def power_getmaxyvalue(self):
        '''
        Read the maximum value of Y-axis

        :Parameters: Query only

        :return: It returns Y-axis max value; NAK on failure
        
        '''
        cmdGetMaxVal = 'READ:POWER:MAX_Y?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMaxVal)
        return result

    def power_setminyvalue(self, minval):
        '''
        Configure the minimum value of Y-axis 

        :param minval: 30 ~ -80

        :return: ACK on success, NAK on failure
        
        '''
        minnum = int(minval)
        if minnum >= -60 and minnum <= 40:
            cmdMinVal = str(minnum)
            cmdSetMinVal = 'CONF:POWER:MIN_Y ' + cmdMinVal + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMinVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def power_getminyvalue(self):
        '''
        Read the minimum value of Y-axis

        :Parameters: Query only

        :return: It returns Y-axis min value; NAK on failure
        
        '''
        cmdGetMinVal = 'READ:POWER:MIN_Y?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMinVal)
        return result

    def power_getnumofpkts_dut(self):
        '''
        Read the number of received packets

        :Parameters: Query only

        :return: It returns number of packets received; NAK on failure
        
        '''
        cmdGetNumPkts = 'READ:POWER:ALL:NUM?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetNumPkts)
        return result

    def power_getmaxdutpower(self):
        '''
        Read the maximum DUT power of all the measured

        :Parameters: Query only

        :return: It returns max DUT power; NAK on failure
        
        '''
        cmdGetMaxDut = 'READ:POWER:ALL:MAX?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMaxDut)
        return result

    def power_getavgdutpower(self):
        '''
        Read the average DUT power of all the measured

        :Parameters: Query only

        :return: It returns average DUT power; NAK on failure
        
        '''
        cmdGetAvgDut = 'READ:POWER:ALL:AVG?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetAvgDut)
        return result

    def power_getmindutpower(self):
        '''
        Read the minimum DUT power of all the measured 

        :Parameters: Query only

        :return: It returns minimum DUT power; NAK on failure
        
        '''
        cmdGetMinDut = 'READ:POWER:ALL:MIN?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMinDut)
        return result

    def power_getnumofpkts_dut_sf(self, index):
        '''
        Read the number of received packets 

        :param index: 7 - 12

        :return: It returns number of packets received; NAK on failure
        
        '''
        indexnum = int(index)
        if indexnum >= 7 and indexnum <= 12:
            cmdSfIndex = str(indexnum)
            cmdGetSfNumPkts = 'READ:POWER:SF' + cmdSfIndex + ':NUM?' + '\n'
            result = RwcSerialSetup.transceive(self, cmdGetSfNumPkts)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def power_getmaxdutpower_sf(self, index):
        '''
        Read the maximum DUT power using SF* of all the measured 

        :param index: 7 - 12

        :return: It returns max DUT power; NAK on failure
        
        '''
        indexnum = int(index)
        if indexnum >= 7 and indexnum <= 12:
            cmdSfIndex = str(indexnum)
            cmdGetSfMaxDut = 'READ:POWER:SF' + cmdSfIndex + ':MAX?' + '\n'
            result = RwcSerialSetup.transceive(self, cmdGetSfMaxDut)
            return result
        else:
            raise Exception('Invalid parameter received.')
    
    def power_getavgdutpower_sf(self, index):
        '''
        Read the average DUT power using SF* of all the measured

        :param index: 7 - 12

        :return: It returns average DUT power; NAK on failure
        
        '''
        indexnum = int(index)
        if indexnum >= 7 and indexnum <= 12:
            cmdSfIndex = str(indexnum)
            cmdGetSfAvgDut = 'READ:POWER:SF' + cmdSfIndex + ':AVG?' + '\n'
            result = RwcSerialSetup.transceive(self, cmdGetSfAvgDut)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def power_getmindutpower_sf(self, index):
        '''
        Read the minimum DUT power using SF* of all the measured 

        :param index: 7 - 12

        :return: It returns minimum DUT power; NAK on failure
        
        '''
        indexnum = int(index)
        if indexnum >= 7 and indexnum <= 12:
            cmdSfIndex = str(indexnum)
            cmdGetSfMinDut = 'READ:POWER:SF' + cmdSfIndex + ':MIN?' + '\n'
            result = RwcSerialSetup.transceive(self, cmdGetSfMinDut)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def power_getnumofpkts_dut_ch(self, index):
        '''
        Read the number of received packets

        :param index: 0 - 7

        :return: It returns number of packets received; NAK on failure
        
        '''
        indexnum = int(index)
        if indexnum >= 0 and indexnum <= 7:
            cmdChIndex = str(indexnum)
            cmdGetChNumPkts = 'READ:POWER:CH_' + cmdChIndex + ':NUM?' + '\n'
            result = RwcSerialSetup.transceive(self, cmdGetChNumPkts)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def power_getmaxdutpower_ch(self, index):
        '''
        Read the maximum DUT power using CH_* of all the measured

        :param index: 0 - 7

        :return: It returns max DUT power; NAK on failure
        
        '''
        indexnum = int(index)
        if indexnum >= 0 and indexnum <= 7:
            cmdChIndex = str(indexnum)
            cmdGetChMaxDut = 'READ:POWER:CH_' + cmdChIndex + ':MAX?' + '\n'
            result = RwcSerialSetup.transceive(self, cmdGetChMaxDut)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def power_getavgdutpower_ch(self, index):
        '''
        Read the average DUT power using CH_* of all the measured

        :param index: 0 - 7

        :return: It returns average DUT power; NAK on failure
        
        '''
        indexnum = int(index)
        if indexnum >= 0 and indexnum <= 7:
            cmdChIndex = str(indexnum)
            cmdGetChAvgDut = 'READ:POWER:CH_' + cmdChIndex + ':AVG?' + '\n'
            result = RwcSerialSetup.transceive(self, cmdGetChAvgDut)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def power_getmindutpower_ch(self, index):
        '''
        Read the minimum DUT power using CH_* of all the measured

        :param index: 0 - 7

        :return: It returns minimum DUT power; NAK on failure
        
        '''
        indexnum = int(index)
        if indexnum >= 0 and indexnum <= 7:
            cmdChIndex = str(indexnum)
            cmdGetChMinDut = 'READ:POWER:CH_' + cmdChIndex + ':MIN?' + '\n'
            result = RwcSerialSetup.transceive(self, cmdGetChMinDut)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def power_getnumofpkts_dut_rx2(self):
        '''
        Read the number of received packets  

        :Parameters: Query only

        :return: It returns number of packets received; NAK on failure
        
        '''
        cmdGetRxNumPkts = 'READ:POWER:RX2:NUM?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetRxNumPkts)
        return result

    def power_getmaxdutpower_rx2(self):
        '''
        Read the maximum DUT power using RX2 of all the measured 

        :Parameters: Query only

        :return: It returns max DUT power; NAK on failure
        
        '''
        cmdGetRxMaxDut = 'READ:POWER:RX2:MAX?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetRxMaxDut)
        return result

    def power_getavgdutpower_rx2(self):
        '''
        Read the average DUT power using RX2 of all the measured    

        :Parameters: Query only

        :return: It returns average DUT power; NAK on failure
        
        '''
        cmdGetRxAvgDut = 'READ:POWER:RX2:AVG?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetRxAvgDut)
        return result

    def power_getmindutpower_rx2(self):
        '''
        Read the minimum DUT power using RX2 of all the measured 

        :Parameters: Query only

        :return: It returns minimum DUT power; NAK on failure

        '''
        cmdGetRxMinDut = 'READ:POWER:RX2:MIN?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetRxMinDut)
        return result

    def power_run(self):
        '''
        It starts the power measure test.

        :param: Query only

        :return: ACK on success; NAK on failure
        
        '''
        cmdExecPower = 'EXEC:POWER:RUN' + '\n'
        result = RwcSerialSetup.transceive(self, cmdExecPower)
        return result

    def power_stop(self):
        '''
        It stops the power measure test.

        :param: Query only

        :return: ACK on success; NAK on failure
        
        '''
        cmdStopPower = 'EXEC:POWER:STOP' + '\n'
        result = RwcSerialSetup.transceive(self, cmdStopPower)
        return result

    def power_setmode(self, mode):
        '''
        Configure the operating mode of power measure test.

        :param mode: SYNC_TO_LINK, SCENARIO

        :return: ACK on success, NAK on failure
        
        '''
        modelist = ['SYNC_TO_LINK', 'SCENARIO']
        if mode in modelist:
            cmdSetMode = 'CONF:POWER:MODE ' + mode + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMode)
            return result
        else:
            raise Exception('Invalid Power Mode received.')

    def power_getmode(self):
        '''
        Read the operating mode of power measure test.

        :param: Query only

        :return: It returns the mode of power measure test; 
                 NAK on failure
        
        '''
        cmdGetModeValue = 'READ:POWER:MODE? ' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetModeValue)
        return result

    def power_setscenario(self, scenario):
        '''
        Configure the scenario for power measure test.

        :param scenario: NORMAL_UL, CERTI_UL, CERTI_CW

        :return: ACK on success, NAK on failure
        
        '''
        scenariolist = ['NORMAL_UL', 'CERTI_UL', 'CERTI_CW']
        if scenario in scenariolist:
            cmdSetScenario = 'CONF:POWER:SCENARIO ' + scenario + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetScenario)
            return result
        else:
            raise Exception('Invalid Power Scenario received.')

    def power_getscenario(self):
        '''
        Read the scenario for power measure test.

        :param: Query only

        :return: It returns the scenario of power measure test; 
                 NAK on failure
        
        '''
        cmdGetScenarioValue = 'READ:POWER:SCENARIO? ' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetScenarioValue)
        return result

    def power_settargetchmask(self, value):
        '''
        Configure the channel mask value to be used in power 
        measure test. This parameter allows power measure testing 
        for specific channels

        :param value: 0x00 ~ 0xFF

        :return: ACK on success, NAK on failure
        
        '''
        cmdValue = int(value)
        if (value >= 0 and value <= 2**8 - 1):
            cmdHexValue = hex(cmdValue)
            cmdSetTargetChMaskVal = 'CONF:POWER:TARGET_CH_MASK ' \
                                        + cmdHexValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetTargetChMaskVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def power_gettargetchmask(self):
        '''
        Read the channel mask value to be used in power measure test.

        :param: Query only

        :return: It returns the channel mask value of power measure  
                 test; NAK on failure
        
        '''
        cmdGetTargetChMaskValue = 'READ:POWER:TARGET_CH_MASK? ' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetTargetChMaskValue)
        return result

    def power_settargetchmaskopt(self, value):
        '''
        Configure the channel mask value for optional DR for 
        power measurement. 

        :param value: 0x01 ~ 0x80

        :return: ACK on success, NAK on failure
        
        '''
        cmdValue = int(value)
        if (value >= 1 and value <= 2**7):
            cmdHexValue = hex(cmdValue)
            cmdSetTargetChMaskOptVal = 'CONF:POWER:TARGET_CH_MASK_OPT ' \
                                        + cmdHexValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetTargetChMaskOptVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def power_gettargetchmaskopt(self):
        '''
        Read the channel mask value for optional DR for 
        power measurement.

        :param: Query only

        :return: It returns the channel mask value of 
                 power measurement; NAK on failure
        
        '''
        cmdGetTargetChMaskOptValue = 'READ:POWER:TARGET_CH_MASK_OPT? ' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetTargetChMaskOptValue)
        return result

    def power_setadrpower(self, value):
        '''
        Configure the power index value to be used in power measure test

        :param value: 1 ~ 10

        :return: ACK on success, NAK on failure
        
        '''
        
        if (value >= 1 and value <= 10):
            cmdAdrPowerValue = str(value)
            cmdSetAdrPowerVal = 'CONF:POWER:ADR_POWER ' \
                                    + cmdAdrPowerValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetAdrPowerVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def power_getadrpower(self):
        '''
        Read the power index value of power measure test.

        :param: Query only

        :return: It returns the power index value; NAK on failure
        
        '''
        cmdGetAdrPowerValue = 'READ:POWER:ADR_POWER? ' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetAdrPowerValue)
        return result

    def power_setuldatarate(self, datarate):
        '''
        Configure the Data Rate to be used in power measure test

        :param datarate: DR0_SF12BW125, DR1_SF11BW125, DR2_SF10BW125, 
                         DR3_SF9BW125, DR4_SF8BW125, DR5_SF7BW125, 
                         DR6_SF7BW250, DR7_FSK50

        :return: ACK on success, NAK on failure
        
        '''
        cmdUlDr = datarate
        if cmdUlDr == 'DR0_SF12BW125':
            cmdSetUlDr = 'CONF:POWER:UL_DR DR0_SF12BW125' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetUlDr)
            return result
        elif cmdUlDr == 'DR1_SF11BW125':
            cmdSetUlDr = 'CONF:POWER:UL_DR DR1_SF11BW125' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetUlDr)
            return result
        elif cmdUlDr == 'DR2_SF10BW125':
            cmdSetUlDr = 'CONF:POWER:UL_DR DR2_SF10BW125' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetUlDr)
            return result
        elif cmdUlDr == 'DR3_SF9BW125':
            cmdSetUlDr = 'CONF:POWER:UL_DR DR3_SF9BW125' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetUlDr)
            return result
        elif cmdUlDr == 'DR4_SF8BW125':
            cmdSetUlDr = 'CONF:POWER:UL_DR DR4_SF8BW125' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetUlDr)
            return result
        elif cmdUlDr == 'DR5_SF7BW125':
            cmdSetUlDr = 'CONF:POWER:UL_DR DR5_SF7BW125' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetUlDr)
            return result
        elif cmdUlDr == 'DR6_SF7BW250':
            cmdSetUlDr = 'CONF:POWER:UL_DR DR6_SF7BW250' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetUlDr)
            return result
        elif cmdUlDr == 'DR7_FSK50':
            cmdSetUlDr = 'CONF:POWER:UL_DR DR7_FSK50' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetUlDr)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def power_getuldatarate(self):
        '''
        Read the data rate value of power measure test.

        :param: Query only

        :return: It returns the data rate value; NAK on failure
        
        '''
        cmdGetUlDrValue = 'READ:POWER:UL_DR? ' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetUlDrValue)
        return result

    def power_setpacketnum(self, value):
        '''
        Configure the minimum packet number for each channel in 
        power measure test

        :param value: 3 ~ 100

        :return: ACK on success, NAK on failure
        
        '''
    
        if (value >= 3 and value <= 100):
            cmdPktNumValue = str(value)
            cmdSetPktNumVal = 'CONF:POWER:PKT_NUM ' + cmdPktNumValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPktNumVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def power_getpacketnum(self):
        '''
        Read the minimum packet number for each channel in 
        power measure test.

        :param: Query only

        :return: It returns the packet number value; NAK on failure
        
        '''
        cmdGetPktNumValue = 'READ:POWER:PKT_NUM? ' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetPktNumValue)
        return result

    def power_setcwtimeout(self, value):
        '''
        Configure the CW Timeout for CERTI_CW scenario in 
        power measure test

        :param value: 5 ~ 65535

        :return: ACK on success, NAK on failure
        
        '''
    
        if (value >= 5 and value <= 65535):
            cmdTimeoutValue = str(value)
            cmdSetTimeoutVal = 'CONF:POWER:CW_TIMEOUT ' \
                                + cmdTimeoutValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetTimeoutVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def power_getcwtimeout(self):
        '''
        Read the CW Timeout for CERTI_CW scenario in power 
        measure test.

        :param: Query only

        :return: It returns the CW timeout value; NAK on failure
        
        '''
        cmdGetTimeoutValue = 'READ:POWER:CW_TIMEOUT? ' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetTimeoutValue)
        return result

    def power_setcwfrequency(self, value):
        '''
        Configure the CW frequency for CERTI_CW scenario in 
        power measure test

        :param value: 400 ~ 510, 862 ~ 960 MHz

        :return: ACK on success, NAK on failure
        
        '''
    
        if (value >= 400 and value <= 510) or (value >= 862 and value <= 960):
            cmdFreqValue = str(value)
            cmdSetFreqVal = 'CONF:POWER:CW_FREQ ' + cmdFreqValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetFreqVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def power_getcwfrequency(self):
        '''
        Read the CW frequency for CERTI_CW scenario in power 
        measure test.

        :param: Query only

        :return: It returns the CW frequency value; NAK on failure
        
        '''
        cmdGetFrequencyValue = 'READ:POWER:CW_FREQ? ' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetFrequencyValue)
        return result

    def power_setcwpower(self, value):
        '''
        Configure the CW power for CERTI_CW scenario in power measure test

        :param value: 0 ~ 40 dBm

        :return: ACK on success, NAK on failure
        
        '''
    
        if (value >= 0 and value <= 40):
            cmdPowerValue = str(value)
            cmdSetPowerVal = 'CONF:POWER:CW_POW ' + cmdPowerValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPowerVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def power_getcwpower(self):
        '''
        Read the CW power for CERTI_CW scenario in power measure test.

        :param: Query only

        :return: It returns the CW power value; NAK on failure
        
        '''
        cmdGetPowerValue = 'READ:POWER:CW_POW? ' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetPowerValue)
        return result

    def power_cleardata(self):
        '''
        It clears the previous measured values during power measurement 
        and restart measuring.

        :param: Query only

        :return: It returns the CW power value; NAK on failure

    
        .. _sensitivitylabel:    
        '''
        cmdGetPowerValue = 'EXEC:POWER:CLEAR_DATA' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetPowerValue)
        return result

    # Sensitivity Command Methods
    def sensitivity_run(self):
        '''
        Start the sensitivity test

        :param: N/A

        :return: None
        
        '''
        cmdStartSensitivityTest = 'EXEC:SENSITIVITY:RUN' + '\n'
        result = RwcSerialSetup.transceive(self, cmdStartSensitivityTest)
        return result

    def sensitivity_stop(self):
        '''
        Stop the sensitivity test

        :param: N/A

        :return: None
        
        '''
        cmdStopSensitivityTest = 'EXEC:SENSITIVITY:STOP' + '\n'
        result = RwcSerialSetup.transceive(self, cmdStopSensitivityTest)
        return result

    def sensitivity_restart(self):
        '''
        Re-start the sensitivity test without stopping

        :param: N/A

        :return: None
        
        '''
        cmdRestartSensitivityTest = 'EXEC:SENSITIVITY:RESTART' + '\n'
        result = RwcSerialSetup.transceive(self, cmdRestartSensitivityTest)
        return result

    def sensitivity_setopmode(self, opmode):
        '''
        Configure the operating mode for sensitivity test

        :param opmode: mode of operation (CERTI_ECHO, NORMAL_UL)

        :return: ACK on success, NAK on failure
        
        '''
        cmdOperatingMode = opmode
        if cmdOperatingMode == 'CERTI_ECHO':
            cmdSetOperatingMode = 'CONF:SENSITIVITY:SCENARIO CERTI_ECHO' \
                                    + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetOperatingMode)
            return result
        elif cmdOperatingMode == 'NORMAL_UL':
            cmdSetOperatingMode = 'CONF:SENSITIVITY:SCENARIO NORMAL_UL' \
                                    + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetOperatingMode)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def sensitivity_getopmode(self):
        '''
        Read the operating mode for sensitivity test

        :param: N/A (Query only)

        :return: It returns the operating mode; NAK on failure
        
        '''
        cmdGetOperatingMode = 'READ:SENSITIVITY:SCENARIO?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetOperatingMode)
        return result
    
    def sensitivity_setpacketnum(self, packetnum):
        '''
        Configure the number of repetition for each test point

        :param packetnum: Packet repitition value (5 ~ 1000)

        :return: ACK on success, NAK on failure
        
        '''
        if packetnum >= 5 and packetnum <= 1000:
            cmdRepetitionNum = str(packetnum)
            cmdSetRepetitionNum = 'CONF:SENSITIVITY:PACKET_NUM ' \
                                    + cmdRepetitionNum + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRepetitionNum)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def sensitivity_getpacketnum(self):
        '''
        Read the number of repetition for each test point

        :param: N/A (Query only)

        :return: It returns number of packets; NAK on failure
        
        '''
        cmdGetRepetitionNum = 'READ:SENSITIVITY:PACKET_NUM?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetRepetitionNum)
        return result

    def sensitivity_setstartpower(self, power):
        '''
        Configure the start power value

        :param power: Start power value (-10 ~ -143)

        :return: ACK on success, NAK on failure
        
        '''
        if power >= -143 and power <= -10:
            cmdStartPower = str(power)
            cmdSetStartPower = 'CONF:SENSITIVITY:START_POW ' \
            + cmdStartPower + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetStartPower)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def sensitivity_getstartpower(self):
        '''
        Read the start power value

        :param: N/A (Query only)

        :return: It returns the start power value; NAK on failure
        
        '''
        cmdGetStartPower = 'READ:SENSITIVITY:START_POW?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetStartPower)
        return result

    def sensitivity_getstoppower(self):
        '''
        Read the stop power value

        :param: N/A (Query only)

        :return: It returns the stop power value; NAK on failure
        
        '''
        cmdGetStopPower = 'READ:SENSITIVITY:STOP_POW?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetStopPower)
        return result

    def sensitivity_setnumpower(self, power):
        '''
        Configure the number of power values

        :param power: Power value (1 ~ 100)

        :return: ACK on success, NAK on failure
        
        '''
        if power >= 1 and power <= 100:
            cmdNumPower = str(power)
            cmdSetNumPower = 'CONF:SENSITIVITY:NUM_POW ' + cmdNumPower + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetNumPower)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def sensitivity_getnumpower(self):
        '''
        Read the number of power values

        :param: N/A (Query only)

        :return: It returns the number of power value; NAK on failure
        
        '''
        cmdGetNumPower = 'READ:SENSITIVITY:NUM_POW?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetNumPower)
        return result

    def sensitivity_setsteppower(self, power):
        '''
        Configure the step value of power

        :param power: Power step value (1 ~ 20)

        :return: ACK on success, NAK on failure
        
        '''
        if power >= 1 and power <= 20:
            cmdStepPower = str(power)
            cmdSetStepPower = 'CONF:SENSITIVITY:STEP_POW ' \
                                + cmdStepPower + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetStepPower)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def sensitivity_getsteppower(self):
        '''
        Read the step value of power

        :param: N/A (Query only)

        :return: It returns the step power; NAK on failure
        
        '''
        cmdGetStepPower = 'READ:SENSITIVITY:STEP_POW?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetStepPower)
        return result

    def sensitivity_settargetpower(self, value):
        '''
        Configure the value of users target PER

        :param value: Targer power (0 ~ 0.999)

        :return: ACK on success, NAK on failure
        
        '''
        cmdValue = float(value)
        if (cmdValue >= 0.000 and cmdValue <= 0.999):
            cmdPerValue = str(cmdValue)
            cmdSetTargetPer = 'CONF:SENSITIVITY:TARGET_PER ' \
                                + cmdPerValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetTargetPer)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def sensitivity_gettargetpower(self):
        '''
        Read the value of users target PER

        :param: N/A (Query only)

        :return: It returns target PER; NAK on failure
        
        '''
        cmdGetTargetPower = 'READ:SENSITIVITY:TARGET_PER?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetTargetPower)
        return result

    def sensitivity_getcurrentstatus(self):
        '''
        Read the run status of the current test

        :param: N/A (Query only)

        :return: It returns the status of sensitivity test; 
                 NAK on failure
        
        '''
        cmdGetCurrentStatus = 'READ:SENSITIVITY:STATUS?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetCurrentStatus)
        return result
    
    def sensitivity_getprogress(self):
        '''
        Read the progress of sensitivity test

        :param: N/A (Query only)

        :return: It returns the progress of test; NAK on failure
        
        '''
        cmdGetProgress = 'READ:SENSITIVITY:PROGRESS?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetProgress)
        return result

    def sensitivity_getlevel(self):
        '''
        Read the resultant sensitivity level, [dBm]

        :param: N/A (Query only)

        :return: It returns the sensitivity level; NAK on failure
        
        '''
        cmdGetLevel = 'READ:SENSITIVITY:LEVEL?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetLevel)
        return result

    def sensitivity_getresultpervalue(self):
        '''
        Read the resultant PER value at sensitivity level

        :param: N/A (Query only)

        :return: It returns the PER value; NAK on failure
        
        '''
        cmdGetPerVal = 'READ:SENSITIVITY:PER?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetPerVal)
        return result

    def sensitivity_setdownlinkslot(self, slotval):
        '''
        Configure the selection of downlink slot (RX window)

        :param slotval: For EDT, RX1, 
                                 RX2, 
                                 PING (Class B), 
                                 RXC (Class C)
                        For GWT, RX1, 
                                 RX2, 
                                 RX1&RX2

        :return: ACK on success, NAK on failure
        
        '''
        cmdSlotValue = str(slotval)
        if cmdSlotValue == 'RX1':
            cmdSetDownlinkSlot = 'CONF:SENSITIVITY:DOWNLINK_SLOT RX1' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetDownlinkSlot)
            return result
        elif cmdSlotValue == 'RX2':
            cmdSetDownlinkSlot = 'CONF:SENSITIVITY:DOWNLINK_SLOT RX2' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetDownlinkSlot)
            return result
        elif cmdSlotValue == 'RX1&RX2':
            cmdSetDownlinkSlot = 'CONF:SENSITIVITY:DOWNLINK_SLOT RX1&RX2' \
                                    + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetDownlinkSlot)
            return result
        elif cmdSlotValue == 'PING':
            cmdSetDownlinkSlot = 'CONF:SENSITIVITY:DOWNLINK_SLOT PING' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetDownlinkSlot)
            return result
        elif cmdSlotValue == 'RXC':
            cmdSetDownlinkSlot = 'CONF:SENSITIVITY:DOWNLINK_SLOT RXC' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetDownlinkSlot)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def sensitivity_getdownlinkslot(self):
        '''
        Read the selection of downlink slot (RX window)

        :param: N/A (Query only)

        :return: It returns the selected downlink slot; NAK on failure
        
        '''
        cmdGetDownlinkSlot = 'READ:SENSITIVITY:DOWNLINK_SLOT?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetDownlinkSlot)
        return result

    def sensitivity_settargetchmask(self, value):
        '''
        Configure the mask value to be used in Sensitivity test.

        :param value: 0x01 ~ 0xFF

        :return: ACK on success, NAK on failure
        
        '''
        cmdValue = int(value)
        if (cmdValue >= 1 and cmdValue <= 2**8 - 1):
            cmdHexValue = hex(cmdValue)
            cmdSetTargetChMask = 'CONF:SENSITIVITY:TARGET_CH_MASK ' \
            + cmdHexValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetTargetChMask)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def sensitivity_gettargetchmask(self):
        '''
        Read the mask value to be used in Sensitivity test.

        :param: Query only

        :return: It returns the mask value to be used in 
                 Sensitivity test; NAK on failure
        
        '''
        cmdGetTargetChMask = 'READ:SENSITIVITY:TARGET_CH_MASK?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetTargetChMask)
        return result

    def sensitivity_settargetchmaskopt(self, value):
        '''
        Configure the channel mask value for optional DR for 
        sensitivity test. 

        :param value: 0x01 ~ 0x80

        :return: ACK on success, NAK on failure
        
        '''
        cmdValue = int(value)
        if (value >= 1 and value <= 2**7):
            cmdHexValue = hex(cmdValue)
            cmdSetTargetChMaskOptVal = 'CONF:SENSITIVITY:TARGET_CH_MASK_OPT ' \
                                        + cmdHexValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetTargetChMaskOptVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def sensitivity_gettargetchmaskopt(self):
        '''
        Read the channel mask value for optional DR for 
        sensitivity test.

        :param: Query only

        :return: It returns the channel mask value; NAK on failure
        
        '''
        cmdGetTargetChMaskOptValue = 'READ:SENSITIVITY:TARGET_CH_MASK_OPT? ' \
                                        + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetTargetChMaskOptValue)
        return result

    def sensitivity_settargetdr(self, drvalue):
        '''
        Configure the DR value to be used in sensitivity test

        :param drvalue: DR0_SF12BW125, DR1_SF11BW125, DR2_SF10BW125, 
                        DR3_SF9BW125, DR4_SF8BW125, DR5_SF7BW125

        :return: ACK on success, NAK on failure
        
        '''
        drvallist = [
            'DR0_SF12BW125', 
            'DR1_SF11BW125', 
            'DR2_SF10BW125', 
            'DR3_SF9BW125', 
            'DR4_SF8BW125', 
            'DR5_SF7BW125'
            ]

        if drvalue in drvallist:
            cmdSetTargetDr = 'CONF:SENSITIVITY:TARGET_DR ' + drvalue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetTargetDr)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def sensitivity_gettargetdr(self):
        '''
        Read the DR value to be used in sensitivity test

        :param: Query only

        :return: It returns the DR value to be used in sensitivity test; 
                 NAK on failure
        
        '''
        cmdGetTargetDr = 'READ:SENSITIVITY:TARGET_DR?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetTargetDr)
        return result

    def sensitivity_settargetdlch(self, chnum, freq):
        '''
        Configure the Downlink frequency channel to be used in 
        sensitivity test

        :param chnum: Channel number
        :param freq: 400 ~ 510, 862 ~ 960 MHz

        :return: ACK on success, NAK on failure
        
        '''
        cmdChNum = str(chnum)
        if (freq >= 400 and freq <= 510) or (freq >= 862 
                and freq <= 960):
            cmdChFrequency = str(freq)
            cmdSetTargetDlChFrequencyVal = 'CONF:SENSITIVITY:TARGET_DL_CH ' \
                                            + cmdChNum + ' ' \
                                            + cmdChFrequency + '\n'
            result = RwcSerialSetup.transceive(
                self, 
                cmdSetTargetDlChFrequencyVal)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def sensitivity_gettargetdlch(self, chnum):
        '''
        Read the Downlink frequency channel to be used in 
        sensitivity test

        :param chnum: Channel Number

        :return: It returns the downlink channel frequency value; 
                 NAK on failure
        
        '''
        cmdChNum = str(chnum)
        cmdGetTargetDlChFreq = 'READ:SENSITIVITY:TARGET_DL_CH? ' \
                                + cmdChNum + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetTargetDlChFreq)
        return result

    def sensitivity_setpayloadtype(self, msgtype):
        '''
        Configure the Message type of user-defined MAC command

        :param msgtype: MAC Command Message type 
                        (0000_0000, 1111_1111, 1111_0000, 
                        1010_1010, PRBS, USER)

        :return: ACK on success, NAK on failure
        
        '''
        cmdPayloadType = msgtype
        if cmdPayloadType == '0000_0000':
            cmdSetPayloadType = 'CONF:SENSITIVITY:PAYLOAD_TYPE 0000_0000' \
                                    + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPayloadType)
            return result
        elif cmdPayloadType == '1111_1111':
            cmdSetPayloadType = 'CONF:SENSITIVITY:PAYLOAD_TYPE 1111_1111' \
                                    + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPayloadType)
            return result
        elif cmdPayloadType == '1111_0000':
            cmdSetPayloadType = 'CONF:SENSITIVITY:PAYLOAD_TYPE 1111_0000' \
                                    + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPayloadType)
            return result
        elif cmdPayloadType == '1010_1010':
            cmdSetPayloadType = 'CONF:SENSITIVITY:PAYLOAD_TYPE 1010_1010' \
                                    + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPayloadType)
            return result
        elif cmdPayloadType == 'PRBS':
            cmdSetPayloadType = 'CONF:SENSITIVITY:PAYLOAD_TYPE PRBS' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPayloadType)
            return result
        elif cmdPayloadType == 'USER':
            cmdSetPayloadType = 'CONF:SENSITIVITY:PAYLOAD_TYPE USER' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPayloadType)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def sensitivity_getpayloadtype(self):
        '''
        Read the Message type of user-defined MAC command

        :param: N/A (Query only)

        :return: It returns the payload type; NAK on failure
        
        '''
        cmdGetPayloadType = 'READ:SENSITIVITY:PAYLOAD_TYPE?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetPayloadType)
        return result

    def sensitivity_setfport(self, fport):
        '''
        Configure the FPORT of user-defined MAC command

        :param fport: port number (1 ~ 255)

        :return: ACK on success, NAK on failure
        
        '''
        if fport >= 1 and fport <= 255:
            cmdFport = str(fport)
            cmdSetFport = 'CONF:SENSITIVITY:FPORT ' + cmdFport + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetFport)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def sensitivity_getfport(self):
        '''
        Read the FPORT of user-defined MAC command

        :param: N/A (Query only)

        :return: It returns the fport value; NAK on failure
        
        '''
        cmdGetFport = 'READ:SENSITIVITY:FPORT?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetFport)
        return result

    def sensitivity_setpayloadsize(self, length):
        '''
        Configure the Message length in byte of user-defined 
        MAC command

        :param length: MAC Command Message length (1 ~ 128)

        :return: ACK on success, NAK on failure
        
        '''
        if length >= 1 and length <= 128:
            cmdMsgLength = str(length)
            cmdSetMsgLength = 'CONF:SENSITIVITY:PAYLOAD_SIZE ' \
                                + cmdMsgLength + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMsgLength)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def sensitivity_getpayloadsize(self):
        '''
        Read the Message length in byte of user-defined MAC command

        :param: N/A (Query only)

        :return: It returns the payload length; NAK on failure
        
        '''
        cmdGetMsgLength = 'READ:SENSITIVITY:PAYLOAD_SIZE?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMsgLength)
        return result

    def sensitivity_setpayload(self, data):
        '''
        Configure the Message data of user-defined MAC command

        :param data: Payload data (128-byte HEX value)

        :return: ACK on success, NAK on failure
        
        '''
        cmdData = int(data)
        if (cmdData >= 0 and cmdData <= 2**128 - 1) :
            cmdHexValue = hex(cmdData)
            cmdSetPayload = 'CONF:SENSITIVITY:PAYLOAD ' + cmdHexValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPayload)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def sensitivity_getpayload(self):
        '''
        Read the Message data of user-defined MAC command

        :param: N/A (Query only)

        :return: It returns the payload data; NAK on failure
        
        '''
        cmdGetMsgData = 'READ:SENSITIVITY:PAYLOAD?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMsgData)
        return result

    def sensitivity_setrx2frequency(self):
        '''
        Configure the RX2 Frequency for RX2 channel sensitivity test

        :param: 128-byte HEX value

        :return: ACK on success, NAK on failure
        
        '''
        pass

    def sensitivity_getrx2frequency(self):
        '''
        Read the RX2 Frequency for RX2 channel sensitivity test

        :param: N/A (Query only)

        :return: It returns the RX2 frequency value; NAK on failure


        .. _nstlabel:
        '''
        cmdGetRxFrequency = 'READ:SENSITIVITY:RX2_FREQ?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetRxFrequency)
        return result

    # NST Command Methods
    def nst_tx_run(self):
        '''
        Run the Signal Generator to transmit test packets to DUT

        :Parameters: N/A

        :return: None

        '''
        cmdStartTx = 'EXEC:NST:TX:RUN' + '\n'
        result = RwcSerialSetup.transceive(self, cmdStartTx)
        return result

    def nst_tx_stop(self):
        '''
        Stop the Signal Generator

        :Parameters: N/A

        :return: None
        
        '''
        cmdStopTx = 'EXEC:NST:TX:STOP' + '\n'
        result = RwcSerialSetup.transceive(self, cmdStopTx)
        return result

    def nst_tx_clear(self):
        '''
        Clear previous measured data

        :Parameters: N/A

        :return: None
        
        '''
        cmdClearTx = 'EXEC:NST:TX:CLEAR' + '\n'
        result = RwcSerialSetup.transceive(self, cmdClearTx)
        return result
    
    def nst_tx_status(self):
        '''
        Read number of packets transmitted after started. It will 
        return IDLE if not started

        :Parameters: N/A

        :return: It returns status message; NAK on failure
        
        '''
        cmdStatusTx = 'READ:NST:TX:STATUS?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdStatusTx)
        return result

    def nst_tx_setrepeatnum(self, num):
        '''
        Configure the number of repetition; 0 means infinite 
        transmission

        :param num: 0 ~ 10000

        :return: ACK on success, NAK on failure
        
        '''
        if num >= 0 and num <= 10000:
            cmdRepeatNum = str(num)
            cmdSetRepeatNum = 'CONF:NST:TX:REPEAT_NUM ' + cmdRepeatNum + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRepeatNum)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def nst_tx_getrepeatnum(self):
        '''
        Read the number of repetition; 0 means infinite transmission

        :Parameters: Query only

        :return: It returns the repetition number; NAK on failure
        
        '''
        cmdGetRepeatNum = 'READ:NST:TX:REPEAT_NUM?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetRepeatNum)
        return result

    def nst_tx_setmode(self, mode):
        '''
        Configure the TX mode of Non-signaling test

        :param mode: LORA, FSK, CW

        :return: ACK on success, NAK on failure
        
        '''
        cmdTxMode = mode
        if cmdTxMode == 'LORA':
            cmdSetTxMode = 'CONF:NST:TX:MODULATION LORA' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetTxMode)
            return result
        elif cmdTxMode == 'FSK':
            cmdSetTxMode = 'CONF:NST:TX:MODULATION FSK' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetTxMode)
            return result
        elif cmdTxMode == 'CW':
            cmdSetTxMode = 'CONF:NST:TX:MODULATION CW' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetTxMode)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def nst_tx_getmode(self):
        '''
        Read the TX mode of Non-signaling test

        :Parameters: Query only

        :return: It returns NST TX mode; NAK on failure
        
        '''
        cmdGetTxMode = 'READ:NST:TX:MODE?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetTxMode)
        return result

    def nst_tx_setinterval(self, value):
        '''
        Configure the interval in sec between consecutive LoRa TX frames

        :param value: 0.01 ~ 1000

        :return: ACK on success, NAK on failure
        
        '''
        cmdValue = float(value)
        if (cmdValue >= 0.01 and cmdValue <= 1000.00):
            cmdIntervalValue = str(cmdValue)
            cmdSetInterval = 'CONF:NST:TX:INTERVAL ' + cmdIntervalValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetInterval)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def nst_tx_getinterval(self):
        '''
        Read the interval in sec between consecutive LoRa TX frames

        :Parameters: Query only

        :return: It returns the NST TX interval; NAK on failure
        
        '''
        cmdGetTxInterval = 'READ:NST:TX:INTERVAL?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetTxInterval)
        return result

    def nst_tx_setbw(self, bw):
        '''
        Configure the BW of LoRa TX frame

        :param bw: 500, 250, 125

        :return: ACK on success, NAK on failure
        
        '''
        if (bw == 500) or (bw == 250) or (bw == 125):
            cmdTxBw = str(bw)
            cmdSetTxBw = 'CONF:NST:TX:BW ' + cmdTxBw + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetTxBw)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def nst_tx_getbw(self):
        '''
        Read the BW of LoRa TX frame

        :Parameters: Query only

        :return: It returns the TX bandwidth; NAK on failure
        
        '''
        cmdGetTxBw = 'READ:NST:TX:BW?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetTxBw)
        return result

    def nst_tx_setsf(self, index):
        '''
        Configure the Spreading Factor of LoRa TX frame

        :param index: SF7, SF8, SF9, SF10, SF11, SF12

        :return: ACK on success, NAK on failure
        
        '''
        sflist = ['SF7', 'SF8', 'SF9', 'SF10', 'SF11', 'SF12']
        if index in sflist:
            cmdSetTxSf = 'CONF:NST:TX:SF ' + index + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetTxSf)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def nst_tx_getsf(self):
        '''
        Read the Spreading Factor of LoRa TX frame

        :Parameters: Query only

        :return: It returns TX Spreading Factor; NAK on failure
        
        '''
        cmdGetTxSf = 'READ:NST:TX:SF?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetTxSf)
        return result

    def nst_tx_setcr(self, codingrate):
        '''
        Configure the Coding Rate of LoRa TX frame

        :param codingrate: 4_5, 4_6, 4_7, 4_8, NO_CRC

        :return: ACK on success, NAK on failure
        
        '''
        cmdTxCodingRate = codingrate
        if cmdTxCodingRate == '4_5':
            cmdSetTxCodingRate = 'CONF:NST:TX:CR 4_5' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetTxCodingRate)
            return result
        elif cmdTxCodingRate == '4_6':
            cmdSetTxCodingRate = 'CONF:NST:TX:CR 4_6' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetTxCodingRate)
            return result
        elif cmdTxCodingRate == '4_7':
            cmdSetTxCodingRate = 'CONF:NST:TX:CR 4_7' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetTxCodingRate)
            return result
        elif cmdTxCodingRate == '4_8':
            cmdSetTxCodingRate = 'CONF:NST:TX:CR 4_8' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetTxCodingRate)
            return result
        elif cmdTxCodingRate == 'NO_CRC':
            cmdSetTxCodingRate = 'CONF:NST:TX:CR NO_CRC' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetTxCodingRate)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def nst_tx_getcr(self):
        '''
        Read the Coding Rate of LoRa TX frame

        :Parameters: Query only

        :return: It returns TX Coding rate; NAK on failure
        
        '''
        cmdGetTxCodingRate = 'READ:NST:TX:CR?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetTxCodingRate)
        return result

    def nst_tx_setpreamblesize(self, preamblesize):
        '''
        Configure the preamble size of LoRa TX frame

        :param preamblesize: 2 ~ 12

        :return: ACK on success, NAK on failure
        
        '''
        if preamblesize >= 2 and preamblesize <= 12:
            cmdPreambleSize = str(preamblesize)
            cmdSetTxPreambleSize = 'CONF:NST:TX:PREAMBLE_SIZE ' \
            + cmdPreambleSize + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetTxPreambleSize)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def nst_tx_getpreamblesize(self):
        '''
        Read the preamble size of LoRa TX frame

        :Parameters: Query only

        :return: It returns the preamble size; NAK on failure
        
        '''
        cmdGetTxPreambleSize = 'READ:NST:TX:PREAMBLE_SIZE?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetTxPreambleSize)
        return result

    def nst_tx_setpayloadtype(self, msgtype):
        '''
        Configure the Payload type of LoRa TX frame

        :param msgtype: 0000_0000, 1111_1111, 1111_0000, 
                        1010_1010, PRBS, USER

        :return: ACK on success, NAK on failure
        
        '''
        cmdPayloadType = msgtype
        if cmdPayloadType == '0000_0000':
            cmdSetPayloadType = 'CONF:NST:TX:PAYLOAD_TYPE 0000_0000' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPayloadType)
            return result
        elif cmdPayloadType == '1111_1111':
            cmdSetPayloadType = 'CONF:NST:TX:PAYLOAD_TYPE 1111_1111' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPayloadType)
            return result
        elif cmdPayloadType == '1111_0000':
            cmdSetPayloadType = 'CONF:NST:TX:PAYLOAD_TYPE 1111_0000' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPayloadType)
            return result
        elif cmdPayloadType == '1010_1010':
            cmdSetPayloadType = 'CONF:NST:TX:PAYLOAD_TYPE 1010_1010' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPayloadType)
            return result
        elif cmdPayloadType == 'PRBS':
            cmdSetPayloadType = 'CONF:NST:TX:PAYLOAD_TYPE PRBS' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPayloadType)
            return result
        elif cmdPayloadType == 'USER':
            cmdSetPayloadType = 'CONF:NST:TX:PAYLOAD_TYPE USER' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPayloadType)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def nst_tx_getpayloadtype(self):
        '''
        Read the Payload type of LoRa TX frame

        :Parameters: Query only

        :return: It returns the payload type; NAK on failure
        
        '''
        cmdGetTxPayloadType = 'READ:NST:TX:PAYLOAD_TYPE?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetTxPayloadType)
        return result

    def nst_tx_setpayloadsize(self, length):
        '''
        Configure the Payload size of LoRa TX frame

        :param length: 8 ~ 256

        :return: ACK on success, NAK on failure
        
        '''
        if length >= 8 and length <= 256:
            cmdMsgLength = str(length)
            cmdSetMsgLength = 'CONF:SENSITIVITY:PAYLOAD_SIZE ' \
                                + cmdMsgLength + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMsgLength)
            return result
        else:
            raise Exception('Invalid parameter received.')
    
    def nst_tx_getpayloadsize(self):
        '''
        Read the Payload size of LoRa TX frame

        :Parameters: Query only

        :return: It returns the payload size; NAK on failure
        
        '''
        cmdGetTxPayloadSize = 'READ:NST:TX:PAYLOAD_SIZE?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetTxPayloadSize)
        return result

    def nst_tx_setpayload(self, data):
        '''
        Configure the Payload data of LoRa TX frame

        :param data: 128-byte HEX value

        :return: ACK on success, NAK on failure
        
        '''
        cmdData = int(data)
        if (cmdData >= 0 and cmdData <= 2**128 -1) :
            cmdHexValue = hex(cmdData)
            cmdSetPayload = 'CONF:NST:TX:PAYLOAD ' + cmdHexValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPayload)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def nst_tx_getpayload(self):
        '''
        Read the Payload data of LoRa TX frame

        :Parameters: Query only

        :return: It returns the payload data; NAK on failure
        
        '''
        cmdGetTxPayloadData = 'READ:NST:TX:PAYLOAD?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetTxPayloadData)
        return result

    def nst_tx_setnwktype(self, nwktype):
        '''
        Configure the Sync word in LoRa modulation:

        * 0x12 for private network
        * 0x34 for public network

        :param nwktype: PRIVATE, PUBLIC

        :return: ACK on success, NAK on failure
        
        '''
        cmdNwkType = nwktype
        if cmdNwkType == 'PRIVATE':
            cmdSetTxNwkType = 'CONF:NST:TX:NETWORK PRIVATE' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetTxNwkType)
            return result
        elif cmdNwkType == 'PUBLIC':
            cmdSetTxNwkType = 'CONF:NST:TX:NETWORK PUBLIC' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetTxNwkType)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def nst_tx_getnwktype(self):
        '''
        Read the Sync word in LoRa modulation:

        * 0x12 for private network
        * 0x34 for public network

        :Parameters: Query only

        :return: It returns the network type; NAK on failure
        
        '''
        cmdGetTxNwkType = 'READ:NST:TX:NETWORK?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetTxNwkType)
        return result

    def nst_tx_setfmdeviation(self, value):
        '''
        Configure the FM deviation value for FSK Modulation

        :param value: 10 ~ 100 kHz

        :return: ACK on success, NAK on failure

        '''
        cmdValue = int(value)
        if (cmdValue >= 10 and cmdValue <= 100):
            cmdParam = str(cmdValue)
            cmdSetFmDeviation = 'CONF:NST:TX:FM_DEVIATION ' + cmdParam + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetFmDeviation)
            return result
        else:
            raise Exception('Invalid Parameter received.')

    def nst_tx_getfmdeviation(self):
        '''
        Read the FM deviation value for FSK Modulation

        :Parameters: Query only

        :return: It returns FM deviation value; NAK on failure
        
        '''
        cmdGetFmDeviation = 'CONF:NST:TX:FM_DEVIATION?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetFmDeviation)
        return result

    def nst_tx_setdatarate(self, value):
        '''
        Configure the Data rate value for FSK Modulation

        :param value: 1 ~ 128 kHz

        :return: ACK on success, NAK on failure

        '''
        cmdValue = int(value)
        if (cmdValue >= 1 and cmdValue <= 128):
            cmdParam = str(cmdValue)
            cmdSetDatarate = 'CONF:NST:TX:DATA_RATE ' + cmdParam + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetDatarate)
            return result
        else:
            raise Exception('Invalid Parameter received.')

    def nst_tx_getdatarate(self):
        '''
        Read the Data rate value for FSK Modulation

        :Parameters: Query only

        :return: It returns Data rate value; NAK on failure
        
        '''
        cmdGetDatarate = 'CONF:NST:TX:DATA_RATE?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetDatarate)
        return result

    def nst_tx_setsyncwordsize(self, sizevalue):
        '''
        Configure the Sync Word size for FSK Modulation

        :param sizevalue: 1 ~ 8 byte

        :return: ACK on success, NAK on failure

        '''
        cmdValue = int(sizevalue)
        if (cmdValue >= 1 and cmdValue <= 8):
            cmdParam = str(cmdValue)
            cmdSetSyncWordSize = 'CONF:NST:TX:SYNC_WORD_SIZE ' \
                                    + cmdParam + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetSyncWordSize)
            return result
        else:
            raise Exception('Invalid Parameter received.')

    def nst_tx_getsyncwordsize(self):
        '''
        Read the Sync Word size for FSK Modulation

        :Parameters: Query only

        :return: It returns Sync Word size; NAK on failure
        
        '''
        cmdGetSyncWordSize = 'CONF:NST:TX:SYNC_WORD_SIZE?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetSyncWordSize)
        return result

    def nst_tx_setsyncword(self, value):
        '''
        Configure the Sync Word for FSK Modulation

        :param value: -

        :return: ACK on success, NAK on failure

        '''
        cmdValue = int(value)
        if (cmdValue >= 1 and cmdValue <= 8):
           cmdParam = str(cmdValue)
           cmdSetSyncWord = 'CONF:NST:TX:SYNC_WORD ' + cmdParam + '\n'
           result = RwcSerialSetup.transceive(self, cmdSetSyncWord)
           return result
        else:
           raise Exception('Invalid Parameter received.')

    def nst_tx_getsyncword(self):
        '''
        Read the Sync Word for FSK Modulation

        :Parameters: Query only

        :return: It returns Sync Word; NAK on failure
        
        '''
        cmdGetSyncWord = 'CONF:NST:TX:SYNC_WORD?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetSyncWord)
        return result

    def nst_tx_setpolarity(self, polaritytype):
        '''
        Configure the TX signal polarity for FSK Modulation

        :param polaritytype: NORMAL, INVERSE

        :return: ACK on success, NAK on failure

        '''
        polaritytypelist = ['NORMAL', 'INVERSE']
        if polaritytype in polaritytypelist:
            cmdSetTxPolarity = 'CONF:NST:TX:TX_POLARITY ' \
                                + polaritytype + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetTxPolarity)
            return result
        else:
            raise Exception('Invalid Parameter received.')

    def nst_tx_getpolarity(self):
        '''
        Read the TX signal polarity for FSK Modulation

        :Parameters: Query only

        :return: It returns TX signal polarity; NAK on failure
        
        '''
        cmdGetTxPolarity = 'CONF:NST:TX:TX_POLARITY?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetTxPolarity)
        return result

    def nst_tx_setduttype(self, duttype):
        '''
        Configure the DUT Type for TX NST test 
        (RWC supported version: v1.15 - v1.21)

        :param duttype: END_DEVICE, GATEWAY, UNKNOWN

        :return: ACK on success, NAK on failure

        '''
        duttypelist = ['END_DEVICE', 'GATEWAY', 'UNKNOWN']
        cmdSupportedVersion = [
            '1.150', '1.160', 
            '1.170', '1.200', 
            '1.203', '1.204', 
            '1.206', '1.210']
        verStatus = self.validate_sys_swversion(cmdSupportedVersion)

        if verStatus and duttype in duttypelist:
            cmdSetDutType = 'CONF:NST:TX:DUT_TYPE ' + duttype + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetDutType)
            return result
        else:
            raise Exception('Invalid Parameter received.')

    def nst_tx_getduttype(self):
        '''
        Read the DUT Type for TX NST test 
        (RWC supported version: v1.15 - v1.21)

        :Parameters: Query only

        :return: It returns DUT type; NAK on failure
        
        '''
        cmdSupportedVersion = [
            '1.150', '1.160', 
            '1.170', '1.200', 
            '1.203', '1.204', 
            '1.206', '1.210']
        verStatus = self.validate_sys_swversion(cmdSupportedVersion)

        if verStatus:
            cmdGetDutType = 'CONF:NST:TX:DUT_TYPE?' + '\n'
            result = RwcSerialSetup.transceive(self, cmdGetDutType)
            return result

    def nst_rx_run(self):
        '''
        Run the Signal Analyzer to receive test packets from DUT

        :Parameters: N/A

        :return: None
        
        '''
        cmdStartRx = 'EXEC:NST:RX:RUN' + '\n'
        result = RwcSerialSetup.transceive(self, cmdStartRx)
        return result

    def nst_rx_stop(self):
        '''
        Stop the Signal Analyzer

        :Parameters: N/A

        :return: None
        
        '''
        cmdStopRx = 'EXEC:NST:RX:STOP' + '\n'
        result = RwcSerialSetup.transceive(self, cmdStopRx)
        return result

    def nst_rx_clear(self):
        '''
        Clear previous measured data

        :Parameters: N/A

        :return: None
        
        '''
        cmdClearRx = 'EXEC:NST:RX:CLEAR' + '\n'
        result = RwcSerialSetup.transceive(self, cmdClearRx)
        return result

    def nst_rx_setmode(self, mode):
        '''
        Configure the RX mode of Non-signaling test

        :param mode: LORA, FSK

        :return: ACK on success, NAK on failure
        
        '''
        cmdRxMode = mode
        if cmdRxMode == 'LORA':
            cmdSetRxMode = 'CONF:NST:RX:MODE LORA' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRxMode)
            return result
        elif cmdRxMode == 'FSK':
            cmdSetRxMode = 'CONF:NST:RX:MODE FSK' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRxMode)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def nst_rx_getmode(self):
        '''
        Read the RX mode of Non-signaling test

        :Parameters: Query only

        :return: It returns RX mode; NAK on failure
        
        '''
        cmdGetRxMode = 'READ:NST:RX:MODE?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetRxMode)
        return result

    def nst_rx_setbw(self, bw):
        '''
        Configure the BW in MHz of LoRa RX frame

        :param bw: 500, 250, 125

        :return: ACK on success, NAK on failure
        
        '''
        if (bw == 500) or (bw == 250) or (bw == 125):
            cmdRxBw = str(bw)
            cmdSetRxBw = 'CONF:NST:RX:BW ' + cmdRxBw + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRxBw)
            return result
        else:
            raise Exception('Invalid parameter received.')
    
    def nst_rx_getbw(self):
        '''
        Read the BW in MHz of LoRa RX frame

        :Parameters: Query only

        :return: It returns RX Bandwidth; NAK on failure
        
        '''
        cmdGetRxBw = 'READ:NST:RX:BW?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetRxBw)
        return result

    def nst_rx_setsf(self, index):
        '''
        Configure the Spreading Factor of LoRa RX frame

        :param index: SF7, SF8, SF9, SF10, SF11, SF12

        :return: ACK on success, NAK on failure
        
        '''
        #cmdSfIndex = int(index)
        sflist = [
            'SF7', 
            'SF8', 
            'SF9', 
            'SF10', 
            'SF11', 
            'SF12', 
            'ANY']
        if index in sflist:
            cmdSetRxSf = 'CONF:NST:RX:SF ' + index + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRxSf)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def nst_rx_getsf(self):
        '''
        Read the Spreading Factor of LoRa RX frame

        :Parameters: Query only

        :return: It returns RX spreading factor; NAK on failure
        
        '''
        cmdGetRxSf = 'READ:NST:RX:SF?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetRxSf)
        return result

    def nst_rx_setnwktype(self, nwktype):
        '''
        Configure the Sync word in LoRa modulation:

        * 0x12 for private network
        * 0x34 for public network

        :param nwktype: PRIVATE, PUBLIC

        :return: ACK on success, NAK on failure
        
        '''
        cmdNwkType = nwktype
        if cmdNwkType == 'PRIVATE':
            cmdSetRxNwkType = 'CONF:NST:RX:NETWORK PRIVATE' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRxNwkType)
            return result
        elif cmdNwkType == 'PUBLIC':
            cmdSetRxNwkType = 'CONF:NST:RX:NETWORK PUBLIC' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRxNwkType)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def nst_rx_getnwktype(self):
        '''
        Read the Sync word in LoRa modulation:

        * 0x12 for private network
        * 0x34 for public network

        :Parameters: Query only

        :return: It returns RX network type; NAK on failure
        
        '''
        cmdGetRxNwkType = 'READ:NST:RX:NETWORK?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetRxNwkType)
        return result

    def nst_rx_setpreamblesize(self, preamblesize):
        '''
        Configure the preamble size of LoRa RX frame

        :param preamblesize: 2 ~ 12

        :return: ACK on success, NAK on failure
        
        '''
        if preamblesize >= 2 and preamblesize <= 12:
            cmdPreambleSize = str(preamblesize)
            cmdSetRxPreambleSize = 'CONF:NST:RX:PREAMBLE_SIZE ' \
            + cmdPreambleSize + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRxPreambleSize)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def nst_rx_getpreamblesize(self):
        '''
        Read the preamble size of LoRa RX frame

        :Parameters: Query only

        :return: It returns the preamble size; NAK on failure
        
        '''
        cmdGetRxPreambleSize = 'READ:NST:RX:PREAMBLE_SIZE?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetRxPreambleSize)
        return result

    def nst_rx_setcr(self, codingrate):
        '''
        Configure the Coding Rate of LoRa RX frame

        :param codingrate: 4_5, 4_6, 4_7, 4_8, NO_CRC

        :return: ACK on success, NAK on failure
        
        '''
        cmdRxCodingRate = codingrate
        if cmdRxCodingRate == '4_5':
            cmdSetRxCodingRate = 'CONF:NST:RX:CR 4_5' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRxCodingRate)
            return result
        elif cmdRxCodingRate == '4_6':
            cmdSetRxCodingRate = 'CONF:NST:RX:CR 4_6' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRxCodingRate)
            return result
        elif cmdRxCodingRate == '4_7':
            cmdSetRxCodingRate = 'CONF:NST:RX:CR 4_7' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRxCodingRate)
            return result
        elif cmdRxCodingRate == '4_8':
            cmdSetRxCodingRate = 'CONF:NST:RX:CR 4_8' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRxCodingRate)
            return result
        elif cmdRxCodingRate == 'NO_CRC':
            cmdSetRxCodingRate = 'CONF:NST:RX:CR NO_CRC' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRxCodingRate)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def nst_rx_getcr(self):
        '''
        Read the Coding Rate of LoRa RX frame

        :Parameters: Query only

        :return: It returns RX Coding rate; NAK on failure
        
        '''
        cmdGetRxCodingRate = 'READ:NST:RX:CR?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetRxCodingRate)
        return result

    def nst_rx_getnumofpkts_dut(self):
        '''
        Read the number of received packets of all the measured

        :Parameters: Query only

        :return: It returns RX number of received packets; 
                 NAK on failure
        
        '''
        cmdGetRxNumPkts = 'READ:NST:RX:POW_NUM?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetRxNumPkts)
        return result

    def nst_rx_getmaxdutpower(self):
        '''
        Read the number of the maximum DUT power of all the measured

        :Parameters: Query only

        :return: It returns RX max DUT power
        
        '''
        cmdGetRxMaxPow = 'READ:NST:RX:POW_MAX?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetRxMaxPow)
        return result

    def nst_rx_getavgdutpower(self):
        '''
        Read the number of the average DUT power of all the measured

        :Parameters: Query only

        :return: It returns RX average DUT power; NAK on failure
        
        '''
        cmdGetRxAvgPow = 'READ:NST:RX:POW_AVG?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetRxAvgPow)
        return result

    def nst_rx_getmindutpower(self):
        '''
        Read the number of the minimum DUT power of all the measured

        :Parameters: Query only

        :return: It returns RX minimum DUT power; NAK on failure
        
        '''
        cmdGetRxMinPow = 'READ:NST:RX:POW_MIN?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetRxMinPow)
        return result

    def nst_rx_getcwpow(self):
        '''
        Read RX Power value

        :Parameters: Query only

        :return: It returns RX power; NAK on failure
        
        '''
        cmdGetRxCwPow = 'READ:NST:RX:CW_POW?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetRxCwPow)
        return result

    def nst_rx_getcwfreq(self):
        '''
        Read RX Frequency value

        :Parameters: Query only

        :return: It returns RX frequency value; NAK on failure
        
        '''
        cmdGetRxCwPow = 'READ:NST:RX:CW_FREQ?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetRxCwPow)
        return result

    def nst_rx_setdatarate(self, value):
        '''
        Configure the Data rate value for FSK Modulation

        :param value: 1 ~ 128 kHz

        :return: ACK on success, NAK on failure

        '''
        cmdValue = int(value)
        if (cmdValue >= 1 and cmdValue <= 128):
            cmdParam = str(cmdValue)
            cmdSetDatarate = 'CONF:NST:RX:DATA_RATE ' + cmdParam + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetDatarate)
            return result
        else:
            raise Exception('Invalid Parameter received.')

    def nst_rx_getdatarate(self):
        '''
        Read the Data rate value for FSK Modulation

        :Parameters: Query only

        :return: It returns Data rate value; NAK on failure
        
        '''
        cmdGetDatarate = 'CONF:NST:RX:DATA_RATE?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetDatarate)
        return result

    def nst_rx_setsyncwordsize(self, sizevalue):
        '''
        Configure the Sync Word size for FSK Modulation

        :param sizevalue: 1 ~ 8 byte

        :return: ACK on success, NAK on failure

        '''
        cmdValue = int(sizevalue)
        if (cmdValue >= 1 and cmdValue <= 8):
            cmdParam = str(cmdValue)
            cmdSetSyncWordSize = 'CONF:NST:RX:SYNC_WORD_SIZE ' \
                                    + cmdParam + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetSyncWordSize)
            return result
        else:
            raise Exception('Invalid Parameter received.')

    def nst_rx_getsyncwordsize(self):
        '''
        Read the Sync Word size for FSK Modulation

        :Parameters: Query only

        :return: It returns Sync Word size; NAK on failure
        
        '''
        cmdGetSyncWordSize = 'CONF:NST:RX:SYNC_WORD_SIZE?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetSyncWordSize)
        return result

    def nst_rx_setsyncword(self, sizevalue):
        '''
        Configure the Sync Word for FSK Modulation

        :param value: -

        :return: ACK on success, NAK on failure

        '''
        cmdValue = int(sizevalue)
        if (cmdValue >= 1 and cmdValue <= 8):
           cmdParam = str(cmdValue)
           cmdSetSyncWord = 'CONF:NST:RX:SYNC_WORD ' + cmdParam + '\n'
           result = RwcSerialSetup.transceive(self, cmdSetSyncWord)
           return result
        else:
           raise Exception('Invalid Parameter received.')

    def nst_rx_getsyncword(self):
        '''
        Read the Sync Word for FSK Modulation

        :Parameters: Query only

        :return: It returns Sync Word; NAK on failure
        
        '''
        cmdGetSyncWord = 'CONF:NST:RX:SYNC_WORD?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetSyncWord)
        return result

    def nst_rx_settxpolarity(self, polaritytype):
        '''
        Configure the RX signal polarity for FSK Modulation

        :param polaritytype: NORMAL, INVERSE

        :return: ACK on success, NAK on failure

        '''
        polaritytypelist = ['NORMAL', 'INVERSE']
        if polaritytype in polaritytypelist:
            cmdSetRxPolarity = 'CONF:NST:RX:TX_POLARITY ' \
                                + polaritytype + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetRxPolarity)
            return result
        else:
            raise Exception('Invalid Parameter received.')

    def nst_rx_gettxpolarity(self):
        '''
        Read the RX signal polarity for FSK Modulation

        :Parameters: Query only

        :return: It returns RX signal polarity; NAK on failure
        
        '''
        cmdGetRxPolarity = 'CONF:NST:RX:TX_POLARITY?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetRxPolarity)
        return result

    def nst_rx_setduttype(self, duttype):
        '''
        Configure the DUT Type for RX NST test
        (RWC supported version: v1.15 - v1.21)

        :param duttype: END_DEVICE, GATEWAY, UNKNOWN

        :return: ACK on success, NAK on failure

        '''
        duttypelist = ['END_DEVICE', 'GATEWAY', 'UNKNOWN']
        cmdSupportedVersion = [
            '1.150', '1.160', 
            '1.170', '1.200', 
            '1.203', '1.204', 
            '1.206', '1.210']
        verStatus = self.validate_sys_swversion(cmdSupportedVersion)

        if verStatus and duttype in duttypelist:
            cmdSetDutType = 'CONF:NST:RX:DUT_TYPE ' + duttype + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetDutType)
            return result
        else:
            raise Exception('Invalid Parameter received.')

    def nst_rx_getduttype(self):
        '''
        Read the DUT Type for RX NST test
        (RWC supported version: v1.15 - v1.21)

        :Parameters: Query only

        :return: It returns DUT type; NAK on failure
        
        '''
        cmdSupportedVersion = [
            '1.150', '1.160', 
            '1.170', '1.200', 
            '1.203', '1.204', 
            '1.206', '1.210']
        verStatus = self.validate_sys_swversion(cmdSupportedVersion)

        if verStatus:
            cmdGetDutType = 'CONF:NST:RX:DUT_TYPE?' + '\n'
            result = RwcSerialSetup.transceive(self, cmdGetDutType)
            return result

    def nst_mfg_setduttype(self, duttype):
        '''
        Configure the DUT Type for MFG NST test
        (RWC supported version: v1.15 - v1.21)

        :param duttype: END_DEVICE, GATEWAY, UNKNOWN

        :return: ACK on success, NAK on failure

        '''
        duttypelist = ['END_DEVICE', 'GATEWAY', 'UNKNOWN']
        cmdSupportedVersion = [
            '1.150', '1.160', 
            '1.170', '1.200', 
            '1.203', '1.204', 
            '1.206', '1.210']
        verStatus = self.validate_sys_swversion(cmdSupportedVersion)

        if verStatus and duttype in duttypelist:
            cmdSetDutType = 'CONF:NST:MFG:DUT_TYPE ' + duttype + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetDutType)
            return result
        else:
            raise Exception('Invalid Parameter received.')

    def nst_mfg_getduttype(self):
        '''
        Read the DUT Type for MFG NST test
        (RWC supported version: v1.15 - v1.21)

        :Parameters: Query only

        :return: It returns DUT type; NAK on failure
        
        '''
        cmdSupportedVersion = [
            '1.150', '1.160', 
            '1.170', '1.200', 
            '1.203', '1.204', 
            '1.206', '1.210']
        verStatus = self.validate_sys_swversion(cmdSupportedVersion)

        if verStatus:
            cmdGetDutType = 'CONF:NST:MFG:DUT_TYPE?' + '\n'
            result = RwcSerialSetup.transceive(self, cmdGetDutType)
            return result

    def nst_mfg_setusercriteria(self, value):
        '''
        Configure the user's criteria of PER in MFG test

        :param: 0.001 ~ 1

        :return: ACK on success, NAK on failure
        
        '''
        cmdValue = float(value)
        if (cmdValue >= 0.001 and cmdValue <= 1.000):
            cmdPerCriteriaValue = str(cmdValue)
            cmdSetPerCriteria = 'CONF:NST:MFG:PER_CRITERIA ' \
                                    + cmdPerCriteriaValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPerCriteria)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def nst_mfg_getusercriteria(self):
        '''
        Read the user's criteria of PER in MFG test

        :Parameters: Query only

        :return: It returns MFG user criteria; NAK on failure
        
        '''
        cmdGetMfgPerCriteria = 'READ:NST:MFG:PER_CRITERIA?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMfgPerCriteria)
        return result

    def nst_mfg_setuser_uppercriteria(self, power):
        '''
        Configure the user's upper criteria of TX Power in MFG test

        :param power: -150 ~ 30

        :return: ACK on success, NAK on failure
        
        '''
        if power >= -150 and power <= 30:
            cmdPower = str(power)
            cmdSetMfgPowUpperCriteria = 'CONF:NST:MFG:POW_CRITERIA_UPPER' \
                                            + cmdPower + '\n'
            result = RwcSerialSetup.transceive(
                self, 
                cmdSetMfgPowUpperCriteria)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def nst_mfg_getuser_uppercriteria(self):
        '''
        Read the user's upper criteria of TX Power in MFG test

        :Parameters: Query only

        :return: It returns MFG user upper criteria; NAK on failure
        
        '''
        cmdGetMfgPowUpperCriteria = 'READ:NST:MFG:POW_CRITERIA_UPPER?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMfgPowUpperCriteria)
        return result

    def nst_mfg_setuser_lowercriteria(self, power):
        '''
        Configure the user's lower criteria of TX Power in MFG test

        :param power: -150 ~ 30

        :return: ACK on success, NAK on failure
        
        '''
        if power >= -150 and power <= 30:
            cmdPower = str(power)
            cmdSetMfgPowLowerCriteria = 'CONF:NST:MFG:POW_CRITERIA_LOWER' \
                                            + cmdPower + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMfgPowLowerCriteria)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def nst_mfg_getuser_lowercriteria(self):
        '''
        Read the user's lower criteria of TX Power in MFG test

        :Parameters: Query only

        :return: It returns MFG user lower criteria; NAK on failure
        
        '''
        cmdGetMfgPowLowerCriteria = 'READ:NST:MFG:POW_CRITERIA_LOWER?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMfgPowLowerCriteria)
        return result

    def nst_mfg_getpervalue(self):
        '''
        Read the result value of PER measurement in MFG test

        :Parameters: Query only

        :return: It returns MFG PER value; NAK on failure
        
        '''
        cmdGetMfgPer = 'READ:NST:MFG:PER?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMfgPer)
        return result

    def nst_mfg_getpowervalue(self):
        '''
        Read the result value of POWER measurement in MFG test

        :Parameters: Query only

        :return: It returns MFG power value; NAK on failure
        
        '''
        cmdGetMfgPow = 'READ:NST:MFG:POW?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMfgPow)
        return result

    def nst_mfg_getstatus(self):
        '''
        Read the run status in MFG test; STOPPED, IDLE, PASS or FAIL, 
        TIME_OUT, WAIT_REPORT, BUSY

        :Parameters: Query only

        :return: It returns the MFG run status; NAK on failure
        
        '''
        cmdGetMfgStatus = 'READ:NST:MFG:STATUS?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMfgStatus)
        return result

    def nst_mfg_settimeout(self, timeout):
        '''
        Configure the timeout wait trigger from DUT in MFG test

        :param timeout: 1 ~ 100

        :return: ACK on success, NAK on failure
        
        '''
        if timeout >= 1 and timeout <= 100:
            cmdTimeout = str(timeout)
            cmdSetMfgTimeout = 'CONF:NST:MFG:TIME_OUT ' + cmdTimeout + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMfgTimeout)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def nst_mfg_gettimeout(self):
        '''
        Read the timeout wait trigger from DUT in MFG test

        :Parameters: Query only

        :return: It returns the MFG timeout value; NAK on failure
        
        '''
        cmdGetMfgTimeout = 'READ:NST:MFG:TIME_OUT?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMfgTimeout)
        return result

    def nst_mfg_setmode(self, mode):
        '''
        Configure the mode of MFG test

        :param mode: LORA, CW

        :return: ACK on success, NAK on failure
        
        '''
        cmdMfgMode = mode
        if cmdMfgMode == 'LORA':
            cmdSetMfgMode = 'CONF:NST:MFG:MODE LORA' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMfgMode)
            return result
        elif cmdMfgMode == 'FSK':
            cmdSetMfgMode = 'CONF:NST:MFG:MODE FSK' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMfgMode)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def nst_mfg_getmode(self):
        '''
        Read the mode of MFG test

        :Parameters: Query only

        :return: It returns the MFG mode; NAK on failure
        
        '''
        cmdGetMfgMode = 'READ:NST:MFG:MODE?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMfgMode)
        return result

    def nst_mfg_setinterval(self, value):
        '''
        Configure the interval in sec between consecutive LoRa TX frames 
        in MFG test

        :param value: 0.05 ~ 1000

        :return: ACK on success, NAK on failure
        
        '''
        cmdValue = float(value)
        if (cmdValue >= 0.05 and cmdValue <= 1000.00):
            cmdIntervalValue = str(cmdValue)
            cmdSetInterval = 'CONF:NST:MFG:INTERVAL ' \
                                + cmdIntervalValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetInterval)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def nst_mfg_getinterval(self):
        '''
        Read the interval in sec between consecutive LoRa TX frames 
        in MFG test

        :Parameters: Query only

        :return: It returns MFG interval in seconds; NAK on failure
        
        '''
        cmdGetMfgInterval = 'READ:NST:MFG:INTERVAL?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMfgInterval)
        return result

    def nst_mfg_setbw(self, bw):
        '''
        Configure the BW in kHz of LoRa TX frame in MFG test

        :param bw: 500, 250, 125

        :return: ACK on success, NAK on failure
        
        '''
        if (bw == 500) or (bw == 250) or (bw == 125):
            cmdMfgBw = str(bw)
            cmdSetMfgBw = 'CONF:NST:MFG:BW ' + cmdMfgBw + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMfgBw)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def nst_mfg_getbw(self):
        '''
        Read the BW in kHz of LoRa TX frame in MFG test

        :Parameters: Query only

        :return: It returns MFG bandwidth; NAK on failure
        
        '''
        cmdGetMfgBw = 'READ:NST:MFG:BW?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMfgBw)
        return result

    def nst_mfg_setsf(self, index):
        '''
        Configure the Spreading Factor of LoRa TX frame in MFG test

        :param index: SF7 ~ SF12, ANY

        :return: ACK on success, NAK on failure
        
        '''
        sflist = [
            'SF7', 
            'SF8', 
            'SF9', 
            'SF10', 
            'SF11', 
            'SF12', 
            'ANY']
        if index in sflist:
            cmdSetMfgSf = 'CONF:NST:MFG:SF ' + index + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMfgSf)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def nst_mfg_getsf(self):
        '''
        Read the Spreading Factor of LoRa TX frame in MFG test

        :Parameters: Query only

        :return: It returns the MFG spreading factor; NAK on failure
        
        '''
        cmdGetMfgSf = 'READ:NST:MFG:SF?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMfgSf)
        return result

    def nst_mfg_setcr(self, codingrate):
        '''
        Configure the Coding Rate of LoRa TX frame in MFG test

        :param codingrate: 4_5, 4_6, 4_7, 4_8, NO_CRC

        :return: ACK on success, NAK on failure
        
        '''
        cmdMfgCodingRate = codingrate
        if cmdMfgCodingRate == '4_5':
            cmdSetMfgCodingRate = 'CONF:NST:MFG:CR 4_5' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMfgCodingRate)
            return result
        elif cmdMfgCodingRate == '4_6':
            cmdSetMfgCodingRate = 'CONF:NST:MFG:CR 4_6' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMfgCodingRate)
            return result
        elif cmdMfgCodingRate == '4_7':
            cmdSetMfgCodingRate = 'CONF:NST:MFG:CR 4_7' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMfgCodingRate)
            return result
        elif cmdMfgCodingRate == '4_8':
            cmdSetMfgCodingRate = 'CONF:NST:MFG:CR 4_8' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMfgCodingRate)
            return result
        elif cmdMfgCodingRate == 'NO_CRC':
            cmdSetMfgCodingRate = 'CONF:NST:MFG:CR NO_CRC' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMfgCodingRate)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def nst_mfg_getcr(self):
        '''
        Read the Coding Rate of LoRa TX frame in MFG test

        :Parameters: Query only

        :return: It returns the MFG coding rate; NAK on failure
        
        '''
        cmdGetMfgCodingRate = 'READ:NST:MFG:CR?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMfgCodingRate)
        return result

    def nst_mfg_setpayloadsize(self, length):
        '''
        Configure the Payload size of LoRa TX frame in MFG test

        :param length: 0 ~ 250

        :return: ACK on success, NAK on failure
        
        '''
        if length >= 0 and length <= 250:
            cmdMsgLength = str(length)
            cmdSetMsgLength = 'CONF:NST:MFG:PAYLOAD_SIZE ' \
                                + cmdMsgLength + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMsgLength)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def nst_mfg_getpayloadsize(self):
        '''
        Read the Payload size of LoRa TX frame in MFG test

        :Parameters: Query only

        :return: It returns the MFG payload size; NAK on failure
        
        '''
        cmdGetMfgPayloadSize = 'READ:NST:MFG:PAYLOAD_SIZE?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMfgPayloadSize)
        return result

    def nst_mfg_setpayload(self, value):
        '''
        Configure the Message data of LoRa TX frame

        :param value: 128-byte HEX value

        :return: ACK on success, NAK on failure
        
        '''
        cmdValue = int(value)
        if (cmdValue >= 0 and cmdValue <= 2**128 -1) :
            cmdHexValue = hex(cmdValue)
            cmdSetPayload = 'CONF:NST:MFG:PAYLOAD ' + cmdHexValue + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPayload)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def nst_mfg_getpayload(self):
        '''
        Read the Message data of LoRa TX frame

        :param: Query only

        :return: It returns the payload data; NAK on failure
        
        '''
        cmdGetMsgData = 'READ:NST:MFG:PAYLOAD?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMsgData)
        return result

    def nst_mfg_setpayloadtype(self, msgtype):
        '''
        Configure the Payload type of LoRa TX frame in MFG test

        :param msgtype: 0000_0000, 1111_1111, 1111_0000, 
                        1010_1010, PRBS, USER

        :return: ACK on success, NAK on failure
        
        '''
        cmdPayloadType = msgtype
        if cmdPayloadType == '0000_0000':
            cmdSetPayloadType = 'CONF:NST:MFG:PAYLOAD_TYPE 0000_0000' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPayloadType)
            return result
        elif cmdPayloadType == '1111_1111':
            cmdSetPayloadType = 'CONF:NST:MFG:PAYLOAD_TYPE 1111_1111' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPayloadType)
            return result
        elif cmdPayloadType == '1111_0000':
            cmdSetPayloadType = 'CONF:NST:MFG:PAYLOAD_TYPE 1111_0000' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPayloadType)
            return result
        elif cmdPayloadType == '1010_1010':
            cmdSetPayloadType = 'CONF:NST:MFG:PAYLOAD_TYPE 1010_1010' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPayloadType)
            return result
        elif cmdPayloadType == 'PRBS':
            cmdSetPayloadType = 'CONF:NST:MFG:PAYLOAD_TYPE PRBS' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPayloadType)
            return result
        elif cmdPayloadType == 'USER':
            cmdSetPayloadType = 'CONF:NST:MFG:PAYLOAD_TYPE USER' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetPayloadType)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def nst_mfg_getpayloadtype(self):
        '''
        Read the Payload type of LoRa TX frame in MFG test

        :Parameters: Query only

        :return: It returns the MFG payload type; NAK on failure
        
        '''
        cmdGetMfgPayloadType = 'READ:NST:MFG:PAYLOAD_TYPE?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMfgPayloadType)
        return result

    def nst_mfg_setpreamblesize(self, preamblesize):
        '''
        Configure the Preamble size of LoRa TX frame in MFG test

        :param preamblesize: 2 ~ 12

        :return: ACK on success, NAK on failure
        
        '''
        if preamblesize >= 2 and preamblesize <= 12:
            cmdPreambleSize = str(preamblesize)
            cmdSetMfgPreambleSize = 'CONF:NST:MFG:PREAMBLE_SIZE ' \
                                        + cmdPreambleSize + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMfgPreambleSize)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def nst_mfg_getpreamblesize(self):
        '''
        Read the Preamble size of LoRa TX frame in MFG test

        :Parameters: Query only

        :return: It returns the preamble size; NAK on failure
        
        '''
        cmdGetMfgPreambleSize = 'READ:NST:MFG:PREAMBLE_SIZE?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMfgPreambleSize)
        return result

    def nst_mfg_run(self):
        '''
        Run MFG test

        :Parameters: N/A

        :return: None
        
        '''
        cmdStartMfg = 'EXEC:NST:MFG:RUN' + '\n'
        result = RwcSerialSetup.transceive(self, cmdStartMfg)
        return result

    def nst_mfg_stop(self):
        '''
        Stop MFG test

        :Parameters: N/A

        :return: None
        
        '''
        cmdStopMfg = 'EXEC:NST:MFG:STOP' + '\n'
        result = RwcSerialSetup.transceive(self, cmdStopMfg)
        return result

    def nst_mfg_setrepeatnum(self, num):
        '''
        Configure the number of frame transmission in MFG test

        :param num: 0:INFINITY, 1 ~ 10000

        :return: ACK on success, NAK on failure
        
        '''
        if num >= 0 and num <= 10000:
            cmdRepeatNum = str(num)
            cmdSetMfgRepeatNum = 'CONF:NST:MFG:REPEAT_NUM ' \
                                    + cmdRepeatNum + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMfgRepeatNum)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def nst_mfg_getrepeatnum(self):
        '''
        Read the number of frame transmission in MFG test

        :Parameters: Query only

        :return: It returns the number of frame transmission; 
                 NAK on failure
        
        '''
        cmdRepeatNum = 'READ:NST:MFG:REPEAT_NUM?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdRepeatNum)
        return result

    def nst_mfg_setnwktype(self, nwktype):
        '''
        Configure the Sync word in LoRa modulation in MFG test:

        * 0x12 for private network
        * 0x34 for public network

        :Parameters nwktype: PUBLIC, PRIVATE

        :return: ACK on success, NAK on failure
        
        '''
        cmdNwkType = nwktype
        if cmdNwkType == 'PRIVATE':
            cmdSetMfgNwkType = 'CONF:NST:MFG:NETWORK PRIVATE' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMfgNwkType)
            return result
        elif cmdNwkType == 'PUBLIC':
            cmdSetMfgNwkType = 'CONF:NST:MFG:NETWORK PUBLIC' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMfgNwkType)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def nst_mfg_getnwktype(self):
        '''
        Read the Sync word in LoRa modulation in MFG test:

        * 0x12 for private network
        * 0x34 for public network

        :Parameters: Query only

        :return: It returns the network type; NAK on failure
        
        '''
        cmdGetMfgNwkType = 'READ:NST:MFG:NETWORK?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMfgNwkType)
        return result

    def nst_mfg_setfmdeviation(self, value):
        '''
        Configure the FM deviation value for FSK Modulation

        :param value: 10 ~ 100 kHz

        :return: ACK on success, NAK on failure

        '''
        cmdValue = int(value)
        if (cmdValue >= 10 and cmdValue <= 100):
            cmdParam = str(cmdValue)
            cmdSetFmDeviation = 'CONF:NST:MFG:FM_DEVIATION ' + cmdParam + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetFmDeviation)
            return result
        else:
            raise Exception('Invalid Parameter received.')

    def nst_mfg_getfmdeviation(self):
        '''
        Read the FM deviation value for FSK Modulation

        :Parameters: Query only

        :return: It returns FM deviation value; NAK on failure
        
        '''
        cmdGetFmDeviation = 'CONF:NST:MFG:FM_DEVIATION?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetFmDeviation)
        return result

    def nst_mfg_setdatarate(self, value):
        '''
        Configure the Data rate value for FSK Modulation

        :param value: 1 ~ 128 kHz

        :return: ACK on success, NAK on failure

        '''
        cmdValue = int(value)
        if (cmdValue >= 1 and cmdValue <= 128):
            cmdParam = str(cmdValue)
            cmdSetDatarate = 'CONF:NST:MFG:DATA_RATE ' + cmdParam + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetDatarate)
            return result
        else:
            raise Exception('Invalid Parameter received.')

    def nst_mfg_getdatarate(self):
        '''
        Read the Data rate value for FSK Modulation

        :Parameters: Query only

        :return: It returns Data rate value; NAK on failure
        
        '''
        cmdGetDatarate = 'CONF:NST:MFG:DATA_RATE?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetDatarate)
        return result

    def nst_mfg_setsyncwordsize(self, sizevalue):
        '''
        Configure the Sync Word size for FSK Modulation

        :param sizevalue: 1 ~ 8 byte

        :return: ACK on success, NAK on failure

        '''
        cmdValue = int(sizevalue)
        if (cmdValue >= 1 and cmdValue <= 8):
            cmdParam = str(cmdValue)
            cmdSetSyncWordSize = 'CONF:NST:MFG:SYNC_WORD_SIZE ' \
                                    + cmdParam + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetSyncWordSize)
            return result
        else:
            raise Exception('Invalid Parameter received.')

    def nst_mfg_getsyncwordsize(self):
        '''
        Read the Sync Word size for FSK Modulation

        :Parameters: Query only

        :return: It returns Sync Word size; NAK on failure
        
        '''
        cmdGetSyncWordSize = 'CONF:NST:MFG:SYNC_WORD_SIZE?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetSyncWordSize)
        return result

    def nst_mfg_setsyncword(self, sizevalue):
        '''
        Configure the Sync Word for FSK Modulation

        :param value: -

        :return: ACK on success, NAK on failure

        '''
        cmdValue = int(sizevalue)
        if (cmdValue >= 1 and cmdValue <= 8):
           cmdParam = str(cmdValue)
           cmdSetSyncWord = 'CONF:NST:MFG:SYNC_WORD ' + cmdParam + '\n'
           result = RwcSerialSetup.transceive(self, cmdSetSyncWord)
           return result
        else:
           raise Exception('Invalid Parameter received.')

    def nst_mfg_getsyncword(self):
        '''
        Read the Sync Word for FSK Modulation

        :Parameters: Query only

        :return: It returns Sync Word; NAK on failure
        
        '''
        cmdGetSyncWord = 'CONF:NST:MFG:SYNC_WORD?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetSyncWord)
        return result

    def nst_mfg_settxpolarity(self, polaritytype):
        '''
        Configure the TX signal polarity for FSK Modulation

        :param polaritytype: NORMAL, INVERSE

        :return: ACK on success, NAK on failure

        '''
        polaritytypelist = ['NORMAL', 'INVERSE']
        if polaritytype in polaritytypelist:
            cmdSetMfgTxPolarity = 'CONF:NST:MFG:TX_POLARITY ' \
                                    + polaritytype + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMfgTxPolarity)
            return result
        else:
            raise Exception('Invalid Parameter received.')

    def nst_mfg_gettxpolarity(self):
        '''
        Read the TX signal polarity for FSK Modulation

        :Parameters: Query only

        :return: It returns TX signal polarity; NAK on failure
        
        '''
        cmdGetMfgTxPolarity = 'CONF:NST:MFG:TX_POLARITY?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMfgTxPolarity)
        return result

    def nst_mfg_setrxpolarity(self, polaritytype):
        '''
        Configure the RX signal polarity for FSK Modulation

        :param polaritytype: NORMAL, INVERSE

        :return: ACK on success, NAK on failure

        '''
        polaritytypelist = ['NORMAL', 'INVERSE']
        if polaritytype in polaritytypelist:
            cmdSetMfgRxPolarity = 'CONF:NST:MFG:RX_POLARITY ' \
            + polaritytype + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetMfgRxPolarity)
            return result
        else:
            raise Exception('Invalid Parameter received.')

    def nst_mfg_getrxpolarity(self):
        '''
        Read the RX signal polarity for FSK Modulation

        :Parameters: Query only

        :return: It returns RX signal polarity; NAK on failure
        
        '''
        cmdGetMfgRxPolarity = 'CONF:NST:MFG:RX_POLARITY?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMfgRxPolarity)
        return result

    def nst_mfg_getdutinfo(self):
        '''
        Read the user data received from DUT at start of MFG test,
        e.g. a serial number

        :Parameters: Query only

        :return: It returns the DUT info; NAK on failure


        .. _syslabel:
        '''
        cmdGetMfgDutInfo = 'READ:NST:MFG:DUT_INFO?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetMfgDutInfo)
        return result
            
    # System Command Methods
    def query_sysversion(self):
        '''
        Read the software version
   
        :Parameters: N/A (Query only)

        :return: It returns software version; NAK on failure

        '''
        cmdSysVersion = 'READ:SYSTEM:SW_VERSION?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdSysVersion)
        return result

    def sys_setreferenceclock(self, src):
        '''
        Configure the selection of source for the reference clock
   
        :param src: reference clock source (INT, EXT)

        :return: ACK on success, NAK on failure

        '''
        cmdRefClockParam = src
        if cmdRefClockParam == 'INT':
            cmdSysRefClock = 'CONF:SYSTEM:REF_CLK INT' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSysRefClock)
            return result
        elif cmdRefClockParam == 'EXT':
            cmdSysRefClock = 'CONF:SYSTEM:REF_CLK EXT' + '\n'
            result = RwcSerialSetup.transceive(self, cmdSysRefClock)
            return result
        else:
            raise Exception('Invalid parameter received.')

    def sys_getreferenceclock(self):
        '''
        Read the selection of source for the reference clock

        :Parameters: N/A (Query only)

        :return: It returns the selected reference clock; 
                 NAK on failure

        '''
        cmdGetSysRefClock = 'READ:SYSTEM:REF_CLK?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetSysRefClock)
        return result
    
    def query_sysserialnum(self):
        '''
        Read the serial number of RWC5020A

        :Parameters: N/A (Query only)

        :return: It returns the serial number; NAK on failure

        '''
        cmdGetSysSerialNum = 'READ:SYSTEM:SERIAL_NUM?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetSysSerialNum)
        return result

    def query_gwtoptinfo(self):
        '''
        Read the software option information about Gateway Test

        :Parameters: N/A (Query only)

        :return: It returns the GWT option info; NAK on failure

        '''
        cmdGetGwtOptInfo = 'READ:SYSTEM:OPTION_GWT?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetGwtOptInfo)
        return result

    def query_edtoptinfo(self):
        '''
        Read the software option information about End Device Test

        :Parameters: N/A (Query only)

        :return: It returns the EDT option info; NAK on failure

        '''
        cmdGetEdtOptInfo = 'READ:SYSTEM:OPTION_EDT?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetEdtOptInfo)
        return result

    def query_nstoptinfo(self):
        '''
        Read the software option information about Non-signaling Test

        :Parameters: N/A (Query only)

        :return: It returns the NST option info; NAK on failure

        '''
        cmdGetNstOptInfo = 'READ:SYSTEM:OPTION_NST?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetNstOptInfo)
        return result

    def query_eucertoptinfo(self):
        '''
        Read the software option information about Certification 
        test of EU

        :Parameters: N/A (Query only)

        :return: It returns the EUCERT option info; NAK on failure

        '''
        cmdGetEUCertOptInfo = 'READ:SYSTEM:OPTION_CERTI_EU?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetEUCertOptInfo)
        return result

    def query_sktcertoptinfo(self):
        '''
        Read the software option information about Certification 
        test of SKT

        :Parameters: N/A (Query only)

        :return: It returns the SKTCERT option info; NAK on failure

        '''
        cmdGetSKTCertOptInfo = 'READ:SYSTEM:OPTION_CERTI_SKT?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetSKTCertOptInfo)
        return result

    def query_uscertoptinfo(self):
        '''
        Read the software option information about Certification 
        test of US

        :Parameters: N/A (Query only)

        :return: It returns the USCERT option info; NAK on failure

        '''
        cmdGetUSCertiOptInfo = 'READ:SYSTEM:OPTION_CERTI_US?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetUSCertiOptInfo)
        return result

    def query_ascertoptinfo(self):
        '''
        Read the software option information about Certification 
        test of AS

        :Parameters: N/A (Query only)

        :return: It returns the ASCERT option info; NAK on failure

        '''
        cmdGetASCertiOptInfo = 'READ:SYSTEM:OPTION_CERTI_AS?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetASCertiOptInfo)
        return result

    def query_krcertoptinfo(self):
        '''
        Read the software option information about Certification 
        test of KR

        :Parameters: N/A (Query only)

        :return: It returns the KRCERT option info; NAK on failure

        '''
        cmdGetKRCertiOptInfo = 'READ:SYSTEM:OPTION_CERTI_KR?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetKRCertiOptInfo)
        return result

    def sys_setiptype(self, ipType):
        '''
        To configure the IP type

        :param fieldType: DYNAMIC, STATIC

        :return: ACK on success, NAK on failure
        
        '''
        ipTypelist = ['DYNAMIC', 'STATIC']
        if ipType in ipTypelist:
            cmdSetIPType = 'CONF:SYSTEM:IP_TYPE ' + ipType + '\n'
            result = RwcSerialSetup.transceive(self, cmdSetIPType)
            return result
        else:
            raise Exception('Invalid IP type parameter received.')

    def sys_getiptype(self):
        '''
        To read the IP type

        :Parameters: N/A (Query only)

        :return: It returns the IP type of tester; NAK on failure

        '''
        cmdGetIPType = 'READ:SYSTEM:IP_TYPE?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetIPType)
        return result

    def sys_setipaddress(self, ipval):
        '''
        To configure the ip address (IPV4).
        It should be executed via RS232C

        :param ipval: IPV4 address
        
        :return: ACK on success, NAK on failure

        '''
        try:
            ip = ipaddress.ip_address(ipval)
            if(ip.version == 4):
                cmdSetIpAddress = 'CONF:SYSTEM:IP_ADDR ' + ipval + '\n'
                result = RwcSerialSetup.transceive(self, cmdSetIpAddress)
                return result
            else:
                raise Exception('Invalid IP version parameter received')
        except ValueError:
            print ('Invalid IP address parameter received')

    def sys_getipaddress(self):
        '''
        To read the IP address

        :Parameters: N/A (Query only)

        :return: It returns the IP address of tester; NAK on failure

        '''
        cmdGetIPAddr = 'READ:SYSTEM:IP_ADDR?' + '\n'
        result = RwcSerialSetup.transceive(self, cmdGetIPAddr)
        return result

    def validate_sys_swversion(self, versionlist):
        currVersion = self.query_sysversion()
        if currVersion in versionlist:
            return True
        else:
            raise Exception('Command not supported in current version')
        