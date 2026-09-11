import csv

def ver_peso(peso):
    if int(peso) >= 95 and int(peso) <= 105:
        return True
    else:
        return False

def ver_cor(cor):
    if cor == "azul" or cor == "verde":
        return True
    else:
        return False

def ver_comprimento(comprimento):
    if int(comprimento) >= 10 and int(comprimento) <= 20:
        return True
    else:
        return False

arquivo = input("Informe o arquivo csv: ")

# Open the file using a context manager (safely closes the file when done)
with open(arquivo, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    
    # Optional: Skip the header row if you don't want to print it
    header = next(reader) 

    aprov = []
    repro = []
    box = {}
    
    for row in reader:        

        box.update({row[0]: {row[1], row[2], row[3]}})
        peso_valid = ver_peso(row[1])
        cor_valid = ver_cor(row[2])
        compr_valid = ver_comprimento(row[3])
        
        if peso_valid == True and cor_valid == True and compr_valid == True:        
            print(row, ' -> ', 'APROVADO' )  # 'row' is a list, e.g., ['John', 'Doe', '30']
            aprov.append(row[0])
        else:
            print(row, ' -> ', peso_valid, cor_valid, compr_valid, '**reprovado**' )  # 'row' is a list, e.g., ['John', 'Doe', '30']
            repro.append(row[0])

print(f'APROVADOS: {aprov}\nREPROVADOS: {repro}')

for peca in box:
    print(peca)        

for peca in box.values():
    print(peca)       
