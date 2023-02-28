# lê a string a ser invertida
string = input("Digite uma string: ")

# converte a string em uma lista de caracteres
lista_caracteres = list(string)

# inicializa as variáveis de índice
i = 0
j = len(lista_caracteres) - 1

# inverte os caracteres da lista
while i < j:
    # troca os caracteres de posição
    lista_caracteres[i], lista_caracteres[j] = lista_caracteres[j], lista_caracteres[i]

    # atualiza os índices
    i += 1
    j -= 1

# converte a lista de volta para string
string_invertida = "".join(lista_caracteres)

# imprime a string invertida
print("String invertida:", string_invertida)
