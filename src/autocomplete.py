import requests
import json
import os
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())
key = os.getenv('Ocp-Apim-Subscription-Key')
url = "https://eastus.api.cognitive.microsoft.com/bing/v7.0/suggestions"

headers = {
    'Ocp-Apim-Subscription-Key': key
}


def getSuggestions(query: str) -> list:
    params = {'q': query}
    response = requests.get(url, headers=headers, params=params)
    response_dict = json.loads(response.content)
    suggestion_list = [x['displayText'] for x in response_dict['suggestionGroups'][0]['searchSuggestions']]
    return suggestion_list
