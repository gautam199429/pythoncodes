import requests

action = input("Enter Action:-  ")
username = input("Enter Username:-  ")
app_key = input("Enter App_key:- ")
otp = input("Enter OTP:- ")
clientid = input("Enter Client ID:- ")
clientsec = input("Enter Client Secret:- ")
ip_usr = input("Enter IP Address:- ")
state_cd = input("Enter State Code:- ")
txn = input("Enter Txn Number:- ")
userid = input("Enter username:- ")
payload = {'action': action, 'username': username, 'otp': otp, 'app_key': app_key}
headers = {'clientid': clientid, 'client-secret': clientsec, 'ip-usr': ip_usr, 'state-cd': state_cd, 'txn': txn, 'UserId': userid}
r = requests.post("http://devapi.gstsystem.co.in/taxpayerapi/v0.2/authenticate", json=payload, headers=headers)
print(r.text)
print(r.headers)



