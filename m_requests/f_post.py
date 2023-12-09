import requests


with open('user_data_test2.json') as inputfile:
    json_file = inputfile.read()

response = requests.post('http://93.95.97.207/users', data=json_file)
# response = requests.post('http://127.0.0.1:5000', data = {'login':{}})


print(response.text)

