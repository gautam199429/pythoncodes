import urllib.parse
import urllib.request
from urllib.request import urlopen

url = 'http://devapi.gstsystem.co.in/taxpayerapi/v0.2/authenticate/'
clientid = 'l7xx5edefdd923ad438eb5b332a73269f812'
client_secret = '383dc1f4835f43ad80f80f6cf284cd7b'
ip_usr = '192.168.0.5'
state_cd = '33'
txn = 'LAPN24235325555'
userid = 'balaji.tn.1'
values = {
    'action': 'AUTHTOKEN',
    'app_key': 'R5UxqYG0yAmnE5mGGTliRn2RvmX+AJWAY1fjDfvnnTD/p2GEHQKTPqlFV/qPr1Rp4zs08Pk/AwzKPnzALovqJKSWYqpz4zNua+L5iRz7k/5IY87HuHyB9DDcXPwYBMxjI7Sf0+vOAUDTLrF7l8IAN3J0dTnfTi85TGWZTSH0cqOyR82FEe7smWkBuTmitoE3Q43QJmK5X7musHHFqsGVkNRxuYpz6/f9bbY5dWDlnxl8JXa5s0zhITU0Z/LIZmAo+rfQBlgLnnXs2IftPnkW6OOO9MTfkW3dOGqcgS6pDFqav0xJeWgXcdJ6c2KCRf24xtc7MraTNz9sZqr/R9DIhw==',
    'username': 'balaji.tn.1',
    'otp': 'JrRsYBBmQYE9XdXNh+2w6Q=='
    }
data = {}
data['action'] = 'AUTHTOKEN'
data['app_key'] = 'R5UxqYG0yAmnE5mGGTliRn2RvmX+AJWAY1fjDfvnnTD/p2GEHQKTPqlFV/qPr1Rp4zs08Pk/AwzKPnzALovqJKSWYqpz4zNua+L5iRz7k/5IY87HuHyB9DDcXPwYBMxjI7Sf0+vOAUDTLrF7l8IAN3J0dTnfTi85TGWZTSH0cqOyR82FEe7smWkBuTmitoE3Q43QJmK5X7musHHFqsGVkNRxuYpz6/f9bbY5dWDlnxl8JXa5s0zhITU0Z/LIZmAo+rfQBlgLnnXs2IftPnkW6OOO9MTfkW3dOGqcgS6pDFqav0xJeWgXcdJ6c2KCRf24xtc7MraTNz9sZqr/R9DIhw=='
data['username'] = 'balaji.tn.1'
data[''] = 'JrRsYBBmQYE9XdXNh+2w6Q=='

headers = {
    'Content-Type': 'application/json',
    'clientid': clientid,
    'client-secret': client_secret,
    'ip-usr': ip_usr,
    'state-cd': state_cd,
    'txn': txn,
    'UserId': userid
    }

data = urllib.parse.urlencode(data)

data = data.encode('ascii')

req = urllib.request.Request(url, data, headers=headers)
print(req) 
with urllib.request.urlopen(req) as response:
   the_page = response.read()
