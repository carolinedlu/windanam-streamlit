import requests
import os

API_URL = "https://api-inference.huggingface.co/models/cawoylel/windanam_mms-1b-tts_v2"
headers = {"Authorization": "Bearer XXXXXXX"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

current_dir = os.getcwd()
filename = os.path.join(current_dir, 'src/pages', 'segment18.wav')
output = query(filename)
print(output)