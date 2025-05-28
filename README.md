# curso-aula-em-video
Este repositório reúne os exercícios e desafios práticos que realizo durante o meu curso de programação. Ao longo dele, documentarei minha evolução e aprendizado, desde os primeiros passos até os desafios mais complexos que enfrento, demonstrando meu comprometimento com o desenvolvimento contínuo e a busca por soluções criativas.
Aqui, cada código conta uma parte da minha trajetória na área de tecnologia, oferecendo uma visão real do meu progresso para futuros recrutadores e profissionais da área. Sinta-se à vontade para explorar, comentar e compartilhar sugestões.

Irei atualizar esse repositório constantemente conforme for avançando no curso.
A sigla "dsf" significa "desafio", seguido pelos sufixos numéricos, que indica qual deles é.
Caso haja alteração, por conta de avanços no aprendizado, será feito uma atualização do código.

Irei dispor aqui no readme os enunciados dos desafios.

dsf001 - Crie um script Python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas, de acordo com o valor digitado.
Proposta: Introduzir os conceitos fundamentais de entrada de dados (capturar o que o usuário digita) e saída de dados (exibir informações na tela). O foco é fazer o aluno interagir com o programa pela primeira vez de forma simples.

Desenvolvimento: 
Uso da função input() para receber dados do usuário.
Uso da função print() para exibir mensagens.
Manipulação básica de strings, como concatenar o nome lido com uma mensagem de boas-vindas (ex: "Olá, [nome]!").

dsf002 - Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formada.
Proposta: Praticar a leitura de múltiplos dados de entrada e a formatação de strings para apresentar esses dados de uma maneira específica e legível.

Desenvolvimento: Leitura de diferentes informações em sequência (dia, mês, ano).
Técnicas de formatação de strings para combinar as variáveis lidas em uma única mensagem (ex: f-strings ou o método .format()).

dsf003 - Crie um script Python que leia dois números e tente mostrar a soma entre eles.                  
Proposta: Destacar a importância dos tipos de dados. A função input() retorna texto (string), e para realizar operações matemáticas, é preciso converter esse texto para um tipo numérico (inteiro ou ponto flutuante). A palavra "tente" sugere que o aluno perceberá o erro de concatenar strings se não fizer a conversão.

Desenvolvimento: 
Compreensão de que input() retorna strings.
Uso de funções de conversão como int() ou float() para transformar a entrada em números.
Realização de operações aritméticas básicas (soma).

dsf004 - Crie um script que leia dois números e mostre a soma entre eles:           
Proposta: Reforçar o aprendizado do desafio anterior sobre a conversão de tipos de dados e a execução de operações aritméticas.

Desenvolvimento: Consolidação da leitura de entradas, conversão para tipos numéricos e a operação de soma.


dsf005 - Faça um programa que leia um número inteiro e mostre na tela o seu sucessor, e seu antecesso.          
Proposta: Praticar operações aritméticas simples (adição e subtração) com números inteiros e a manipulação de uma única entrada numérica para gerar múltiplas saídas.

Desenvolvimento: Leitura e conversão de um número inteiro.
Cálculo do sucessor (numero + 1) e do antecessor (numero - 1).
Exibição dos resultados.


dsf006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.            
Proposta: Introduzir diferentes operadores aritméticos (multiplicação e potenciação para raiz quadrada) e a aplicação de múltiplas operações sobre um mesmo dado de entrada.

Desenvolvimento: Cálculo do dobro (numero * 2) e do triplo (numero * 3).
Cálculo da raiz quadrada usando numero ** 0.5


dsf007 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.              
Proposta: Aplicar os conhecimentos de leitura de múltiplos dados, conversão de tipo e operações aritméticas (soma e divisão) para resolver um problema prático e comum.

Desenvolvimento: Leitura de duas notas.
Conversão das notas para tipo numérico.
Cálculo da média: (nota1 + nota2) / 2.
Exibição da média calculada.


dsf008 - Escreva um programa que leia um valor em metros e exiba convertido em centimentros e milimetros.                  
Proposta: Trabalhar com conversão de unidades, aplicando Fórmulas matemáticas simples (multiplicação por constantes) e exibindo múltiplos resultados derivados de uma única entrada.

