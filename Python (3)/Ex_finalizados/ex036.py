''' Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''


casa = float(input('Valor da Casa: R$ '))
salário = float(input('Salário do Comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print ('Para pagar uma casa de R$ {:.2f} em {} anos!'.format(casa,anos), end='')
print('A prestação será e R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
