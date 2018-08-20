import requests
import xlwt
# 读取数据(API)，相应调取参数参见国家气象信息中心API说明
outputs = requests.get("API")
outputs.encoding = 'utf-8'
# 创建excel表格
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('sheet1')
# 写入表头
data = outputs.json()['DS']
title = list(data[0].keys())
for i in range(len(title)):
    worksheet.write(0, i, title[i])
# 写入数据
for j in range(len(data)):
    values = list(data[j].values())
    for k in range(len(values)):
        worksheet.write(j+1, k, values[k])
# 保存到当前目录
workbook.save('test1.xls')





