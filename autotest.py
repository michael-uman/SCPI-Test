import time
from bk9131b import BK9131B


def horiz_line(width = 80):
    print('-' * width)


bk9131b='USB0::65535::37168::802360043747010048::0::INSTR'

try:
    dev = BK9131B(bk9131b)
    # dev.verbose = True

    horiz_line()
    dev.showInfo()

    dev.setRemote()
    chan = dev.getChannel()
    # print("Current channel = {}".format(chan))

    horiz_line()
    print("Current Voltage Settings:")
    horiz_line()
    for c in range(1,4):
        dev.setChannel(c)
        v = dev.getVoltage()
        print("Voltage for channel {} = {}V".format(c, v))

    print('-' * 80)
    time.sleep(2)
    print("Setting voltage on CH1 to 22.5...")
    dev.setVoltage(20.5, 1)
    time.sleep(2)
    print("Setting voltage on CH1 to 24.0...")
    dev.setVoltage(24.0, 1)

    print('-' * 80)

    # Restore local control
    dev.setLocal()

except Exception as e:
    print(e)
