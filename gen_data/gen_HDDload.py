import random
import os
import schedule
import time

def gen_HDDload():
#    mem_load = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
    hdd_load = [10, 15, 20, 25, 30, 35, 40, 45]
    random.shuffle(hdd_load)
    hdd = random.randint(0,len(hdd_load) -1)
    hdd_string = str(hdd_load[hdd]) + "%"
    cmd = 'stress-ng --hdd 1 --hdd-bytes {0} --timeout 10m'.format(hdd_string)
    os.system(cmd)
    print("Task: " + cmd)
schedule.every(20).minutes.do(gen_MEMload)
while True:
     schedule.run_pending()
     time.sleep(1)
