import requests
import json

url = 'http://localhost:5000'

# Create Account
create_url = f'{url}/create_account'
account_details = {'account_id': '123', 'initial_balance': 100}
response = requests.post(create_url, json=account_details)
print(response.json())

# Get Account Details
account_id = '123'
get_url = f'{url}/account/{account_id}'
response = requests.get(get_url)
print(response.json())

# Deposit
deposit_url = f'{url}/deposit'
deposit_data = {'account_id': '123', 'amount': 50}
response = requests.post(deposit_url, json=deposit_data)
print(response.json())

# Withdraw
withdraw_url = f'{url}/withdraw'
withdraw_data = {'account_id': '123', 'amount': 25}
response = requests.post(withdraw_url, json=withdraw_data)
print(response.json())

#Try to withdraw amout from accoount doesn' exist lib

withdraw_data = {'account_id': '125', 'amount': 50}
response = requests.post(withdraw_url, json=withdraw_data)
print(response.json())


