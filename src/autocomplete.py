import requests
import json
import os
import dotenv

class AutoComplete:
    def __init__(self):
        dotenv.load_dotenv(dotenv.find_dotenv())
        self.key = os.getenv('Ocp-Apim-Subscription-Key')
        self.url = "https://eastus.api.cognitive.microsoft.com/bing/v7.0/suggestions"

        self.headers = {
            'Ocp-Apim-Subscription-Key': self.key
        }

    def getSuggestions(self, query: str) -> list:
        params = {'q': query}
        response = requests.get(self.url, headers=self.headers, params=params)
        response_dict = json.loads(response.content)
        suggestion_list = [x['displayText'] for x in response_dict['suggestionGroups'][0]['searchSuggestions']]
        return suggestion_list
