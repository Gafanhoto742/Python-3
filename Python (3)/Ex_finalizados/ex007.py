#média aritmética
nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))
soma = nota1 + nota2
media = soma /2
print('A média entre {} e {} [e igual a {:.2f}.'.format(nota1,nota2,media))

#segundo modo de fazer o mesmo exercio
n1 = float(input('Primeiro nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
media = (n1 + n2)/2
print('A média entre {} e {} [e igual a {:.2f}'.format(n1,n2,media))