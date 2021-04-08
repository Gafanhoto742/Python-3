número = int(input('Digite um número:'))
print (''' Escolha uma das bases para conversão:
[1] para binário
[2} para octal
[3} para hexadecimal''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} Convertido para Binário é igual {}'.format (número, bin(número)[2:]))
elif opção == 2:
    print('{} convertido para Octal é igual {}'.format (número, oct(número)[2:]))
elif opção == 3:
    print ('{} convertido para Hexadecimal é igual {}'.format (número, hex(número)[2:]))
else:
    print ('[ERRO] - Escolher uma opção válida!')



