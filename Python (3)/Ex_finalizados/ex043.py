'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, 
de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida'''

print ('-=-' * 10)
print('      Cálculo de IMC')
print ('-=-' * 10)
peso = float(input('Qual é o seu peso: '))
altura = float(input('Qual é a sua altura: '))
imc = peso / (altura ** 2)
print ('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc <= 18.5:
    print ('ALERTA, você está na faixa \033[1;34;34mABAIXO DO PESO\033[m')
elif imc < 25:
    print ('PARABÉNS! você está na faixa de \033[1;34;34mPESO IDEAL\033[m')
elif imc < 30:
    print('ATENÇÃO! você está na faixa no \033[1;34;34mSOBREPESO\033[m')
elif imc < 40:
    print('ATENÇÃO! você está na faixa de \033[1;34;34mOBESIDADE\033[m')
elif imc > 40:
    print('ANTENÇÃO! você está na faixa de \033[1;34;34mOBESIDADE MÓRBIDA\033[m cuidado')
else:
    print ('[ERRO!]')



