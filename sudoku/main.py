from leitor import leitor_txt, ler_valor
from modos import md_interativo, md_solucionador
from verificadores import verifica_linhas, verifica_quadrante, verifica_colunas, val_possiveis
from dados import rt_nums_lidos, rt_pos_preenchidas
from grade import montar_grade


pos_preenchidas = rt_pos_preenchidas()
nums_lidos = rt_nums_lidos()
def main():

    montar_grade(pos_preenchidas,nums_lidos)
    print("<------------------SUDOKU------------------>")
    print("Escolha o modo que você deseja")
    print("\n1.Modo interativo(Você resolve o sudoku)")
    print("2.Modo Solucionador(O programa resolverá")

    escolha = "0"
    while(escolha != "1" and escolha != "2"):
        escolha = str(input("Digite sua escolha: "))
        if escolha == "1":
            md_interativo()

        elif escolha == "2":
            md_solucionador()

        else:
            print("Opção invalida! Tente novamente.")

if __name__ == "__main__":
    main()