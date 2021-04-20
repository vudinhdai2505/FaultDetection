import random
import os
import schedule
import time


def gen_MEMload():
    mem_load1 = [10, 11, 12, 13, 14, 15]
    random.shuffle(mem_load1)
    mem1 = random.randint(0, len(mem_load1) - 1)
    mem_string1 = str(mem_load1[mem1]) + "%"
    cmd1 = 'stress-ng --vm 1 --vm-bytes {0} --timeout 5m'.format(mem_string1)
    print("Task: " + cmd1)
    os.system(cmd1)


    mem_load2 = [25, 27, 30, 29, 31, 32]
    random.shuffle(mem_load2)
    mem2 = random.randint(0, len(mem_load2) - 1)
    mem_string2 = str(mem_load2[mem2]) + "%"
    cmd2 = 'stress-ng --vm 1 --vm-bytes {0} --timeout 5m'.format(mem_string2)
    print("Task: " + cmd2)
    os.system(cmd2)

    mem_load3 = [38, 39, 42, 44, 46, 48]
    random.shuffle(mem_load3)
    mem3 = random.randint(0, len(mem_load3) - 1)
    mem_string3 = str(mem_load3[mem3]) + "%"
    cmd3 = 'stress-ng --vm 1 --vm-bytes {0} --timeout 5m'.format(mem_string3)
    print("Task: " + cmd3)
    os.system(cmd3)

    mem_load4 = [68, 70, 72, 74, 76, 78]
    random.shuffle(mem_load4)
    mem4 = random.randint(0, len(mem_load4) - 1)
    mem_string4 = str(mem_load4[mem4]) + "%"
    cmd4 = 'stress-ng --vm 1 --vm-bytes {0} --timeout 5m'.format(mem_string4)
    print("Task: " + cmd4)
    os.system(cmd4)
schedule.every(20).minutes.do(gen_MEMload)
#schedule.every(35).minutes.do(gen_CPUload02)
#schedule.every(41).minutes.do(gen_CPUload03)
#schedule.every(47).minutes.do(gen_CPUload04)

while True:
    schedule.run_pending()
    time.sleep(1)
