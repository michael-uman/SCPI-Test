import time
from bk9131b import BK9131B

bk9131b='USB0::65535::37168::802360043747010048::0::INSTR'

try:
    dev = BK9131B(bk9131b)

    dev.showInfo()

    dev.setRemote()
    # time.sleep(2)
    chan = dev.getChannel()
    # print("Current channel = {}".format(chan))

    print('-' * 80)
    print("Current Voltage Settings:")
    print('-' * 80)
    for c in range(1,4):
        dev.setChannel(c)
        v = dev.getVoltage()
        print("Voltage for channel {} = {}V".format(c, v))

    dev.setVoltage(22.5, 1)

    dev.setLocal()
except Exception as e:
    print(e)


# try:
#     bkdevice = rm.open_resource(bk9131b)
#
#     showDeviceInfo(bkdevice)
#
#     # Put the device in remote control mode
#     bkdevice.write('SYST:REMOTE')
#     #
#     bkdevice.write("INST CH1")
#     cur_volts = bkdevice.query("VOLT?").strip()
#     print("CH1 Current Voltage = {}V".format(cur_volts))
#     #
#     bkdevice.write("INST CH2")
#     cur_volts = bkdevice.query("VOLT?").strip()
#     print("CH2 Current Voltage = {}V".format(cur_volts))
#     #
#     time.sleep(2)
#     #
#     bkdevice.write("INST CH1")
#     bkdevice.write("VOLTAGE 12")
#     time.sleep(2)
#     bkdevice.write("VOLTAGE 24")
#
#     # Restore LOCAL control of instrument
#
#     bkdevice.write('SYST:LOCAL')
# except Exception as e:
#     print('Device is in use...')
