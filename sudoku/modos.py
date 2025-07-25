from grade import montar_grade
from verificadores import *
from leitor import *


def md_solucionador(pos_preenchidas,nums_lidos):
    """Modo automático: resolver o Sudoku."""
    num_possiveis = []
    while len(pos_preenchidas) < 81:
        for coluna in range(9):
            for linha in range(9):
                num_possiveis = val_possiveis([coluna,linha], pos_preenchidas)
                if(len(num_possiveis) == 1 and [coluna, linha, num_possiveis[0]] not in pos_preenchidas):
                    pos_preenchidas.append([coluna, linha, num_possiveis[0]])

    montar_grade(pos_preenchidas, nums_lidos)


def md_interativo(pos_preenchidas, nums_lidos):
    """Modo interativo: jogador joga manualmente no terminal."""
    print("-"*40)
    montar_grade(pos_preenchidas, nums_lidos)
    print("\n  Insira o valor desejado no seguinte formato\n'<coluna>,<linha>: <valor>', por exemplo:")
    print("A,1: 1")
    print("\nPara pedir dica é só digitar '?<coluna>,<linha>', exemplo:")
    print("?D,1")
    print("\nE para pedir excluir uma jogda '!<coluna>,<linha>', exemplo:")
    print("!A,2")

    md_ativo = True
    while md_ativo :
        leitura = input("\nInsira a posição e o valor desejado: ")

        if leitura[0] == "!":
            if verif_entrada(leitura):
                pos_atual = ler_valor(leitura)
                pos_valida = False


                if len(pos_preenchidas) > nums_lidos:
                    for item in pos_preenchidas:
                        if item[0] == pos_atual[0] and item[1] == pos_atual[1]:
                            pos_valida = True
                            pos_atual = item

                if pos_valida:
                    pos_preenchidas.remove(pos_atual)
                    print("Valor Removido.\n")

                else:
                    print("Esse valor não pode ser removido.\n")

        elif leitura[0] == "?":
            if verif_entrada(leitura):
                pos_atual = ler_valor(leitura)
                print(val_possiveis(pos_atual, pos_preenchidas))

        else:
            if verif_entrada(leitura):
                pos_atual = ler_valor(leitura)
                pos_preenchidas.append(pos_atual)

                validacao = verifica_linhas(pos_preenchidas) and verifica_colunas(pos_preenchidas) and verifica_quadrante(pos_preenchidas)
                if validacao:
                    montar_grade(pos_preenchidas, nums_lidos)
                else:
                    print("\nValor Inválido!!!\n")
                    pos_preenchidas.pop()

            if len(pos_preenchidas) >= 81:
                md_ativo = False


def md_batch(pos_preenchidas, nums_pistas,leitura_batch):

    colunas = {
        0: "A" , 1: "B", 2: "C", 3: "D", 4: "E",
        5: "F", 6: "G", 7: "H", 8: "I"
    }
    for i in range(nums_pistas):
        pos_atual = leitura_batch[i]
        pos_preenchidas.append(pos_atual)



    for i in range(nums_pistas,len(leitura_batch)):
        item = leitura_batch[i]

        pos_preenchidas.append(item)
        if not(verifica_linhas(pos_preenchidas) and verifica_colunas(pos_preenchidas) and verifica_quadrante(pos_preenchidas)):
            pos_preenchidas.pop()
            print(f"A jogada ({colunas[item[0]]},{item[1] + 1}) = {item[2]} é inválida!")

