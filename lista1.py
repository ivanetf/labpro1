'''
Exercícios sobre os comandos básicos em python
'''

#1. Faça um programa que imprima o seu nome.
def q01():
    print('João Paulo Delgado Preti')

#2. Faça um programa que imprima o produto dos valores 30 e 27.
    produto = 30 * 27
    print("O produto de 30 e 27 é:", produto)


#3. Faça um programa que imprima a média aritmética entre os números 5, 8, 12.
def q02():
    num1 = 5
    num2 = 8
    num3 = 12
    media = (num1 + num2 + num3) / 3
    
    print("A média aritmética é:", media)

#4. Faça um programa que leia e imprima um número inteiro.
def q04():
    num1 = int(input('digite um numero: '))
    print(num1)
#5. Faça um programa que leia dois números reais e os imprima.
def q05():
    num1 = float(input('Digite um número: '))
    num2 = float(input('Digite um outro número: '))
    print(f'Número 1: {num1}')
    print(f'Número 2: {num2}')

#6. Faça um programa que leia um número inteiro e imprima o seu
#   antecessor e o seu sucessor.
def q06():
    num = int(input('Digite um número: '))
    print(f'Sucessor de {num} = {num+1}')
    print(f'Antecessor de {num} = {num-1}')
  
#7. Faça um programa que leia o nome o endereço e o telefone de
#   um cliente e ao final, imprima esses dados.
def q07():    
    nome = input('digite seu nome: ')
    endereco = input('digite seu endereço: ')
    telefone = int(input('digite seu telefone: '))
    print(nome)
    print(endereco)
    print(telefone)
#8. Faça um programa que leia dois números inteiros e imprima a
#   subtração deles.
def q08():
    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))
         subtracao = num1 - num2
         print("A subtração dos números é:", )
  
#9. Faça um programa que leia um número real e imprima ¼ deste número.
def q09():
    num = float(input('Digite um número: '))
    print(f'Resultado: {num/4}')

#10. Faça um programa que leia três números reais e calcule a
#    média aritmética destes números. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def q10():
    num1 = float(input('Digite o 1 número: '))
    num2 = float(input('Digite o 2 número: '))
    num3 = float(input('Digite o 3 número: '))
    media = (num1+num2+num3)/3
    print(f'Média: {media}')

#11. Faça um programa que leia dois números reais e calcule as
#    quatro operações básicas entre estes dois números, adição,
#    subtração,multiplicação e divisão. Ao final, o programa
#    deve imprimir os resultados dos cálculos.
def q11():
    num1 = int(input('digite um numero: '))
    num2 = int(input('digite um numero: '))
    soma = num1 + num2
    subtracao = num1 - num2
    divisao = num1 / num2
    multiplicacao = num1 * num2

    print(f' a soma: {soma}')
    print(f' a subtraçao: {subtracao}')
    print(f' a divisao: {divisao}')
    print(f' a multiplicacao: {multiplicacao}')
#12. Faça um programa que leia um número real e calcule o
#    quadrado deste número. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def q12():
    
        numero = float(input("Digite um número real: "))
        quadrado = numero ** 2 (numero)
        print("O quadrado do número é:", quadrado)

#13. Faça um programa que leia o saldo de uma conta poupança e
#    imprima o novo saldo, considerando um reajuste de 2%.
def q13():
    saldo = float(input('Saldo R$: '))
    print(f'Saldo com reajuste de 2% = R$ {saldo*1.02}')

#14. Faça um programa que leia a base e a altura de um retângulo
#    e imprima o perímetro (base + altura) e a área (base * altura).
def q14():
    base = int(input('digite a base:  '))
    altura = float(input('digite a sua altura: '))
    perimetro = base + altura
    area = base * altura

    print(perimetro)
    print(area)


