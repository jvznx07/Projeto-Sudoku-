
#Função que lê a coluna e converte uma letra em um inteiro de (0 a 8)
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
    with open('arq_01_cfg.txt','r') as file:
        leitura = []
        #lista contendo a leitura completa

        for linha in file:
            leitura.append(linha.strip())


        for i in range(len(leitura)):
            
            aux = ler_valor(leitura[i])
            pos_preenchidas.append(aux)
            nums_lidos += 1
    return nums_lidos
        


#Imprime a grade no terminal
def montar_grade(pos_prenchidas,nums_inseridos):
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

        if (i < nums_inseridos):
            grade[y][x] = "\033[31m" + str(pos_preenchidas[i][2]) +  "\033[0m"

        else:
            grade[y][x] = str(pos_preenchidas[i][2])

           
    #Imprime a grade
    for i in range(len(grade)):
        print (''.join(grade[i]))

    

# Funções a serem implementadas futuramente:
def verifica_colunas():
    """Verifica se uma coluna não tem números repetidos."""
    pass

def verifica_linhas(pos_preenchidas):
    """Verifica se uma linha não tem números repetidos."""
    
    #Percorre cada linha
    for linha in range (9):
        #uma lista não ordenada de valores vistos(conjunto)
        val_vistos = set()
        #vai percorrer todo o pos_preenchida e o item assume o valor da lista inserida no pos_preenchidas
        for item in pos_preenchidas:
            #verifica se o número da linha corresponde ao atual verificado no laço
            if item[1] == linha:
                valor = item[2]
                #se o valor já estiver sido adicionado, a função retorna False
                if valor in val_vistos:
                    return False
                
                #Adiciona o valor ao conjunto val_vistos
                val_vistos.add(valor)
    return True

def verifica_quadrante(pos_preenchidas):
    """Verifica se um quadrante 3x3 não tem números repetidos."""
    
    pass
        
def val_possiveis(pos_check,pos_preenchidas):
    num_possiveis = []

    for i in range (1,10):
        if (len(pos_check) < 3):
            pos_check.append(i)
        else:
            pos_check[2] = str(i)
        
        pos_preenchidas.append(pos_check)
        if (verifica_linhas(pos_preenchidas)):
            num_possiveis.append(i)

        pos_preenchidas.pop()
        

    return num_possiveis


def md_solucionador():
    """Modo automático: resolver o Sudoku."""
    pass

def md_interativo():
    """Modo interativo: jogador joga manualmente no terminal."""

    pass


pos_preenchidas = []
def main():
    nums_lidos = leitor_txt(pos_preenchidas)
    montar_grade(pos_preenchidas,nums_lidos)

main()