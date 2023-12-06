import requests

API_URL = "https://api-inference.huggingface.co/models/cawoylel/windanam_mms-1b-tts_v2"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()


output = query("segment18.wav")
print(output)