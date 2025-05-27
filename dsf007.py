print ('Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.')

n1 = int (input ('Insira sua primeira nota: '))
n2 = int (input ('Insira sua segunda nota: '))
r = int (n1+n2)/2

print ('Sua média é {}.' .format (r))

print ('Correção do professor: ')

n3 = float (input ('Primeira nota do aluno: '))
n4 = float (input ('Segunda nota do aluno: '))
m = (n3 + n4) / 2
print ('A média entre {:.1f} e {:.1f} é igual a {:.1f}' .format(n3, n4, m))