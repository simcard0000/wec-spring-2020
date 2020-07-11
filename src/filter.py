whitelist = [
    # whitelisted TLDs
    '.edu', '.gov',
    # general
    'coursera.org', 'edx.org', 'academicearth.org',
    'khanacademy.org', 'researchgate.net', 'libretexts.org',
    'wikipedia.org', 'jstor.org', 'academicwebpages.com',
    'udemy.org', 'openculture.com', 'alison.com', 'freecodecamp.org',
    'codecademy.com', 'oxfordre.com', 'libraryspot.com', 'britannica.com',
    'rand.org', 'russellsage.org'
    # canadian universities
    'ubc.ca', 'uwaterloo.ca', 'utoronto.ca', 'mcmaster.ca', 'queensu.ca', 'ucalgary.ca', 'ualberta.ca',
    'yorku.ca', 'umontreal.ca', 'uottawa.ca', 'uwo.ca', 'mcgill.ca', 'ulaval.ca',
    # online solvers
    'www.symbolab.com', 'www.wolframalpha.com'
]


# takes in a list of dictionaries
def filter_results(results: list, args: dict) -> list:
    filtered = list()
    valid = False
    for result in results:
        if 'from_sites' in args:
            if any(x in result['url'] for x in args['from_sites']):
                valid = True
        else:
            if any(x in result['url'] for x in whitelist):
                valid = True

        if 'ignore_sites' in args and any(x in result['url'] for x in args['ignore_sites']):
            valid = False
        if valid:
            filtered.append(result)
        valid = False
    return filtered


def combine_results(all_results: list) -> list:
    unique_urls = set()
    combined = list()
    for result_list in all_results:
        for result in result_list:
            if result['url'] not in unique_urls:
                combined.append(result)
                unique_urls.add(result['url'])
    return(combined)


# accepted args:
    # 'from_sites' : tuple of strings
    # 'ignore_sites' : tuple of strings
def filter(all_results: list, args: dict) -> list:
    filtered = list()
    for result_list in all_results:
        for x in filter_results(result_list, args):
            filtered.append(filter_results(result_list, args))
    return combine_results(filtered)


