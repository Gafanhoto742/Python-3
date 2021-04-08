#conversor de medidas

#resposta montada por Henrique

metros = float(input('Digite uma distância em metros: '))
km = metros/1000 #Kilometros
hm = metros/100 #Hectômetro
dam = metros/10 #Decâmetro
dm = metros*10 #Decimetro
cm = metros*100 #Centimetros
mm = metros*1000 #milimetros

print('A medida de {}m corresponde a \n{:.3f}Km \n{:.2f}hm \n{:.1f}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(metros, km, hm, dam, dm, cm, mm))
