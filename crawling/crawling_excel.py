import requests, openpyxl
from bs4 import BeautifulSoup


def write_excel_template(filename, sheetname, listdata):
    excel_file = openpyxl.Workbook()
    excel_sheet = excel_file.active
    excel_sheet.column_dimensions['A'].width = 100
    excel_sheet.column_dimensions['A'].width = 20

    if sheetname != '':
        excel_sheet.title = sheetname

    for item in listdata:
        excel_sheet.append(item)
    excel_file.save(filename)
    excel_file.close()


product_lists = []
for page_num in range(10):
    if page_num == 0:
        res = requests.get("https://davelee-fun.github.io/")
    else:
        res = requests.get("https://davelee-fun.github.io/" + str(page_num + 1))
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.select('div.card')

    for item in data:
        product_name = item.select_one("div.card-body h4.card-text")
        product_date = item.select_one("div.wrapfooter span.post-date")
        product_info = [product_name.get_text().strip(), product_date.get_text()]
        product_lists.append(product_info)

write_excel_template('tmp.xlsx', '상품정보', product_lists)