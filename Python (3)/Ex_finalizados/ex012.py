# cálculo de desconto + juros para parcelamentos

preco = float(input('Qual é o preso do produto? R$ '))
digperc = float(input('Qual é o percentual de desconto? '))
percent = (preco * digperc) /100  #percentual
vldesc = preco - percent
print('O Produto que custava R$ {:.2F}, na promoção com desconto de {:.2} % vai custar R$ {:.2f}, você teve um desconto de R$ {:.2f}'.format(preco, digperc, vldesc, percent))
print('Caso queira temos a opção do parcelado! Mas o valor haverá um juros pelo numero de parcelas')
numparc = int(input('Quantas parcelas? '))
reaj = preco + (preco * 2 / 100)
totpar = reaj * numparc
print ('A sua compra de R$ {:.2f}, foi parcelada em {} vezes de R$ {:.2f}, totalizando em R$ {:.2f}'.format(preco, numparc,reaj, totpar))