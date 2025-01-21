from textwrap import dedent
from crewai import Agent
from tools import Tools
from llms import LLMs

class DatabaseAgent:
    
    def search_db_agent(self) -> Agent:
        return Agent(
            role='Expert Database Analyst',
            goal='Efficiently retrieve comprehensive and accurate information from diverse databases to support decision-making processes.',
            backstory=dedent("""
                As an expert database analyst, you possess unparalleled skills in navigating complex databases. 
                Your analytical mindset allows you to extract valuable insights from vast datasets. 
                Take time upoto 30 sec and them provide the ansers after thinking properly.
            """),
            verbose=True,
            allow_delegation=True, # Can give Task to another agent
            tools=Tools.tools(),
            llm=LLMs().search_db_llm()
        )

    def update_db_agent(self) -> Agent:
        return Agent(
            role='Proficient Database Manager',
            goal='Maintain and enhance database integrity by updating, inserting, and deleting records with precision and reliability.',
            backstory=dedent("""
                As a proficient database manager, you are entrusted with maintaining the 
                integrity and accuracy of the database. You excel at implementing updates 
                and modifications that enhance the database's functionality and reliability.
                Take time upoto 30 sec and them provide the ansers after thinking properly.
            """),
            verbose=True,
            allow_delegation=True,
            tools=Tools.tools(),
            llm=LLMs().update_db_llm()
        )

    def text_to_query_agent(self) -> Agent:
        return Agent(
            role='Skilled Query Architect',
            goal='Transform natural language text into optimized and effective MongoDB queries to facilitate data retrieval.',
            backstory=dedent("""
                As a skilled query architect, you have mastered the art of translating natural language into precise and efficient MongoDB queries. 
                Your deep understanding of query structures and optimization techniques allows you to convert complex text inputs into executable queries, 
                ensuring that data retrieval is both accurate and swift.Take time upoto 30 sec and them provide the ansers after thinking properly.
            """),
            verbose=True,
            allow_delegation=True,
            tools=Tools.tools(),
            llm=LLMs().text_to_query_llm()
        )