from random import shuffle
a1 = str(input('Primeiro aluno: ')).title()
a2 = str(input('Segundo aluno: ')).title()
a3 = str(input('Terceiro aluno: ')).title()
a4 = str(input('Quarto aluno: ')).title()
lista_alunos = [a1, a2, a3, a4]
shuffle(lista_alunos)
print('-'*30)
print('A ordem de apresentação será:')
print('-'*30)
for c, v in enumerate(lista_alunos):
    print(f'{c + 1}- {v}')
print('-'*30)
