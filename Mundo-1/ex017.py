from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hipotenusa = hypot(co, ca)
print(f'O tamanho da hipotenusa é {hipotenusa:.2f}.')
