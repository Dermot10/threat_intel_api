from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DB_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in environment variables")

# Create async database engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Manages db session
SessionLocal = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession)


async def check_db_connection():
    try:
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1"))
        print("✅ Database connection successful!")
    except Exception as e:
        print(f"❌ Database connection failed: {e}")

# Run the connection check
if __name__ == "__main__":
    asyncio.run(check_db_connection())
