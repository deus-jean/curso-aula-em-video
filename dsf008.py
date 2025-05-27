print ('Escreva um programa que leia um valor em metros e exiba convertido em centimentros e milimetros.')

m = int (input ('Insira quantos metros você deseja converter: '))
cm = int (m*100)
mm = int (m*1000)

print ('{} metros tem: {}cm e {}mm.' .format (m, cm, mm))

print ('Correção do professor: ')

medida = float (input ('Uma distância em metros: '))
cm1 = medida*100
mm1 = medida*1000
print ('A medida de {}m correspondem a {}cm e {}mm.' .format(medida, cm1, mm1))