from langchain_groq import ChatGroq
from dotenv import load_dotenv

class LLMs:
    def planning_llm(self):
        return ChatGroq(model="groq/llama-3.1-70b-specdec")
    def search_db_llm(self):
        return ChatGroq(model="groq/llama-3.1-70b-versatile")
    def update_db_llm(self):
        return ChatGroq(model="groq/llama-3.3-70b-versatile")
    def text_to_query_llm(self):
        return ChatGroq(model="groq/llama-3.3-70b-versatile")