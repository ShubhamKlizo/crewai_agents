from langchain.agents import tool
from duckduckgo_search import DDGS
from pymongo import MongoClient


class Tools:
    @tool("MongoDB Search Tool")
    def mongodb_search_tool(query: dict, action: str = "find") -> list:
        """Fetch data from MongoDB based on a query and perform specified actions such as 'find', 'insert', 'update', and 'delete'.
        
        **Parameters**:
        - `query` (dict): The query or data for the action to be performed.
        - `action` (str): The action to be performed. Options are 'find', 'insert', 'update', 'delete'. Default is 'find'.
        
        **Returns**:
        - `list` or `dict`: The result of the specified action. For 'find', it returns a list of documents. For 'insert', 'update', and 'delete', it returns a dictionary with the operation's details.
        """
        # Connect to MongoDB
        client = MongoClient("mongo_URL")  # Update with your connection string
        db = client['sample_mflix']  # Replace with your database name
        collection = db['test']  # Replace with your collection name

        if action == "find":
            return list(collection.find(query))  # Fetch documents matching the query
        elif action == "insert":
            result = collection.insert_one(query)  # Insert a new document
            return {"inserted_id": str(result.inserted_id)}
        elif action == "update":
            result = collection.update_one(query['filter'], {"$set": query['update']})  # Update documents
            return {"matched_count": result.matched_count, "modified_count": result.modified_count}
        elif action == "delete":
            result = collection.delete_one(query)  # Delete documents matching the query
            return {"deleted_count": result.deleted_count}
        else:
            return {"error": "Invalid action specified."}
        

    @tool("MongoDB Schema Tool")
    def mongodb_schema_tool() -> dict:
        """Retrieve the schema of the MongoDB collection.
        
        **Returns**:
        - `dict`: A dictionary describing the schema of the collection. Each key is a field name and each value is the type of the field.
        """
        client = MongoClient("mongo_URL")
        db = client['sample_mflix']  # Replace with your database name
        collection = db['movies']  # Replace with your collection name

        # Fetch a sample document to infer the schema
        sample_document = collection.find_one()
        
        if sample_document:
            return {"Schema of the MongoDB collection" : list(sample_document.keys())}
        
        return {"error": "No documents found in the collection."}
        

    @tool("DuckDuckGo Search Tool")
    def duck_duck_go_search(query: str) -> list:
        """Search the internet for relevant information based on a query using DuckDuckGo.
        
        **Parameters**:
        - `query` (str): The search query to be executed.
        
        **Returns**:
        - `list`: A list of search results, where each result contains a brief description or body of the content found.
        """
        # Perform the search
        results = DDGS().text(
            keywords = query,
            region = "wt-wt",
            safesearch = "off",
            max_results = 3
            )
        return [result['body'] for result in results]

    def tools():
        return [
            Tools.mongodb_search_tool,
            Tools.mongodb_schema_tool,
            Tools.duck_duck_go_search
        ]
