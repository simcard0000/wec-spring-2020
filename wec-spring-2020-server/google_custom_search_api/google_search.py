import requests
import os
import json
from dotenv import load_dotenv

url = 'https://www.googleapis.com/customsearch/v1?'

# Google custom search engine credentials
def get_credentials() -> tuple:
    load_dotenv()
    return os.getenv('GOOGLE_API_KEY'), os.getenv('GOOGLE_CUSTOM_SEARCH_ENGINE_ID')

# Extracts only relevant content from results json and returns a 
# list of dict objects each containing the following content:
# - title
# - link (aka display link)
# - snippet
# - url (aka formatted url)
def get_filtered_results(results_json: dict) -> list:
    filtered_results = []
    items = results_json['items']

    for item in items:
        search_result = {
            'title': item['title'],
            'link': item['displayLink'],
            'snippet': item['snippet'],
            'url': item['formattedUrl']
        }
        filtered_results.append(search_result)

    return filtered_results


def test_search():
    key, engineID = get_credentials()
    query = 'some test query string'
    payload = {'key': key, 'cx': engineID, 'q': query}

    res = requests.get(url, params=payload)
    filtered_res = get_filtered_results(res.json())

    print(json.dumps(filtered_res, indent=4))

if __name__ == '__main__':
    test_search()