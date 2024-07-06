import requests
import time
import random

API_ENDPOINT = "http://localhost:5000/data"

def simulate_smart_meter(meter_id):
    while True:
        usage = random.uniform(0.5, 1.5)  
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        data = {"meter_id": meter_id, "usage": usage, "timestamp": timestamp}
        
        response = requests.post(API_ENDPOINT, json=data)
        print(f"Sent data: {data} with response: {response.status_code}")
        
        time.sleep(60)  

simulate_smart_meter("meter_001")
