import csv, requests

arquivoCSV = "../TC_001_PaginaPrincipal_02_07_2020_13_27.csv"
url = "http://localhost:8080/api/testefuncional"

try:
    with open (arquivoCSV) as csvFile:
        id =1
        csvReader = csv.DictReader(csvFile)
        statusAPI = requests.get(url)

        while statusAPI.status_code == "200":
            for csvRow in csvReader:
                dic = {'id':id,'status':csvRow['status'],'data':csvRow['data'],'hora':csvRow['hora'],'mtodo':csvRow['metodo'],'mensagem':csvRow['mensagem']}
                requests.post(url, json=dic)
                id+=1
    
except Exception as e:
    print(e)