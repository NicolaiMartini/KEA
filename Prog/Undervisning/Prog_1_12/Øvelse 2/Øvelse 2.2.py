import requests

# Requires internet connection
response=requests.get(url="https://api.energidataservice.dk/dataset/Elspotprices?limit=2")

response=response.json()

for k,v in response.items():
    print(k,v)
    
records=response.get("records",[])

print("Records:")
for record in records:
    print(" ", record)