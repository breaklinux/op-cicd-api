def readExcel():
    import xlrd
    workbook = xlrd.open_workbook(r'./excel/data_service.xls')
    sheet_name = workbook.sheet_names()
    sheet = workbook.sheet_by_index(0)
    # sheet索引从0开始
    data = []
    rows = sheet.row_values(0)
    for i in list(range(1, sheet.nrows)):
        machineInfo = sheet.row_values(i)
        if machineInfo[1]:
            data.append(machineInfo)
    return data
resultData = readExcel()

def foramtData():
    for i in resultData:
        reqPushData(business=i[4],group=i[1],appname=i[3],apptype=i[7],giturl=i[2],owner=i[16],port=i[8],level=i[9],used=i[21])
#         #测试元素
#         print(i[0],i[4],i[1],i[3],i[7],i[2],i[16],i[8],i[9],i[21])

#---------------业务线----小组---应用名称--语言类型--git地址-负责人-端口-级别--用途
def reqPushData(business,group,appname,apptype,giturl,owner,port,level,used):
    import requests
    Data = {'business': business,
            'group': group,
            'appname': appname,
            'apptype': apptype,
            'giturl': giturl,
            'owner': owner,
            'port': port,
            'level': level,
            'used': used
            }
    r = requests.post('http://192.168.11.101:5000/app/api/v1', json=Data)
    print(r.json())

foramtData()
