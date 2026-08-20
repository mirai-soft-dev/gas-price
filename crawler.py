import os
import json
import requests

API_KEY = os.environ.get("OPINET_API_KEY")

# 1. 전국 평균 데이터
url_all = f"https://www.opinet.co.kr/api/avgAllPrice.do?code={API_KEY}&out=json"
# 2. 시/도별 평균 데이터 (올바른 엔드포인트: sidoPrice.do)
url_area = f"https://www.opinet.co.kr/api/sidoPrice.do?code={API_KEY}&out=json"

res_all = requests.get(url_all)
res_area = requests.get(url_area)

combined_data = {}

if res_all.status_code == 200:
    combined_data["ALL"] = res_all.json()

if res_area.status_code == 200:
    combined_data["AREA"] = res_area.json()

os.makedirs("data", exist_ok=True)
with open("data/price.json", "w", encoding="utf-8") as f:
    json.dump(combined_data, f, ensure_ascii=False, indent=4)

print("Data saved successfully.")
