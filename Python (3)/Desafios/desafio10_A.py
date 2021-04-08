# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

nomep = str(input('Qual é o seu nome?' ))
print ('é um grande prazer em te conhecer {}!'.format(nomep))
n = int(input('Eu gostaria de fazer uma brincadeira de adivinhação, você gostaria de tentar adivinhar o número que pensei entre 0 a 5?' ))
if n == 2:
    print('Acertou, VOCÊ VENCEU!!!!!!')
else:
    print('Errouuuuuuuuuuu criança feliz, EU VENCI!!!!!!!!!')