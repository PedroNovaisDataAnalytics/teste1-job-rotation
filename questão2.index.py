# número a ser verificado
numero_verificar = 13

# inicialização dos dois primeiros valores da sequência
valor_anterior = 0
valor_atual = 1

# loop para calcular a sequência de Fibonacci até encontrar um número maior ou igual ao número a ser verificado
while valor_atual < numero_verificar:
    # calcula o próximo valor da sequência
    proximo_valor = valor_anterior + valor_atual
    
    # atualiza os valores anteriores para a próxima iteração
    valor_anterior = valor_atual
    valor_atual = proximo_valor
    
# verifica se o número a ser verificado pertence ou não à sequência
if valor_atual == numero_verificar:
    print(numero_verificar, "pertence à sequência de Fibonacci")
else:
    print(numero_verificar, "não pertence à sequência de Fibonacci")
