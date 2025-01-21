#Duck duck go search
from duckduckgo_search import DDGS

#search_query = input("Enter your search query: ")
search_query ="ai agents"

# Perform the search
results = DDGS().text(
    keywords = search_query,
    region = "wt-wt",
    safesearch = "off",
    timelimit = '10d',
    max_results = 3
    )


body_element = [result['body'] for result in results]
print(body_element)