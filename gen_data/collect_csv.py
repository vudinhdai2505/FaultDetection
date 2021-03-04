import csv
import requests
import sys
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
a = '100 - (avg by (instance) (rate(node_cpu_seconds_total{instance="kubernetes-worker-1",job="kubernetes-nodes",mode="idle"}[1m])) * 100)'
b = 'rate(node_memory_Active_anon_bytes{instance="kubernetes-worker-1",job="kubernetes-nodes"}[1m])'

test = []
metrixName = {"node_cpu_seconds_total": a, "node_memory_MemFree_bytes": b}
print(metrixName.values())
f = open('test.csv', 'a')
with f:
    writer = csv.writer(f)
    for metrix in metrixName.keys():
         response = requests.get('{0}/api/v1/query'.format(sys.argv[1]), params={'query': metrixName[metrix]})
         results = response.json()['data']['result'][0]['value'][1]
         results = round(results, 2)
         test.append(results)
    writer.writerow(test)