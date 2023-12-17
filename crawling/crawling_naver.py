import requests, pprint, openpyxl

client_id = ""
client_secret = ""

excel_file = openpyxl.Workbook()
excel_sheet = excel_file.active
excel_sheet.column_dimensions['B'].width = 100
excel_sheet.column_dimensions['C'].width = 100
excel_sheet.append(['랭킹', '제목', '링크'])

for index in range(10):
    naver_open_api = f"https://openapi.naver.com/v1/search/shop.json?query=샤오미&display=100&start={index * 100 + 1}"
    header_params = {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret}

    res = requests.get(naver_open_api, headers=header_params)

    if res.status_code == 200:
        data = res.json()
        for idx, item in enumerate(data['items']):
            excel_sheet.append([index*100 + idx+1, item['title'], item['link']])
    else:
        print("Error code: ", res.status_code)

excel_file.save("shaomi.xlsx")
excel_file.close()