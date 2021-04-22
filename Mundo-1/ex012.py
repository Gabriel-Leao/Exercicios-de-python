preco = float(input('\033[1;97mPreço do produto: R$'))
desconto = preco - (preco * (5 / 100))
print(f'O produto que custava R${preco:.2f}, com o desconto de 5% saí por R${desconto:.2f}.\033[m')
