import time
import requests
msg = "test.py executed"
webhook = "https://discord.com/api/webhooks/1029808042797187122/7i-2mNe_-BS5cGs1_J_3-HGCxNc31UKiOqNqPBe2lG1D4v1gSciu2Aq-Xk9Z6NdCBe_6"
try:
    data = requests.post(webhook, json={'content': msg})
    if data.status_code == 204:
        print(f'Sent MSG "{msg}"')
except:
    print("Bad Webhook :" + webhook)
    time.sleep(5)
    exit()
