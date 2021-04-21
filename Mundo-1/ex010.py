real = float(input('\033[1;97mQuanto reais você tem? R$'))
dolar = real / 5.57
print(f'Com R${real:.2f} você pode comprar US${dolar:.2f}\033[m')
