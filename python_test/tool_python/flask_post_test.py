import requests

payload = {'name': 'mike'}
r = requests.post('http://127.0.0.1:5000/employee', params=payload)
print(r.status_code)
print(r.text)

payload = {'name': 'mike', 'new_name': 'mike2'}
r = requests.put('http://127.0.0.1:5000/employee', params=payload)
print(r.status_code)
print(r.text)

payload = {'name': 'mike'}
r = requests.delete('http://127.0.0.1:5000/employee', params=payload)
print(r.status_code)
print(r.text)
