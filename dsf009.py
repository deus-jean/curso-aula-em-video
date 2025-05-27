print ('Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.')

n = int (input('Insira um número: '))
r1 = n*1
r2 = n*2
r3 = n*3
r4 = n*4
r5 = n*5
r6 = n*6
r7 = n*7
r8 = n*8
r9 = n*9
print (' {} x 1 = {} \n {} x 2 = {} \n {} x 3 = {} \n {} x 4 = {} \n {} x 5 = {} \n {} x 6 = {} \n {} x 7 = {} \n {} x 8 = {} \n {} x 9 = {}' .format (n, r1, n, r2, n, r3, n, r4, n, r5, n, r6, n, r7, n, r8, n, r9))

print ('Correção do professor: ')

num = int (input ('Digite um número para ver sua tabuada: '))
print ('-' * 15)
print ('{} x {:2} = {}' .format (num, 1, num*1))
print ('{} x {:2} = {}' .format (num, 2, num*2))
print ('{} x {:2} = {}' .format (num, 3, num*3))
print ('{} x {:2} = {}' .format (num, 4, num*4))
print ('{} x {:2} = {}' .format (num, 5, num*5))
print ('{} x {:2} = {}' .format (num, 6, num*6))
print ('{} x {:2} = {}' .format (num, 7, num*7))
print ('{} x {:2} = {}' .format (num, 8, num*8))
print ('{} x {:2} = {}' .format (num, 9, num*9))
print ('{} x {:2} = {}' .format (num, 10, num*10))
print ('-' * 15)