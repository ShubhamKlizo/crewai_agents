from textwrap import dedent
from crewai import Agent
from tools import Tools
from llms import LLMs

class ResearcherAgents():
    def researcher_agent(self) -> Agent:
        return Agent(
    role='Researcher',
    goal='Conduct comprehensive research on each of the individuals and companies involved in the upcoming meeting.',
    tools=Tools.tools(),
    backstory=dedent("""\
                        As a seasoned researcher, you have a knack for uncovering hidden gems in the industry.
                        You're also a master of gathering information from various online sources."""),
    verbose=True,
    llm=LLMs().research_llm(),
    allow_delegation=False
    )

    def industry_analyst_agent(self) -> Agent:
        return Agent(
    role='Industry Analyst',
    goal='Analyze the current state of the industry.',
    tools=Tools.tools(),
    backstory=dedent("""\
                        As an industry analyst, you have a deep understanding of the industry's dynamics.
                        You're also a master of gathering information from various online sources."""),
    verbose=True,
    llm=LLMs().analysis_llm(),
    allow_delegation=False
    )
    
    def decission_maker_agent(self) -> Agent:
        return Agent(
    role='Decision Maker',
    goal='Based on the research and industry analysis, form a concise report outlining the main points that should be discussed in the meeting.',
    tools=[],
    backstory=dedent("""\
                        As a seasoned decision maker, you have a knack for crafting clear and concise reports.
                        You're also a master of gathering information from various online sources."""),
    verbose=True,
    llm=LLMs().dessision_presentation_llm(),
    allow_delegation=False
    )

    def presentation_agent(self) -> Agent:  
        return Agent(
    role='Presentation Specialist',
    goal='Based on the concise report, write a concise presentation outlining the main points that should be discussed in the meeting.',
    tools=[],
    backstory=dedent("""\
                        As a seasoned presentation specialist, you have a knack for crafting clear and concise presentations.
                        You're also a master of gathering information from various online sources."""),
    verbose=True,
    llm=LLMs().dessision_presentation_llm(),
    allow_delegation=False
    )