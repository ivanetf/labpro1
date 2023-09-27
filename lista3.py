'''
Lista de Exercícios referentes a estruturas de iteração (repetição)
'''

#1.Faça um programa que imprima todos os números de 1 até 100.
def questao01():
for x in range(1,100)
print(x)
  

#2. Faça um programa que imprima todos os números pares de 100 até 1.
def questao02():
    for x in range(100,1,-1)
      print(x)


#3. Faça um programa que imprima os múltiplos de 5, no intervalo de 1 até 500.
def questao03():
   for x in range(0,500,5)
      print(x)

#4. Faça umprograma que permita entrar com o nome, a idade e o sexo de 20
#pessoas.O programa deve imprimir o nome da pessoa se ela for do sexo masculino
#e tiver mais de 21 anos.
def questao04():
    for i in range(20):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    sexo = input("Digite o sexo da pessoa (M/F): ")
        if sexo == "M" and idade > 21:
            print(" sexo masculino com mais de 21 anos:
            print(nome)

#5. Sabendo-se que a unidade lógica e aritmética calcula o produto através de somas
#sucessivas, crie um programa que calcule o produto de dois números inteiros
#lidos. Suponha que os números lidos sejam positivos.
def q05():
    pass

#6. Crie um programa que imprima os 20 primeiros termos da série de Fibonacci.
#Observação: os dois primeiros termos desta série são 1 e 1 e os demais são gerados
#a partir da soma dos anteriores. Exemplo:
#• 1 + 1 = 2, terceiro termo;
#• 1 + 2 = 3, quarto termo, etc.
def q06():
    pass

#7. Crie um programa que permita entrar com o nome, a nota da
#prova 1 e da prova 2 de 15 alunos. Ao final, imprimir uma listagem, contendo:
#nome, nota da prova 1, nota da prova 2, e média das notas de cada aluno. Ao final,
#imprimir a média geral da turma.
def q07():
    mediageral = 0
      for x in range(15):
      nome = input(f"Digite o nome do aluno {i + 1}: ")
      nota_prova1 = float(input(f"Digite a nota da prova 1: "))
      nota_prova2 = float(input(f"Digite a nota da prova 2: "))
    
       media = (nota1 + nota2) / 2
       mediageral+=media
       print(f'nome:  {nome} ')
       print(f'nota1: {nota1} ')
       print(f'nota2: {nota2} ')
       print(f'media: {media} ')

    print(mediageral/15)
    
    




#8. Faça umprograma que permita entrar com o nome e o salário bruto de 10 pessoas.
#Após ler os dados, imprimir o nome e o valor da alíquota do imposto de renda
#calculado conforme a tabela a seguir:
#Salário IRRF
#Salário menor que R$1300,00 Isento
#Salário maior ou igual a R$1300,00 e menor que R$2300,00 10% do salário bruto
#Salário maior ou igual a R$2300,00 15% do salário bruto
def q08():
    pass

#9. No dia da estréia do filme "Procurando Dory", uma grande emissora de TV realizou
#uma pesquisa logo após o encerramento do filme. Cada espectador respondeu
#a um questionário no qual constava sua idade e a sua opinião em relação ao filme:
#excelente - 3; bom - 2; regular - 1. Criar um programa que receba a idade e a
#opinião de 20 espectadores, calcule e imprima:
#• A média das idades das pessoas que responderam excelente;
#• A quantidade de pessoas que responderam regular;
#• A percentagem de pessoas que responderam bom entre todos os expectadores
#analisados.
def q09():
  
idade_excelente_total = 0
qtd_excelente = 0
qtd_regular = 0
qtd_bom = 0

for i in range(20):
    idade = int(input(f"Digite a idade do espectador {i + 1}: "))
    opiniao = int(input(f"Digite a opinião do espectador {i + 1} (excelente - 3, bom - 2, regular - 1): "))

  
    if opiniao == 3:
        idade_excelente_total += idade
        qtd_excelente += 1
    elif opiniao == 2:
        qtd_bom += 1
    elif opiniao == 1:
        qtd_regular += 1
 
          if qtd_excelente > 0:
          media_idade_excelente = idade_excelente_total / qtd_excelente
        else:
        media_idade_excelente = 0

          percentagem_bom = (qtd_bom / 20) * 100


      print(f"Média das idades das pessoas que responderam excelente: {media_idade_excelente:.2f} anos")
      print(f"Quantidade de pessoas que responderam regular: {qtd_regular}")
      print(f"Percentagem de pessoas que responderam bom: {percentagem_bom:.2f}%")


#10. Em um campeonato Europeu de Volleyball, se inscreveram 30 países. Sabendo-se
#que na lista oficial de cada país consta, além de outros dados, peso e idade de 12
#jogadores, crie um programa que apresente as seguintes informações:
#
#• O peso médio e a idade média de cada um dos times;
#• O atleta mais pesado de cada time;
#• O atleta mais jovem de cada time;
#• O peso médio e a idade média de todos os participantes.
def q10():
    pass
    
#11. Construa um programa que leia vários números e informe quantos números
#entre 100 e 200 foram digitados. Quando o valor 0 (zero) for lido, o algoritmo
#deverá cessar sua execução.
def q11():
    pass

#12. Dado um país A, com 5 milhões de habitantes e uma taxa de natalidade de 3% ao
#ano, e um país B com 7 milhões de habitantes e uma taxa de natalidade de 2% ao
#ano, fazer um programa que calcule e imprima o tempo necessário para que a
#população do país A ultrapasse a população do país B.
def q12():
    pass

#13. Uma empresa de fornecimento de energia elétrica faz a leitura mensal dos medidores
#de consumo. Para cada consumidor, são digitados os seguintes dados:
#• número do consumidor
#• quantidade de kWh consumidos durante o mês
#• tipo (código) do consumidor
#1-residencial, preço em reais por kWh = 0,3
#2-comercial, preço em reais por kWh = 0,5
#3-industrial, preço em reais por kWh = 0,7
#Os dados devem ser lidos até que seja encontrado o consumidor com número 0
#(zero). O programa deve calcular e imprimir:
#• O custo total para cada consumidor
#• O total de consumo para os três tipos de consumidor
#• Amédia de consumo dos tipos 1 e 2

      total_consumo_residencial = 0
      total_consumo_comercial = 0
      total_consumo_industrial = 0
      total_custos = 0
      num_consumidores_residencial_comercial = 0

      while True:
    numero_consumidor = int(input("Digite o número do consumidor (ou 0 para sair): "))
  
    if numero_consumidor == 0:
        break
    
    consumo_kwh = float(input("Digite a quantidade de kWh consumidos durante o mês: "))
    tipo_consumidor = int(input("Digite o tipo do consumidor (1 - residencial, 2 - comercial, 3 - industrial): "))
    
    if tipo_consumidor == 1:
        preco_por_kwh = 0.3
        total_consumo_residencial += consumo_kwh
    elif tipo_consumidor == 2:
        preco_por_kwh = 0.5
        total_consumo_comercial += consumo_kwh
        num_consumidores_residencial_comercial += 1
    elif tipo_consumidor == 3:
        preco_por_kwh = 0.7
        total_consumo_industrial += consumo_kwh
    else:
        print("Tipo de consumidor inválido. Ignorando este consumidor.")
        continue
    
    custo_total = consumo_kwh * preco_por_kwh
    total_custos += custo_total
    
  
            print(f"Consumidor {numero_consumidor}: Custo Total = R${custo_total:.2f}")
  
            if num_consumidores_residencial_comercial > 0:
    media_consumo_residencial_comercial = (total_consumo_residencial + total_consumo_comercial) / num_consumidores_residencial_comercial
            else:
    media_consumo_residencial_comercial = 0


        print(f"Total de consumo residencial: {total_consumo_residencial} kWh")
        print(f"Total de consumo comercial: {total_consumo_comercial} kWh")
        print(f"Total de consumo industrial: {total_consumo_industrial} kWh")
        print(f"Média de consumo dos tipos 1 e 2: {media_consumo_residencial_comercial:.2f} kWh")
        print(f"Custo total para todos os consumidores: R${total_custos:.2f}")

#14. Faça um programa que leia vários números inteiros e apresente o fatorial de cada
#número. O algoritmo encerra quando se digita um número menor do que 1.n
def q14():
     fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
 
while True:
    numero = int(input("Digite um número inteiro (ou um número menor que 1 para sair): "))
    
    if numero < 1:
        break
    
    resultado = fatorial(numero)
    print(f"O fatorial de {numero} é {resultado}")


#15. Faça um programa que permita entrar com a idade de várias pessoas e
#imprima:
#• total de pessoas com menos de 21 anos
#• total de pessoas com mais de 50 anos
def questao15():
    pass

#16. Sabendo-se que a unidade lógica e aritmética calcula a divisão por meio de subtrações
#sucessivas, criar um algoritmo que calcule e imprima o resto da divisão de
#números inteiros lidos. Para isso, basta subtrair o divisor ao dividendo, sucessivamente,
#até que o resultado seja menor do que o divisor. O número de subtrações
#realizadas corresponde ao quociente inteiro e o valor restante da subtração corresponde
#ao resto. Suponha que os números lidos sejam positivos e que o dividendo
#seja maior do que o divisor.
#Exemplo:
#  10 / 5
#  10 é o Dividendo
#  5 é o Divisor
#  2 é o Quociente (resultado inteiro da divisão)
#  0 é o Resto da Divisão
def q16():
    

#17. Crie um programa que possa ler um conjunto de pedidos de compra e
#calcule o valor total da compra. Cada pedido é composto pelos seguintes campos:
#• número de pCedido
#72 Aula 3. Estruturas de Iteração
#• data do pedido (dia, mês, ano)
#• preço unitário
#• quantidade
#O programa deverá processar novos pedidos até que o usuário digite 0 (zero)
#como número do pedido.
 total_compra = 0

   while True:
    numero_pedido = int(input("Digite o número do pedido (ou 0 para sair): "))
    if numero_pedido == 0:
        break
      
    dia = int(input("Digite o dia do pedido: "))
    mes = int(input("Digite o mês do pedido: "))
    ano = int(input("Digite o ano do pedido: "))
    preco_unitario = float(input("Digite o preço unitário: "))
    quantidade = int(input("Digite a quantidade: "))
    
    valor_pedido = preco_unitario * quantidade
    total_compra += valor_pedido
    
    print(f"Pedido {numero_pedido} ({dia}/{mes}/{ano}): R${valor_pedido:.2f}")
    print(f"Valor total da compra: R${total_compra:.2f}")


#18. Uma pousada estipulou o preço para a diária em R$30,00 e mais uma taxa de
#serviços diários de:
#• R$15,00, se o número de dias for menor que 10;
#• R$8,00, se o número de dias for maior ou igual a 10;
#Faça umprograma que imprima o nome, a conta e o número da conta de cada
#cliente e ao final o total faturado pela pousada.
#O programa deverá ler novos clientes até que o usuário digite 0 (zero) como
#número da conta.

#19. Emuma Universidade, os alunos das turmas de informática fizeram uma prova
#de algoritmos. Cada turma possui um número de alunos. Criar um programa que
#imprima:
#• quantidade de alunos aprovados;
#• média de cada turma;
#• percentual de reprovados.
#Obs.: Considere aprovado comnota >= 7.0

#20. Uma pesquisa de opinião realizada no Rio de Janeiro, teve as seguintes perguntas:
#• Qual o seu time de coração?
#1-Fluminense;
#2-Botafogo;
#3-Vasco;
#4-Flamengo;
#5-Outros
#• Onde você mora?
#1-RJ;
#2-Niterói;
#3-Outros
#• Qual o seu salário?
#Faça um programa que imprima:
#• o número de torcedores por clube;
#• a média salarial dos torcedores do Botafogo;
#• o número de pessoas moradoras do Rio de Janeiro, torcedores de outros
#clubes;
#• o número de pessoas de Niterói torcedoras do Fluminense
#3.12. Exercícios da Aula 73
#Obs.: O programa encerra quando se digita 0 para o time.

torcedores_fluminense = 0
torcedores_botafogo = 0
torcedores_vasco = 0
torcedores_flamengo = 0
torcedores_outros = 0
media_salarial_botafogo = 0
num_moradores_rj_outros = 0
num_moradores_niteroi_fluminense = 0
total_salarial_botafogo = 0
total_torcedores_botafogo = 0


while True:
    time = int(input("Qual o seu time de coração? (1-Fluminense, 2-Botafogo, 3-Vasco, 4-Flamengo, 5-Outros, 0-Sair): "))
    
    if time == 0:
        break
    
    moradia = int(input("Onde você mora? (1-RJ, 2-Niterói, 3-Outros): "))
    salario = float(input("Qual o seu salário? "))
    
    if time == 1:
        torcedores_fluminense += 1
    elif time == 2:
        torcedores_botafogo += 1
        total_salarial_botafogo += salario
        total_torcedores_botafogo += 1
    elif time == 3:
        torcedores_vasco += 1
    elif time == 4:
        torcedores_flamengo += 1
    elif time == 5:
        torcedores_outros += 1
    
    if moradia == 1 and time == 5:
        num_moradores_rj_outros += 1
    
    if moradia == 2 and time == 1:
        num_moradores_niteroi_fluminense += 1

 
     if total_torcedores_botafogo > 0:
    media_salarial_botafogo = total_salarial_botafogo / total_torcedores_botafogo


print(f"Número de torcedores por clube:")
print(f"Fluminense: {torcedores_fluminense}")
print(f"Botafogo: {torcedores_botafogo}")
print(f"Vasco: {torcedores_vasco}")
print(f"Flamengo: {torcedores_flamengo}")
print(f"Outros: {torcedores_outros}")
print(f"Média salarial dos torcedores do Botafogo: R${media_salarial_botafogo:}")
print(f"Número de pessoas moradoras do Rio de Janeiro, torcedores de outros clubes: {num_moradores_rj_outros}")
print(f"Número de pessoas de Niterói torcedoras do Fluminense: {num_moradores_niteroi_fluminense}")


#21. Emuma universidade cada aluno possui os seguintes dados:
#• Renda pessoal;
#• Renda familiar;
#• Total gasto com alimentação;
#• Total gasto com outras despesas;
#Faça um programa que imprima a porcentagem dos alunos que gasta acima de
#R$200,00 com outras despesas. O número de alunos com renda pessoal maior
#que a renda familiar e a porcentagem gasta com alimentação e outras despesas
#em relação às rendas pessoal e familiar.
#Obs.: O programa encerra quando se digita 0 para a renda pessoal.
def q21():
  renda_pessoal = 0
  renda_familiar = 0
  total_gasto_com_alimentacao = 0
  total_gasto_com_outras_despesas = 0

if aluno > 200:
  total_gasto_com_outras_despesas += 1
if aluno >= renda_pessoal:

  




#22. Crie um programa que ajude o DETRAN a saber o total de recursos que foram
#arrecadados com a aplicação de multas de trânsito.
#O algoritmo deve ler as seguintes informações para cada motorista:
#• número da carteira de motorista (de 1 a 4327);
#• número demultas;
#• valor de cada uma das multas.
#Deve ser impresso o valor da dívida para cada motorista e ao final da leitura o
#total de recursos arrecadados (somatório de todas as multas). O programa deverá
#imprimir tambémo número da carteira domotorista que obteve o maior número
#de multas.
#Obs.: O programa encerra ao ler a carteira de motorista de valor 0.


#23. Crie um programa que leia um conjunto de informações (nome, sexo, idade, peso
#e altura) dos atletas que participaram de uma olimpíada, e informar:
#• a atleta do sexo feminino mais alta;
#• o atleta do sexomasculinomais pesado;
#• amédia de idade dos atletas.
#Obs.: Deverão se lidos dados dos atletas até que seja digitado o nome @ para um
#atleta.
#Para resolver este exercício, consulte a aula 7 que aborda o tratamento de strings,
#como comparação e atribuição de textos.

#24. Faça um programa que calcule quantos litros de gasolina são usados em uma
#viagem, sabendo que um carro faz 10 km/litro. O usuário fornecerá a velocidade
#do carro e o período de tempo que viaja nesta velocidade para cada trecho do
#percurso. Então, usando as fórmulas distância = tempo x velocidade e litros
#consumidos = distância / 10, o programa computará, para todos os valores nãonegativos
#de velocidade, os litros de combustível consumidos. O programa deverá
#imprimir a distância e o número de litros de combustível gastos naquele trecho.
#Deverá imprimir também o total de litros gastos na viagem. O programa encerra
#quando o usuário informar umvalor negativo de velocidade.
#74 Aula 3. Estruturas de Iteração
total_litros = 0

while True:
    velocidade = float(input("Digite a velocidade do carro (em km/h, negativo para sair): "))
    
    if velocidade < 0:
        break
    
    tempo = float(input("Digite o período de tempo (em horas): "))
  
    distancia = tempo * velocidade
    
     (litros = distância / 10)
    litros_consumidos = distancia / 10
    
    total_litros += litros_consumidos
    
    print(f"Trecho: Distância = {distancia} km, Litros Consumidos = {litros_consumidos} litros")
    
     print(f"Total de litros gastos na viagem: {total_litros} litros")

#25. Faça umprograma que calcule o imposto de renda de umgrupo de contribuintes,
#considerando que:
#a) os dados de cada contribuinte (CIC, número de dependentes e renda bruta
#anual) serão fornecidos pelo usuário via teclado;
#b) para cada contribuinte será feito umabatimento de R$600 por dependente;
#c) a renda líquida é obtida diminuindo-se o abatimento com os dependentes
#da renda bruta anual;
#d) para saber quanto o contribuinte deve pagar de imposto, utiliza-se a tabela
#a seguir:
#Renda Líquida Imposto
#até R$1000 Isento
#de R$1001 a R$5000 15%
#acima de R$5000 25%
#e) o valor de CIC igual a zero indica final de dados;
#f ) o programa deverá imprimir, para cada contribuinte, o número do CIC e o
#imposto a ser pago;
#g) ao final o programa deverá imprimir o total do imposto arrecadado pela
#Receita Federal e o número de contribuintes isentos;
#h) leve em consideração o fato de o primeiro CIC informado poder ser zero.

total_imposto = 0
num_contribuintes_isentos = 0
    while True:
    cic = int(input("Digite o número do CIC (ou 0 para sair): "))

      if cic == 0:
        break
    
    num_dependentes = int(input("Digite o número de dependentes: "))
    renda_bruta_anual = float(input("Digite a renda bruta anual: "))
    
    renda_liquida = renda_bruta_anual - (num_dependentes * 600)
    
        if renda_liquida <= 1000:
        imposto = 0
        num_contribuintes_isentos += 1
        elif 1001 <= renda_liquida <= 5000:
        imposto = renda_liquida * 0.15
        else:
        imposto = renda_liquida * 0.25
    
       total_imposto += imposto
    
       print(f"Contribuinte CIC {cic}: Imposto a ser pago: R${imposto:.2f}")

       print(f"Total do imposto arrecadado: R${total_imposto:.2f}")
       print(f"Número de contribuintes isentos: {num_contribuintes_isentos}")


#26. Foi feita uma pesquisa de audiência de canal de TV em várias casas de uma
#certa cidade, em umdeterminado dia. Para cada casa visitada foram fornecidos o
#número do canal (4, 5, 7, 12) e o número de pessoas que estavam assistindo a ele
#naquela casa. Se a televisão estivesse desligada, nada seria anotado, ou seja, esta
#casa não entraria na pesquisa. Criar um programa que:
#• Leia um número indeterminado de dados, isto é, o número do canal e o
#número de pessoas que estavam assistindo;
#• Calcule e imprima a porcentagem de audiência em cada canal.
#Obs.: Para encerrar a entrada de dados, digite o número do canal zero.

audiencia_canal4 = 0
audiencia_canal5 = 0
audiencia_canal7 = 0
audiencia_canal12 = 0
total_audiencia = 0

while True:
    canal = int(input("Digite o número do canal (4, 5, 7, 12) ou 0 para encerrar: "))
    
    if canal == 0:
        break
    
    audiencia = int(input("Digite o número de pessoas assistindo: "))
    
    if canal == 4:
        audiencia_canal4 += audiencia
    elif canal == 5:
        audiencia_canal5 += audiencia
    elif canal == 7:
        audiencia_canal7 += audiencia
    elif canal == 12:
        audiencia_canal12 += audiencia
    
    total_audiencia += audiencia

       if total_audiencia > 0:
    percentagem_canal4 = (audiencia_canal4 / total_audiencia) * 100
    percentagem_canal5 = (audiencia_canal5 / total_audiencia) * 100
    percentagem_canal7 = (audiencia_canal7 / total_audiencia) * 100
    percentagem_canal12 = (audiencia_canal12 / total_audiencia) * 100
    else:
    percentagem_canal4 = 0
    percentagem_canal5 = 0
    percentagem_canal7 = 0
    percentagem_canal12 = 0

print(f"Porcentagem de audiência no Canal 4: {percentagem_canal4:.2f}%")
print(f"Porcentagem de audiência no Canal 5: {percentagem_canal5:.2f}%")
print(f"Porcentagem de audiência no Canal 7: {percentagem_canal7:.2f}%")
print(f"Porcentagem de audiência no Canal 12: {percentagem_canal12:.2f}%")

#27. Crie um programa que calcule e imprima o CR do período para os alunos de
#computação. Para cada aluno, o algoritmo deverá ler:
#• número da matrícula;
#• quantidade de disciplinas cursadas;
#• notas em cada disciplina;
#Além do CR de cada aluno, o programa deve imprimir o melhor CR dos
#alunos que cursaram5 ou mais disciplinas.
#• fim da entrada de dados é marcada por uma matrícula inválida (matrículas
#válidas de 1 a 5000);
#• CR do aluno é igual à média aritmética de suas notas.

#28. Construa umprograma que receba a idade, a altura e o peso de várias pessoas,
#Calcule e imprima:
#3.12. Exercícios da Aula 75
#• a quantidade de pessoas com idade superior a 50 anos;
#• amédia das alturas das pessoas com idade entre 10 e 20 anos;
#• a porcentagem de pessoas com peso inferior a 40 quilos entre todas as
#pessoas analisadas.

#29. Construa um programa que receba o valor e o código de várias mercadorias
#vendidas em umdeterminado dia. Os códigos obedecem a lista a seguir:
#L-limpeza
#A-Alimentação
#H-Higiene
#Calcule e imprima:
#• o total vendido naquele dia, com todos os códigos juntos;
#• o total vendido naquele dia em cada um dos códigos.
#Obs.: Para encerrar a entrada de dados, digite o valor da mercadoria zero.

#30. Faça um programa que receba a idade e o estado civil (C-casado, S-solteiro, Vviúvo
#e D-desquitado ou separado) de várias pessoas. Calcule e imprima:
#• a quantidade de pessoas casadas;
#• a quantidade de pessoas solteiras;
#• amédia das idades das pessoas viúvas;
#• a porcentagem de pessoas desquitadas ou separadas dentre todas as pessoas
#analisadas.
#Obs.: Para encerrar a entrada de dados, digite um número menor que zero para a
#idade.
