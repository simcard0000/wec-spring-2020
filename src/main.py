from autocomplete import AutoComplete
from filter import Filter
from apis.google_custom_search import GoogleCustomSearch
from apis.google_scholar import GoogleScholar


class SearchHandler:
    def __init__(self):
        self.autoComplete = AutoComplete()
        self.resultFilter = Filter()
        self.googleCustom = GoogleCustomSearch()
        self.googleScholar = GoogleScholar()


    def search(self, query: str, from_sites: tuple=None, ignore_sites: tuple=None):
        args = dict()
        results = list()
        if from_sites:
            args['from_sites'] = from_sites
        if ignore_sites:
            args['ignore_sites'] = ignore_sites

        results.append(self.googleCustom.search(query))
        results.append(self.googleScholar.search(query))

        filtered = self.resultFilter.filter(results, args)
        return filtered



