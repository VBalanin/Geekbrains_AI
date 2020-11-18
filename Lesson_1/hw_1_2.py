time_sec = int(input('Input time in sec:'))
time_in_hr = time_sec // 3600
time_in_min = (time_sec - time_in_hr * 3600) // 60
time_in_sec = (time_sec - time_in_hr * 3600) % 60
if time_in_hr // 10 == 0:
    time = format("0%d" % time_in_hr)
else:
    time = format("%d" % time_in_hr)
if time_in_min // 10 == 0:
    time_in_min = format("0%d" % time_in_min)
else:
    time_in_min = format("%d" % time_in_min)
if time_in_sec // 10 == 0:
    time_in_sec = format("0%d" % time_in_sec)
else:
    time_in_sec = format("%d" % time_in_sec)
time = ':'.join([time, time_in_min, time_in_sec])
print(time)
