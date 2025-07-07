from leitor import leitor_txt, ler_valor
from verificadores import verifica_linhas, verifica_quadrante, verifica_colunas, val_possiveis


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

    

pos_preenchidas = []
def main():
    nums_lidos = leitor_txt(pos_preenchidas)
    montar_grade(pos_preenchidas,nums_lidos)

main()