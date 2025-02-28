import httpx #async operations
import json
from app.config import abuseIP_key

async def get_ip_intel(ip: str):
    headers = {
        'Key': abuseIP_key,
        'Accept': 'application/json'
    }
    querystring = {
        'ipAddress': ip,
        'maxAgeInDays': '90'
    }
    url = 'https://api.abuseipdb.com/api/v2/check'
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url,
            headers=headers, 
            params=querystring
        )
        if response.status_code == 200:
            decodedResponse = response.json()
            # Formatted output
            print(json.dumps(decodedResponse, sort_keys=True, indent=4))
            return decodedResponse
        else:
            response.raise_for_status()

        