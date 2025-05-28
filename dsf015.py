print ('Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado.')
# Como esse desafio também não constava nas aulas, apenas na lista de resoluções, eu acompanhei o desenvolvimento e já preenchi conforme orientação do professor. 
dias = int (input ('Quantos dias alugados? '))
km = float (input ('Quantos KM rodados? '))
pago = (dias*60)+(km*0.15)
print ('O total a ser pago é R${:.2f}.' .format(pago))