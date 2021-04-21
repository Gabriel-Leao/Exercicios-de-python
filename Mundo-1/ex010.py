real = float(input('\033[1;97mQuanto reais você tem? R$'))
dolar = real / 5.57 # Essa é a cotação do dolar em 21/04/2021
euro = real / 6.70 # Essa é a cotação do euro em 21/04/2021
libra = real / 7.76 # Essa é a cotação da libra em 21/04/2021
print(f'Com R${real:.2f} você pode comprar US${dolar:.2f}, EUR${euro:.2f} e GBP${libra:.2f}.\033[m')
