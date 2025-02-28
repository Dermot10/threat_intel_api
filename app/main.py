from fastapi import FastAPI
from app.api.endpoints.threat_intel import threat_intel_router
from app.api.endpoints.background_intel import background_intel_router

app = FastAPI(title="OSINT Aggregator", 
    version="1.0.0",
    description="Fetch real-time threat intelligence from multiple OSINT sources."
)

app.include_router(threat_intel_router, prefix="/api/v1/osint/threat-intelligence")
app.include_router(background_intel_router)
# app.include_router(ip.router, prefix="/api/v1/osint/threat-intel")