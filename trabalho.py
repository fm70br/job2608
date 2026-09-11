

print("CONTROLE DE PRODUÇÃO E QUALIDADE\n")
print("1. Cadastrar nova peça")
print("2. Listar peças aprovadas/reprovadas")
print("3. Remover peça cadastrada")
print("4. Listar caixas fechadas")
print("5. Gerar relatório final\n")

opcao = int(input("escolha 1 a 5: "))

match opcao:
    case 1:
        print("Informe (id, peso, cor e comprimento)")
    case 2:
        print("escolheu 2")
    case 3:
        print("escolheu 3")        
    case 4:
        print("4")
    case 5:
        print("5")
    case _:
        print("Opção inválida")


def ver_peso(peso):
    # verifica o peso da peca
    if peso >= 95 and peso <= 105:
        return True
    else:
        return False

def ver_cor(cor):
    # verifica a cor da peca
    if cor == "azul" or cor == "verde":
        return True
    else:
        return False

def ver_comprimento(comprimento):
    # verifica o comprimento da peca
    if comprimento >= 10 and comprimento <= 20:
        return True
    else:
        return False




















