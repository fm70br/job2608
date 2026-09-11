# Sistema de Controle de Produção e Qualidade
# Código gerado pelo copilot

pecas = []
caixas_fechadas = []
caixa_atual = []

CAPACIDADE_CAIXA = 10

def validar_peca(peso, cor, comprimento):

    motivos = []

    if peso < 95 or peso > 105:
        motivos.append("Peso fora do padrão")

    if cor.lower() not in ["azul", "verde"]:
        motivos.append("Cor inválida")

    if comprimento < 10 or comprimento > 20:
        motivos.append("Comprimento fora do padrão")

    if len(motivos) == 0:
        return True, "Aprovada"
    else:
        return False, ", ".join(motivos)

def cadastrar_peca():
    global caixa_atual

    try:
        id_peca = input("ID da peça: ")
        peso = float(input("Peso (g): "))
        cor = input("Cor: ")
        comprimento = float(input("Comprimento (cm): "))
        aprovada, resultado = validar_peca(peso, cor, comprimento)

        peca = {
            "id": id_peca,
            "peso": peso,
            "cor": cor,
            "comprimento": comprimento,
            "status": "Aprovada" if aprovada else "Reprovada",
            "motivo": resultado
        }
 
        pecas.append(peca)

        if aprovada:
            caixa_atual.append(id_peca)

            if len(caixa_atual) == CAPACIDADE_CAIXA:
                caixas_fechadas.append(caixa_atual.copy())
                print("\nCaixa fechada com 10 peças!")
                caixa_atual.clear()

            print("\nPeça cadastrada com sucesso.")
            print("Resultado:", peca["status"])
 
        if not aprovada:
            print("Motivo:", resultado)

    except ValueError:
        print("Erro: informe valores numéricos válidos.")

def listar_pecas():
    if len(pecas) == 0:
        print("\nNenhuma peça cadastrada.")
        return
 
    print("\n=== PEÇAS CADASTRADAS ===")

    for peca in pecas:
        print("ID:", peca["id"], "| Status:", peca["status"], "| Motivo:", peca["motivo"])

def remover_peca():
    id_remover = input("Informe o ID da peça: ")
 
    for peca in pecas:
        if peca["id"] == id_remover:
            pecas.remove(peca)
            print("Peça removida com sucesso.")
            return

    print("Peça não encontrada.")

def listar_caixas():
    if len(caixas_fechadas) == 0:
        print("\nNenhuma caixa fechada.")
        return
 
    print("\n=== CAIXAS FECHADAS ===")

    numero = 1

    for caixa in caixas_fechadas:
        print("Caixa", numero, ":", caixa)
        numero += 1

def gerar_relatorio():
    aprovadas = []
    reprovadas = []

    for peca in pecas:
        if peca["status"] == "Aprovada":
            aprovadas.append(peca)
        else:
            reprovadas.append(peca)

    print("\n===== RELATÓRIO FINAL =====")
    print("Total de peças cadastradas:", len(pecas))
    print("Total aprovadas:", len(aprovadas))
    print("Total reprovadas:", len(reprovadas))
    print("Caixas fechadas:", len(caixas_fechadas))

def menu():

    while True:

        print("\n1 - Cadastrar nova peça")
        print("2 - Listar peças")
        print("3 - Remover peça")
        print("4 - Listar caixas fechadas")
        print("5 - Gerar relatório final")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_peca()
        elif opcao == "2":
            listar_pecas()
        elif opcao == "3":
            remover_peca()
        elif opcao == "4":
            listar_caixas()
        elif opcao == "5":
            gerar_relatorio()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":

    menu()
