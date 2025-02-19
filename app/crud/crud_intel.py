from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.models import ThreatIntel
from datetime import date


async def create_threat_intel(db: AsyncSession, indicator: str, type_: str, intel_source: str, description: str = None):
    """Add threat intel to database, providing key fields"""
    intel = ThreatIntel(indicator=indicator, type=type_,
                        intel_source=intel_source, description=description)
    db.add(intel)
    await db.commit()
    await db.refresh(intel)
    return intel


async def get_threat_intel(db: AsyncSession, indicator: str):
    """Retrieve record for a specific indicator"""
    result = await db.execute(select(ThreatIntel).where(ThreatIntel.indicator == indicator))
    return result.scalars().first()


async def get_intel_type(db: AsyncSession, type_: str):
    """Retreive all from one type, all IPs, all Hashes etc"""
    result = await db.execute(select(ThreatIntel).where(ThreatIntel.type == type_))
    return result.scalars().all()


async def get_todays_intel(db: AsyncSession):
    """Retrieve todays intel"""
    result = await db.execute(
        select(ThreatIntel).where(ThreatIntel.created_at >= date.today()))
    return result.scalars().all()


async def get_intel_source(db: AsyncSession, source: str):
    """Retreive all from one vendor source"""
    result = await db.execute(select(ThreatIntel).where(ThreatIntel.source == source))
    return result.scalars().all()
