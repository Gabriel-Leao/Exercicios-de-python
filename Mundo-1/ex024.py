cidade = str(input('Digite a cidade em que você nasceu: ')).title().strip()
cidade_separada = cidade.split()
print('\033[1;97m-\033[m'*50)
if cidade_separada[0] == "Santo":
    print(f'\033[1;33mQue legal, Você nasceu em uma cidade que começa com Santo. Vocẽ nasceu em {cidade}\033[m')
else:
    print('\033[1;31mInfelizmente você nasceu em uma cidade que começa não com Santo\033[m')
