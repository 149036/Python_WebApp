import requests
headers = {
    'Content-Type' : 'application/json'
}


data = '{"name":"dummy", "age":21, "friends":["dummy1", "dummy2", "dummy3"], "is_man":false}' 

resopnse = requests.post('http://127.0.0.1:5000/try_rest', headers=headers, data=data)