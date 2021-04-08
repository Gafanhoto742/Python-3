'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante '
a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')'''

def leiaInt(texto):
    ok = False
    valor = 0
    while True:
        num = str(input(texto))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('ERRO')
        if ok:
            break
    return valor



#principal
num = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número: {num}')