#15. Faça um programa que leia o valor de um produto, o percentual
#    do desconto desejado e imprima o valor do desconto e o valor
#    do produto subtraindo o desconto.P1
def q15():
    valor_produto = float(input('Valor do Produto: R$ '))
    perc_desconto = float(input('% do desconto: '))
    valor_desconto = valor_produto * perc_desconto/100
    print(f'Desconto: R$ {valor_desconto}')
    print(f'Valor final do produto: R$ {valor_produto-valor_desconto}')

#16. Faça um programa que calcule o reajuste do salário de um
#    funcionário. Para isso, o programa deverá ler o salário atual
#    do funcionário e ler o percentual de reajuste. Ao final imprimir
#    o valor do novo salário.
def q16():
        salario_atual = float(input("Digite o salário atual do funcionário: R$  "))
        percentual_reajuste = float(input("Digite o percentual de reajuste (%): "))
       
        novo_salario =  (salario_atual * percentual_reajuste) / 100

        print("O novo salário do funcionário é: R$", novo_salario)

#17. Faça um programa que calcule a conversão entre graus centígrados
#    e Fahrenheit. Para isso, leia o valor em centígrados e calcule
#    com base na fórmula a seguir. Após calcular o programa deve
#    imprimir o resultado da conversão.
#    F = (9 x C + 160) / 5
def q17():
        centigrados = float(input("Digite a temperatura em graus centígrados: "))

        fahrenheit = (9 * centigrados + 160) / 5
        print("A temperatura em graus Fahrenheit é:", fahrenheit)

#18. Faça um programa que calcule a quantidade de litros de combustível
#    consumidos em uma viagem, sabendo-se que o carro tem autonomia de
#    12 km por litro de combustível. O programa deverá ler o tempo
#    decorrido na viagem e a velocidade média e aplicar as fórmulas:
#    D = T x V       L = D / 12
#    Em que:
#    • D = Distância percorrida em horas
#    • T = Tempo
#    • V = Velocidade média
#    • L = Litros de combustível consumidos
#    Ao final, o programa deverá imprimir a distância percorrida e a
#    quantidade de litros consumidos na viagem.
def q18():
        tempo = float(input("Digite o tempo decorrido na viagem (horas): "))
        velocidade_media = float(input("Digite a velocidade média (km/h): "))

        distancia_percorrida = tempo * velocidade_media
        litros_combustivel = (distancia_percorrida) / 12

        print("Distância percorrida: {:.2f} km" (distancia_percorrida))
        print("Quantidade de litros de combustível consumidos: {:.2f} litros" (litros_combustivel))

#19. Faça um programa que calcule o valor de uma prestação em atraso.
#    Para isso, o programa deve ler o valor da prestação vencida, a
#    taxa periódica de juros e o período de atraso. Ao final, o
#    programa deve imprimir o valor da prestação atrasada, o período
#    de atraso, os juros que serão cobrados pelo período de atraso, o
#    valor da prestação acrescido dos juros. Considere juros simples.
def q19():
        valor_prestacao_vencida = float(input("Digite o valor da prestação vencida: R$"))
        taxa_juros = float(input("Digite a taxa periódica de juros (em decimal): "))
        periodo_atraso = int(input("Digite o período de atraso (em meses): "))

        juros = valor_prestacao_vencida * (taxa_juros * periodo_atraso)
        valor_prestacao_atrasada = valor_prestacao_vencida + juros

        print("Valor da prestação atrasada: R$", valor_prestacao_atrasada)
        print("Período de atraso (em meses):", periodo_atraso)
        print("Juros pelo período de atraso: R$", juros)
        print("Valor da prestação acrescido dos juros: R$", valor_prestacao_atrasada)

#20. Faça um programa que efetue a apresentação do valor da conversão
#    em real (R$) de um valor lido em dólar (US$). Para isso, será
#    necessário também ler o valor da cotação do dólar.
def q20(): 
        valor_dolar = float(input("Digite o valor em dólar (USD): $"))
        cotacao_dolar = float(input("Digite a cotação do dólar (USD para BRL): R$"))

        valor_real = valor_dolar * cotacao_dolar
        print("O valor em real (BRL) é: R$", valor_real)
    


