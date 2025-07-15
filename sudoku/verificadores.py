# Funções a serem implementadas futuramente:
def verifica_colunas(pos_preenchidas):
    # Percorre cada coluna
    for coluna in range(9):
        # uma lista não ordenada de valores vistos(conjunto)
        val_vistos = set()
        # vai percorrer todo o pos_preenchida e o item assume o valor da lista inserida no pos_preenchidas
        for item in pos_preenchidas:
            # verifica se o número da coluna corresponde ao atual verificado no laço
            if item[0] == coluna:
                valor = item[2]
                # se o valor já estiver sido adicionado, a função retorna False
                if valor in val_vistos:
                    return False
                
                # Adiciona o valor ao conjunto val_vistos
                val_vistos.add(valor)    
    
    """Verifica se uma coluna não tem números repetidos."""
    return True


def verifica_linhas(pos_preenchidas):
    """Verifica se uma linha não tem números repetidos."""

    # Percorre cada linha
    for linha in range(9):
        # uma lista não ordenada de valores vistos(conjunto)
        val_vistos = set()
        # vai percorrer todo o pos_preenchida e o item assume o valor da lista inserida no pos_preenchidas
        for item in pos_preenchidas:
            # verifica se o número da linha corresponde ao atual verificado no laço
            if item[1] == linha:
                valor = item[2]
                # se o valor já estiver sido adicionado, a função retorna False
                if valor in val_vistos:
                    return False

                # Adiciona o valor ao conjunto val_vistos
                val_vistos.add(valor)
    return True


def verifica_quadrante(pos_preenchidas):
    inicio_linha = (pos_preenchidas[1] // 3) * 3
    inicio_coluna = (pos_preenchidas[0] // 3) * 3

    for i in range(inicio_linha, inicio_linha + 3):
        for j in range(inicio_coluna, inicio_coluna + 3):
            if pos_preenchidas[i][j] == pos_preenchidas[3]:
                return True

    
    
    
    
    
    
    
    
    """Verifica se um quadrante 3x3 não tem números repetidos."""

    return False


def val_possiveis(pos_check, pos_preenchidas):
    num_possiveis = []

    for i in range(1, 10):
        if (len(pos_check) < 3):
            pos_check.append(i)
        else:
            pos_check[2] = str(i)

        pos_preenchidas.append(pos_check)
        if (verifica_linhas(pos_preenchidas)):
            num_possiveis.append(i)

        pos_preenchidas.pop()

    return num_possiveis

def verif_entrada(entrada):
    """Vai verificar a entrada no modo interativo e no arquivo base txt
    inserido, se a entrada for inválida, ela retorna False e se for váalida retorna True"""

    colunas = set(("A", "B", "C", "D", "E", "F", "G", "H", "I"))
    linhas = set(("1", "2", "3", "4", "5", "6", "7", "8", "9"))


    if len(entrada) == 6:
        if entrada[0] in colunas and entrada[2] in linhas and entrada[5] in linhas:
            return True
        else:
            return False
    else:
        return False

