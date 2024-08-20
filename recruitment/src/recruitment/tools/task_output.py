import os
import requests
from crewai import Agent, Task, Crew, Process

# Custom Tool to send data to API


class SendToAPI:
    def __init__(self, api_endpoint):
        self.api_endpoint = api_endpoint

    def __call__(self, data):
        response = requests.post(self.api_endpoint, json=data)
        return response.json()


# Create an API sender tool
api_sender_tool = SendToAPI(
    api_endpoint="https://your-api-endpoint.com/update")

# Custom callback function to track progress


def progress_callback(agent_name, task_description, progress, output):
    data = {
        "agent": agent_name,
        "task": task_description,
        "progress": progress,
        "output": output,
    }
    # Send progress to API
    api_sender_tool(data)


# Creating a researcher agent with memory and progress tracking
researcher = Agent(
    role='Researcher',
    goal='Research and compile data on {topic}',
    memory=True,
    # This callback will be used to track progress
    progress_callback=progress_callback,
)

# Research task with tracking and callback
research_task = Task(
    description="Research the impact of AI in healthcare.",
    expected_output="A detailed report on the impact of AI in healthcare.",
    tools=[api_sender_tool],
    agent=researcher,
)

# Form the crew and start the process
crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    process=Process.sequential,
)

result = crew.kickoff(inputs={'topic': 'AI in healthcare'})

print(result)
