from InquirerPy import prompt
from InquirerPy.base.control import Choice

def obter_perfil_usuario():
    perguntas = [
        {
            "type": "list",
            "name": "nivel_python",
            "message": "Qual o seu nível de experiência com Python?",
            "choices": [
                Choice(value="iniciante", name="Iniciante (Estou aprendendo as bases)"),
                Choice(value="avancado", name="Avançado (Já domino automações e APIs)"),
            ],
            "default": "iniciante",
        },
    ]

    return prompt(perguntas)

def principal():
    print("--- Bem-vindo ao Sistema de Perfil ---")
    
    respostas = obter_perfil_usuario()
    nivel = respostas.get("nivel_python")

    if nivel == "avancado":
        print("\n Impressionante! Você já está pronto para projetos complexos.")
    else:
        print("\n Que legal! O Python é uma jornada incrível. Continue praticando!")

if __name__ == "__main__":
    try:
        principal()
    except KeyboardInterrupt:
        print("\n\nOperação cancelada pelo usuário.")
