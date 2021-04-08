'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''

from time import sleep
print('-=-' * 12)
print('\033[7;30;39mSISTEMA DE CÁLCULO DE MÉDIA ESCOLAR\033[m')
print('-=-' * 12)
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print ('\033[2;33mAvaliando a sua média\033[m')
sleep (1)
print ('\033[2mProcessando ...\033[m')
sleep (2)
print ('O aluno tirou {} na primeira prova, {} na segunda prova, e a sua média ficou em {}'.format(nota1, nota2,media))
sleep (2)
if media < 5:
    print('O aluno foi \033[1;31mREPROVADO!\033[m')
elif media > 7:
    print ('O aluno foi \033[1;32mAPROVADO!\033[m')
else:
    print ('O aluno está em \033[0;33mRECUPERAÇÃO!\033[m')
