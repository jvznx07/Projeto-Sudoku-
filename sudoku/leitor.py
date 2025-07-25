def remove_espac(entrada):
    saida = []
    for i in range(len(entrada)):

        if entrada[i] != " ":
            saida.append(entrada[i])

    return "".join(saida)

def verif_entrada(entrada):
    """Vai verificar a entrada no modo interativo e no arquivo base txt
    inserido, se a entrada for inválida, ela retorna False e se for váalida retorna True"""
    verif = remove_espac(entrada)

    colunas = set(["A", "B", "C", "D", "E", "F", "G", "H", "I"])
    linhas = set(["1", "2", "3", "4", "5", "6", "7", "8", "9"])

    if verif[0] == "?" or verif[0] == "!":
        if len(verif) == 4:
            if verif[1].upper() in colunas and verif[3] in linhas:
                return True
            else:
                return False
        else:
            return False

    else:
        if len(verif) == 5:
            if (verif[0].upper() in colunas) and (verif[2] in linhas) and (verif[4] in linhas):
                return True

            else:
                return False

        else:
            return False


def ler_valor(entrada):
    """
    Parâmetros:
    coluna (str): Letra da coluna.

    Retorna:
    int: Índice correspondente da coluna.
    """

    entrada = remove_espac(entrada)
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

    if entrada[0] == "?" or entrada[0] == "!":
        leitura.append(colunas[(str(entrada[1]).upper())])
        leitura.append(int(entrada[3]) - 1)

    else:
        leitura.append(colunas[str(entrada[0].upper())])
        leitura.append(int(entrada[2]) - 1)
        leitura.append(str(entrada[4]))

    return leitura



# Lê o arquivo e preenche a lista com posições iniciais do Sudoku
def leitor_txt(pos_preenchidas,nome_arquivo):
    """
    Lê o arquivo 'arq_01_cfg.txt' e preenche a lista `pos_preenchidas`
    com os valores de entrada do Sudoku.
    """

    nums_lidos = 0
    try:
        with open(nome_arquivo, 'r') as file:

            for linha in file:

                leitura = linha.strip()
                if ler_valor(leitura) not in pos_preenchidas and verif_entrada(leitura):
                    pos_preenchidas.append(ler_valor(leitura))
                    nums_lidos += 1

                elif not verif_entrada(leitura[i]):
                    return nums_lidos, 1

    except FileNotFoundError:
        print("Erro na leitura do arquivo")


    return nums_lidos, 0

def leitor_md_batch(arq_cfg, arq_jog, leitura_batch):
    nums_lidos = 0
    erro_leitura = 0
    valores_ivalidos = False

    try:
        with open(arq_cfg, "r") as file:
            for linha in file:
                leitura = linha.strip()
                if verif_entrada(leitura):
                    if ler_valor(leitura) not in leitura_batch:
                        leitura_batch.append(ler_valor(leitura))
                        nums_lidos += 1
                else:
                    valores_ivalidos = True

            if valores_ivalidos:
                print("Arquivo de Pistas com valores inválidos")
                erro_leitura = 1

    except FileNotFoundError:
        print("Arquivo de pistas não encontrado")

    try:
        with open(arq_jog, "r") as file:
            for linha in file:
                leitura = linha.strip()
                if verif_entrada(leitura):
                    leitura_batch.append(ler_valor(leitura))

                else:
                    print("Arquivo de Jogadas com valores inválidos")

    except FileNotFoundError:
        print("Arquivo Jogadas não encontrado")

    return nums_lidos, erro_leitura
