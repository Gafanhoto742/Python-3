'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''

print ('=' * 18)
print ('\033[7;30;39mLOJA DOS PRETINHOS\033[m')
print ('='*18)
preço = float(input('Preço das compras: R$ '))
print ('''ESCOLA A FORMA DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão de crédito
[ 4 ] 3x ou mais no cartão de crédito''')
opção = int(input('Qual é a opção? '))
if opção == 0 or opção >= 5:
    print('[ERRO] escolha uma opção entre 1 e 4')
elif opção == 1 :
    formapgto1 = (-preço * 5) / 100 + preço
    print ('Sua compra de R${:.2f} teve um desconto 5 %' ' e você vai pagar R${:.2f}'.format(preço,formapgto1))
elif opção == 2:
    print('Sua compra de R${:.2f} sera debito à vista no cartão'.format(preço))
elif opção == 3:
    formapgto3 = preço / 2
    print('Sua compra de R${:.2f} será parcelada em 2x de R${:.2f} sem Juros!'.format(preço,formapgto3))
elif opção == 4:
    vezes = int(input('Vai parcelar em quantas vezes? '))
    if vezes <= 4 :
        formapgto4 = preço / vezes
        print ('A sua compra de R${:.2f} será parcelado em {}x e você pagará R${:.2f} ao mês sem juros.'.format(preço,vezes,formapgto4))
    elif vezes > 5:
        formapgto5 = ((-preço * 3) / 100 + preço)/vezes
        print ('A sua compra de R${:.2f} será parcelado em {}x e você pagará R${:.2f} ao mês com o juros de 3.% '.format(preço,vezes,formapgto5))