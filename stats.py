import psutil
# print(psutil.sensors_temperatures())

battery=psutil.sensors_battery()
percent,minsLeft=battery.percent,battery.secsleft//60
print(percent,minsLeft)
# print(psutil.cpu_count()) #NO OF CORES
# print(psutil.cpu_stats()) #CPU STATS
# print(psutil.cpu_freq()) #CPU FREQ
# print(psutil.cpu_percent()) #CPU PERCENT