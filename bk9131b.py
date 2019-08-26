"""
    Module for B&KPrecision Programmable DC Power Supply
"""
import visa
import time
import usb.core
import usb.util
import sys


class BK9131B:
    """
    Class encapsulating functionality of B&KPrecision 9131b Programmable DC
    Power Supply
    """
    device = None
    dev_id = None
    verbose = False

    def __init__(self, id):
        self.device = visa.ResourceManager().open_resource(id)
        self.dev_id = id
        # print(self.device)

    def getInfo(self):
        if self.device:
            ident = self.device.query('*IDN?').split(',')
            for i in range(0, len(ident)):
                ident[i] = ident[i].strip()
            return ident
        else:
            print('Device not available')
            return []

    def showInfo(self):
        parms = self.getInfo()
        print('mfg    : {}'.format(parms[0]))
        print('model  : {}'.format(parms[1]))
        print('serial : {}'.format(parms[2]))

    def setLocal(self):
        """
        Set the device to local control (disable control via SCPI interface)
        """
        self.device.write('SYST:LOCAL')

    def setRemote(self):
        """
        Set the device to remote control (enable control via SCPI interface)
        """
        self.device.write('SYST:REMOTE')

    def getChannel(self):
        chanNum = self.device.query("INST?")
        return int(chanNum[2])

    def setChannel(self, chan: int):
        if self.verbose:
            print("DEBUG : Setting channel to {}".format(chan), file=sys.stderr)
        if 0 < chan < 4:
            self.device.write("INST CH{}".format(chan))
        else:
            print("Channel {} is invalid".format(chan))
            raise Exception('Invalid channel')

    def getVoltage(self):
        volts = self.device.query("VOLTAGE?")
        return float(volts)

    def setVoltage(self, v: int, chan=None):
        if chan is not None:
            self.setChannel(chan)
        if self.verbose:
            print("DEBUG : Setting voltage to {}".format(v), file=sys.stderr)
        self.device.write("VOLTAGE {}".format(v))
