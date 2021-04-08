''' Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
No final, mostre o conteúdo da estrutura na tela'''


aluno = {}
c = 0

print('-+'*30)
print(f'{"*** SISTEMA DE APROVAÇÃO DE ALUNOS ***":^60}')
print('-+'*30)

c += 1
aluno ['nome'] = str(input(f'\nNome do {c}º Aluno: ')).strip()
aluno ['média'] = float(input(f'Informe a média do {aluno["nome"]}: '))

if aluno['média'] >= 7:
    aluno['sit']= 'APROVADO'

elif 5 <= aluno['média'] <7:
    aluno['sit'] = 'RECUPERAÇÃO'

else:
    aluno['sit'] = 'REPROVADO'


print('-+'*30)

for k, v in aluno.items():
    print(f'\n ---{k} é igual à {v}\n')

print('-+'*30)
print('\nPROGRAMA ENCERRADO!\n')