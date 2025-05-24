print ('Escreva um programa que leia um valor em metros e exiba convertido em centimentros e milimetros.')

m = int (input ('Insira quantos metros você deseja converter: '))
cm = int (m*100)
mm = int (m*1000)

print ('{} metros tem: {}cm e {}mm.' .format (m, cm, mm))