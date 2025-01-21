from langchain_groq import ChatGroq
from dotenv import load_dotenv

class LLMs:
    def planning_llm(self):
        return ChatGroq(model="groq/llama-3.1-70b-versatile")
    def research_llm(self):
        return ChatGroq(model="groq/llama-3.3-70b-versatile")
    def analysis_llm(self):
        return ChatGroq(model="groq/llama-3.3-70b-versatile")
    def dessision_presentation_llm(self):
        return ChatGroq(model="groq/llama-3.1-70b-versatile")