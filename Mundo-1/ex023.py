num = int(input('Informe um número: '))
print('\033[1;97m-\033[m'*40)
print(f'Analisando o número {num}, ele tem:')
print('\033[1;97m-\033[m'*40)
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print(f'Milhar: {milhar}')
print(f'Centenas: {centena}')
print(f'Dezenas: {dezena}')
print(f'Unidades: {unidade}')
