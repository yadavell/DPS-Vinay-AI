import requests
 
url = "https://dps-vinay.herokuapp.com/"
 
data = {
    "year": 2021,
    "month": 10
}
 
response = requests.post(url, json=data)
 
print("Status Code", response.status_code)
