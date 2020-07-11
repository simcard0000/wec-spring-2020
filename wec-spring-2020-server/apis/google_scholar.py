import requests
import os
import json
from dotenv import load_dotenv

from serpapi.google_search_results import GoogleSearchResults


# Google API credentials
def get_credentials() -> str:
    load_dotenv()
    return os.getenv('SERPAPI_KEY')


# Extracts only relevant content from results json and returns a 
# list of dict objects each containing the following content:
# - title
# - snippet
# - url (aka formatted url)
def get_filtered_results(results_json: dict) -> list:
    filtered_results = []

    for item in results_json:
        search_result = {
            'title': item['title'] if 'title' in item else None,
            'snippet': item['snippet'] if 'snippet' in item else None,
            'url': item['link'] if 'link' in item else None
        }
        filtered_results.append(search_result)

    return filtered_results


# Performs a search for the given query
def search(query: str) -> list:
    key = get_credentials()

    params = {
        'engine': 'google_scholar',
        'q': query,
        'api_key': key
    }

    client = GoogleSearchResults(params)
    res = client.get_dict()

    filtered_res = get_filtered_results(res['organic_results'])
    return filtered_res


# Sample search
def test_search():
    filtered_results = search('cat')
    print('Number of results:', len(filtered_results))
    with open('testing_data/filtered_results.json', 'w') as f:
        f.write(json.dumps(filtered_results, indent=4))


if __name__ == '__main__':
    test_search()