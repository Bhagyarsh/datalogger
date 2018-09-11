import minimalmodbus as mb
import time


def find_slave_id():
    slave_ids = []
    for slave_id in range(1, 33):
        for i in range(3000, 3003):
            try:
                instrument = mb.Instrument('/dev/ttyACM0', slave_id)

            # instrument.serial.port          # this is the serial port name
                instrument.serial.baudrate = 9600  # Baud
                instrument.serial.bytesize = 8

                instrument.serial.stopbits = 1
                instrument.serial.timeout = 1  # seconds

                instrument.address = slave_id   # this is the slave address
                instrument.mode = mb.MODE_RTU   # rtu or ascii mode
            # instrument.debug = True
            # print(i, end=" ")

                value = instrument.read_register(i, 0, 4)
                print(value)
                if slave_id not in slave_ids:
                    slave_ids.append(slave_id)
                time.sleep(0.5)
            except:
                print("can't read {} rig".format(i))

    print('done')
    print(slave_ids)
    return(slave_ids)


print(find_slave_id())
