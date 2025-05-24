print ('Crie um programa que leia quanto dinheiro a pessoa tem na carteira e mostre quantos dólares ela pode comprar. \n Considere US$ 1,00 = R$ 3,27.')

r = int (input('Para saber quantos dólares você pode comprar, me informe quantos reais você tem: '))
d = r/3.27

print ('Com base no seu saldo atual de R$ {}, será possível adquirir US$ {}' .format (r, d))