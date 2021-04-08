''' Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = somal = somac= 0

for l in range (0, 3):
    for c in range(0, 3):
        matriz [l][c] = int(input(f'Digite um número [{l, c}]:'))


print('-='*30)

for l in range (0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]',end='')
        if matriz [l][c] % 2 == 0:
            somap += matriz [l][c]                 
    print()

print('-='*30)

print(f'A soma dos valores pares {somap}')

print('-='*30)

for l in range (0, 3):
    somal += matriz [l][2]
print(f'A soma dos valores apresentados na terceira coluna é: {somal}')

print('-='*30)
for c in range(0, 3):
    if c == 0:
        somac = matriz [1][c]
    elif matriz [1][c] > somac:
        somac = matriz [1][c]
print(f'O maior valor da segunda linda é {somac}')


print('-='*30)


