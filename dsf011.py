print ('Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².')

print ('Para calcularmos a área da sua parede e sabermos do quanto de tinta será necessário para pintá-la, primeiro me informe: ')

a = int (input ('Qual a altura da sua parede (em metros): '))
c = int (input ('Qual o comprimento da sua parede (em metros): '))
ar = a*c
ct = ar/2

print ('Com {}m de altura e {}m de comprimento, sua parede apresenta uma área total de {}m², sendo necessários {} litros de tinta para pintá-la por completo.' .format(a, c, ar, ct))

print ('Correção do professor: ')

larg = float (input ('Largura da parede: '))
alt = float (input ('Altura da parede: '))
área = larg*alt
print ('Sua parede tem a dimensão de {}x{} e sua área é de {}m²' .format (larg, alt, área))
tinta = área / 2
print ('Para pintar essa parede, você precisará de {}l de tinta.' .format (tinta))
