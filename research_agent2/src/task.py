from textwrap import dedent
from crewai import Task
from tools import Tools


class ResearchTasks():

    def research_task(self, agent , meeting_participants , meeting_context) -> Task:
        return Task(
    description=dedent(f"""\Conduct comprehensive research on each of the individuals and companies involved in the upcoming meeting. 
                        Gather information on recent news, achievements, professional background, and any relevant business activities.
                        Participants: {meeting_participants}
                        Meeting Context: {meeting_context}"""),
    expected_output=dedent("""\
                            A detailed report summarizing key findings about each participant
                            and company, highlighting information that could be relevant for the meeting."""),
    async_execution=True,
    tools=Tools.tools(),
    agent=agent
    )

    def industry_analysis_task(self, agent, meeting_participants, meeting_context) -> Task:
        return Task(
    description=dedent(f"""\Analyze the current state of the industry.
                        Identify trends, challenges, and opportunities relevant to the meeting.
                        Participants: {meeting_participants}
                        Meeting Context: {meeting_context}"""),
    expected_output=dedent("""\
                            An analysis report that identifies major trends, challenges, and opportunities."""),
    async_execution=True,
    tools=Tools.tools(),
    agent=agent
    )

    def decision_making_task(self, agent, meeting_context, meeting_objective) -> Task:
        return Task(
    description=dedent(f"""\Based on the research and industry analysis, form a concise report
                        outlining the main points that should be discussed in the meeting.
                        Meeting Context: {meeting_context}
                        Meeting objective: {meeting_objective}"""),
    expected_output=dedent("""\
                            A concise report that outlines the main points to be discussed in the meeting."""),
    async_execution=False,
    tools=Tools.tools(),
    agent=agent
    )

    def presentation_task(self, agent, meeting_context, meeting_objective) -> Task:
        return Task(
    description=dedent(f"""\Based on the concise report, write a concise presentation
                        outlining the main points that should be discussed in the meeting.
                        Meeting Context: {meeting_context}
                        Meeting objective: {meeting_objective}"""),
    expected_output=dedent("""\
                            A concise presentation that outlines the main points to be discussed in the meeting."""),
    async_execution=False,
    tools=Tools.tools(),
    agent=agent
    )