print ('O professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.')
from random import choice
aluno1 = input ('Insira o nome do primeiro aluno: ')
aluno2 = input ('Insira o nome do segundo aluno: ')
aluno3 = input ('Insira o nome do terceiro aluno: ')
aluno4 = input ('Insira o nome do quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
r = choice (lista)

print (f'O aluno escolhido foi: {r}.')
