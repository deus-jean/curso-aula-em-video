print ('Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.')

n1 = int (input ('Digite um número: '))
d = int (n1*2)
t = int (n1*3)
r = int (n1**(1/2))

print ('O seu dobro é {}, seu triplo é {}, e sua raiz quadrada é {}.' .format (d, t, r))