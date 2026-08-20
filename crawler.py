import os
import json
import requests

API_KEY = os.environ.get("OPINET_API_KEY")

# 1. 전국 평균 데이터 가져오기
url_all = f"https://www.opinet.co.kr/api/avgAllPrice.do?code={API_KEY}&out=json"
# 2. 전국 시/도별 데이터 가져오기
url_area = f"https://www.opinet.co.kr/api/areaOilPrice.do?code={API_KEY}&out=json&area=All"

data_all = requests.get(url_all).json()
data_area = requests.get(url_area).json()

# 합쳐서 저장
combined_data = {
    "ALL": data_all,
    "AREA": data_area
}

os.makedirs("data", exist_ok=True)
with open("data/price.json", "w", encoding="utf-8") as f:
    json.dump(combined_data, f, ensure_ascii=False, indent=4)
print("Data saved successfully.")
