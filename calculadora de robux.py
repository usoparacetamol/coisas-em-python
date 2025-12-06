# Calculadora de Robux com menu repetitivo
TAXA = 0.07375
senha = 123

print("=== Calculadora de Robux ===")
print("Digite 'rbx' para calcular pelo número de Robux.")
print("Digite 'r' para calcular pelo valor em reais.")
print("Digite 'sair' para encerrar.\n")

while True:
    opcao = input("Escolha uma opção (rbx/r/sair): ").lower().strip()

    if opcao == "rbx":
        quantidade = float(input("Quantos Robux você quer comprar? "))
        custo = quantidade * TAXA
        print(f"💰 Isso vai custar R${custo:.2f} reais.\n")

    elif opcao == "123":
         print("voce descobriu a senha, as opcoes secretas sao (sla/oi/pq vc fez uma calculadora de robux?)")

    elif opcao == "r":
        reais = float(input("Quantos reais você vai gastar? "))
        robux = reais / TAXA
        print(f"🎮 Com R${reais:.2f} você compra {robux:.0f} Robux.\n")
            
    elif opcao == "sla":
         print("Entao decida e volte depois")
         break
         
    elif opcao == "pq vc fez uma calculadora de robux?":
         print("a maioria das calculadoras da internet sao apenas para voce comprar robux, e nao calcular de verdade. vendo isso decidi fazer, e tambem, tava querendo treinar python")

    elif opcao == "oi":
         print("tchau")
         break

    elif opcao == "sair":
        print("👋 Encerrando a calculadora.")  
        break

    else:
        print("⚠️ Opção inválida! Digite apenas 'rbx', 'r' ou 'sair'.\n")