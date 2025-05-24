print ('Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formada.')

print ('Resposta inicial: ')

dianasc = input ('Qual o dia do seu nascimento? ')
mesnasc = input ('Consegue se lembrar do mês? ')
anonasc = input ('E em qual ano foi? ')
print ('Você nasceu em',dianasc,'de',mesnasc,'de',anonasc+'.','Correto?')

print ('Resposta aperfeiçoada com os conhecimentos obtidos até a aula 07: ')

print ('Olá, vamos nos conhecer um pouco mais.')
d = input ('Me diga o dia do seu nascimento: ')
m = input ('Agora me informe o mês, por extenso: ')
a = input ('Por último, me diz aí o ano: ')
print ('Você nasceu no dia {} de {} de {}, correto?' .format (d, m, a))