#'print ('Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.')

#co = float (input ('Insira o comprimento do cateto oposto: '))
#ca = float (input ('Insira o comprimento do cateto adjacente: '))
#r = ((co**2)+(ca**2))**0.5
#print ('A hipotenusa é {}.' .format(r))

print ('Correção do professor: ')

from math import hypot
co = float (input ('Comprimento do cateto oposto: '))
ca = float (input ('Comprimento do cateto adjacente: '))
hi = hypot (co, ca)
print ('A hipotenusa vai medir {:.2f}' .format(hi))