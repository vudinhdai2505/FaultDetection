import random
import os
import schedule
import time


def gen_CPUload01():
 #   cpu_load = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
    cpu_load = [20, 22, 24, 28, 32, 34, 36]
    random.shuffle(cpu_load)
    cpu = random.randint(0,len(cpu_load) -1)
    cmd = 'stress-ng --cpu 4 --cpu-load {0} --timeout 5m'.format(cpu_load[cpu])
    print("Task: " + cmd)
    os.system(cmd)
def gen_CPUload02():
 #   cpu_load = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
    cpu_load = [40, 42, 46, 48, 50, 54, 56]
    random.shuffle(cpu_load)
    cpu = random.randint(0,len(cpu_load) -1)
    cmd = 'stress-ng --cpu 4 --cpu-load {0} --timeout 5m'.format(cpu_load[cpu])
    print("Task: " + cmd)
    os.system(cmd)
def gen_CPUload03():
    #   cpu_load = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
    cpu_load = [60, 62, 64, 66, 70, 72]
    random.shuffle(cpu_load)
    cpu = random.randint(0, len(cpu_load) - 1)
    cmd = 'stress-ng --cpu 4 --cpu-load {0} --timeout 5m'.format(cpu_load[cpu])
    print("Task: " + cmd)
    os.system(cmd)
def gen_CPUload04():
    #   cpu_load = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
    cpu_load = [82, 84, 86, 88]
    random.shuffle(cpu_load)
    cpu = random.randint(0, len(cpu_load) - 1)
    cmd = 'stress-ng --cpu 4 --cpu-load {0} --timeout 5m'.format(cpu_load[cpu])
    print("Task: " + cmd)
    os.system(cmd)
schedule.every(30).minutes.do(gen_CPUload01)
schedule.every(35).minutes.do(gen_CPUload02)
schedule.every(40).minutes.do(gen_CPUload03)
schedule.every(45).minutes.do(gen_CPUload04)

while True:
    schedule.run_pending()
    time.sleep(1)