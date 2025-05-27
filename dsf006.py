print ('Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.')

n1 = int (input ('Digite um número: '))
d = int (n1*2)
t = int (n1*3)
r = n1**(1/2)

print ('O seu dobro é {}, seu triplo é {}, e sua raiz quadrada é {}.' .format (d, t, r))

print ('Correção do professor: ')

n = int ( input ('Digite um número: '))
print ('O dobro de {} vale.' .format (n, (n*2)))
print ('O triplo de {} vale {}. \n A raiz quadrada de {} é igual a {:.2f}.' .format (n, (n*3), n, pow (n, (1/2))))