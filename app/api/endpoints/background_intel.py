from fastapi import FastAPI, BackgroundTasks
from fastapi import APIRouter, Depends
from .threat_intel import fetch_threat_intel

background_intel_router = APIRouter()


@background_intel_router.get("/intel/fetch")
async def fetch_intel(background_tasks: BackgroundTasks):
    task = fetch_threat_intel.delay()
    return {"task_id": task.id}


@background_intel_router.get("/intel/status/{task_id}")
async def check_task_status(task_id: str):
    from ...workers.celery_worker_config import celery_app
    task_result = celery_app.AsyncResult(task_id)
    if task_result.state == "PENDING":
        return {"status": "Pending..."}
    elif task_result.state != "FAILURE":
        return {
            "status": task_result.state,
            "result": task_result.result
        }
    else:
        return {"status": "Failed", "error": str(task_result.info)}
