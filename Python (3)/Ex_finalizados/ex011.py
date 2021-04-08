# calular metragem 

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {} x {} e sua área é de {:.2f}m2.'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {:.2f}l de tinta.'.format(tinta))


#outro formato de preparar o script
lar = float(input('Largura da parede: '))
al = float(input('Altura da parede: '))
ar = lar * al
tint = ar / 2
print('Sua parede tem a dimensão de {}m x {}m e sua área é de {}m. \nPara pintar essa parede, você precisará de {}l de tinta.'.format(lar, al, ar, tint))