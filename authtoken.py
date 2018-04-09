import requests
import json
url = 'https://devapi.gstsystem.co.in/taxpayerapi/v0.2/authenticate'
payload = {
    'action': 'AUTHTOKEN',
    'app_key': 'R5UxqYG0yAmnE5mGGTliRn2RvmX+AJWAY1fjDfvnnTD/p2GEHQKTPqlFV/qPr1Rp4zs08Pk/AwzKPnzALovqJKSWYqpz4zNua+L5iRz7k/5IY87HuHyB9DDcXPwYBMxjI7Sf0+vOAUDTLrF7l8IAN3J0dTnfTi85TGWZTSH0cqOyR82FEe7smWkBuTmitoE3Q43QJmK5X7musHHFqsGVkNRxuYpz6/f9bbY5dWDlnxl8JXa5s0zhITU0Z/LIZmAo+rfQBlgLnnXs2IftPnkW6OOO9MTfkW3dOGqcgS6pDFqav0xJeWgXcdJ6c2KCRf24xtc7MraTNz9sZqr/R9DIhw==',
    'username': 'balaji.tn.1',
    'otp': 'JrRsYBBmQYE9XdXNh+2w6Q=='
}
# Adding empty header as parameters are being sent in payload
headers = {
    'Content-Type': 'application/json',
    'clientid': 'l7xx5edefdd923ad438eb5b332a73269f812',
    'client-secret': '383dc1f4835f43ad80f80f6cf284cd7b',
    'ip-usr': '192.168.0.5',
    'state-cd': '33',
    'txn': 'LAPN24235325555',
    'UserId': 'balaji.tn.1',
}
r = requests.post(url, data=json.dumps(payload), headers=headers)
print(r.json)
