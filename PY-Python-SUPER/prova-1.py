# Programa para verificar email e senha

# Dados cadastrados antecipadamente
email_cadastrado = "ermesson@gmail.com"
senha_cadastrada = "123456"

while True:
    # Solicita email e senha do usuário
    email_usuario = input("Digite seu email: ")
    senha_usuario = input("Digite sua senha: ")

    # Verificação de email e senha
    if email_usuario == email_cadastrado and senha_usuario == senha_cadastrada:
        print("Acesso permitido. Bem-vindo!")
        break
    else:
        print("Email ou senha incorretos. Tente novamente.")
