from random import choice
a1 = str(input('Primeiro aluno: ')).title()
a2 = str(input('Segundo aluno: ')).title()
a3 = str(input('Terceiro aluno: ')).title()
a4 = str(input('Quarto aluno: ')).title()
lista_alunos = [a1, a2, a3, a4]
print(f'O aluno escolhido foi {choice(lista_alunos)}')
