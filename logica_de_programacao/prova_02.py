# Programa que calcula multa por excesso de velocidade

# Solicita ao usuário a velocidade do carro
velocidade = float(input("Informe a velocidade do carro em km/h: "))

# Verifica se a velocidade ultrapassa 80 km/h
if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * 20
    print(f"Você foi multado! O valor da multa é de R${multa:.2f}.")
else:
    print("Velocidade dentro do limite permitido. Boa viagem!")
