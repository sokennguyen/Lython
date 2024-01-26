import time

i = 0
increase = True

while True:
    print(' ' * i + '*****')
    time.sleep(0.005)
    if increase:
        i += 1
        if i == 100:
            increase = False

    else:
        i -= 1
        if i == 0:
            increase = True
