from grade import montar_grade
from verificadores import verifica_linhas, verifica_quadrante, verifica_colunas
from dados import rt_pos_preenchidas,rt_nums_lidos
from leitor import ler_valor

pos_preenchidas = rt_pos_preenchidas()
nums_lidos = rt_nums_lidos()
def md_solucionador():
    """Modo automático: resolver o Sudoku."""
    pass

def md_interativo():
    """Modo interativo: jogador joga manualmente no terminal."""
    print("-"*30)
    print("\nVocê está no modo interativo.")
    md_ativo = True
    while(md_ativo):
        montar_grade(pos_preenchidas, nums_lidos)
        leitura = input("\nInsira a posição e o valor desejado: ")
        pos_atual = ler_valor(leitura)
        pos_preenchidas.append(pos_atual)
        validacao = verifica_linhas(pos_preenchidas) and verifica_colunas(pos_preenchidas) and verifica_quadrante(pos_preenchidas)
        if (validacao):
            print("\n --------->Valor Inserido!")
        else:
            print("\n --------->Valor Invalido!!!")
            pos_preenchidas.pop()

        if(len(pos_preenchidas) >= 81):
            md_ativo = False