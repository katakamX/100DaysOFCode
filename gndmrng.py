import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamph = int(time.strftime('%H'))

timestampm = int(time.strftime('%M'))

timestamps = int(time.strftime('%S'))

# https://docs.python.org/3/library/time.html#time.strftime
print("hour : ", timestamph)
print("minute : ", timestampm)
print("second : ", timestamps)

if timestamph < 12 :
    print("good morning my nigga")
elif timestamph >= 12 and timestamph < 18 :
    print("good afternoon my nigga")
elif timestamph > 18  :
    print("good night my nigga")
    
    