largura = float(input('\033[1;97mLargura da parede: '))
altura = float(input('Altura parede: '))
area = largura * altura
tinta = area / 2
print(f'A sua parede tem a dimensão de {largura}x{altura} e sua área é de {area}².')
print(f'Para pintar essa parede, será necessario {tinta}L de tinta.\033[m')
