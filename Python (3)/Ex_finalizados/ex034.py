''' Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1250,00,  um aumento de 10%. Para os inferiores ou iguais, 
o aumento é de 15%. '''

sal = float(input('Qual é o salário do funcionário? R$ ' ))
if sal <= 1250:
    novo = sal + (sal * 15 / 100)
else:
    novo = sal + (sal * 10 / 100)
print ('Quem ganhava \033[1;31mR${:.2f}\033[m passou a ganhar \033[1;32mR${:.2f}\033[m'.format(sal, novo))