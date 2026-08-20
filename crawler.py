import os
import json
import requests

API_KEY = os.environ.get("OPINET_API_KEY")

url_all = f"https://www.opinet.co.kr/api/avgAllPrice.do?code={API_KEY}&out=json"
# sidoPrice.do 호출 시 지역별 데이터를 정확히 가져오는지 확인
url_area = f"https://www.opinet.co.kr/api/sidoPrice.do?code={API_KEY}&out=json"

res_all = requests.get(url_all)
res_area = requests.get(url_area)

print(f"AREA Status Code: {res_area.status_code}")
print(f"AREA Response: {res_area.text[:200]}") # 응답 앞부분만 출력

combined_data = {}
if res_all.status_code == 200:
    combined_data["ALL"] = res_all.json()

# AREA 데이터가 실제 존재하는지 체크
if res_area.status_code == 200 and len(res_area.text) > 100:
    combined_data["AREA"] = res_area.json()
else:
    print("AREA data is empty or invalid")

os.makedirs("data", exist_ok=True)
with open("data/price.json", "w", encoding="utf-8") as f:
    json.dump(combined_data, f, ensure_ascii=False, indent=4)
