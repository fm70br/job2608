# Sistema de Controle de Produção e Qualidade
#
# Trabalho apresentado por: Fabio Minami 
# Disciplina: Algoritmos e Lógica de Programação 
# Curso: Inteligência Artificial e Automação Digital
# UNIFECAF
#
# 2026-09-25

# listas 
pecas = [] # todas as pecas
caixas_fechadas = [] # lista de caixas fechadas
caixa_atual = [] # caixa aberta

# constantes com os valores dos critérios de qualidade e o valor do tamanho da caixa
PESO_MIN = 95
PESO_MAX = 105
CORES_VALIDAS = ("azul", "verde")
COMPRIMENTO_MIN = 10
COMPRIMENTO_MAX = 20
CAPACIDADE_CAIXA = 10

def validar_peca(peso, cor, comprimento):
    """
    Confere os critérios de qualidade.
    Retorna verdadeiro ou falso, e a lista de motivos de reprovação.    
    """
    motivos = []

    if peso < PESO_MIN or peso > PESO_MAX:
        motivos.append("Peso fora do padrão")

    if cor.lower() not in CORES_VALIDAS:
        motivos.append("Cor inválida")

    if comprimento < COMPRIMENTO_MIN or comprimento > COMPRIMENTO_MAX:
        motivos.append("Comprimento fora do padrão")

    if len(motivos) == 0:
        return True, "OK"
    else:
        return False, ", ".join(motivos)

def cadastrar_peca():
    """
    Guarda a peça aprovada na caixa aberta.
    Ao atingir a capacidade, fecha a caixa e inicia uma nova.
    """    
    global caixa_atual

    try:
        # dados da peca informados pelo usuario
        id_peca = input("ID da peça: ")
        peso = float(input("Peso (g): "))
        cor = input("Cor: ")
        comprimento = float(input("Comprimento (cm): "))
        aprovada, resultado = validar_peca(peso, cor, comprimento)

        # dicionario dos valores das peças 
        peca = {
            "id": id_peca,
            "peso": peso,
            "cor": cor,
            "comprimento": comprimento,
            "status": "Aprovada" if aprovada else "Reprovada",
            "motivo": resultado
        }

        # adiciona peca a lista pecas
        pecas.append(peca)

        # se a peca for aprovada
        if aprovada:
            # adiciona a pecaa a caixa atual
            caixa_atual.append(id_peca)
            # a quantidade de pecas chegou ao limite da caixa
            if len(caixa_atual) == CAPACIDADE_CAIXA:
                # fecha a caixa: adiciona a copia da caixa atual em caixas fechadas
                caixas_fechadas.append(caixa_atual.copy())
                print("\nCaixa fechada com 10 peças!")
                # esvazia a caixa atual
                caixa_atual.clear()

            # avisa o usuario peca aprovada
            print("\nPeça cadastrada com sucesso.")
            print("Resultado:", peca["status"])

        # se a peca for reprovada
        if not aprovada:
            # avisa o usuario peca reprovada
            print(f"\nPeça {peca['id']} REPROVADA")
            print("Motivo:", resultado)

    except ValueError:
        # avisa o usuario sobre erro de digitação
        print("Erro: informe valores numéricos válidos.")

# exibe a listagem de todas as pecas guardadas na lista de pecas
def listar_pecas():
    # zero pecas
    if len(pecas) == 0:
        print("\nNenhuma peça cadastrada.")
        return
 
    print("\n=== PEÇAS CADASTRADAS ===")
    # para cada item na lista, exibir...
    for peca in pecas:
        print("ID:", peca["id"], peca["peso"], peca["cor"], peca["comprimento"], "| Status:", peca["status"], "| Motivo:", peca["motivo"])

# apaga um item da lista de pecas
def remover_peca():
    # pergunta qual é o id da peca
    id_remover = input("Informe o ID da peça: ")
    
    # percorre a lista item por item
    for peca in pecas:
        # id encontrado
        if peca["id"] == id_remover:
            # exclui a peca da lista de pecas
            pecas.remove(peca)
            # avisa o usuario sucesso na remocao
            print("Peça removida com sucesso.")
            return

    # peca nao encontrada, avisar usuario
    print("Peça não encontrada.")

# exibe a listagem de caixas fechadas
def listar_caixas():
    # zero caixas
    if len(caixas_fechadas) == 0:
        print("\nNenhuma caixa fechada.")
        return
 
    print("\n=== CAIXAS FECHADAS ===")

    # variavel contador de caixas fechadas
    numero = 1

    # percorre a lista de caixas fechadas
    for caixa in caixas_fechadas:
        print("Caixa", numero, ":", caixa)
        # adiciona 1 a cada caixa fechada 
        numero += 1

# exibe a quantide de itens nas listas
def gerar_relatorio():    
    # listas de pecas aprovadas e reprovadas
    aprovadas = []
    reprovadas = []

    # conta a quantidade de aprovadas e reprovadas um por um
    for peca in pecas:
        if peca["status"] == "Aprovada":
            aprovadas.append(peca)
        else:
            reprovadas.append(peca)

    # exibe o relatorio
    print("\n===== RELATÓRIO FINAL =====")
    print("Total de peças cadastradas:", len(pecas))
    print("Total aprovadas:", len(aprovadas))
    print("Total reprovadas:", len(reprovadas))
    print("Caixas fechadas:", len(caixas_fechadas))

def menu():

    # laco permanece em execucao enquanto nao selecionar 0
    while True:
        print("\n===== CONTROLE DE QUALIDADE DE PEÇAS =====")
        print("1 - Cadastrar nova peça")
        print("2 - Listar peças")
        print("3 - Remover peça")
        print("4 - Listar caixas fechadas")
        print("5 - Gerar relatório final")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        # sem usar case (para manter retrocompatibilidade)
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
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":

    menu()
