
#Função que lê a coluna e converte uma letra em um inteiro de (0 a 8)
def ler_colunas(coluna):
    """
    Parâmetros:
    coluna (str): Letra da coluna.

    Retorna:
    int: Índice correspondente da coluna.
    """
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
    if str(coluna) in colunas:
        return colunas[str(coluna)]

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
    with open('arq_01_cfg.txt','r') as file:
        leitura = []
        #lista contendo a leitura completa

        for linha in file:
            leitura.append(linha.strip())


        for i in range(len(leitura)):
            
            aux = [ler_colunas(leitura[i][0]),int(leitura[i][2]) - 1,"\033[31m" + str(leitura[i][5]) + "\033[0m"]
            pos_preenchidas.append(aux)
        


#Imprime a grade no terminal
def montar_grade(pos_prenchidas):
    '''
    Parâmetros:
    pos_prenchidas (list): Lista de valores preenchidos na grade.
    '''

    colunas = "    A   B   C    D   E   F    G   H   I   "
    linha1 = " ++---+---+---++---+---+---++---+---+---++ "
    linha2 = "||   |   |   ||   |   |   ||   |   |   ||"
    linha3 = " ++===+===+===++===+===+===++===+===+===++ "

    #preenchendo a grade como uma lista aninhada
    grade = [list(colunas), list(linha1)]
    for i in range(1,10):
    
        grade.append(list(str(i) + linha2 + str(i)))
        if (i ==3 or i == 6):
            grade.append(list(linha3))
        else:
            grade.append(list(linha1))

    grade.append(colunas)

    #Insere os valores na grade
    for i in range(len(pos_prenchidas)):
        if pos_preenchidas[i][0] < 3:
            x = int(pos_preenchidas[i][0])*4 + 4
        
        elif pos_preenchidas[i][0] < 6 :
            x = int(pos_preenchidas[i][0])*4 + 5

        else:
            x = int(pos_preenchidas[i][0])*4 + 6

        y = pos_preenchidas[i][1]*2 + 2

        grade[y][x] = str(pos_preenchidas[i][2])

           
    #Imprime a grade
    for i in range(len(grade)):
        print (''.join(grade[i]))

    

# Funções a serem implementadas futuramente:
def verifica_coluna():
    """Verifica se uma coluna não tem números repetidos."""
    pass

def verifica_linha():
    """Verifica se uma linha não tem números repetidos."""
    pass

def verifica_quadrante():
    """Verifica se um quadrante 3x3 não tem números repetidos."""
    pass

def md_solucionador():
    """Modo automático: resolver o Sudoku."""
    pass

def md_interativo():
    """Modo interativo: jogador joga manualmente no terminal."""
    pass



pos_preenchidas = []
leitor_txt(pos_preenchidas)
montar_grade(pos_preenchidas)
