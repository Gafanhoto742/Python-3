'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá 
perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''

tot18 = sexom = sexof = totm20 = 0

print('-'*21)
print (' Cadastre uma pessoa')
print('-'*21)
while True:
    
    
    nome = str(input('Nome: ')).strip().upper()

    idade = int(input('Idade: '))


    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Gênero: [M/F]: ')).strip().upper()[0]
    
    if idade >= 18:
        tot18 += 1

    if sexo == 'M':
        sexom += 1

    if sexo == 'F': 
        sexof += 1

        if idade < 20: 
            totm20 += 1


    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar: [S/N]')).strip().upper()[0]
    if resp =='N':
        break

    print('-'*30)
    
    
print(f'Temos {tot18} pessoas com mais de 18 anos')
print(f'Temos {sexom} homens cadastrado')
print(f'Ao todo temos {sexof} mulheres cadastradas e {totm20} delas tem menos de 20 anos!')

