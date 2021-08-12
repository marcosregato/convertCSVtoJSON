import csv, requests
import os
import platform
import getpass
import glob

# pegar o arquivo csv mais recente no diretorio
def get_export_result_csv():
         
    if platform.system == 'Windows':    
        fileReuslt = 'c:/projetoArquiteturaQA/'
        arqFileCsv = glob.glob(fileReuslt+'*.csv')
        
        if os.path.isfile(fileReuslt) and os.path.getsize(fileReuslt) > 0:
            return max(arqFileCsv, key=os.path.getctime)        
    else:
        fileReuslt = '/home/'+getpass.getuser()+'/projetoArquiteturaQA/'
        arqFileCsv = glob.glob(fileReuslt+'*.csv')
        if os.path.isfile(fileReuslt) and os.path.getsize(fileReuslt) > 0:
            return max(arqFileCsv, key=os.path.getctime)

# pegar o arquivo txt mais recente no diretorio
def get_export_result_txt():
         
    if platform.system == 'Windows':    
        fileReuslt = 'c:/projetoArquiteturaQA/'
        arqFileCsv = glob.glob(fileReuslt+'*.txt')
        
        if os.path.isfile(fileReuslt) and os.path.getsize(fileReuslt) > 0:
            return max(arqFileCsv, key=os.path.getctime())        
    else:
        fileReuslt = '/home/'+getpass.getuser()+'/projetoArquiteturaQA/'
        arqFileCsv = glob.glob(fileReuslt+'*.txt')
        if os.path.isfile(fileReuslt) and os.path.getsize(fileReuslt) > 0:
            return max(arqFileCsv, key=os.path.getctime())

def testFuncional_CSV_JSON():

    try:
        url_api_testFuncional = "http://localhost:8080/api/testefuncional"
        #arquivoCSV = "../TC_001_PaginaPrincipal_02_07_2020_13_27.csv"

        #with open (arquivoCSV) as csvFile:
        with open (get_export_result_csv()) as csvFile:
            id = 1
            csvReader = csv.DictReader(csvFile)
            statusAPI = requests.get(url_api_testFuncional)

            while statusAPI.status_code == "200":
                for csvRow in csvReader:
                    dic = {'id':id,'status':csvRow['status'],'data':csvRow['data'],'hora':csvRow['hora'],'mtodo':csvRow['metodo'],'mensagem':csvRow['mensagem']}
                    requests.post(url_api_testFuncional, json=dic)
                    id+=1

    except Exception as e:
        print(e)

def testeUnitario_TXT_JSON():

    try:
        url_api_testUnitario = "http://localhost:8080/api/testeUnitario"
        arquivoTXT = get_export_result_txt()
        nun_linha = 0
        test_run = []
        list_dic = []
        with open(arquivoTXT, 'r') as arq:
            for linha in arq:
                nun_linha += 1
                if "Tests run:" in linha:
                    test_run.append((linha.strip()))
        list_1 = test_run[1]
        list_item = list_1.split(',')
        for n in list_item:
            list_dic.append(n.strip())

        with open(arquivoTXT, 'r') as arq:
            for linha in arq:
                nun_linha += 1
                if "Total time:" in linha:
                    total_time = linha.rstrip()
        list_dic.append(total_time[7:].strip())

        with open(arquivoTXT, 'r') as arq:
            for linha in arq:
                nun_linha += 1
                if "Finished at:" in linha:
                    finished_at = linha.rstrip()
        list_dic.append(finished_at[7:].strip())
        remove_skipped = list_dic.pop(3)

        data = list_dic[4][12:23]
        hora = list_dic[4][24:32]
        teste_ok = int(list_dic[0][18:].strip()) - int(list_dic[1][10:].strip())

        dic = {'id': 1,'total_teste': list_dic[0][18:].strip(), 'passou':teste_ok,\
               'erro': list_dic[2][8:].strip(), 'tempo_total': list_dic[3][11:19].strip(), \
               'data': data.strip(), 'hora': hora.strip()}

        print(dic)
        requests.post(url_api_testUnitario, json=dic)

    except Exception as e:
        print(e)
