import csv
import json
import requests

url = 'https://rest.iad-06.braze.com/email/status'
API_KEY = 'Bearer fa27c31c-e5fe-49c0-b453-f0b30d630beb'

headers = {
    'Content-Type': 'application/json',
    'Authorization': API_KEY
}

with open('Unsubscribes List 1.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        if len(row) == 0:
            continue
        temp = row[0].split(",")
        if temp[0]=="email":
            continue

        body = json.dumps({
            "subscription_state": "unsubscribed",
            "email": temp[0]
        })

        response = requests.post(url, data=body, headers=headers)
        print(response.json())