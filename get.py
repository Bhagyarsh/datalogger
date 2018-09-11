
import minimalmodbus as mb
import datetime
import requests
import csv
import json
from save import sentsavedata, createfile
import time
from var import registers
import pandas as pd

from findslave import find_slave_id
print(registers)
slave_ids = find_slave_id()
slave_ids = [1, 2, 3]
uid = "28487678947878"
file_name = uid + '.csv'

while True:
    for slave_id in slave_ids:
        for i in range(3000, 3064):
            try:
                if (registers.get(i)[4]["send"]) is True:

                    instrument = mb.Instrument('/dev/ttyUSB0', slave_id)

                # instrument.serial.port          # this is the serial port name
                    instrument.serial.baudrate = 9600  # Baud
                    instrument.serial.bytesize = 8

                    instrument.serial.stopbits = 1
                    instrument.serial.timeout = 2  # seconds

                    instrument.address = slave_id   # this is the slave address number
                    instrument.mode = mb.MODE_RTU   # rtu or ascii mode
                # instrument.debug = True
                # print(i, end=" ")
                    try:
                        value = instrument.read_register(
                            i,
                            registers.get(i)[2]["decimal"], 4)
                        registers.get(i)[5]["value"] = value
                        print(i)
                        print(value)
                        time.sleep(0.2)
                    except:
                        registers.get(i)[5]["value"] = '0'
                        print("can't read {} rig".format(i))
            except IOError:
                registers.get(i)[5]["value"] = '0'
                print("Failed to read from instrument")

        # for i in range(3000, 3064):
        #     if (registers.get(i)[4]["send"]) is True:
        #         print(datetime.datetime.now().strftime("%x"), end='  ')
        #         print(datetime.datetime.now().strftime("%X"), end='  ')
        #         print(i, end='  ')
        #         print(registers.get(i)[0]["item"], end=' ')
        #         print(registers.get(i)[5]["value"], end=' ')
        #         print(registers.get(i)[1]["unit"])

        pv1_power = str(registers.get(3006)[5]["value"]) + str(registers.get(3007)[5]["value"])

        pv2_power = str(registers.get(3008)[5]["value"]) + str(registers.get(3009)[5]["value"])

        pv3_power = str(registers.get(3010)[5]["value"]) + str(registers.get(3011)[5]["value"])

        grid_power = str(registers.get(3023)[5]["value"]) + str(registers.get(3024)[5]["value"])

        total_energy_1 = str(registers.get(3034)[5]["value"]) + str(registers.get(3035)[5]["value"])

        total_energy_2 = str(registers.get(3038)[5]["value"]) + str(registers.get(3039)[5]["value"])

        annual_energy = str(registers.get(3040)[5]["value"]) + str(registers.get(3041)[5]["value"])

        daily_energy = str(registers.get(3042)[5]["value"])

        apparent_power = str(registers.get(3052)[5]["value"]) + str(registers.get(3053)[5]["value"])

        reactive_power = str(registers.get(3054)[5]["value"]) + str(registers.get(3055)[5]["value"])

        timesend = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print(timesend)
        print(uid + "{0:0=2d}".format(slave_id))
        url = "http://solar.bhkdev.tk/api/stats/update"
        data = {
            "mac": uid + "{0:0=2d}".format(slave_id),
            "pv1_voltage": registers.get(3000)[5]["value"],
            "pv2_voltage": registers.get(3001)[5]["value"],
            "pv3_voltage": registers.get(3002)[5]["value"],
            "pv1_current": registers.get(3003)[5]["value"],
            "pv2_current": registers.get(3004)[5]["value"],
            "pv3_current": registers.get(3005)[5]["value"],
            "pv1_power": pv1_power,
            "pv2_power": pv2_power,
            "pv3_power":  pv3_power,
            "rs_grid_voltage":  registers.get(3014)[5]["value"],
            "st_grid_voltage":  registers.get(3015)[5]["value"],
            "tr_grid_voltage": registers.get(3016)[5]["value"],
            "grid_power": grid_power,
            "radiator_temperature": registers.get(3025)[5]["value"],
            "module_temperature":  registers.get(3026)[5]["value"],
            "total_energy": total_energy_1,
            "alarm_code":  registers.get(3036)[5]["value"],
            "annual_energy": annual_energy,
            "daily_energy": registers.get(3042)[5]["value"],
            "apparent_power": apparent_power,
            "reactive_power": reactive_power,
            "power_factor": registers.get(3056)[5]["value"],
            "recorded_at": timesend
        }
        headers = {'Content-type': 'application/json'}
        try:
            sentsavedata(file_name)
            # r = requests.post(url, data=json.dumps(data), headers=headers)

            print("send")
        except:
            print('no net')

            with open(file_name, mode='a') as csv_file:
                fieldnames = [
                    'mac',
                    'pv1_voltage',
                    'pv2_voltage',
                    'pv3_voltage',
                    'pv1_current',
                    'pv2_current',
                    'pv3_current',
                    'pv1_power',
                    'pv2_power',
                    'pv3_power',
                    'rs_grid_voltage',
                    'st_grid_voltage',
                    'tr_grid_voltage',
                    'grid_power',
                    'radiator_temperature',
                    'module_temperature',
                    'total_energy',
                    'alarm_code',
                    'annual_energy',
                    'daily_energy',
                    'apparent_power',
                    'reactive_power',
                    'power_factor',
                    'recorded_at'
                ]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                writer.writerow(data)

    time.sleep(10)
