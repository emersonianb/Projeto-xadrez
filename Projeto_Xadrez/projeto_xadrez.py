from projeto_xadrez_funcoes import *
from CONS import *
from termcolor import colored

tabuleiro = posiciona_pecas()
nome_jogador_b = input("NOME DO JOGADOR DAS PEÇAS BRANCAS: ").upper()
nome_jogador_p = input("NOME DO JOGADOR DAS PEÇAS PRETAS: ").upper()

lista_pec_b = lista_pec_b
lista_pec_p = lista_pec_p
peca = ""
li_m = 0
co_m = 0
cont = 0
cont_tb_7 = 0
cont_tb_0 = 0
cont_tp_7 = 0
cont_tp_0 = 0
cont_rb = 0
cont_rp = 0
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
            if cont > 1:
                cheque = indentificaCheque(tabuleiro, li_m, co_m, peca, "RE_B")
                if cheque:
                    print()
                    print(colored("SEU REI ESTÁ EM CHEQUE. CUIDADO, MOVA-O!", "red", attrs=['bold']))
                    print()
            ent = input("EM QUE CASA ESTÁ LOCALIZADA A PEÇA QUE VOCÊ DESEJA MOVER? ").upper()
            if ent == "DESISTIR":
                m = "O JOGADOR {} DESISTIU, SENDO ASSIM, O JOGADOR {} VENCEU".format(nome_jogador_p, nome_jogador_b)
                print()
                print(colored(m, "green", attrs=['bold']))
                exit(0)
            li, co = map(int, ent.split(","))
            peca = tabuleiro[li][co]
            if peca == "TO_B" or peca == "RE_B" and cont_rb == 0:
                if peca == "TO_B":
                    if co == 0:
                        if cont_tb_0 == 0 and tabuleiro[0][3] == "RE_B":
                            vazio = roqueCasV(tabuleiro, 0, 3, co)
                            if vazio:
                                faz_ro = input("VOCÊ GOSTARIA DE FAZER O ROQUE? ").upper()
                                if faz_ro == "SIM":
                                    tabuleiro = roqueMov(tabuleiro, 0, 3, co, "RE_B", "TO_B")
                                    break
                    elif co == 7:
                        if cont_tb_7 == 0 and tabuleiro[0][3] == "RE_B":
                            vazio = roqueCasV(tabuleiro, 0, 3, co)
                            if vazio:
                                faz_ro = input("VOCÊ GOSTARIA DE FAZER O ROQUE? ").upper()
                                if faz_ro == "SIM":
                                    tabuleiro = roqueMov(tabuleiro, 0, 3, co, "RE_B", "TO_B")
                                    break
                elif peca == "RE_B" and li == 0 and co == 3:
                    to_e = False
                    to_d = False
                    if tabuleiro[0][0] == "TO_B":
                        if cont_tb_0 == 0:
                            vazio = roqueCasV(tabuleiro, li, co, 0)
                            if vazio:
                                to_e = True
                    elif tabuleiro[0][7] == "TO_B":
                        if cont_tb_7 == 0:
                            vazio = roqueCasV(tabuleiro, li, co, 0)
                            if vazio:
                                to_d = True
                    if to_e == True and to_d == True:
                        faz_ro = input("VOCÊ GOSTARIA DE FAZER O ROQUE? ").upper()
                        if faz_ro == "SIM":
                            esc_to = input("ESCOLHA UMA TORRE:\nTO_E    TO_D").upper()
                            if esc_to == "TO_E":
                                tabuleiro = roqueMov(tabuleiro, li, co, 0, "RE_B", "TO_B")
                                break
                            elif esc_to == "TO_D":
                                tabuleiro = roqueMov(tabuleiro, li, co, 7, "RE_B", "TO_B")
                                break
                    elif to_e:
                        faz_ro = input("VOCÊ GOSTARIA DE FAZER O ROQUE? ").upper()
                        if faz_ro == "SIM":
                            tabuleiro = roqueMov(tabuleiro, li, co, 0, "RE_B", "TO_B")
                            break
                    elif to_d:
                        faz_ro = input("VOCÊ GOSTARIA DE FAZER O ROQUE? ").upper()
                        if faz_ro == "SIM":
                            tabuleiro = roqueMov(tabuleiro, li, co, 7, "RE_B", "TO_B")
                            break

            if li == 0 and co == 0:
                cont_tb_0 += 1
            elif li == 0 and co == 7:
                cont_tb_7 += 1
            elif li == 0 and co == 3:
                cont_rb += 1

            if peca in PECAS_B:
                lista_s = movimentos(tabuleiro, co, li, peca)
                if li > INDICE7 or co > INDICE7 or li < INDICE0 or co < INDICE0:
                    print((colored("ESSA CASA NÃO ESTA CONTIDA NO TABULEIRO", "red")))
                elif lista_s:
                    s = "ESSAS SÃO SUAS OPÇÕES DE MOVIMENTO\n{}".format(lista_s)
                    print((colored(s, "blue", attrs=['bold'])))
                    print()
                    while True:
                        mov = input("PARA QUAL DESSAS CASAS VOCÊ DESEJA MOVER A PEÇA? ").upper()
                        li_m, co_m = map(int, mov.split(","))
                        l_m = tabuleiro[li_m][co_m]
                        if l_m == "RE_B":
                            print()
                            print("REI PRETO CAPTURADO! O(A) JOGADOR(A) {} É O(A) VENCEDOR(A)!".format(
                                nome_jogador_b))
                            exit(0)
                        elif l_m in PECAS_P:
                            if l_m == "TO_P":
                                lista_pec_p.remove(l_m)
                            elif l_m == "CA_P":
                                lista_pec_p.remove(l_m)
                            elif l_m == "BI_P":
                                lista_pec_p.remove(l_m)
                            elif l_m == "PE_P":
                                lista_pec_p.remove(l_m)
                            elif l_m == "RA_P":
                                lista_pec_p.remove(l_m)
                            tabuleiro = moverPecas(tabuleiro, peca, li_m, co_m, li, co)
                            break
                        elif l_m in lista_s:
                            if peca == "PE_B" and li_m == INDICE7:
                                print(colored(
                                    "SEU PEÃO FOI PROMOVIDO, ESCOLHA A PEÇA NA QUAL ELE SERÁ TRANSFORMADO: ",
                                    "green"))
                                print(colored("TO_B, BI_B, CA_B, RA_B", "green"))
                                peca_pro = input().upper()
                                tabuleiro = moverPecas(tabuleiro, peca_pro, li_m, co_m, li, co)
                            else:
                                tabuleiro = moverPecas(tabuleiro, peca, li_m, co_m, li, co)
                            break
                        else:
                            print(colored("A CASA SELECIONADA NÃO PODE SER ESCOLHIDA", "red"))
                    break
                elif lista_s == []:
                    print(colored("ESSA PEÇA NÃO PODE SE MOVER, SELECIONE OUTRA.", "red"))
                    print()
                else:
                    print(colored("ESSA PEÇA NÃO FOI ENCONTRADA", "red"))
            elif peca in PECAS_P:
                print(colored("ESSA PEÇA É DO SEU ADVERSÁRIO. ESCOLHA UMA ALIADA.", "red"))
            else:
                print(colored("NÃO HÁ NENHUMA PEÇA NESSA CASA. SELECIONA OUTRA.", "red"))
    else:
        print("VEZ DO(A) JOGADOR(A) {}\n".format(nome_jogador_p))
        while True:
            if cont != 0 and cont != 1:
                cheque = indentificaCheque(tabuleiro, li_m, co_m, peca, "RE_P")
                if cheque:
                    print()
                    print(colored("SEU REI ESTÁ EM CHEQUE. CUIDADO, MOVA-O OU PERDERÁ O JOGO!", "red", attrs=['bold']))
                    print()
            ent = input("EM QUE CASA ESTÁ LOCALIZADA A PEÇA QUE VOCÊ DESEJA MOVER? ").upper()
            if ent == "DESISTIR":
                m = "O JOGADOR {} DESISTIU, SENDO ASSIM, O JOGADOR {} VENCEU".format(nome_jogador_p, nome_jogador_b)
                print(colored(m, "green", attrs=['bold']))
                exit(0)
            li, co = map(int, ent.split(","))
            peca = tabuleiro[li][co]
            if peca == "TO_P" or peca == "RE_P" and cont_rp == 0:
                if peca == "TO_P":
                    if co == 0:
                        if cont_tp_0 == 0 and tabuleiro[0][3] == "RE_P":
                            vazio = roqueCasV(tabuleiro, 0, 3, co)
                            if vazio:
                                faz_ro = input("VOCÊ GOSTARIA DE FAZER O ROQUE? ").upper()
                                if faz_ro == "SIM":
                                    tabuleiro = roqueMov(tabuleiro, li, co, 0, "RE_P", "TO_P")
                                    break
                    elif co == 7:
                        if cont_tp_7 == 0 and tabuleiro[0][3] == "RE_P":
                            vazio = roqueCasV(tabuleiro, 0, 3, co)
                            if vazio:
                                faz_ro = input("VOCÊ GOSTARIA DE FAZER O ROQUE? ").upper()
                                if faz_ro == "SIM":
                                    tabuleiro = roqueMov(tabuleiro, li, co, 7, "RE_P", "TO_P")
                                    break
                elif peca == "RE_P" and li == 0 and co == 3:
                    to_e = False
                    to_d = False
                    if tabuleiro[0][0] == "TO_P":
                        if cont_tp_0 == 0:
                            vazio = roqueCasV(tabuleiro, li, co, 0)
                            if vazio:
                                to_e = True
                    elif tabuleiro[0][7] == "TO_P":
                        if cont_tp_7 == 0:
                            vazio = roqueCasV(tabuleiro, li, co, 0)
                            if vazio:
                                to_d = True
                    if to_e == True and to_d == True:
                        faz_ro = input("VOCÊ GOSTARIA DE FAZER O ROQUE? ").upper()
                        if faz_ro == "SIM":
                            esc_to = input("ESCOLHA UMA TORRE:\nTO_E    TO_D").upper()
                            if esc_to == "TO_E":
                                tabuleiro = roqueMov(tabuleiro, li, co, 0, "RE_P", "TO_P")
                                break
                            elif esc_to == "TO_D":
                                tabuleiro = roqueMov(tabuleiro, li, co, 7, "RE_P", "TO_P")
                                break
                    elif to_e:
                        faz_ro = input("VOCÊ GOSTARIA DE FAZER O ROQUE? ").upper()
                        if faz_ro == "SIM":
                            tabuleiro = roqueMov(tabuleiro, li, co, 0, "RE_P", "TO_P")
                            break
                    elif to_d:
                        faz_ro = input("VOCÊ GOSTARIA DE FAZER O ROQUE? ").upper()
                        if faz_ro == "SIM":
                            tabuleiro = roqueMov(tabuleiro, li, co, 7, "RE_P", "TO_P")
                            break

            if li == 0 and co == 0:
                cont_tb_0 += 1
            elif li == 0 and co == 7:
                cont_tb_7 += 1
            elif li == 0 and co == 3:
                cont_rb += 1

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
                        if l_m == "RE_B":
                            print()
                            s = "REI BRANCO CAPTURADO! O(A) JOGADOR(A) {} É O(A) VENCEDOR(A)!".format(
                                nome_jogador_p)
                            print(colored(s, "blue", attrs=['bold']))
                            exit(0)
                        elif l_m in PECAS_B:
                            if l_m == "TO_B":
                                lista_pec_p.remove(l_m)
                            elif l_m == "CA_B":
                                lista_pec_p.remove(l_m)
                            elif l_m == "BI_B":
                                lista_pec_p.remove(l_m)
                            elif l_m == "PE_B":
                                lista_pec_p.remove(l_m)
                            elif l_m == "RA_B":
                                lista_pec_p.remove(l_m)
                            tabuleiro = moverPecas(tabuleiro, peca, li_m, co_m, li, co)
                            break
                        if l_m in lista_s:
                            if peca == "PE_P" and li_m == INDICE0:
                                print(colored(
                                    "SEU PEÃO FOI PROMOVIDO, ESCOLHA A PEÇA NA QUAL ELE SERÁ TRANSFORMADO: ",
                                    "green"))
                                print(colored("TO_B, BI_B, CA_B, RA_B", "green"))
                                peca_pro = input().upper()
                                tabuleiro = moverPecas(tabuleiro, peca_pro, li_m, co_m, li, co)
                            else:
                                tabuleiro = moverPecas(tabuleiro, peca, li_m, co_m, li, co)
                            break
                        else:
                            print(colored("A CASA SELECIONADA NÃO PODE SER ESCOLHIDA", "red"))
                    break
                elif lista_s == []:
                    print(colored("ESSA PEÇA NÃO PODE SE MOVER, SELECIONE OUTRA.", "red"))
                    print()
                else:
                    print(colored("ESSA PEÇA NÃO FOI ENCONTRADA", "red"))
            elif peca in PECAS_B:
                print(colored("ESSA PEÇA É DO SEU ADVERSÁRIO. ESCOLHA UMA ALIADA.", "red"))
            else:
                print(colored("NÃO HÁ NENHUMA PEÇA NESSA CASA. SELECIONA OUTRA.", "red"))
    # Casos de empate
    if lista_pec_p == ["RE_P"] and lista_pec_b == ["RE_B"]:
        print("O JOGO TERMINOU EMPATADO!")
        exit(0)
    elif lista_pec_p == ["RE_P"] and lista_pec_b == ["CA_B", "RE_B"] or lista_pec_p == ["RE_P",
                                                                                        "CA_P"] and lista_pec_b == [
        "RE_B"]:
        print("O JOGO TERMINOU EMPATADO!")
        exit(0)
    elif lista_pec_p == ["RE_P"] and lista_pec_b == ["BI_B", "RE_B"] or lista_pec_p == ["RE_P",
                                                                                        "BI_P"] and lista_pec_b == [
        "RE_B"]:
        print("O JOGO TERMINOU EMPATADO!")
        exit(0)
    elif lista_pec_p == ["RE_P"] and lista_pec_b == ["CA_B", "CA_B", "RE_B"] or lista_pec_p == ["RE_P", "CA_P",
                                                                                                "CA_P"] and lista_pec_b == [
        "RE_B"]:
        print("O JOGO TERMINOU EMPATADO!")
        exit(0)
    elif lista_pec_p == ["RE_P"] and lista_pec_b == ["TO_B", "RE_B"] or lista_pec_p == ["TO_P",
                                                                                        "BI_P"] and lista_pec_b == [
        "RE_B"]:
        print("O JOGO TERMINOU EMPATADO!")
        exit(0)
    cont += 1  # Adiciona '+ 1' ao contador da quantidade de jogadas
