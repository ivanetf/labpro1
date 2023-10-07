import random
'''
Lista de Exercícios referentes a coleções em python
'''

#1. Faça um programa que armazene 15 números inteiros em uma lista e depois
#permita que o usuário digite um número inteiro para ser buscado na lista, se
#for encontrado o programa deve imprimir a posição desse número na lista, caso
#contrário, deve imprimir a mensagem: "Nao encontrado!".
def q01():
    lista = []
    for x in range(15):
        lista.append(random.randrange(100))
    print(lista)
    num = 0
    erro = True
    while erro == True:
        try:
            num = int(input('Digite um número a ser buscado: '))
            erro = False
        except:
            print('Informe um valor válido para inteiro!')
            erro = True
    try:
        print(f'Valor encontrado na posição: {lista.index(num)}')
    except ValueError:
        print('Valor não encontrado na lista')
    except:
        print('Erro desconhecido, contate o administrador do sistema!')

#2. Faça um programa que armazene 10 letras em uma lista e imprima uma listagem
#numerada.
def q02():
      lista=[]
      for x in range(10):
        lista.append(chr(random.randrange(65,91)
      cont = 0                    
      for letra in lista:
      print(f' {cont}: {letra}')
      cont += 1
                                  
#3. Construa uma programa que armazene 15 números em uma lista e imprima
#uma listagem numerada contendo o número e uma das mensagens: par ou ímpar.
def q03():
    lista = []
    for x in range(15):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numero.append(numero)   
    print("Listagem numerada com par ou ímpar: ")
    print(f"{x + 1}. Número: {numero}, é {tipo}.")

#4. Faça um programa que armazene 8 números em uma lista e imprima todos os
#números. Ao final, imprima o total de números múltiplos de seis.
def q04():            
    lista = []
    for x in range(8):
    numeros = int(input(f"Digite o {i + 1}º número: "))
    lista.append(numeros)
    cont = 0
    print("Números armazenados:")
    total_multiplos_seis = contar_multiplos_de_seis(numeros)
    print(f"Total de números múltiplos de seis: {total_multiplos_seis}")
    cont += 1

#5. Faça um programa que armazene as notas das provas 1 e 2 de 15 alunos. Calcule
#e armazene a média arredondada. Armazene também a situação do aluno: 1-
#Aprovado ou 2-Reprovado. Ao final o programa deve imprimir uma listagem
#contendo as notas, a média e a situação de cada aluno em formato tabulado.
#Utilize quantas listas forem necessárias para armazenar os dados.
# Função para calcular a média arredondada e a situação do aluno
def q05():
    notas_prova1 = []
    notas_prova2 = []
    medias_arredondadas = []
    situacoes = []
    for x in range(15):
    nota1 = float(input(f"Digite a nota da prova 1 para o aluno {x+1}: "))
    nota2 = float(input(f"Digite a nota da prova 2 para o aluno {x+1}: "))
    
    media = (nota1 + nota2) / 2
    media_arredondada = round(media, 1)
    if media >= 6.0:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    
    notas_prova1.append(nota1)
    notas_prova2.append(nota2)

    media, situacao = (nota1, nota2)
    medias_arredondadas.append(media)
    situacoes.append(situacao)
    print("Listagem de notas, médias e situações dos alunos:")
    print("Aluno\tNota Prova 1\tNota Prova 2\tMédia\tSituação")
    for x in range(15):
    print(f"{x+1}\t{notas_prova1[i]}\t\t{notas_prova2[i]}\t\t{medias_arredondadas[x]}\t{situacoes[x]}")

#6. Construa um programa que permita armazenar o salário de 20 pessoas. Calcular
#e armazenar o novo salário sabendo-se que o reajuste foi de 8%. Imprimir uma
#listagem numerada com o salário e o novo salário. Declare quantas listas forem
#necessárias.
def q06():
    salario = []
    novos_salarios = []
    for x in range(20):
    salario = float(input(f"Digite o salário da pessoa {i+1}: "))
    salarios_originais.append(salario)
    novo_salario = salario * 1.08  # Reajuste de 8%
    novos_salarios.append(novo_salario)

    print("Listagem numerada de salários e novos salários (com reajuste de 8%):")
    print("Pessoa\tSalário\tNovo Salário")
    print(f"{x+1}\t{salarios_originais[x]:.2f}\t{novos_salarios[x]:.2f}")

#7. Crie umprograma que leia o preço de compra e o preço de venda de 100 mercadorias
#(utilize listas). Ao final, o programa deverá imprimir quantas mercadorias
#proporcionam:
#• lucro < 10%
#• 10% <= lucro <= 20%
#• lucro > 20%
def q07():
    
   return ((preco_venda - preco_compra) / preco_compra) * 100
    preco_compra = []
    preco_venda = []
    for x in range(100):
    preco_compra = float(input(f"Digite o preço de compra da mercadoria {x+1}: "))
    preco_venda = float(input(f"Digite o preço de venda da mercadoria {x+1}: "))
    precos_compra.append(preco_compra)
    precos_venda.append(preco_venda)
    lucro_menor_10 = 0
    lucro_10_20 = 0
    lucro_maior_20 = 0

    for x in range(100):
    if lucro_percentual < 10:
        lucro_menor_10 += 1
    elif lucro_percentual <= 20:
        lucro_10_20 += 1
    else:
        lucro_maior_20 += 1
    print("Quantidade de mercadorias por faixa de lucro:")
    print(f"Lucro < 10%: {lucro_menor_10} mercadorias")
    print(f"10% <= Lucro <= 20%: {lucro_10_20} mercadorias")
    print(f"Lucro > 20%: {lucro_maior_20} mercadorias")

#8. Construa um programa que armazene o código, a quantidade, o valor de compra
#e o valor de venda de 30 produtos. A listagem pode ser de todos os produtos ou
#somente de um ao se digitar o código. Utilize dicionário como estrutura de dados.
# Função para imprimir as informações de um produto com base no código
def q08():
    produto = produtos.get(codigo)
    if produto:
        print(f"Informações do produto (Código {codigo}):")
        print("Código:", produto["codigo"])
        print("Quantidade:", produto["quantidade"])
        print("Valor de compra:", produto["valor_compra"])
        print("Valor de venda:", produto["valor_venda"])
    else:
        print(f"Produto com código {codigo} não encontrado.")
    produtos = {}
    for x in range(30):
    codigo = int(input(f"Digite o código do produto {x+1}: "))
    quantidade = int(input(f"Digite a quantidade do produto {x+1}: "))
    valor_compra = float(input(f"Digite o valor de compra do produto {x+1}: "))
    valor_venda = float(input(f"Digite o valor de venda do produto {x+1}: "))

    produtos[codigo] = {
        "codigo": codigo,
        "quantidade": quantidade,
        "valor_compra": valor_compra,
        "valor_venda": valor_venda
    }
    print("Listagem de todos os produtos:")
    for codigo, produto in produtos.items():
    print(f"Código: {produto['codigo']}, Quantidade: {produto['quantidade']}, Valor de compra: {produto['valor_compra']}, Valor de venda: {produto['valor_venda']}")

    codigo_produto_visualizar = int(input("Digite o código do produto que deseja visualizar (ou -1 para sair): "))
    while codigo_produto_visualizar != -1:
    imprimir_produto_por_codigo(produtos, codigo_produto_visualizar)
    codigo_produto_visualizar = int(input("Digite o código do produto que deseja visualizar (ou -1 para sair): "))

    
#9. Faça um programa que leia dois conjuntos de números inteiros, tendo
#cada um 10 elementos. Ao final o programa deve listar os elementos comuns aos
#conjuntos.
# Função para encontrar elementos comuns entre dois conjuntos
def q09():
    
    conjunto1 = []
    for x in range(10):
    elemento = int(input(f"Elemento {x + 1}: "))
    conjunto1.append(elemento)
    print("Digite os 10 elementos do primeiro conjunto:")

    print("Digite os 10 elementos do segundo conjunto:")
    conjunto2 = []
    for x in range(10):
    elemento = int(input(f"Elemento {x + 1}: "))
    conjunto2.append(elemento)
    print("\nElementos comuns aos conjuntos:")
    if elementos_comuns:
    for elemento in elementos_comuns:
        print(elemento)
    else:
    print("Não há elementos comuns.")

#10. Faça um programa que leia uma lista com 10 elementos e obtenha outra lista resultado
#cujos valores são os fatoriais da lista original.
#Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
#média dos elementos da lista.
def q10():
    
    lista_original = []
    for x in range(10):
    elemento = int(input(f'Elemento {x + 1}: '))
    lista_original.append(elemento)
    print("Digite os 10 elementos da lista:")

    maior = max(lista_original)
    menor = min(lista_original)


    total_elementos = len(lista_original)
    total_pares = sum(1 for elemento in lista_original if elemento % 2 == 0)
    percentual_pares = (total_pares / total_elementos) * 100
    media = sum(lista_original) / total_elementos
    print(f'Fatoriais da lista original:')
    print(f'Fatoriais: {fatoriais}')
    print(f'Maior elemento: {maior}')
    print(f'Menor elemento: {menor}')
    print(f'Percentual de números pares: {percentual_pares:.2f}%')
    print(f'Média dos elementos: {media:.2f}')


#11. Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
#média dos elementos da lista.
# Lendo os 10 elementos da lista

    lista = []
    for x in range(10):
    elemento = int(input(f"Elemento {x + 1}: "))
    lista_original.append(elemento)
    print("Digite os 10 elementos da lista:")


    maior = lista_original[0]
    menor = lista_original[0]
    for elemento in lista:
    if elemento > maior:
        maior = elemento
    if elemento < menor:
        menor = elemento

    total_elementos = len(lista_original)
    total_pares = sum(1 for elemento in lista_original if elemento % 2 == 0)
    percentual_pares = (total_pares / total_elementos) * 100
    media = sum(lista_original) / total_elementos

    print(f'Resultados:')
    print(f'Maior elemento: {maior}')
    print(f'Menor elemento: {menor}')
    print(f'Percentual de números pares: {percentual_pares:.2f}%')
    print(f'Média dos elementos: {media:.2f}')


#12. Crie um programa para gerenciar um sistema de reservas de mesas em uma casa
#de espetáculo. A casa possui 30 mesas de 5 lugares cada. O programa deverá
#permitir que o usuário escolha o código de uma mesa (1 a 30) e forneça a
#quantidade de lugares desejados. O programa deverá informar se foi possível
#realizar a reserva e atualizar a reserva. Se não for possível, o programa deverá
#emitir uma mensagem. O programa deve terminar quando o usuário digitar
#o código 0 (zero) para uma mesa ou quando todos os 150 lugares estiverem
#ocupados.

#13. Construa um programa que realize as reservas de passagens áreas de uma companhia.
#O programa deve permitir cadastrar o número de 10 voos e definir a
#quantidade de lugares disponíveis para cada um. Após o cadastro, leia vários
#pedidos de reserva, constituídos do número da carteira de identidade do cliente e
#do número do voo desejado. Para cada cliente, verificar se há possibilidade no
#voo desejado. Em caso afirmativo, imprimir o número da identidade do cliente e
#o número do voo, atualizando o número de lugares disponíveis. Caso contrário,
#avisar ao cliente a inexistência de lugares. A leitura do número 0 (zero) para o voo
#desejado indica o término da leitura de reservas.
# Dicionário para armazenar o número de lugares disponíveis para cada voo
def q13():
    lugares_disponiveis = {}
    for x in range(10):
    num_voo = x + 1
    lugares = int(input(f'Digite o número de lugares disponíveis para o voo {num_voo}: '))
    lugares_disponiveis[num_voo] = lugares
    print("Cadastro de voos:")
    
    print(f'Reservas de passagens aéreas:')
    while True:
    identidade_cliente = input("Digite o número da carteira de identidade do cliente (ou '0' para encerrar): ")
    
    if identidade_cliente == '0':
        break
    
    voo_desejado = int(input("Digite o número do voo desejado: "))
    if voo_desejado in lugares_disponiveis and lugares_disponiveis[voo_desejado] > 0:
        print(f'Reserva confirmada para o cliente com identidade {identidade_cliente} no voo {voo_desejado}.)
        lugares_disponiveis[voo_desejado] -= 1
    else:
        print(f'Não há lugares disponíveis no voo {voo_desejado} para o cliente com identidade {identidade_cliente}.')


     print(f'Número de lugares disponíveis após as reservas:')
     for voo, lugares in lugares_disponiveis.items():
     print(f'Número de lugares disponíveis para o voo {voo}: {lugares}')


#14. Faça um programa que armazene 50 números inteiros em uma lista. O programa
#deve gerar e imprimir uma segunda lista em que cada elemento é o quadrado do
#elemento da primeira lista.
def q14():
    lista = []
    for x in range(50):
    numero = int(input(f"Digite o {x + 1}º número: "))
    lista_original.append(numero)
    print("Digite os 50 números inteiros:")

    lista_quadrados = [x ** 2 for x in lista_original]
    print(f'Segunda lista com os quadrados dos números da primeira lista:')
    print(lista_quadrados)


#15. Faça um programa que leia e armazene vários números, até digitar o número
#0. Imprimir quantos números iguais ao último número foram lidos. O limite de
#números é 100.
def q15():
    numeros = []
    for x in range(100):
    numero = int(input(f'Digite o {x + 1}º número: '))
    print("Digite os números (digite 0 para parar):")
    if numero == 0:
        break
    numeros.append(numero)
    ultimo_numero = numeros[-1] if numeros else None
    numeros_iguais_ao_ultimo = numeros.count(ultimo_numero)
    print(f'Quantidade de números iguais ao último número lido ({ultimo_numero}): {numeros_iguais_ao_ultimo}')


#16. Crie um programa para ler um conjunto de 100 números reais e informe:
#• quantos números lidos são iguais a 30
#• quantos são maior que a média
#• quantos são iguais a média
def q16():
    numeros = []

    for x in range(100):
    numero = float(input(f'Digite o {x + 1}º número:' ))
    numeros.append(numero)
    print("Digite os 100 números reais:")

    quantidade_igual_30 = numeros.count(30)

    media = sum(numeros) / len(numeros)

    quantidade_maior_que_media = sum(1 for num in numeros if num > media)

    print(f'Quantidade de números iguais a 30: {quantidade_igual_30}')
    print(f'Quantidade de números maiores que a média ({media:.2f}): {quantidade_maior_que_media}')


#17. Faça um programa que leia um conjunto de 30 valores inteiros, armazene-os em
#um vetor e os imprima ao contrário da ordem de leitura.
# Lista para armazenar os 30 valores inteiros
def q17():
    valores = []
    for x in range(30):
    valor = int(input(f'Digite o {x + 1}º valor:'))
    valores.append(valor)
    print("Digite os 30 valores inteiros:")

    print(f'Valores na ordem reversa:')
    for x in range(29, -1, -1):
    print(f'Valores na ordem reversa:')
    print(valores[x])

#18. Faça um programa que permita entrar com 20 valores numéricos,
# em que podem existir vários elementos repetidos. Gere
#uma lista ordenada que terá apenas os elementos não repetidos.

#19. Suponha uma estrutura de 30 elementos contendo: código e telefone. Faça
#um programa que permita buscar pelo código e imprimir o telefone.

#20. Faça um programa que leia a matrícula e a média de 100 alunos. Ordene da maior
#para a menor nota e imprima uma relação contendo todas as matrículas e médias.
