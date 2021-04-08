'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai 
retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)'''

def notas(*n, sit=False):
    """
    ->Calcula função de Notas.
    :param n= O número a ser calculado.
    :param sit=(Opcional) Mostrar ou não a situação da nota. 
    :return = O valor do Fatorial de um número n.
    Função criada por Henrique Oliveira
    """
    r = {} #dicionário
    r ['Total'] = len(n)
    r ['Maior'] = max(n)
    r ['Menor'] = min(n)
    r ['Média'] = sum(n)/len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = "BOA"
        elif r['Média'] >= 5:
            r['Situação'] = "RAZOÁVEL"
        else:
            r['Situação'] = "RUIM"
    return r


#programa principal
resp = notas (5.5, 2.5, 1.5, sit=True) # opção Sit para aparecer a situação da nota, caso apagar some
print(resp)

help(notas)