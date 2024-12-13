# Solicita ao usuário que digite 10 valores para preencher uma lista
valores = []
print("Digite 10 valores:")
for _ in range(10):
    numero = int(input("Digite um número: "))
    valores.append(numero)

# Separar os números pares e ímpares em listas diferentes
pares = []
impares = []
for numero in valores:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

# Converter a lista de ímpares em tupla
impares_tupla = tuple(impares)

# Calcular as quantidades e somas
quantidade_pares = len(pares)
quantidade_impares = len(impares)
soma_pares = sum(pares)
soma_impares = sum(impares)

# resultados
print(f"Números pares: {pares}")
print(f"Números ímpares (tupla): {impares_tupla}")
print(f"Quantidade de números pares: {quantidade_pares}")
print(f"Quantidade de números ímpares: {quantidade_impares}")
print(f"Soma dos números pares: {soma_pares}")
print(f"Soma dos números ímpares: {soma_impares}")
