import csv,json, requests
import time
arquivoCSV = "../TC_001_PaginaPrincipal_02_07_2020_13_27.csv"
arqJSON = "../TC_001_PaginaPrincipal_02_07_2020_13_27.json"
arr = []

url = "http://localhost:8080/api/testefuncional"
json_data = None
data = {}
def postAPI():
    try:
        with open (arquivoCSV) as csvFile:
            id =1
            statusApi = requests.get(url)
            csvReader = csv.DictReader(csvFile)
            for csvRow in csvReader:
                if statusApi == "200":
                    dic = {'id':id,'status':csvRow['status'],'data':csvRow['data'],'hora':csvRow['hora'],'mtodo':csvRow['metodo'],'mensagem':csvRow['mensagem']}
                    arr.append(dic)
                    id+=1
                    body = json.dumps(arr, indent = 2)
                    headers = {'Content-Type': 'application/json'}
                    requests.post(url, headers=headers, data=body, verify=False)
                    time.sleep(5)
                else:
                    print('ERRO NO API >> '+statusApi)

    except Exception as e:
        print(e)

def getAPI():
    result = requests.get(url)
    print(result.text)

getAPI()


