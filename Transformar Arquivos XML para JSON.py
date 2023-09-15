import xmltodict
import os
import json

#Foram criadas duas funções que trabalha com XML para JSON.
#Caso queira somente ler o arquivo XML no formato de JSON use a função 1
#Caso queira mudar o arquivo XML para JSON use a função 2

try:
    def pegar_infos(nome_arquivos):
        print(f"Pegou as informações de {nome_arquivos}")
        with open(f"{diretorio}/{nome_arquivos}", "rb") as arquivo_xml:
            dic_arquivo = xmltodict.parse(arquivo_xml)
            print(json.dumps(dic_arquivo, indent= 4))


    def transfor_json(nome_arquivos):
        with open(f"{diretorio}/{nome_arquivos}", "rb") as arquivo_xml:
            dic_arquivo = xmltodict.parse(arquivo_xml)
            arquivos_json = json.dumps(dic_arquivo, indent= 4)
            with open(f"{nome_arquivos}.json", "w") as novojson:
                novojson.write(arquivos_json)

#Informe onde se encontra o arquivo e depois a função que você deseja usar.
    diretorio = input(f"Informe o diretório em que se encontra o arquivo: \n")
    funcao = int(input (f"Digite o valor correspondente a funcao: \n 1. Pegar informação de arquivos\n 2. Transformar arquivos\n"))

# Aqui vai listar os arquivos com a extensão XML.
    listar_arquivos = os.listdir(f"{diretorio}")

#Aqui é a condição de qual função está rodando
    if funcao == 1:
        for arquivos in listar_arquivos:
            pegar_infos(arquivos)

    elif funcao == 2:
        for arquivos in listar_arquivos:
            transfor_json(arquivos)

    else:
        print("Valor não encontrado")
    
#Tratamento de Exceções
except Exception as e:
    print(f"Ocorreu um erro porque {e}")