Desenvolvimento: Leitura de um valor em metros.
Conversão para centímetros (metros * 100).
Conversão para milímetros (metros * 1000).
Exibição dos valores convertidos.


dsf009 - Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.                  
Proposta: Reforçar a entrada de dados e a conversão para tipo numérico. Fazendo o aluno praticar a repetição de uma lógica de cálculo (multiplicação) e de exibição de resultados de forma manual e explícita.

Desenvolvimento: Leitura de um número inteiro e sua conversão.
Realização de uma série de operações de multiplicação sequenciais para calcular cada item da tabuada.
Uso intensivo da função print() e do método .format() para construir e exibir a tabuada linha por linha.


dsf010 - Crie um programa que leia quanto dinheiro a pessoa tem na carteira e mostre quantos dólares ela pode comprar. \n Considere US$ 1,00 = R$ 3,27.              
Proposta: Aplicar operações aritméticas (divisão) para resolver um problema prático de conversão monetária, utilizando uma taxa de câmbio fixa.

Desenvolvimento: Leitura do valor em reais.
Cálculo da conversão para dólares (reais / 3.27).
Exibição do valor em dólares, possivelmente com formatação para duas casas decimais.


dsf011 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².              
Proposta: Desenvolver a capacidade de resolver problemas em etapas: primeiro calcular uma medida (área) e depois usar esse resultado para um segundo cálculo (quantidade de tinta). Envolve interpretação de requisitos.

Desenvolvimento: Leitura da largura e altura.
Cálculo da área da parede (largura * altura).
Cálculo da quantidade de tinta necessária (area / 2).
Exibição da área e da quantidade de tinta.


dsf012 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.                
Proposta: Introduzir o conceito de cálculo de porcentagem e sua aplicação para determinar um valor com desconto.

Desenvolvimento: Leitura do preço original.
Cálculo do valor do desconto (preco * 0.05 ou preco * 5 / 100).
Cálculo do novo preço (preco - desconto).
Exibição do novo preço.


dsf013 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com aumento de 15%.            
Proposta: Similar ao desafio anterior, mas aplicando a porcentagem para um aumento de valor. Reforça o cálculo de porcentagens.

Desenvolvimento: Leitura do salário original.
Cálculo do valor do aumento (salario * 0.15 ou salario * 15 / 100).
Cálculo do novo salário (salario + aumento).
Exibição do novo salário.


Atualização 27.05.2025: hoje assisti as aulas de correção dos exercícios 005 ao 013. Estou subindo os arquivos .py com as correções feitas pelo professor.
PS.: ao mencionar correção, não significa que seja algo direto, feito especialmente sobre o meu código, mas sim como ele havia pensado no resultado do problema proposto.

dsf014 - Escreva um programa que converta uma temperatura digitada em °C e converta para °F.            
Proposta: Fazer o aluno praticar a leitura de dados numéricos de ponto flutuante (float).
Aplicar uma fórmula matemática específica para a conversão de unidades de temperatura (F = 9×C/5+32).
Ilustrar e reforçar o conceito da ordem de precedência dos operadores aritméticos. O professor intencionava mostrar que, na fórmula de conversão, a multiplicação (9*c) e a divisão (/5) são realizadas antes da adição (+32) devido às regras de precedência do Python, tornando parênteses explícitos (como em ((9*c)/5)+32) funcionalmente desnecessários.


Desenvolvimento: Utilização da função input() para receber um valor e da função float() para convertê-lo para um número de ponto flutuante, adequado para temperaturas que podem ter casas decimais. 
Compreensão prática da ordem de precedência dos operadores, percebendo que Python avalia * e / antes de +, o que permite escrever a expressão de forma mais concisa sem alterar o resultado.

dsf015 - Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado.                  
Proposta: O desafio visa reforçar conceitos fundamentais de Python, como a interação com o usuário (`input`), a conversão de tipos de dados (`int` e `float`), a realização de operações aritméticas básicas, a atribuição de variáveis e a formatação de saída (`print` com `.format`).

Desenvolvimento: Quais variáveis são necessárias? Quais cálculos devem ser feitos?
Executar o código com diferentes valores para verificar se funciona.

