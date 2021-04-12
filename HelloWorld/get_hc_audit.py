import requests
import time
import json

curr_time_in_ms=int(time.time()) * 1000

#num_of_months=input("Please provide how many months of audit logs you need, 1 or 2 or 3 etc : ")
  
num_of_months = -1
while num_of_months < 0:
  try:
     num_of_months = int(input("\nPlease provide how many months of Harmony Audit logs need to display, 1 or 2 or 3 etc : "))       
  except ValueError:
     print("Not an integer, please provide numeric for months\n")
     continue
  else:
    # print("Yes an integer!")
     break 
  
if num_of_months < 0:
    print("Months can't be negative integers, please provide correct positive value\n")
     

start_time=curr_time_in_ms - (num_of_months*30*24*3600*1000)
#print(curr_time_in_ms)
#print(start_time)


headers = {
    'Content-type': 'application/json',
    'provider': 'root',
    'x-providerids': '47147174-410a-11ea-ad3d-5e5ef414adc5'
}

#data = '{"total":{"rangeby":{"start":1610749801000,"end":1614292323356,"field":"ts"},"type":"audit","filterby":{"and":{}},"fields":["ts"],"aggregation":"count"},"logs":{"rangeby":{"start":1610749801000,"end":1614292323356,"field":"ts"},"type":"audit","filterby":{"and":{}},"from":0,"size":100,"sort":"desc"},"user":{"rangeby":{"start":1610749801000,"end":1614292323356,"field":"ts"},"fields":["user"],"groupby":"user","type":"audit","size":100,"aggregation":"count"},"client_ip":{"rangeby":{"start":1610749801000,"end":1614292323356,"field":"ts"},"fields":["client_ip"],"groupby":"client_ip","type":"audit","size":100,"aggregation":"count"}}'

data = {"total":{"rangeby":{"start":start_time,"end":curr_time_in_ms,"field":"ts"},"type":"audit","filterby":{"and":{}},"fields":["ts"],"aggregation":"count"},"logs":{"rangeby":{"start":start_time,"end":curr_time_in_ms,"field":"ts"},"type":"audit","filterby":{"and":{}},"from":0,"size":100,"sort":"desc"},"user":{"rangeby":{"start":start_time,"end":curr_time_in_ms,"field":"ts"},"fields":["user"],"groupby":"user","type":"audit","size":100,"aggregation":"count"},"client_ip":{"rangeby":{"start":start_time,"end":curr_time_in_ms,"field":"ts"},"fields":["client_ip"],"groupby":"client_ip","type":"audit","size":100,"aggregation":"count"}}

response = requests.post('https://proddemo.hc.a10networks.com/api/v2/analytics/hc/hc_audit', headers=headers, json=data, auth=('c-success@a10networks.com', 'A10Rocks'))
#print(response.text)

print (json.dumps(response.json(), indent=6, sort_keys=True))
