# Aluguel de carros
algdias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
preco = (60 * algdias) + (0.15 * km)
print('O Aluguel do carro ficará em R$ {:.2f} por tantos dias {}'.format(preco, algdias))