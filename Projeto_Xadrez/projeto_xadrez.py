from projeto_xadrez_funcoes import *
from CONS import *
from termcolor import colored

tabuleiro = posiciona_pecas()
nome_jogador_b = input("NOME DO JOGADOR DAS PEÇAS BRANCAS: ").upper()
nome_jogador_p = input("NOME DO JOGADOR DAS PEÇAS PRETAS: ").upper()

lista_pec_b = lista_pec_b
lista_pec_p = lista_pec_p
lista_mov_b = lista_mov_b
lista_mov_p = lista_mov_p
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
pos_re_b = "1d"
pos_re_p = "8e"
while True:
    # Imprime o tabuleiro
    cont_t = 1
    print()
    print(colored(L_1_TAB, "yellow", attrs=['bold']))
    for a in tabuleiro:
        print(colored("{} |".format(cont_t), "yellow", attrs=['bold']), end=" ")
        indice = INDICE0
        for b in a:
            if indice != QTD_C - PONTO_P:
                indice += PONTO_P
                if b in PECAS_B:
                    if b != "RE_B" and b != "RA_B":
                        b = b[0]
                        s = (colored(b, attrs=['bold']))
                        print("{} |".format(s), end=" ")
                    elif b == "RE_B":
                        b = "K"
                        s = (colored(b, attrs=['bold']))
                        print("{} |".format(s), end=" ")
                    elif b == "RA_B":
                        b = "Q"
                        s = (colored(b, attrs=['bold']))
                        print("{} |".format(s), end=" ")
                elif b in PECAS_P:
                    if b != "RE_P" and b != "RA_P":
                        b = b[0]
                        s = (colored(b, "grey", attrs=['bold']))
                        print("{} |".format(s), end=" ")
                    elif b == "RE_P":
                        b = "K"
                        s = (colored(b, "grey", attrs=['bold']))
                        print("{} |".format(s), end=" ")
                    elif b == "RA_P":
                        b = "Q"
                        s = (colored(b, "grey", attrs=['bold']))
                        print("{} |".format(s), end=" ")
                else:
                    s = (colored(b, "white"))
                    print("{} |".format(s), end=" ")
            else:
                if b in PECAS_B:
                    if b != "RE_B" and b != "RA_B":
                        b = b[0]
                        s = (colored(b, attrs=['bold']))
                        print("{}".format(s))
                    elif b == "RE_B":
                        b = "K"
                        s = (colored(b, attrs=['bold']))
                        print("{}".format(s))
                    elif b == "RA_B":
                        b = "Q"
                        s = (colored(b, attrs=['bold']))
                        print("{}".format(s))
                elif b in PECAS_P:
                    if b != "RE_P" and b != "RA_P":
                        b = b[0]
                        s = (colored(b, "grey", attrs=['bold']))
                        print("{}".format(s))
                    elif b == "RE_P":
                        b = "K"
                        s = (colored(b, "grey", attrs=['bold']))
                        print("{}".format(s))
                    elif b == "RA_P":
                        b = "Q"
                        s = (colored(b, "grey", attrs=['bold']))
                        print("{}".format(s))
                else:
                    s = (colored(b, "white"))
                    print(s)
        cont_t += 1
    print()
    # Abaixo desse ponto, encontram-se as condicionais que irão definir quem é o jogador da vez
    if cont % DIVISOR == INDICE0:  # Jogadas pares, indica que é a vez do jogador das peças brancas
        print("VEZ DO(A) JOGADOR(A) {}\n".format(nome_jogador_b))
        # Os laços while a seguir servem para caso a peça selecionada não seja possível ser movida, o jogador deverá
        # selecionar outra peça
        while True:
            if cont > 1:
                cheque = indentificaCheque(tabuleiro, pos_re_b, "RE_B", lista_pec_b, lista_mov_b, lista_pec_p,
                                           lista_mov_p)
                if cheque == "XEQUE":
                    print()
                    print(colored("SEU REI ESTÁ EM XEQUE. CUIDADO!", "red", attrs=['bold']))
                    print()
                    while True:
                        li, co = input("QUE PEÇA VOCÊ DESEJA MOVER? ").split()
                        li = int(li) - 1
                        co = tradLet(int(co))
                        peca = tabuleiro[li][co]
                        if peca in PECAS_B:
                            lista_m = movimentos(tabuleiro, co, li, peca)
                            print(lista_m)
                            mov = input("PARA QUAL CASA VOCÊ DESEJA MOVER? ")
                            li_m = int(li) - 1
                            co_m = tradLet(int(co))
                            if mov in lista_m:
                                if peca == "RE_B":
                                    pos_t_r = pos_re_b
                                    cheque = indentificaCheque(tabuleiro, pos_re_b, "RE_B", lista_pec_b, lista_mov_b,
                                                               lista_pec_p, lista_mov_p)
                                    if cheque == "XEQUE":
                                        pass
                                    elif cheque == "MATE":
                                        print(colored("XEQUE MATE, SEU ADVERSÁRIO VENCEU O JOGO!", "yellow"))
                                        exit(0)
                                    else:
                                        pos_re_b = mov
                                        tabuleiro = moverPecas(tabuleiro, peca, li_m, co_m, li, co)
                                        break
                                else:
                                    cheque = indentificaCheque(tabuleiro, pos_re_b, "RE_B", lista_pec_b, lista_mov_b,
                                                               lista_pec_p, lista_mov_p)
                                    if cheque == "XEQUE":
                                        pass
                                    elif cheque == "MATE":
                                        print(colored("XEQUE MATE, SEU ADVERSÁRIO VENCEU O JOGO!", "yellow"))
                                        exit(0)
                                    else:
                                        pos_re_b = mov
                                        tabuleiro = moverPecas(tabuleiro, peca, li_m, co_m, li, co)
                                        break
                            else:
                                print(colored("JOGADA INVÁLIDA"), "red")
                    break
                elif cheque == "MATE":
                    print(colored("XEQUE MATE, SEU ADVERSÁRIO VENCEU O JOGO!", "yellow"))
                    exit(0)
            ent = input("EM QUE CASA ESTÁ LOCALIZADA A PEÇA QUE VOCÊ DESEJA MOVER? ").upper()
            if ent == "DESISTIR":
                m = "O JOGADOR {} DESISTIU, SENDO ASSIM, O JOGADOR {} VENCEU".format(nome_jogador_p, nome_jogador_b)
                print()
                print(colored(m, "green", attrs=['bold']))
                exit(0)
            li = int(ent[0]) - INDICE1
            co = tradLet(ent[1].lower())
            peca = tabuleiro[li][co]
            if peca == "RE_B" and cont_rb == 0:
                if peca == "RE_B" and li == 0 and co == 3:
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
                    if to_e is True and to_d is True:
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
                        mov = input("PARA QUAL DESSAS CASAS VOCÊ DESEJA MOVER A PEÇA? ").lower()
                        lista_mov_b = posPecas(lista_mov_b, ent.lower(), mov)
                        li_m = int(mov[0]) - 1
                        co_m = tradLet(mov[1])
                        l_m = tabuleiro[li_m][co_m]
                        if peca == "RE_B":
                            pos_re_b = mov
                        if l_m == "RE_P":
                            print()
                            print("REI PRETO CAPTURADO! O(A) JOGADOR(A) {} É O(A) VENCEDOR(A)!".format(
                                nome_jogador_b))
                            exit(0)
                        elif l_m in PECAS_P:
                            lista_pec_p, lista_mov_p = removPecas(lista_pec_p, lista_mov_p, mov, l_m, "P")
                            if peca == "PE_B" and li_m == INDICE7:
                                print(colored(
                                    "SEU PEÃO FOI PROMOVIDO, ESCOLHA A PEÇA NA QUAL ELE SERÁ TRANSFORMADO: ",
                                    "green"))
                                print(colored("T, B, C, Q", "green"))
                                peca_pro = input().upper()
                                peca_pro, lista_pec_p = promoPeao(lista_pec_b, lista_mov_b, mov, peca_pro, "B")
                                tabuleiro = moverPecas(tabuleiro, peca_pro, li_m, co_m, li, co)
                            else:
                                tabuleiro = moverPecas(tabuleiro, peca, li_m, co_m, li, co)
                            break
                        elif mov in lista_s:
                            if peca == "PE_B" and li_m == INDICE7:
                                print(colored(
                                    "SEU PEÃO FOI PROMOVIDO, ESCOLHA A PEÇA NA QUAL ELE SERÁ TRANSFORMADO: ",
                                    "green"))
                                print(colored("T, B, C, Q", "green"))
                                peca_pro = input().upper()
                                peca_pro, lista_pec_p = promoPeao(lista_pec_b, lista_mov_b, mov, peca_pro, "B")
                                tabuleiro = moverPecas(tabuleiro, peca_pro, li_m, co_m, li, co)
                            else:
                                tabuleiro = moverPecas(tabuleiro, peca, li_m, co_m, li, co)
                            break
                        else:
                            print(colored("A CASA SELECIONADA NÃO PODE SER ESCOLHIDA", "red"))
                    break
                elif lista_s is []:
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
            if cont > 1:
                cheque = indentificaCheque(tabuleiro, pos_re_p, "RE_P", lista_pec_p, lista_mov_p, lista_pec_b,
                                           lista_mov_b)
                if cheque == "XEQUE":
                    print()
                    print(colored("SEU REI ESTÁ EM XEQUE. CUIDADO!", "red", attrs=['bold']))
                    print()
                    while True:
                        li, co = input("QUE PEÇA VOCÊ DESEJA MOVER? ").split()
                        li = int(li) - 1
                        co = tradLet(int(co))
                        peca = tabuleiro[li][co]
                        if peca in PECAS_P:
                            lista_m = movimentos(tabuleiro, co, li, peca)
                            print(lista_m)
                            mov = input("PARA QUAL CASA VOCÊ DESEJA MOVER? ")
                            li_m = int(li) - 1
                            co_m = tradLet(int(co))
                            if mov in lista_m:
                                if peca == "RE_B":
                                    pos_t_r = pos_re_p
                                    cheque = indentificaCheque(tabuleiro, pos_re_p, "RE_P", lista_pec_p, lista_mov_p,
                                                               lista_pec_b, lista_mov_b)
                                    if cheque == "XEQUE":
                                        pass
                                    elif cheque == "MATE":
                                        print(colored("XEQUE MATE, SEU ADVERSÁRIO VENCEU O JOGO!", "yellow"))
                                        exit(0)
                                    else:
                                        pos_re_p = mov
                                        tabuleiro = moverPecas(tabuleiro, peca, li_m, co_m, li, co)
                                        break
                                else:
                                    cheque = indentificaCheque(tabuleiro, pos_re_p, "RE_P", lista_pec_p, lista_mov_p,
                                                               lista_pec_b, lista_mov_b)
                                    if cheque == "XEQUE":
                                        pass
                                    elif cheque == "MATE":
                                        print(colored("XEQUE MATE, SEU ADVERSÁRIO VENCEU O JOGO!", "yellow"))
                                        exit(0)
                                    else:
                                        pos_re_p = mov
                                        tabuleiro = moverPecas(tabuleiro, peca, li_m, co_m, li, co)
                                        break
                            else:
                                print(colored("JOGADA INVÁLIDA"), "red")
                    break
                elif cheque == "MATE":
                    print(colored("XEQUE MATE, SEU ADVERSÁRIO VENCEU O JOGO!", "yellow"))
                    exit(0)
            ent = input("EM QUE CASA ESTÁ LOCALIZADA A PEÇA QUE VOCÊ DESEJA MOVER? ").upper()
            if ent == "DESISTIR":
                m = "O JOGADOR {} DESISTIU, SENDO ASSIM, O JOGADOR {} VENCEU".format(nome_jogador_p, nome_jogador_b)
                print(colored(m, "green", attrs=['bold']))
                exit(0)
            li = int(ent[0]) - 1
            co = tradLet(ent[1].lower())
            peca = tabuleiro[li][co]
            if peca == "RE_P" and cont_rp == 0:
                if peca == "RE_P" and li == 7 and co == 4:
                    to_e = False
                    to_d = False
                    if tabuleiro[7][0] == "TO_P":
                        if cont_tp_0 == 0:
                            vazio = roqueCasV(tabuleiro, li, co, 0)
                            if vazio:
                                to_e = True
                    elif tabuleiro[7][7] == "TO_P":
                        if cont_tp_7 == 0:
                            vazio = roqueCasV(tabuleiro, li, co, 7)
                            if vazio:
                                to_d = True
                    if to_e is True and to_d is True:
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
                        mov = input("PARA QUAL DESSAS CASAS VOCÊ DESEJA MOVER A PEÇA? ").lower()
                        lista_mov_p = posPecas(lista_mov_p, ent.lower(), mov)
                        li_m = int(mov[0]) - 1
                        co_m = tradLet(mov[1])
                        l_m = tabuleiro[li_m][co_m]
                        if l_m == "RE_B":
                            print()
                            s = "REI BRANCO CAPTURADO! O(A) JOGADOR(A) {} É O(A) VENCEDOR(A)!".format(
                                nome_jogador_p)
                            print(colored(s, "blue", attrs=['bold']))
                            exit(0)
                        elif l_m in PECAS_B:
                            lista_pec_b, lista_mov_b = removPecas(lista_pec_b, lista_mov_b, mov, l_m, "B")
                            tabuleiro = moverPecas(tabuleiro, peca, li_m, co_m, li, co)
                            break
                        elif mov in lista_s:
                            if peca == "PE_P" and li_m == INDICE0:
                                print(colored(
                                    "SEU PEÃO FOI PROMOVIDO, ESCOLHA A PEÇA NA QUAL ELE SERÁ TRANSFORMADO: ",
                                    "green"))
                                print(colored("T, B, C, Q", "green"))
                                peca_pro = input().upper()
                                peca_pro, lista_pec_p = promoPeao(lista_pec_p, lista_mov_p, mov, peca_pro, "P")
                                tabuleiro = moverPecas(tabuleiro, peca_pro, li_m, co_m, li, co)
                            else:
                                tabuleiro = moverPecas(tabuleiro, peca, li_m, co_m, li, co)
                            break
                        else:
                            print(colored("A CASA SELECIONADA NÃO PODE SER ESCOLHIDA", "red"))
                    break
                elif lista_s is []:
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
