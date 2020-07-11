import requests

key = ''
url = "https://eastus.api.cognitive.microsoft.com/bing/v7.0/suggestions"

with open('auth.txt', 'r') as file:
    data = file.read().split(' ')
    for i, x in enumerate(data):
        if x == 'Ocp-Apim-Subscription-Key':
            key = data[i+1]


payload = {}
params = {'q': "hello"}
headers = {
'Ocp-Apim-Subscription-Key': key
}


response = requests.get(url, headers=headers, params=params, data=payload)

print(response.content)