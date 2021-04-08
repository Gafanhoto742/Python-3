#Reajuste salarial

sal = float(input('Qual é o seu salário? R$ '))
indc = float(input('Qual é o percentual de reajuste do seu salário? '))
salindc = (sal * indc) / 100 #Salário * %
reaj = sal + salindc
print('Um funcionário que ganhava R$ {:.2f}, com o {:.1f}% de aumento, passa a receber R${:.2f}, houve um aumento de R$ {:.2f}'.format(sal, indc, reaj, salindc))
