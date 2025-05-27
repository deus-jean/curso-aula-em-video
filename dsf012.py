print ('Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.')

p = int (input ('Insira o preço do produto aqui: '))
d = p*0.95

print ('O valor do produto com o desconto de 5% aplicado é de R$ {}.' .format(d))

preço = float (input ('Qual é o preço do produto? R$'))
novo = preço - (preço*5/100)
print ('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar r${:.2f}' .format (preço, novo))
