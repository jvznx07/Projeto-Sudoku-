from modos import *
from grade import montar_grade
from leitor import *
import sys

pos_preenchidas = []
leitura_batch = []

#Verificações para saber o número de argumentos passados no terminal
if len(sys.argv) == 2:
    arq_cfg = sys.argv[1]
    md_batch_atv = False
    nums_lidos, erro_leitura = leitor_txt(pos_preenchidas, arq_cfg)

elif len(sys.argv) == 3:
    arq_cfg = sys.argv[1]
    arq_jog = sys.argv[2]
    nums_lidos, erro_leitura = leitor_md_batch(arq_cfg, arq_jog, leitura_batch)
    md_batch_atv = True


def main():


    print("<------------------SUDOKU------------------>\n")
    montar_grade(pos_preenchidas,nums_lidos)

    #verifica se as pistas são válidas
    if verifica_colunas(pos_preenchidas) and verifica_linhas(pos_preenchidas) and verifica_quadrante(pos_preenchidas):
        if len(pos_preenchidas) >= 1 and len(pos_preenchidas) <= 80:
            if erro_leitura == 0:
                print("\nEscolha o modo que você deseja:")
                print("1.Modo interativo(Você resolve o sudoku).")
                print("2.Modo Solucionador(O programa resolverá).")
                jogar = True
            else:
                print(f"\nErro na leitura da linha {nums_lidos + 1} do arquivo: {arq_cfg}.")
                jogar = False
        else:
            print("Tamanho do arquivo de pistas inválido")

    else:
        print("\nSuas pistas são inválidas.")
        jogar = False


    #escolha do modo solucionador ou interativo
    while jogar:
        escolha = str(input("Digite sua escolha: "))
        if escolha == "1":
            md_interativo(pos_preenchidas,nums_lidos)
            jogar = False

        elif escolha == "2":
            md_solucionador(pos_preenchidas,nums_lidos)
            jogar = False

        else:
            print("Opção invalida! Tente novamente.")





if __name__ == "__main__":
    if md_batch_atv:
        md_batch(pos_preenchidas,nums_lidos,leitura_batch)
        if len(pos_preenchidas) == 81:
            print("A grade foi preenchida com sucesso!")

        else:
            print("A grade não foi preenchida!")

    else:
        main()