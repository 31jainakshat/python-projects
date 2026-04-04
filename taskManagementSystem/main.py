#!/usr/bin/env python3

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, validator
from typing import Optional, Dict, List
from datetime import datetime
import uuid

app = FastAPI(title="Smart Task Manager")

TASKS: Dict[str, dict] = {}

class Task(BaseModel):
    title: str
    description: Optional[str] = None
    priority: Optional[str] = "low"
    deadline: Optional[str] = None

    @validator("priority")
    def validate_priority(cls, v):
        if v not in ["low", "medium", "high"]:
            raise ValueError("Priority must be low, medium, or high")
        return v

def auto_priority(task: dict):
    if task.get("deadline"):
        deadline = datetime.strptime(task["deadline"], "%Y-%m-%d")
        days_left = (deadline - datetime.now()).days

        if days_left <= 1:
            task["priority"] = "high"
        elif days_left <= 3:
            task["priority"] = "medium"

    return task

@app.post("/tasks")
def create_task(task: Task):
    data = task.dict()

    data = auto_priority(data)

    task_id = str(uuid.uuid4())
    data["created_at"] = datetime.now().isoformat()

    TASKS[task_id] = data

    return {"task_id": task_id, "task": data}

@app.get("/tasks")
def get_tasks(priority: Optional[str] = Query(None)):
    results = []

    for tid, task in TASKS.items():
        if priority and task["priority"] != priority:
            continue
        results.append({"id": tid, **task})

    return results

@app.get("/tasks/{task_id}")
def get_task(task_id: str):
    if task_id not in TASKS:
        raise HTTPException(status_code=404, detail="Task not found")
    return TASKS[task_id]

@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    if task_id not in TASKS:
        raise HTTPException(status_code=404, detail="Task not found")
    
    del TASKS[task_id]
    return {"message": "Task deleted"}

@app.get("/analytics")
def get_analytics():
    total = len(TASKS)
    high = sum(1 for t in TASKS.values() if t["priority"] == "high")
    overdue = 0

    for t in TASKS.values():
        if t.get("deadline"):
            deadline = datetime.strptime(t["deadline"], "%Y-%m-%d")
            if deadline < datetime.now():
                overdue += 1

    return {
        "total_tasks": total,
        "high_priority_tasks": high,
        "overdue_tasks": overdue
    }