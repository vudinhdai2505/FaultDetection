import random
import os
import schedule
import time


def gen_CPUload():
 #   cpu_load = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
    cpu_load = [10, 15, 20, 25, 30, 35, 40, 45, 50, 60]
    random.shuffle(cpu_load)
    cpu = random.randint(0,len(cpu_load) -1)
    cmd = 'stress-ng --cpu 4 --cpu-load {0} --timeout 20m'.format(cpu_load[cpu])
    os.system(cmd)
    print("Task: " + cmd)
schedule.every(35).minutes.do(gen_CPUload)
while True:
    schedule.run_pending()
    time.sleep(1)
