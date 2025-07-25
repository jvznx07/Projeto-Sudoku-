def verifica_colunas(pos_preenchidas):
    """Verifica se uma coluna não tem números repetidos."""
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
    """Verifica se um quadrante 3x3 não tem números repetidos."""

    # Percorre os blocos de linhas que formam o topo de cada quadrante (0, 3, 6)
    for q_linha in range(0, 9, 3):
        # Percorre os blocos de colunas que formam o lado esquerdo de cada quadrante (0, 3, 6)
        for q_coluna in range(0, 9, 3):
            # Cria um conjunto para registrar os valores já vistos no quadrante atual
            vistos = set()
            # Para cada posição preenchida no Sudoku
            for item in pos_preenchidas:
                col, lin, val = item  # col = coluna, lin = linha, val = valor inserido

                # Verifica se a posição está dentro do quadrante atual
                if q_coluna <= col < q_coluna + 3 and q_linha <= lin < q_linha + 3:
                    # Se o valor já foi visto nesse quadrante, é duplicado → inválido
                    if val in vistos:
                        return False

                    # Caso contrário, adiciona o valor ao conjunto de vistos
                    vistos.add(val)
    # Se todos os quadrantes foram validados sem repetição, retorna True
    return True

def val_possiveis(pos_check, pos_preenchidas):
    num_possiveis = []
    val_in_pos = False

    for item in pos_preenchidas:
        if(item[0] == pos_check[0] and item[1] == pos_check[1]):
            val_in_pos = True
    if not val_in_pos:
        for i in range(1, 10):

            if (len(pos_check) < 3):
                pos_check.append(str(i))
            else:
                pos_check[2] = str(i)

            pos_preenchidas.append(pos_check)
            if (verifica_linhas(pos_preenchidas) and verifica_colunas(pos_preenchidas) and verifica_quadrante(pos_preenchidas)):
                num_possiveis.append(str(i))

            pos_preenchidas.pop()

    return num_possiveis

