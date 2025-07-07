def ler_valor(input):
    """
    Parâmetros:
    coluna (str): Letra da coluna.

    Retorna:
    int: Índice correspondente da coluna.
    """
    leitura = []

    colunas = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
        "F": 5,
        "G": 6,
        "H": 7,
        "I": 8
    }
    if str(input[0]) in colunas:
        leitura.append(colunas[str(input[0])])
    leitura.append(int(input[2]) - 1)
    leitura.append(str(input[5]))

    return leitura


# Lê o arquivo e preenche a lista com posições iniciais do Sudoku
def leitor_txt(pos_preenchidas):
    """
    Lê o arquivo 'arq_01_cfg.txt' e preenche a lista `pos_preenchidas`
    com os valores de entrada do Sudoku.

    Parâmetros:
    pos_preenchidas (list): Lista que será preenchida.

    Retorna:
    pos_preenchidas atualizada com os valores lidosno seguinte formato:
    [coluna,linha, valor em vermelho]
    """
    nums_lidos = 0
    with open('arq_01_cfg.txt', 'r') as file:
        leitura = []
        # lista contendo a leitura completa

        for linha in file:
            leitura.append(linha.strip())

        for i in range(len(leitura)):
            aux = ler_valor(leitura[i])
            pos_preenchidas.append(aux)
            nums_lidos += 1
    return nums_lidos


