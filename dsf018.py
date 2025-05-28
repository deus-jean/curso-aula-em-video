print ('Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.')
from math import radians, sin, cos, tan
ângulo = float (input ('Digite o ângulo que você deseja: '))
seno = sin(radians(ângulo))
print ('O ângulo de {} tem o SENO de {:.2f}' .format(ângulo, seno))
cosseno = cos(radians(ângulo))
print (f'O ângulo de {ângulo} tem o COSSENO de {cosseno:.2f}')
tangente = tan(radians(ângulo))
print (f'O ângulo de {ângulo} tem a TANGENTE de {tangente:.2f}')