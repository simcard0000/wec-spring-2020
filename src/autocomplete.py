import requests
import json

key = ''
url = "https://eastus.api.cognitive.microsoft.com/bing/v7.0/suggestions"

with open('../auth.txt', 'r') as file:
    data = file.read().split(' ')
    for i, x in enumerate(data):
        if x == 'Ocp-Apim-Subscription-Key':
            key = data[i + 1]

headers = {
    'Ocp-Apim-Subscription-Key': key
}


def getSuggestions(query: str) -> list:
    params = {'q': query}
    response = requests.get(url, headers=headers, params=params)
    response_dict = json.loads(response.content)
    suggestion_list = [x['displayText'] for x in response_dict['suggestionGroups'][0]['searchSuggestions']]
    return suggestion_list
