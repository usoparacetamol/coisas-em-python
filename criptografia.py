import os
from cryptography.fernet import Fernet
from InquirerPy import prompt
from InquirerPy.base.control import Choice

def carregar_ou_gerar_chave():
    if os.path.exists("chave.key"):
        with open("chave.key", "rb") as f_chave:
            return f_chave.read()
    else:
        chave = Fernet.generate_key()
        with open("chave.key", "wb") as f_chave:
            f_chave.write(chave)
        return chave

def menu_principal():
    chave = carregar_ou_gerar_chave()
    f = Fernet(chave)
    
    while True:
        perguntas = [
            {
                "type": "list",
                "name": "opcao",
                "message": "--- MENU DE SEGURANÇA ---",
                "choices": [
                    Choice(value="cripto", name="1. Criptografar novo texto"),
                    Choice(value="descripto", name="2. Descriptografar um código (Token)"),
                    Choice(value="sair", name="3. Sair"),
                ],
            },
        ]

        respostas = prompt(perguntas)
        opcao = respostas.get("opcao")

        if opcao == "cripto":
            texto_pergunta = [{"type": "input", "name": "texto", "message": "Digite o que deseja esconder:"}]
            texto = prompt(texto_pergunta).get("texto")
            
            if texto:
                token = f.encrypt(texto.encode())
                print(f"\n✅ TEXTO CRIPTOGRAFADO (Guarde isso):")
                print(f"{token.decode()}\n")
            
        elif opcao == "descripto":
            token_pergunta = [{"type": "input", "name": "token", "message": "Cole o código (Token) para abrir:"}]
            token_usuario = prompt(token_pergunta).get("token")
            
            if token_usuario:
                try:
                    texto_revelado = f.decrypt(token_usuario.encode()).decode()
                    print(f"\n🔓 CONTEÚDO REVELADO: {texto_revelado}\n")
                except Exception:
                    print("\n❌ ERRO: Chave incorreta ou código inválido!\n")

        elif opcao == "sair":
            print("\nSaindo... Mantenha sua 'chave.key' segura!")
            break

if __name__ == "__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        print("\n\nOperação cancelada pelo usuário.")
