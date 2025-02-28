import asyncio
from .abuseipdb import get_ip_intel

# Test the function with a sample IP
ip_to_check = "8.8.8.8"  # Google's public DNS for testing

async def main():
    await get_ip_intel(ip_to_check)

# Run the async function
asyncio.run(main())
