'''Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
 No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média '''


print('-'*30)
print(f'{"Castrado":^30}')
print('-'*30)

bdados = {} #banco de dados
reg = [] #Registro
soma = media = 0


while True:

    bdados.clear()

    bdados['Nome'] = str(input('Nome: ')).strip().upper()

    while True:
        bdados['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if bdados['Sexo'] in 'MF':
            break
        print('[ERRO] - Dados inválido, favor digitar apenas M ou F.')
        
    while True:
        bdados['Idade'] = int(input('Idade: '))
        if bdados['Idade'] >= 0 and bdados['Idade'] <= 120:
            break
        print('[ERRO] - DADOS INVÁLIDOS - favor digitar uma idade válida!')
    soma += bdados['Idade']
    

    reg.append(bdados.copy())
    while True:
        res = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
        if res in 'SN':
            break
        print(f'[ERRO]-Digite um valor válido, S ou N')
    if res == 'N':
        break
    print('='*30)
        

print('='*30)
print(f'{"RESUMO DE CADASTROS":^30}')
print()
print(f'    A)-  Temos {len(reg)} pessoas cadastradas')

media = soma / len(reg)
print(f'    B)-  A média de idade é {media:3.2f} anos.')

print(f'    C)-  Mulheres cadastradas ', end='')
for m in reg:
    if m['Sexo'] == 'F':
        print(f'{m["Nome"]}', end=' ')
print()

print(f'    D)-  Pessoas acima da média de idade: ')
for i in reg:
    if i['Idade'] >= media:
        print('      ',end =' ')
        for k, v in i.items():
            print(f'{k} = {v}', end=' ')
        print()
print()
print('='*30)

print('='*30)
print(f'{"==* PROGRAMA ENCERRADO *==":^30}')

