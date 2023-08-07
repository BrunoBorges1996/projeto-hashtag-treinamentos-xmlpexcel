import xmltodict
import os
import pandas as pd

def pegar_informacoes(nome_arquivo, tabela_valores):
    with open(f'nfs/{nome_arquivo}', 'rb') as arquivo_xml:
        dicionario_arquivo = xmltodict.parse(arquivo_xml)
        if 'NFe' in dicionario_arquivo:
            informacoes_nfe = dicionario_arquivo['NFe']['infNFe']
        else:
            informacoes_nfe = dicionario_arquivo['nfeProc']['NFe']['infNFe']
        numero_nota = informacoes_nfe['@Id']
        empresa_emissora = informacoes_nfe['emit']['xNome']
        nome_cliente = informacoes_nfe['dest']['xNome']
        endereco = informacoes_nfe['dest']['enderDest']
        if 'vol' in informacoes_nfe['transp']:
            peso_bruto = informacoes_nfe['transp']['vol']['pesoB']
        else:
            peso_bruto = 'N/I'
        tabela_valores.append([numero_nota, empresa_emissora, nome_cliente, endereco, peso_bruto])

lista_arquivos = os.listdir('nfs')

tabela_colunas = ['numero_nota', 'empresa_emissora', 'nome_cliente', 'endereco', 'peso_bruto']
tabela_valores = []

for arquivo in lista_arquivos:
    pegar_informacoes(arquivo, tabela_valores)

tabela = pd.DataFrame(columns = tabela_colunas, data = tabela_valores)
tabela.to_excel('notas_fiscais.xlsx', index = False)