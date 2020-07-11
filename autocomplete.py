import requests

response = requests.get(
    "https://eastus.api.cognitive.microsoft.com/bing/v7.0/suggestions",
    params={'q': 'hello', 'Ocp-Apim-Subscription-Key': 'f778d2410d5948398ea947128b325e48'}
)

print(response.content)