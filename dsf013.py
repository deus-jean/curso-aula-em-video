print ('Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com aumento de 15%')

s = int (input ('Insira seu salário base aqui: '))
a = s*1.15

print ('Após o aumento de 15%, seu novo salário é de R$ {}' .format(a))

print ('Correçãodo professor: ')

salário = float (input ('Qual é o salário do funcionário? R$'))
novo = salário + (salário*15/100)
print ('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}' .format(salário, novo))
