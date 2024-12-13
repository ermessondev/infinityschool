# Programa que lê números inteiros até que o usuário digite 0 e exibe quantidade, soma e média

quantidade = 0
soma = 0

while True:
    numero = int(input("Digite um número inteiro (digite 0 para sair): "))
    if numero == 0:
        break
    quantidade += 1
    soma += numero

if quantidade > 0:
    media = soma / quantidade
    print(f"Quantidade de números digitados: {quantidade}")
    print(f"Soma dos números: {soma}")
    print(f"Média aritmética: {media:.2f}")
else:
    print("Nenhum número foi digitado.")