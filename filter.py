import json

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
        if 'from_site' in args and any(x in result['url'] for x in args['from_site']):
            valid = True
        else:
            if any(x in result['url'] for x in whitelist):
                valid = True

        if 'ignore_site' in args and any(x in result['url'] for x in args['ignore_site']):
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


def filter(all_results: list, args: dict) -> list:
    for i, result_list in enumerate(all_results):
        for x in filter_results(result_list, args):
            all_results[i] = filter_results(result_list, args)
    return combine_results(all_results)


y = filter([[
    {
        "title": "Cat | global-selector | Caterpillar",
        "link": "www.cat.com",
        "snippet": "Genuine enabler of sustainable world progress and opportunity, defined by the \nbrand attributes of global leadership, innovation and sustainability.",
        "url": "https://www.cat.com/"
    },
    {
        "title": "Cat - Wikipedia",
        "link": "en.wikipedia.org",
        "snippet": "The cat (Felis catus) is a domestic species of small carnivorous mammal. It is the \nonly domesticated species in the family Felidae and is often referred to as the\u00a0...",
        "url": "https://en.wikipedia.org/wiki/Cat"
    },
    {
        "title": "Cat Footwear: Caterpillar Work Boots - Comfortable Work Shoes",
        "link": "www.catfootwear.com",
        "snippet": "Official Cat Footwear Site - Shop Caterpillar work boots, steel toe work boots & \nshoes along with casual shoes & casual boots. Free shipping!",
        "url": "https://www.catfootwear.com/US/en/home"
    },
    {
        "title": "Caterpillar | Caterpillar",
        "link": "www.caterpillar.com",
        "snippet": "5 days ago ... Caterpillar Inc. Company information, investor information, news and careers. Cat \nproducts and services. Dow Jones Top 30. NYSE Symbol\u00a0...",
        "url": "https://www.caterpillar.com/en.html"
    }],
    [{
        "title": "Cats are so funny you will die laughing - Funny cat compilation ...",
        "link": "www.youtube.com",
        "snippet": "Dec 24, 2016 ... Cats are simply the funniest and most hilarious pets, they make us laugh all the \ntime! Just look how all these cats & kittens play, fail, get along\u00a0...",
        "url": "https://www.youtube.com/watch?v=5dsGWM5XGdg"
    },
    {
        "title": "Cat phones: Rugged Phones",
        "link": "www.catphones.com",
        "snippet": "Welcome to Cat\u00ae phones. Discover a range of rugged phones with waterproof, \ndust and drop proof features & long battery life built to last.",
        "url": "https://www.catphones.com/"
    },
    {
        "title": "Cat and Dog Road Trip - YouTube",
        "link": "www.youtube.com",
        "snippet": "Feb 5, 2020 ... Prince Michael and his new friend, Bob, set out for a road trip in the brand new \nfilm Cat and Dog Road Trip. Turn on Closed Captions for Prince\u00a0...",
        "url": "https://www.youtube.com/watch?v=o1YA_6tXs5E"
    },
    {
        "title": "Cat Care | Grooming | Nutrition | Disease | Behavior | ASPCA",
        "link": "www.aspca.org",
        "snippet": "Cat Care. Do you have a feline companion? We've got you covered. Our ASPCA \nveterinarians and behaviorists offer up tips, solutions and answers to some of\u00a0...",
        "url": "https://www.aspca.org/pet-care/cat-care"
    },
    {
        "title": "World's First Cat Lifeguard - YouTube",
        "link": "www.youtube.com",
        "snippet": "Sep 12, 2019 ... Aaron's Animals - World's First Cat Lifeguard Prince Michael sets to achieve his \ngoal of becoming the world's first cat lifeguard. Turn on Closed\u00a0...",
        "url": "https://www.youtube.com/watch?v=x3sUOqHkNt4"
    },
    {
        "title": "Cat Health Center | Cat Care and Information from WebMD",
        "link": "pets.webmd.com",
        "snippet": "WebMD veterinary experts provide comprehensive information about cat health \ncare, offer nutrition and feeding tips, and help you identify illnesses in cats.",
        "url": "https://pets.webmd.com/cats/default.htm"
    }
]], {'from_site': ('pets.webmb.com',)}
)

for x in y:
    print(x['url'])


