time_sec = int(input('Input time in sec:'))
time_in_hr = time_sec//3600
time_in_min = (time_sec-time_in_hr*3600) // 60
time_in_sec = (time_sec-time_in_hr*3600) % 60
# print(time_in_hr, '\n')
# print(time_in_min, '\n')
# print(time_in_sec, '\n')
print("%d:%d:%d" % (time_in_hr, time_in_min, time_in_sec))
