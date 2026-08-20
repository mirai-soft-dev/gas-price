import os
import json
import requests

API_KEY = os.environ.get("OPINET_API_KEY")

# 1. 전국 평균 데이터 가져오기
url_all = f"https://www.opinet.co.kr/api/avgAllPrice.do?code={API_KEY}&out=json"
# 2. 전국 시/도별 데이터 가져오기
url_area = f"https://www.opinet.co.kr/api/areaOilPrice.do?code={API_KEY}&out=json&area=All"

res_all = requests.get(url_all)
res_area = requests.get(url_area)

combined_data = {}

if res_all.status_code == 200:
    combined_data["ALL"] = res_all.json()
else:
    print(f"Failed to fetch ALL data: {res_all.status_code}")

if res_area.status_code == 200:
    combined_data["AREA"] = res_area.json()
else:
    print(f"Failed to fetch AREA data: {res_area.status_code}")

os.makedirs("data", exist_ok=True)
with open("data/price.json", "w", encoding="utf-8") as f:
    json.dump(combined_data, f, ensure_ascii=False, indent=4)

print("Data saved successfully.")
