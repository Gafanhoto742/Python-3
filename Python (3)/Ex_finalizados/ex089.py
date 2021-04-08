'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar 
as notas de cada aluno individualmente.'''

alunos = []
c = 0

print ('-'*30)
print (f'\033[7;30;39m{"Lista de Média Escolar":^30}\033[m')
print ('-'*30)

while True:
    c +=1
    print (f'----{c}º Aluno(a)----')

    nome = str(input('Nome: ')).strip()
    n1 = float(input('1º Nota: '))
    n2 = float(input('2º Nota: '))
    m = (n1 + n2) / 2

    alunos.append([nome, [n1, n2], m])

    resp = str(input('Deseja Continuar [S/N]: ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input(f'DADOS INVÁLIDOS. Por favor, informe se deseja continuar [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        print('-='*30) 
        break
    
print(f'{"Nº":<5} {"NOME":<10} {"MÉDIA":>8}')

print('-='*30)

for i, a in enumerate(alunos):
    print(f'{i:<5} {a[0]:<10} {a[2]:>8.1f}')

print('-='*30)

while True:
    r = int(input('Mostrar o detalhamento através do nº do aluno?: (999 interrompe):'))
    if r == 999:
        print('Finalizado!')
        break
    if r <= len(alunos) -1:
        print (f'Notas de {alunos[r][0]} são {alunos[r][1]}')
print('Tenha um bom dia!')






  

