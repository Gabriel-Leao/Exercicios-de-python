name = str(input('\033[1;97mDigite seu nome completo: \033[m')).title()
print('\033[1;97m-\033[m'*65)
if 'Silva' in name:
    print('\033[1;31mSeu nome tem Silva. Como a maioria dos brasileiros.\033[m')
else:
    print('\033[1;33mSeu nome não tem Silva, vocẽ é uma pessoa diferente da maioria.\033[m')
print('\033[1;97m-\033[m'*65)
