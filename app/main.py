from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.api.endpoints.threat_intel import threat_intel_router
from app.api.endpoints.background_intel import background_intel_router

app = FastAPI(title="Threat Intelligence API")
app.include_router(threat_intel_router)
app.include_router(background_intel_router)
