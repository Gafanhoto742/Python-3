'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
 indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''


def fat(n=0, show=False):
    """
    ->Calcula o Fatorial de um número.
    :param n= O número a ser calculado.
    :param show=(Opcional) Mostrar ou não a conta. 
    :return = O valor do Fatorial de um número n.
    Função criada por Henrique Oliveira
    """
    f = 1
    for c in range (n, 0 , -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' -> ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

n = int(input('Digite um número: '))
print(fat(n, show=True))

#help(fat)
