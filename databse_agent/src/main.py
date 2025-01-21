from crewai import Crew
from dotenv import load_dotenv
from llms import LLMs
from task import DatabaseTasks
from agents import DatabaseAgent

def main():
    load_dotenv()

    task = DatabaseTasks()
    agent = DatabaseAgent()

    user_query = input("Enter your query: ")

    # Create agents
    search_db_agent = agent.search_db_agent()
    update_db_agent = agent.update_db_agent()
    text_to_query_agent = agent.text_to_query_agent()

    # Assign tasks to agents
    write_mongodb_query_task = task.write_mongodb_query_task(text_to_query_agent, user_query)
    search_db_task = task.search_db_task(search_db_agent)
    insert_db_task = task.insert_db_task(update_db_agent)
    update_db_task = task.update_db_task(update_db_agent)
    delete_db_task = task.delete_db_task(update_db_agent)

    # Link tasks and contexts
    search_db_task.context = [write_mongodb_query_task]
    insert_db_task.context = [write_mongodb_query_task]
    update_db_task.context = [write_mongodb_query_task]
    delete_db_task.context = [write_mongodb_query_task]

    crew = Crew(
        agents=[search_db_agent, update_db_agent, text_to_query_agent],
        tasks=[write_mongodb_query_task, search_db_task, insert_db_task, update_db_task, delete_db_task],
        planning_llm=LLMs().planning_llm(),
        verbose=True
    )

    result = crew.kickoff()
    return result

if __name__ == "__main__":
    print(main())
    try:
        result = main()
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
