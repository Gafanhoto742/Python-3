'''#função
def lin():
    print('-'*30)

def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {a}m.')


#programa principal
lin()
print(f'\033[7;30;32m{"CONTROLE DE TERRENOS":^30}\033[m')
lin()

l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
área(l, c)
'''


# teste de conhecimento Henrique
def lin():
    print('-'*60)


def metragem(larg , comp):
    tot = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {tot}m.')

while True:
    print(' ')
    print(f'{"CONTROLE DE MEDIDAS DE TERRENO":^60}')
    lin()

    l = float(input('Largura m: '))
    c = float(input('Comprimento m: '))
    lin()
    metragem(l, c)
    lin()
    while True:
        resp = str(input('Deseja Continuar [S/N]: ')).strip().upper()[0]
        if resp in "SN":
            break
        print("[ERRO] - Digite um apenas valores válidos S ou N: ")
    if resp == "N":
        break
    lin()

lin()
print(f'{"<<<PROGRAMA ENCERRADO>>>":^60}')



