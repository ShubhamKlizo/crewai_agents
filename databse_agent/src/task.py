from textwrap import dedent
from crewai import Task
from tools import Tools

class DatabaseTasks:

    def search_db_task(self, agent) -> Task:
        return Task(
            description=dedent("""
                Perform a comprehensive search in the MongoDB to retrieve relevant information based on specified criteria.
            """),
            expected_output=dedent("""
                A detailed list of relevant documents or records found in the database, including metadata and any pertinent annotations.
            """),
            async_execution=False,
            agent=agent
        )

    def insert_db_task(self, agent) -> Task:
        return Task(
            description=dedent("""
                Insert a new record into the MongoDB database, ensuring it meets all schema and validation requirements.
            """),
            expected_output=dedent("""
                A confirmation message indicating successful insertion of the record, including details of the inserted record and any relevant IDs.
            """),
            async_execution=False,
            agent=agent
        )

    def update_db_task(self, agent) -> Task:
        return Task(
            description=dedent("""
                Update an existing record in the MongoDB database by modifying specified fields with new values, while maintaining data integrity.
            """),
            expected_output=dedent("""
                A confirmation message indicating the record was successfully updated, including a summary of the changes made and the final state of the record.
            """),
            async_execution=False,
            agent=agent
        )

    def delete_db_task(self, agent) -> Task:
        return Task(
            description=dedent("""
                Delete a specified record from the Mongo database, ensuring that the deletion is performed safely and does not violate any data constraints.
            """),
            expected_output=dedent("""
                A confirmation message indicating the record was successfully deleted, along with any relevant details or IDs of the deleted record.
            """),
            async_execution=False,
            agent=agent
        )

    def write_mongodb_query_task(self, agent, user_query) -> Task:
        return Task(
            description=dedent(f"""
                Develop a MongoDB query based on the user's input query: "{user_query}". The query should be optimized for efficient data retrieval.
            """),
            expected_output=dedent("""
                A well-structured MongoDB query that accurately reflects the user's input and is optimized for performance.
            """),
            async_execution=False,
            agent=agent
        )
