nome = str(input('Qual é o seu nome? '))
if nome == 'Amanda':
    print('Que lindo nome que você tem Gatinha!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))



n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A seu média é {:.1f}!'.format(m))
if m >=7.0:
    print('Parabéns aprovado!')
else:
    print('Reprovado, estude mais!')
print('--FIM--')