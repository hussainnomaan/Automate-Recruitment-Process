from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

# Define the data model to store task statuses


class TaskStatus(BaseModel):
    research_candidates_task: bool = False
    match_and_score_candidates_task: bool = False
    outreach_strategy_task: bool = False
    report_candidates_task: bool = False


# Create an instance of FastAPI
app = FastAPI()

# Initialize a global object to store the status of tasks
task_status = TaskStatus()


@app.get("/tasks", response_model=TaskStatus)
async def get_task_status():
    """
    Retrieve the current status of all tasks.
    """
    return task_status


@app.put("/tasks")
async def update_task_status(updated_status: TaskStatus):
    """
    Update the status of tasks.
    """
    global task_status
    task_status = updated_status
    return {"message": "Task statuses updated successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
