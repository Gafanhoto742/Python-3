'''Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3): # for de alimentação dos valores da Matriz
    for coluna in range (0, 3):
        matriz [linha][coluna] = int(input(f'Digite um valor na [{linha}, {coluna}]:'))


print('-='*30)
for linha in range(0, 3): #for de repetição na matriz
    for coluna in range (0, 3):
        print (f'[{matriz[linha][coluna]:^5}]', end='')
    print()