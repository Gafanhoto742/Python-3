# Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A letra A aparece na posição {} a primeira vez.'.format(frase.find('A')+1))
print('A letra A aparece na posição {} na última vez.'.format(frase.rfind('A')+1))