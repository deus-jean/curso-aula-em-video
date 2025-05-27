print ('Faça um programa que leia um número inteiro e mostre na tela o seu sucessor, e seu antecesso.')

n1 = int (input ('Insira um número aqui: '))
ant = int (n1-1)
suc = int (n1+1)
print ('O número que você escolheu foi {}. Seu antecessor é {}, e seu sucessor é {}.' .format(n1, ant, suc))

print ('Correção do professor: ')

n = int ( input ('Digite um número: '))
print ('Analisando o valor {}, seu antecessor é {} e o sucessor é {}' .format(n, (n-1), (n+1)))