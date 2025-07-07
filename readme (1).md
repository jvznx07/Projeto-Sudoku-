# Sudoku Terminal

Um pequeno projeto em Python que imprime, valida e (em breve) resolve quebra‑cabeças Sudoku diretamente no terminal, com números iniciais destacados em vermelho.

## ✨ Funcionalidades

- **Leitura de configuração**: carrega valores iniciais a partir do arquivo `arq_01_cfg.txt`.
- **Renderização colorida**: exibe a grade 9×9 no terminal com ANSI/Colorama.
- **Modos planejados**:
  - **Interativo**: o usuário preenche as casas manualmente.
  - **Solucionador**: resolve o Sudoku automaticamente.

## 📂 Estrutura do projeto

```
├── sudoku.py            # Arquivo principal (contém as funções do jogo)
├── arq_01_cfg.txt       # Configuração inicial do tabuleiro
└── README.md            # Este documento
```

## 🔧 Pré‑requisitos

- Python ≥ 3.9

## 🚀 Como executar

```bash
python main.py
```

1. O script carrega `arq_01_cfg.txt`.
2. A grade é exibida no terminal.
3. (Futuro) Escolha entre modo **interativo** ou **solver**.

### Formato do `arq_01_cfg.txt`

Cada linha descreve um valor fixo na grade. Exemplo:

```
A 1 5
B 3 7
C 1 6
```

| Coluna | Linha | Valor |
| ------ | ----- | ----- |
| A‑I    | 1‑9   | 1‑9   |

> O parser espera que a letra da coluna esteja no índice 0, o número da linha no índice 2 e o valor no índice 5 da string. Ajuste se necessário.

## 🗂️ Principais funções

| Função                            | Descrição                                                |
| --------------------------------- | -------------------------------------------------------- |
| `ler_colunas`                     | Converte a letra de coluna em índice 0‑8.                |
| `leitor_txt`                      | Lê o arquivo de configuração e popula `pos_preenchidas`. |
| `montar_grade`                    | Renderiza a grade no terminal.                           |
| `verifica_linha/coluna/quadrante` | (TODO) Validações de regras.                             |
| `md_interativo`                   | (TODO) Modo de jogo manual.                              |
| `md_solucionador`                 | (TODO) Solver automático.                                |

## 🛠️ Próximos passos

- Implementar validações de linha/coluna/quadrante.
- Adicionar solver usando backtracking.
- Criar menu CLI para escolher modo.
- Escrever testes unitários (pytest).

##

