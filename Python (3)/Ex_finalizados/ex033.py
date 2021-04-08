# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('Digite primeiro valor: '))
b = int(input('Digite segundo valor: '))
c = int(input('Digite terceiro valor: '))
#Verificar quem é o menor número
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# verificar quem é o maior numero
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print ('O menor valor digitado foi {}'.format(menor))
print ('O maior valor digitado foi {}'.format(maior))