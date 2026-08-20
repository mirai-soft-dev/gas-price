import os
import json
import requests

API_KEY = os.environ.get("OPINET_API_KEY")
url = f"https://www.opinet.co.kr/api/avgAllPrice.do?code={API_KEY}&out=json"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    
    # data 디렉토리 생성
    os.makedirs("data", exist_ok=True)
    
    # JSON 파일 저장
    with open("data/price.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("Data saved successfully.")
else:
    print(f"Failed to fetch data: {response.status_code}")
