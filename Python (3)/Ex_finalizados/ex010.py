#Conversor de Moedas 29/01/20

real = float(input('Quanto de dinheiro você tem na carteira? R$'))
dolar = real / 4.23   #3.27 Dolar do dia do curso
euro = real / 4.66      #euro do dia
ienejap = real / 25.77  #moeda Japonesa
peso = real / 187.37 #Peso Chileno
print('Com R${:.2f} você pode comprar US${:.2f} \n Euro {:.2F} \n Iene Japonês {:.2F} \n Peso Chileno {:.2F}'.format(real,dolar,euro,ienejap,peso))