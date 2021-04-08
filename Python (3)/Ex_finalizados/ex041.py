'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER'''

from datetime import date
atual = date.today().year
ano = int(input('Ano de Nascimento: '))
idade = atual - ano
print('O atleta tem \033[34m{}\033[m anos.'.format(idade))
if idade <= 9:
    print('Classificação: \033[;32mMIRIM\033[m')
elif idade <= 14:
    print('Classificação: \033[;32mINFANTIL\033[m')
elif idade <= 19:
    print('Classificação: \033[;32mJÚNIOR\033[m')
elif idade <= 25:
    print('Classificação: \033[;32mSÊNIOR\033[m')
else:
    print('Classificação: \033[;32mMASTER\033[m')