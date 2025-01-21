from duckduckgo_search import DDGS
from langchain.agents import tool

class Tools():
    @tool
    def duck_duck_go_search(query: str) -> list:
        """Search Internet for relevant information based on a query."""
        # Perform the search
        results = DDGS().text(
            keywords = query,
            region = "wt-wt",
            safesearch = "off",
            timelimit = '10d',
            max_results = 3
            )
        return [result['body'] for result in results]
    
    @tool
    def find_similar_website(query: str) -> list:
        """Find similar websites using DuckDuckGo."""
        # Perform the search
        results = DDGS().text(
            keywords = query,
            region = "wt-wt",
            safesearch = "off",
            timelimit = '10d',
            max_results = 3
            )
        return [result['href'] for result in results]
    
    def tools():
        return [
        Tools.duck_duck_go_search,
        Tools.find_similar_website
        ]
    