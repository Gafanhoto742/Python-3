#Desenvolva um programa que leia o comprimento de 
# três retas e diga ao usuário se elas podem ou não formar um triângulo.

print ('-=-' * 20)
print ('Analisando Triangulo')
print ('-=-' * 20)

r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triângulo!')
else:
    print('Os segmentos não podem formar um triângulo!')


# minha primeiro código

'''
media1 = float(input('Digite o primeiro número: '))
media2 = float(input('Digite o segundo número: '))
media3 = float(input('Digite o terceiro número: '))
if media1 >= media2 and media1 <= media3:
    print ('Ok, temos um triangulo')
if media1 <= media2 and media1 >= media3:
    print ('Ok, temos um triangulo')
if media3 >= media2 and media3 <= media1:
    print ('Ok, temos um triangulo')
if media3 <= media2 and media3 >= media1:
    print ('Ok, temos um triangulo')


else:
    print('Erro')
'''
