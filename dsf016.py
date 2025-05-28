print ('Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira. Exemplo: ' \
'Digite um número: 6.127. O número 6.127 tem a parte inteira 6.')
from math import trunc
num = float (input ('Insira um número real para converte-lo ao número inteiro: '))
print ('O número inteiro em {} é equivalente a {}.' .format (num, trunc(num)))

print ('Correções do professor: ')


