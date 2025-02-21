from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.models._init__intel_table import SessionLocal
from app.crud.crud_intel import create_threat_intel, get_threat_intel

threat_intel_router = APIRouter()


async def get_db():
    async with SessionLocal() as session:
        yield session


@threat_intel_router.post("/threat_intel/")
async def add_threat_intel(indicator: str, type_: str, intel_source: str, db: AsyncSession = Depends(get_db)):
    return await create_threat_intel(db, indicator, type_, intel_source)


@threat_intel_router.get("/threat_intel/{indicator}")
async def fetch_threat_intel(indicator: str, db: AsyncSession = Depends(get_db)):
    return await get_threat_intel(db, indicator)
