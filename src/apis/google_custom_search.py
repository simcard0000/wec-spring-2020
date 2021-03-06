import requests
import os
import json
from dotenv import load_dotenv, find_dotenv


class GoogleCustomSearch():
    def __init__(self):
        self.URL = 'https://www.googleapis.com/customsearch/v1?'

    # Google custom search engine credentials
    def get_credentials(self) -> tuple:
        load_dotenv(find_dotenv())
        return os.getenv('GOOGLE_API_KEY'), os.getenv('GOOGLE_CUSTOM_SEARCH_ENGINE_ID')

    # Extracts only relevant content from results json and returns a
    # list of dict objects each containing the following content:
    # - title
    # - snippet
    # - url (aka formatted url)
    def get_filtered_results(self, results_json: dict) -> list:
        filtered_results = []
        items = results_json['items']

        for item in items:
            search_result = {
                'title': item['title'] if 'title' in item else None,
                'snippet': item['snippet'] if 'snippet' in item else None,
                'url': item['formattedUrl'] if 'formattedUrl' in item else None
            }
            filtered_results.append(search_result)

        return filtered_results

    # Performs a search for the given query. Returns max 100 results
    def search(self, query: str) -> list:
        key, engineID = self.get_credentials()
        filtered_results_all = []

        # Each API call returns max 10 results. Perform the call 10 times to retrieve (max) all 100 results
        for i in range(10):
            payload = {'key': key, 'cx': engineID, 'q': query, 'start': i*10}
            res = requests.get(self.URL, params=payload)
            res_json = res.json()

            # Check for maximum API quota exceeded
            if 'error' in res_json:
                print(res_json)
                return []

            filtered_res = self.get_filtered_results(res_json)

            filtered_results_all += filtered_res

            # Exit if last page or no more results
            if len(filtered_res) < 10:
                break

        return filtered_results_all

    # Sample search
    def test_search(self):
        filtered_results = self.search('cat')
        print('Number of results:', len(filtered_results))
        with open('testing_data/filtered_results.json', 'w') as f:
            f.write(json.dumps(filtered_results, indent=4))