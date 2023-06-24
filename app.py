from openpyxl import Workbook

from time import sleep

print('iniciando robô.......')
sleep(2)
print( 'Leando dados do arquivo de texto')
sleep(2)

file_text = open('gastos.txt','r', encoding='utf-8')

#ler arquivo
arquivo = file_text.read()

lista_dados = arquivo.splitlines()

for i in range(0,len(lista_dados)):
    lista_dados[i] = lista_dados[i].split(',') #Separa um em cada linha



print(lista_dados)


#Criando arquivo 

print('Criando arquivo excel.....')
sleep(2)
wb= Workbook()
ws = wb.active

for row in lista_dados:
    ws.append(row)
wb.save('gastos.xlsx')
sleep(3)
print('Arquivo criado com sucesso!....')