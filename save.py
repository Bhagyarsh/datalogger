import csv

# import json

import pandas as pd
import requests

import eventlet
eventlet.monkey_patch()
# data = {
#     "mac": 1,
#     "pv1_voltage": pv1_voltage,
#     "pv2_voltage": pv2_voltage,
#     "pv3_voltage": pv3_voltage,
#     "pv1_current": pv1_current,
#     "pv2_current": pv2_current,
#     "pv3_current": pv3_current,
#     "pv1_power": pv1_power,
#     "pv2_power": pv2_power,
#     "pv3_power":  pv3_power,
#     "rs_grid_voltage":  rs_grid_voltage,
#     "st_grid_voltage":  st_grid_voltage,
#     "tr_grid_voltage": tr_grid_voltage,
#     "grid_power": grid_power,
#     "radiator_temperature": radiator_temperature,
#     "module_temperature":  module_temperature,
#     "total_energy": total_energy,
#     "alarm_code":  alarm_code,
#     "annual_energy": annual_energy,
#     "daily_energy": daily_energy,
#     "apparent_power": apparent_power,
#     "reactive_power": reactive_power,
#     "power_factor": power_factor,
#     "recorded_at": timesend
# }


def createfile(file_name):

    with open(file_name, mode='w') as csv_file:

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
        writer.writeheader()


# createfile('123456789012341')
# d = fakerdata(count=0, timedelay=10, date_now='12/7/18', time_now='14:00:00')
# # createfile(1, 12345678901234)
# for i in d:
#     with open('123456789012341.csv', mode='a') as csv_file:
#         fieldnames = [
#             'mac',
#             'pv1_voltage',
#             'pv2_voltage',
#             'pv3_voltage',
#             'pv1_current',
#             'pv2_current',
#             'pv3_current',
#             'pv1_power',
#             'pv2_power',
#             'pv3_power',
#             'rs_grid_voltage',
#             'st_grid_voltage',
#             'tr_grid_voltage',
#             'grid_power',
#             'radiator_temperature',
#             'module_temperature',
#             'total_energy',
#             'alarm_code',
#             'annual_energy',
#             'daily_energy',
#             'apparent_power',
#             'reactive_power',
#             'power_factor',
#             'recorded_at'
#         ]
#         writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#
#         writer.writerow(i)
#     print(d)


# with open('123456789012341.csv', mode='r') as csv_file:
#     reader = csv.reader(csv_file)
#     header = None
#     data = []
#     for row in reader:
#         if header is None:
#             header = row
#             print(header)
#         else:
#             data.append(row)
# reader = csv.DictReader(open('123456789012341.csv', 'r'))
# dict_list = []
# for line in reader:
#     dict_list.append(line)
# for i in dict_list:
#     url = 'http://test.solardata.tk/api/stats/update'
#     print("///////////////////////////////")
#     headers = {'Content-type': 'application/json'}
#     r = requests.post(url, data=json.dumps(i), headers=headers)
#
#     print(len(i))
def sentsavedata(file_name):
    print('in sentsavedata')
    data = pd.read_csv(file_name)
    total_rows = len(data)
    print('read data')
    print(total_rows)
    url = 'http://test.solardata.tk/api/stats/update'
    while(total_rows):

        dataread = data.head(1).to_json(orient='records')[1:-1].replace('},{', '} {')
        headers = {'Content-type': 'application/json'}
        print(dataread)
        try:
            print("in try")
            # with eventlet.Timeout(10):

            r = requests.post(url, data=dataread, headers=headers)
            print(r)
            data.drop(data.index[0], inplace=True)
            total_rows -= 1

        except:
            data.to_csv(file_name, sep=',', encoding='utf-8', index=False)
            print('nooooo')
            break
        finally:
            data.to_csv(file_name, sep=',', encoding='utf-8', index=False)
