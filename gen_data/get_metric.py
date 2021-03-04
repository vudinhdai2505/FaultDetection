import csv
import requests
import sys
import schedule
import time
from itertools import zip_longest
# def GetMetrixNames(url):
#     response = requests.get('{0}/api/v1/label/__name__/values'.format(url))
#     names = response.json()['data']
#     #Return metrix names
#     return names
# """
# Prometheus hourly data as csv.
# """
#
# metrixNames=GetMetrixNames(sys.argv[1])
queryState = []
#print(len(metrixNames))
a1 = '100 - (avg by (instance) (rate(node_cpu_seconds_total{instance="worker01", mode="idle"}[1m])) * 100)'
a2 = 'sum(node_load5{instance="worker01"}) / count(node_cpu_seconds_total{mode="system",instance="worker01"}) *100'
a3 = '100 - (sum(node_memory_MemAvailable_bytes{instance="worker01"}) / sum(node_memory_MemTotal_bytes{instance="worker01"}) *100)'
a4 = '(sum(node_filesystem_size_bytes{instance="worker01"}) - sum(node_filesystem_free_bytes{instance="worker01"})) / sum(node_filesystem_size_bytes{instance="worker01"}) *100'
a5 = 'sum(rate(node_disk_read_bytes_total{instance="worker01"}[1m]))/1048576'               #1024*1024
a6 = 'sum(rate(node_disk_written_bytes_total{instance="worker01"}[1m]))/1048576'
a7 = 'sum(rate(node_network_receive_bytes_total{device="ens3", instance="worker01"}[1m]))/1024'
a8 = 'sum(rate(node_network_transmit_bytes_total{device="ens3", instance="worker01"}[1m]))/1024'
test = []
metrixName = {"Node_CPU_Utiliztion": a1, "Node_Load_Average": a2, "Node Memory Utilization": a3, "Node_Disk_Utilization" : a4,
              "Node_Disk_read_MB" : a5, "Node_Disk_write_MB": a6, "Node_network_receive_kb" : a7, "Node_network_transmit_kb": a8}


#print(metrixName)
def get_metric():
    f = open('test.csv', 'a')
    with f:
        writer = csv.writer(f)
        for metrix in metrixName.keys():
             response = requests.get('{0}/api/v1/query'.format(sys.argv[1]), params={'query': metrixName[metrix]})
             results = response.json()['data']['result'][0]['value'][1]
             results = float(results)
             results = round(results, 3)
             test.append(results)
        writer.writerow(test)
schedule.every(30).seconds.do(get_metric)
while True:
    schedule.run_pending()
    time.sleep(1)