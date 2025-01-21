from crewai import Crew
from dotenv import load_dotenv
from llms import LLMs
import litellm

from task import ResearchTasks
from agents import ResearcherAgents



#Main function
def main():
    load_dotenv()
    litellm.set_varbose=True

    #Intaraction with the user
    print("Welcome to the Research Agent!")
    print("Please provide your research topic:")
    meeting_participants = input("Participants: ")
    meeting_context = input("Meeting Context: ")
    meeting_objective = input("Meeting Objective: ")

    task = ResearchTasks()
    agent = ResearcherAgents()

    #create agent
    researcher = agent.researcher_agent()
    analyst = agent.industry_analyst_agent()
    dissission_maker = agent.decission_maker_agent()
    presentation = agent.presentation_agent()

    #assign tasks to agents
    research = task.research_task(researcher, meeting_participants, meeting_context)
    industry_analysis = task.industry_analysis_task(analyst, meeting_participants, meeting_context)
    decision_making = task.decision_making_task(dissission_maker, meeting_context, meeting_objective)
    presentation_giving = task.presentation_task(presentation, meeting_context, meeting_objective)

    #link tasks and contexts
    decision_making.context = [research, industry_analysis]
    presentation_giving.context = [research, industry_analysis,decision_making]

    crew = Crew(
        agents=[researcher, analyst, dissission_maker, presentation], 
        tasks=[research, industry_analysis, decision_making, presentation_giving],
        planning_llm=LLMs().planning_llm(), 
        verbose=True)
    result = crew.kickoff()

    return result


if __name__ == "__main__":
    try:
        result = main()
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")