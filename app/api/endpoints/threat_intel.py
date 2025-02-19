from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from models._init__intel_table import SessionLocal
from crud.crud_intel import create_threat_intel, get_threat_intel

router = APIRouter()


async def get_db():
    async with SessionLocal() as session:
        yield session


@router.post("/threat_intel/")
async def add_threat_intel(indicator: str, type_: str, intel_source: str, db: AsyncSession = Depends(get_db)):
    return await create_threat_intel(db, indicator, type_, intel_source)


@router.get("/threat_intel/{indicator}")
async def fetch_threat_intel(indicator: str, db: AsyncSession = Depends(get_db)):
    return await get_threat_intel(db, indicator)
