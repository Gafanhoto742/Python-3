''' Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
  o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa 
  tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''



def opc (ano):
    from datetime import date
    atual = date.today().year
    idade = atual - nasc
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO!'
    elif 16 <= idade < 18 or idade > 65 :
        return f'Com {idade} anos: O VOTO É OPCIONAL!'
    else:
        return f'Com {idade} anos: O VOTO É OBRIGATÓRIO, PESQUISE O SEU CANDIDATO ANTES DE VOTAR!'

while True:
    print('-'*30)
    nasc = int(input('Em que ano você nasceu? '))
    print(opc(nasc))
    print('-'*30)
    while True:
        resp = str(input('Deseja Continuar [S/N]: ')).strip().upper()[0]
        if resp in "SN":
            break
        print("[ERRO] - Digite um apenas valores válidos S ou N: ")
    if resp == "N":
        break
print('<<< PROGRAMA ENCERRADO >>>')


