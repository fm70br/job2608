# Sistema de Controle de Produção e Qualidade

Protótipo em Python para automatizar o controle de qualidade e o armazenamento de peças em uma linha de montagem, substituindo a inspeção manual por regras objetivas de aprovação e reprovação.

---

## Sumário

- [Funcionamento do sistema](#funcionamento-do=sistema)
- [Critérios de qualidade](#critérios-de-qualidade)
- [Estrutura do código](#estrutura-do-código)
- [Requisitos](#requisitos)
- [Como executar](#como-executar)
- [Passo a passo de uso (menu)](#passo-a-passo-de-uso-menu)
- [Exemplos de entradas e saídas](#exemplos-de-entradas-e-saídas)
- [Tratamento de erros](#tratamento-de-erros)
- [Possíveis evoluções](#possíveis-evoluções)

---

## Funcionamento do sistema

O programa mantém três estruturas de dados em memória durante a execução:

| Estrutura | Conteúdo |
|---|---|
| `pecas` | Todas as peças cadastradas, aprovadas e reprovadas, com seus dados e status |
| `caixa_atual` | A caixa aberta no momento, com as peças aprovadas ainda não fechadas |
| `caixas_fechadas` | Lista de caixas que já atingiram a capacidade máxima |

Fluxo geral de uma peça:

1. O usuário informa **id, peso, cor e comprimento**.
2. O sistema valida os dados (números, id não vazio e não duplicado).
3. A peça é avaliada segundo os critérios de qualidade.
4. Se **aprovada**, ela é adicionada à caixa aberta. Ao atingir 10 peças, a caixa é fechada e uma nova é iniciada automaticamente.
5. Se **reprovada**, o(s) motivo(s) da reprovação são registrados junto com a peça — o sistema verifica **todos os critérios**, não parando no primeiro erro, para que uma peça possa ter mais de um motivo de reprovação.

Ao remover uma peça aprovada do cadastro, o sistema **reorganiza automaticamente as caixas**, refazendo o empacotamento das peças aprovadas restantes, para que nenhuma caixa fique com contagem inconsistente.

## Critérios de qualidade

Uma peça é **aprovada** somente se atender às três condições ao mesmo tempo:

| Critério | Faixa aceita |
|---|---|
| Peso | entre **95 g** e **105 g** (inclusive) |
| Cor | **azul** ou **verde** |
| Comprimento | entre **10 cm** e **20 cm** (inclusive) |

Peças fora de qualquer uma dessas faixas são reprovadas, com o(s) motivo(s) específico(s) registrado(s).

## Estrutura do código

O arquivo `controle_qualidade.py` está organizado em blocos de funções, cada uma com uma única responsabilidade:

```
controle_qualidade.py
├── Constantes de configuração (critérios de qualidade e capacidade da caixa)
├── Estado do sistema (listas globais: pecas, caixa_atual, caixas_fechadas)
├── Funções 
│   ├── validar_peca()              -> confere os critérios de qualidade
│   ├── cadastrar_peca()            -> adiciona a peça à caixa e fecha ao atingir 10
│   ├── listar_pecas()
│   ├── remover_peca()
│   ├── listar_caixas()
│   ├── gerar_relatorio()
│   └── menu() -> laço do menu interativo
└── main()  
```

## Requisitos

- **Python 3.8 ou superior**
- Nenhuma biblioteca externa é necessária (o programa usa apenas recursos nativos da linguagem)

## Como executar

1. Baixe ou clone o repositório:

   ```bash
   git clone [<URL-do-repositório>](https://github.com/fm70br/job2608.git)
   cd job2608
   ```

2. Execute o script com o Python:

   ```bash
   python controle_qualidade.py
   ```

   Em sistemas Linux/macOS, pode ser necessário usar `python3`:

   ```bash
   python3 controle_qualidade.py
   ```

3. O menu interativo será exibido no terminal. Basta digitar o número da opção desejada e pressionar Enter.

## Passo a passo de uso (menu)

Ao iniciar, o programa exibe:

```
=== CONTROLE DE QUALIDADE DE PEÇAS ===
1 - Cadastrar nova peça
2 - Listar peças
3 - Remover peça
4 - Listar caixas fechadas
5 - Gerar relatório final
0 - Sair
Escolha uma opção:
```

| Opção | O que faz |
|---|---|
| **1** | Cadastra uma nova peça: pede id, peso, cor e comprimento, avalia e informa se foi aprovada ou reprovada |
| **2** | Lista todas as peças cadastradas, separadas em aprovadas e reprovadas (mostrando o motivo das reprovadas) |
| **3** | Remove uma peça pelo id informado e, se necessário, reorganiza as caixas |
| **4** | Mostra as caixas já fechadas (com os ids das peças) e o status da caixa aberta no momento |
| **5** | Gera o relatório final: total de aprovadas, total de reprovadas com motivos, e quantidade de caixas utilizadas |
| **0** | Encerra o programa |

## Exemplos de entradas e saídas

### Exemplo 1 — cadastro de peça aprovada

**Entrada:**
```
Escolha uma opção: 1
ID da peça: ID01
Peso (g): 100
Cor: azul
Comprimento (cm): 15
```

**Saída:**
```
Peça cadastrada com sucesso.
Resultado: Aprovada
```

### Exemplo 2 — cadastro de peça reprovada (com múltiplos motivos)

**Entrada:**
```
Escolha uma opção: 1
ID da peça: ID02
Peso (g): 120
Cor: vermelha
Comprimento (cm): 25
```

**Saída:**
```
Peça ID02 REPROVADA
Motivo: Peso fora do padrão, Cor inválida, Comprimento fora do padrão
```

### Exemplo 3 — fechamento automático de caixa (10ª peça aprovada)

**Saída ao cadastrar a 10ª peça aprovada em sequência:**
```
Caixa fechada com 10 peças!

Peça cadastrada com sucesso.
Resultado: Aprovada
```

### Exemplo 4 — listar peças

**Entrada:**
```
Escolha uma opção: 2
```

**Saída:**
```
=== PEÇAS CADASTRADAS ===
ID: ID01 100.0 azul 15.0 | Status: Aprovada | Motivo: OK
ID: ID02 120.0 vermelha 25.0 | Status: Reprovada | Motivo: Peso fora do padrão, Cor inválida, Comprimento fora do padrão
```

### Exemplo 5 — remover uma peça

**Entrada:**
```
Escolha uma opção: 3
Informe o ID da peça: ID02
```

**Saída:**
```
Peça removida com sucesso.
```

### Exemplo 6 — listar caixas fechadas

**Entrada:**
```
Escolha uma opção: 4
```

**Saída:**
```
=== CAIXAS FECHADAS ===
Caixa 1 : ['id01', 'id02', 'id03', 'id04', 'id05', 'id06', 'id07', 'id08', 'id09', 'id10']
Caixa 2 : ['id11', 'id14', 'id15', 'id16', 'id17', 'id19', 'id20', 'id21', 'id22', 'id23']
```

### Exemplo 7 — relatório final

**Entrada:**
```
Escolha uma opção: 5
```

**Saída:**
```
===== RELATÓRIO FINAL =====
Total de peças cadastradas: 23
Total aprovadas: 20
Total reprovadas: 3
Caixas fechadas: 2
```

### Exemplo 9 — saindo do programa

**Entrada:**
```
Escolha uma opção: 0
```

**Saída:**
```
Encerrando o sistema. Até logo!
```

## Possíveis evoluções

- Persistência dos dados em arquivo (CSV, JSON) ou banco de dados, mantendo o histórico entre execuções.
- Integração com sensores (balança, sensor óptico, leitor de código de barras) para entrada automática dos dados, eliminando a digitação manual.
- Exportação do relatório final em PDF ou planilha.
- Interface gráfica (desktop ou web) no lugar do menu em terminal.
