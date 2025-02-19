from fastapi import FastAPI
from api.endpoints import threat_intel

app = FastAPI(title="Threat Intelligence API")
app.include_router(threat_intel.router)
