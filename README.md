# Sistema de Controle de Produção e Qualidade

Protótipo em Python para automatizar o controle de qualidade e o armazenamento de peças em uma linha de montagem, substituindo a inspeção manual por regras objetivas de aprovação e reprovação.

## Funcionamento do sistema

O programa mantém três estruturas de dados em memória durante a execução:

| Estrutura | Conteúdo |
|---|---|
| `pecas` | Todas as peças cadastradas, aprovadas e reprovadas, com seus dados e status |
| `caixa_atual` | A caixa aberta no momento, com as peças aprovadas ainda não fechadas |
| `caixas_fechadas` | Lista de caixas que já atingiram a capacidade máxima |

Fluxo geral de uma peça:

1. O usuário informa **id, peso, cor e comprimento**.
2. A peça é avaliada segundo os critérios de qualidade.
3. Se **aprovada**, ela é adicionada à caixa aberta. Ao atingir 10 peças, a caixa é fechada e uma nova é iniciada automaticamente.
4. Se **reprovada**, o(s) motivo(s) da reprovação são registrados junto com a peça — o sistema verifica **todos os critérios**, não parando no primeiro erro, para que uma peça possa ter mais de um motivo de reprovação.

Ao remover uma peça aprovada do cadastro, o sistema **reorganiza automaticamente as caixas**, refazendo o empacotamento das peças aprovadas restantes, para que nenhuma caixa fique com contagem inconsistente.

## Critérios de qualidade

Uma peça é **aprovada** somente se atender às três condições ao mesmo tempo:

| Critério | Faixa aceita |
|---|---|
| Peso | entre **95 g** e **105 g** (inclusive) |
| Cor | **azul** ou **verde** |
| Comprimento | entre **10 cm** e **20 cm** (inclusive) |

As peças que não estiverem dentro dessas faixas são reprovadas, e cada critério fora do padrão é registrado.

## Estrutura do código

O arquivo `controle_qualidade.py` está organizado em blocos de funções:

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
- Não há necessidade de instalação de nenhuma biblioteca externa (o programa usa somente os recursos nativos da linguagem)

## Como executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/fm70br/job2608.git
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
| **1** | Cadastra uma nova peça: solicita id, peso, cor e comprimento. Avalia e informa se a peça foi aprovada ou reprovada |
| **2** | Lista todas as peças cadastradas, separadas em aprovadas e reprovadas (exibe o motivo das reprovadas) |
| **3** | Remove uma peça pelo id informado
| **4** | Mostra as caixas já fechadas (com os ids das peças) e o estado da caixa aberta no momento |
| **5** | Gera o relatório final: totais de: peças cadastradas, aprovadas, reprovadas, e quantidade de caixas fechadas |
| **0** | Encerra o programa |

## Exemplos

### 1. cadastro de peça aprovada

```
Escolha uma opção: 1
ID da peça: id01
Peso (g): 100
Cor: azul
Comprimento (cm): 15
```

```
Peça cadastrada com sucesso.
Resultado: Aprovada
```

### 2. cadastro de peça reprovada (com múltiplos motivos)

```
Escolha uma opção: 1
ID da peça: id02
Peso (g): 120
Cor: vermelha
Comprimento (cm): 25
```

```
Peça id02 REPROVADA
Motivo: Peso fora do padrão, Cor inválida, Comprimento fora do padrão
```

### 3. fechamento automático de caixa (10ª peça aprovada)

**Saída ao cadastrar a 10ª peça aprovada em sequência:**
```
Caixa fechada com 10 peças!

Peça cadastrada com sucesso.
Resultado: Aprovada
```

### 4. listar peças

```
Escolha uma opção: 2
```

```
=== PEÇAS CADASTRADAS ===
ID: id01 100.0 azul 15.0 | Status: Aprovada | Motivo: OK
ID: id02 120.0 vermelha 25.0 | Status: Reprovada | Motivo: Peso fora do padrão, Cor inválida, Comprimento fora do padrão
```

### 5. remover uma peça

```
Escolha uma opção: 3
Informe o ID da peça: id02
```

```
Peça removida com sucesso.
```

### 6. listar caixas fechadas

```
Escolha uma opção: 4
```

```
=== CAIXAS FECHADAS ===
Caixa 1 : ['id01', 'id03', 'id04', 'id05', 'id06', 'id07', 'id08', 'id09', 'id10', 'id11']
Caixa 2 : ['id12', 'id13', 'id15', 'id16', 'id17', 'id19', 'id20', 'id21', 'id22', 'id23']
```

### 7. relatório final

```
Escolha uma opção: 5
```

```
===== RELATÓRIO FINAL =====
Total de peças cadastradas: 23
Total aprovadas: 20
Total reprovadas: 3
Caixas fechadas: 2
```

### 8. encerrando o programa

```
Escolha uma opção: 0
```

```
Encerrando o sistema. Até logo!
```

## Possíveis evoluções

- Persistência dos dados em arquivo (CSV, JSON) ou banco de dados, para manter o histórico entre execuções.
- Integração com sensores (balança, sensor óptico, leitor de código de barras) para entrada automática dos dados.
- Inclusão de mais detalhes no relatório final e exportação em PDF ou planilha.
- Interface gráfica (desktop ou web) no lugar do menu em terminal.
