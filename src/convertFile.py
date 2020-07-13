import csv, requests
import io

def testFuncional_CSV_JSON():
    arquivoCSV = "../TC_001_PaginaPrincipal_02_07_2020_13_27.csv"
    url_api_testFuncional = "http://localhost:8080/api/testefuncional"

    try:
        with open (arquivoCSV) as csvFile:
            id =1
            csvReader = csv.DictReader(csvFile)
            statusAPI = requests.get(url_api_testFuncional)

            while statusAPI.status_code == "200":
                for csvRow in csvReader:
                    dic = {'id':id,'status':csvRow['status'],'data':csvRow['data'],'hora':csvRow['hora'],'mtodo':csvRow['metodo'],'mensagem':csvRow['mensagem']}
                    requests.post(url_api_testFuncional, json=dic)
                    id+=1

    except Exception as e:
        print(e)

def testeUnitario_TXT_JSON(palavra):
    try:
        arquivoTXT = "../log_maven_teste.txt"
        nun_linha = 0
        result = []
        with open(arquivoTXT, 'r') as arq:
            for linha in arq:
                nun_linha += 1
                if palavra in linha:
                    result.append((linha.rstrip()))
        return result
    except Exception as e:
        print(e)

print(testeUnitario_TXT_JSON("Tests run:"))