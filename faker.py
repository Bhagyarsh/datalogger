import random
import time
import datetime


def fakerdata(count, timedelay, date_now, time_now):
    datalist = []
    my_time = datetime.datetime.strptime(date_now, '%d/%m/%y')
    time_ = time_now.split(':')
    my_time = my_time.replace(hour=int(time_[0]), minute=int(time_[1]),
                              second=int(time_[2]))

    for i in range(0, count):

        # url = http+url_input+"/api/stats/update"
        pv1_voltage = 608.2 + random.randrange(-600, 100)
        pv2_voltage = 579.8 + random.randrange(-600, 100)
        pv3_voltage = 10*random.uniform(0, 1)
        pv1_current = 5 + 1*random.uniform(0, 1) - 2*random.uniform(0, 1)
        pv2_current = 5 + 1*random.uniform(0, 1) - 2*random.uniform(0, 1)
        pv3_current = 0.07 + 1*random.uniform(0, 1)
        pv1_power = pv1_voltage*pv1_current
        pv2_power = pv2_voltage*pv2_current
        pv3_power = 0
        total_power = pv1_power + pv2_power
        rs_grid_voltage = 233.6 + random.randrange(-50, 50)
        st_grid_voltage = rs_grid_voltage + random.randrange(-10, 10)
        tr_grid_voltage = rs_grid_voltage + random.randrange(-10, 10)
        grid_power = 0
        radiator_temperature = 53.5 + random.randrange(-10, 10)
        module_temperature = 60 + random.randrange(-10, 10)
        alarm_code = 0
        annual_energy = random.randrange(1600, 2000)
        daily_energy = 11
        apparent_power = 6483
        reactive_power = 655354 + random.randrange(-10000, 10000)
        power_factor = 1000
        # timesend = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        timesend = my_time.strftime("%Y-%m-%d %H:%M:%S")
        recorded_at = timesend
        total_energy = random.randrange(-10000, 10000)
        # print(pv1_voltage)
        # print(pv2_voltage)
        # print(pv3_voltage)
        # print(pv1_current)
        # print(pv2_current)
        # print(pv3_current)
        # print(pv1_power)
        # print(pv2_power)
        # print(pv3_power)
        # print(total_power)
        # print(rs_grid_voltage)
        # print(st_grid_voltage)
        # print(tr_grid_voltage)
        # print(grid_power)
        # print(radiator_temperature)
        # print(module_temperature)
        # print(alarm_code)
        # print(annual_energy)
        # print(daily_energy)30
        # print(apparent_power)
        # print(power_factor)
        # print(recorded_at)
        data = {
            "mac": 1,
            "pv1_voltage": pv1_voltage,
            "pv2_voltage": pv2_voltage,
            "pv3_voltage": pv3_voltage,
            "pv1_current": pv1_current,
            "pv2_current": pv2_current,
            "pv3_current": pv3_current,
            "pv1_power": pv1_power,
            "pv2_power": pv2_power,
            "pv3_power":  pv3_power,
            "rs_grid_voltage":  rs_grid_voltage,
            "st_grid_voltage":  st_grid_voltage,
            "tr_grid_voltage": tr_grid_voltage,
            "grid_power": grid_power,
            "radiator_temperature": radiator_temperature,
            "module_temperature":  module_temperature,
            "total_energy": total_energy,
            "alarm_code":  alarm_code,
            "annual_energy": annual_energy,
            "daily_energy": daily_energy,
            "apparent_power": apparent_power,
            "reactive_power": reactive_power,
            "power_factor": power_factor,
            "recorded_at": timesend
        }
        datalist.append(data)
        my_time = my_time + datetime.timedelta(seconds=30*timedelay*2)
    return datalist
