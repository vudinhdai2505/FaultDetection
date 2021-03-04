import random
import os
import schedule
import time

def gen_MEMload():
#    mem_load = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
    mem_load = [10, 15, 20, 25, 30, 35, 40, 45, 50]
    random.shuffle(mem_load)
    print(mem_load)
    mem = random.randint(0,len(mem_load) -1)
    mem_string = str(mem_load[mem]) + "%"
    cmd = 'stress-ng --vm 1 --vm-bytes {0} --timeout 15m'.format(mem_string)
    os.system(cmd)
    print("Task: " + cmd)
schedule.every(10).minutes.do(gen_MEMload)
while True:
    schedule.run_pending()
    time.sleep(1)
