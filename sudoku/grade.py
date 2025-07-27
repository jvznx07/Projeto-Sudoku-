"""
Aluno 1: Arthur Rodrigues Fernandes | Matrícula: 580801
Aluno 2: João Victor Alves Aprigio | Matrícula: 582694
"""

def montar_grade(pos_preenchidas, nums_inseridos):
    '''
    Parâmetros:
    pos_prenchidas (matriz): Lista de valores preenchidos na grade.
    num_inseridos: numeros lidos no arquivo de pistas para
    pinta-los de vermelho no terminal.
    '''

    colunas = "    A   B   C    D   E   F    G   H   I   "
    linha1 = " ++---+---+---++---+---+---++---+---+---++ "
    linha2 = "||   |   |   ||   |   |   ||   |   |   ||"
    linha3 = " ++===+===+===++===+===+===++===+===+===++ "

    # preenchendo a grade como uma lista aninhada
    grade = [list(colunas), list(linha1)]
    for i in range(1, 10):

        grade.append(list(str(i) + linha2 + str(i)))
        if (i == 3 or i == 6):
            grade.append(list(linha3))
        else:
            grade.append(list(linha1))

    grade.append(colunas)

    # Insere os valores na grade
    for i in range(len(pos_preenchidas)):

        if pos_preenchidas[i][0] < 3:
            x = int(pos_preenchidas[i][0]) * 4 + 4

        elif pos_preenchidas[i][0] < 6:
            x = int(pos_preenchidas[i][0]) * 4 + 5

        else:
            x = int(pos_preenchidas[i][0]) * 4 + 6

        y = pos_preenchidas[i][1] * 2 + 2

        if i < nums_inseridos:
            grade[y][x] = "\033[31m" + str(pos_preenchidas[i][2]) + "\033[0m"

        else:
            grade[y][x] = str(pos_preenchidas[i][2])

    # Imprime a grade
    for i in range(len(grade)):
        print(''.join(grade[i]))