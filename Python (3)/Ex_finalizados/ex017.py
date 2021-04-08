# catetos e hipotenusa
'''1 modo de calcular
cop = float(input('Comprimento do cateto oposto: '))
cad = float(input('Comprimento do cateto adjacente: '))
hi = (cop ** 2 + cad **2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi)) '''

#import hipotenusa

from math import hypot
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hi = hypot(co,ca)
print ('a hipotenusa vai medir {:.2f}'.format(hi))