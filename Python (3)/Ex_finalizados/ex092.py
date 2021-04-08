'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
 em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de 
 contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''

from datetime import datetime

trabalhador = {}


print(' ')
print('='*30)
print(f'{"CADASTRO DO TRABALHADOR":^30}')
print('='*30)

trabalhador ['Nome'] = str(input(f'Nome do Trabalhador: ')).strip()
nasc = int(input(f'Ano de Nascimento: '))
trabalhador ['Idade'] = datetime.now().year - nasc
trabalhador ['CTPS'] = str(input(f'Trabalhador possui CTPS: [S/N]')).strip().upper()[0]
if trabalhador ['CTPS'] !='Nn':
    trabalhador ['NCTPS'] = int(input('Nº CTPS: '))
    trabalhador ['Contratação'] = int(input('Ano da 1º Contratação: '))
    trabalhador ['Salário'] = float(input('Salário R$ '))
    trabalhador ['Aposent'] = trabalhador['Idade'] + ((trabalhador['Contratação'] + 35) - datetime.now().year)

for k, v in trabalhador.items():
    print(f'    - {k} tem o valor {v}')


print('='*60)

while True:
    resp = str(input('Deseja Continuar [S/N]: ')).strip().upper()[0]
    while resp not in 'SsNn':
        resp = str(input(f'DADOS INVÁLIDOS. Por favor, informe se deseja continuar [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        print('==PROGRAMA ENCERRADO!==')
        break