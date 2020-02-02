# 30 min = 180 deg
# 15 min = 90 deg
# 1 min = 6 deg

time = input("Enter a time: ").split(':')
minute = int(time[1])
hour = (int(time[0]) % 12)
hm = hour*5 + minute // 12
diff = abs(minute - hm)
if diff > 30:
    diff = 60 - diff
print (diff*6)
print (hm)