
import os
import requests

# 1. Your API key
HINDSIGHT_API_KEY = "hsk_62dd6a59c21165ebbdc3d693b416b532_26fec321a54f2890" 

# 2. Setup the REST API URL pointing to Hindsight Cloud
BANK_ID = "deal-agent-bank"
HINDSIGHT_URL = f"https://api.hindsight.vectorize.io/mcp/{BANK_ID}"

headers = {
    "Authorization": f"Bearer {HINDSIGHT_API_KEY}",
    "Content-Type": "application/json"
}

print("Uploading synthetic deal history to Hindsight Memory Bank...")

call_1 = """
Call Date: Sept 10, 2026. Account: Acme Corp. Contact: Sarah (VP of Sales).
Summary: Sarah loved the product demo but explicitly noted that Acme is undergoing Q4 budget cuts. 
She is worried about the $120k upfront enterprise cost.
"""

call_2 = """
Call Date: Sept 15, 2026. Account: Acme Corp. Contact: Mark (Security Lead).
Summary: Mark brought up SOC2 compliance and data residency. He needs assurance that our servers 
are located in the US and latency will be under 50ms.
"""

call_3 = """
Call Date: Sept 22, 2026. Account: Acme Corp. Contact: David (CFO).
Summary: David objected to the annual billing cycle. He mentioned that our competitor, Datadog, 
is offering them a 15% discount and quarterly billing options. 
"""

def retain_memory(content):
    payload = {"content": content}
    # Direct REST API call bypassing the SDK entirely
    response = requests.post(f"{HINDSIGHT_URL}/retain", json=payload, headers=headers)
    if response.status_code == 200:
        print("Memory stored.")
    else:
         print(f"Error storing memory: {response.status_code} - {response.text}")

# 3. Push the memories
retain_memory(call_1)
retain_memory(call_2)
retain_memory(call_3)

print("Finished! The AI Agent now has persistent memory of Acme Corp.")