from projeto_xadrez_funcoes import *
from CONS import *
from termcolor import colored

tabuleiro = posiciona_pecas()
nome_jogador_b = input("NOME DO JOGADOR DAS PEÇAS BRANCAS: ")
nome_jogador_p = input("NOME DO JOGADOR DAS PEÇAS PRETAS: ")

cont = 0
while True:
    # Imprime o tabuleiro
    print()
    for a in tabuleiro:
        indice = INDICE0
        for b in a:
            if indice != QTD_C - PONTO_P:
                indice += PONTO_P
                if b in PECAS_B:
                    s = (colored(b, attrs=['bold']))
                    print("{} |".format(s), end=" ")
                elif b in PECAS_P:
                    s = (colored(b, "grey", attrs=['bold']))
                    print("{} |".format(s), end=" ")
                else:
                    s = (colored(b, "white"))
                    print("{}  |".format(s), end=" ")
            else:
                if b in PECAS_B:
                    s = (colored(b, attrs=['bold']))
                    print(s)
                elif b in PECAS_P:
                    s = (colored(b, "grey", attrs=['bold']))
                    print(s)
                else:
                    s = (colored(b, "white"))
                    print(s)
    print()
    # Abaixo desse ponto, encontram-se as condicionais que irão definir quem é o jogador da vez
    if cont % DIVISOR == INDICE0:  # Jogadas pares, indica que é a vez do jogador das peças brancas
        print("VEZ DO(A) JOGADOR(A) {}\n".format(nome_jogador_b))
        # Os laços while a seguir servem para caso a peça selecionada não seja possível ser movida, o jogador deverá
        # selecionar outra peça
        while True:
            li, co = map(int, input("EM QUE CASA ESTÁ LOCALIZADA A PEÇA QUE VOCÊ DESEJA MOVER? ").split(","))
            print()
            peca = tabuleiro[li][co]
            if peca in PECAS_B:
                lista_s = movimentos(tabuleiro, co, li, peca)
                if li > INDICE7 or co > INDICE7 or li < INDICE0 or co < INDICE0:
                    print((colored("ESSA CASA NÃO ESTA CONTIDA NO TABULEIRO", "red")))
                elif lista_s:
                    s = "ESSAS SÃO SUAS OPÇÕES DE MOVIMENTO\n{}".format(lista_s)
                    print((colored(s, "blue", attrs=['bold'])))
                    print()
                    while True:
                        mov = input("PARA QUAL DESSAS CASAS VOCÊ DESEJA MOVER A PEÇA? ")
                        li_m, co_m = map(int, mov.split(","))
                        l_m = tabuleiro[li_m][co_m]
                        if l_m in lista_s:
                            tabuleiro = moverPecas(tabuleiro, peca, li_m, co_m, li, co)
                            break
                        else:
                            print("A CASA SELECIONADA NÃO PODE SER ESCOLHIDA")
                    break
                elif lista_s == []:
                    print(colored("ESSA PEÇA NÃO PODE SE MOVER, SELECIONE OUTRA.", "red"))
                    print()
                else:
                    print("ESSA PEÇA NÃO FOI ENCONTRADA")
            elif peca in PECAS_P:
                print(colored("ESSA PEÇA É DO SEU ADVERSÁRIO. ESCOLHA UMA ALIADA.", "red"))
            else:
                print(colored("NÃO HÁ NENHUMA PEÇA NESSA CASA. SELECIONA OUTRA.", "red"))
    else:
        print("VEZ DO(A) JOGADOR(A) {}\n".format(nome_jogador_p))
        while True:
            li, co = map(int, input("EM QUE CASA ESTÁ LOCALIZADA A PEÇA QUE VOCÊ DESEJA MOVER? ").split(","))
            print()
            peca = tabuleiro[li][co]
            if peca in PECAS_P:
                lista_s = movimentos(tabuleiro, co, li, peca)
                if li > INDICE7 or co > INDICE7 or li < INDICE0 or co < INDICE0:
                    print((colored("ESSA CASA NÃO ESTA CONTIDA NO TABULEIRO", "red")))
                elif lista_s:
                    s = "ESSAS SÃO SUAS OPÇÕES DE MOVIMENTO\n{}".format(lista_s)
                    print((colored(s, "blue", attrs=['bold'])))
                    print()
                    while True:
                        mov = input("PARA QUAL DESSAS CASAS VOCÊ DESEJA MOVER A PEÇA? ")
                        li_m, co_m = map(int, mov.split(","))
                        l_m = tabuleiro[li_m][co_m]
                        if l_m in lista_s:
                            tabuleiro = moverPecas(tabuleiro, peca, li_m, co_m, li, co)
                            break
                        else:
                            print("A CASA SELECIONADA NÃO PODE SER ESCOLHIDA")
                    break
                elif lista_s == []:
                    print(colored("ESSA PEÇA NÃO PODE SE MOVER, SELECIONE OUTRA.", "red"))
                    print()
                else:
                    print("ESSA PEÇA NÃO FOI ENCONTRADA")
            elif peca in PECAS_B:
                print(colored("ESSA PEÇA É DO SEU ADVERSÁRIO. ESCOLHA UMA ALIADA.", "red"))
            else:
                print(colored("NÃO HÁ NENHUMA PEÇA NESSA CASA. SELECIONA OUTRA.", "red"))
    cont += 1  # Adiciona '+ 1' ao contador da quantidade de jogadas
