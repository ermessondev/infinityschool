# SIMULADOR DE CADASTRO DE SENHA E INICIALIZAÇÃO DE CELULAR
import time

# Cadastro de senha pelo usuário
senha_cadastrada = input("Cadastre a sua senha: ")
time.sleep(1)
print("Celular inicializando...")
time.sleep(2)
print("Por favor, insira a senha para desbloquear.")

# Variável de controle
tentativas_restantes = 3

# Loop para tentativas de desbloqueio
for tentativa in range(tentativas_restantes):
    senha_digitada = input(f"Tentativa {tentativa + 1}/{tentativas_restantes} - Digite a senha: ")
    
    if senha_digitada == senha_cadastrada:
        print("Bem-vindo.")
        break
    else:
        if tentativa < tentativas_restantes - 1:
            print(f"Senha incorreta. Você tem {tentativas_restantes - tentativa - 1} tentativa(s) restante(s).")
        else:
            print("Senha incorreta. Celular bloqueado.")
