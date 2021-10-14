import copy
from projeto_xadrez_funcoes import *
from CONS import *
from termcolor import colored

print("|SEJA MUITO BEM-VINDO AO NOSSO PYDREZ|".center(INDICE120, "_"))
print("(uma piadinha com python + xadrez)".center(INDICE120, " "))
print()
print("MAS E ENTÃO, VOCÊ JÁ SABE JOGAR XADREZ?".center(INDICE120, " "))
print("CASO AINDA NÃO SAIBA, VAMOS PASSAR AS REGRAS".center(INDICE120, " "))
print("E CASO JÁ SAIBA, VAMOS APENAS PASSAR O MODO DE JOGAR".center(INDICE120, " "))
print()
while True:
    decisao = input("E ENTÃO... VOCÊ JÁ SABE JOGAR? ".rjust(INDICE75, " ")).upper()
    print()

    if decisao == "SIM":
        print("ÓTIMO!! ENTÃO VAMOS DIRETO PARA O PASSO A PASSO DE COMO JOGAR".center(INDICE120, " "))
        print("PODE FICAR TRANQUILO(A) QUE O JOGO É BEM INTUÍTIVO".center(INDICE120, " "))
        print("PARA COMEÇAR, O NOSSO TABULEIRO É DIVIDIDO ENTRE LINHAS, QUE VÃO DE 1 À 8, E COLUNAS, DE 'A' À 'H'".center(INDICE120, " "))
        print("PARA MOVIMENTAR AS PEÇAS, VOCÊ VAI PRECISAR ESCOLHER A CASA AONDE A PEÇA ESTÁ LOCALIZADA".center(INDICE120, " "))
        print("SEMPRE ESCOLHENDO PRIMEIRO A LINHA, E DEPOIS A COLUNA".center(INDICE120, " "))
        print("E NÃO ESQUEÇA COLOCAR NA ORDEM CORRETA, POR EXEMPLO: 1d".center(INDICE120, " "))
        print("APÓS ESCOLHER A PEÇA QUE DESEJA MOVER, NOSSO PROGRAMA IRÁ TE PASSAR AS POSSÍVEIS CASAS PARA QUAL A SUA PEÇA PODE SE MOVER".center(INDICE120, " "))
        print("DAÍ, É SÓ SELECIONAR PARA QUAL DAS CASAS POSSÍVEIS VOCÊ DESEJA MOVER A SUA PEÇA".center(INDICE120, " "))
        print("CASO NÃO SEJA POSSÍVEL MOVER A PEÇA QUE VOCÊ SELECIONOU, VAMOS PEDIR PARA QUE SELECIONE OUTRA".center(INDICE120, " "))
        print("CASO QUEIRA FAZER O ROQUE, BASTA SELECIONAR O SEU REI, E SE FOR POSSÍVEL FAZER O ROQUE, VAMOS TE PERGUNTAR SE GOSTARIA DE FAZER".center(INDICE120, " "))
        print("E BASTA RESPONDER COM UM 'SIM', CASO QUEIRA, OU QUALQUER OUTRA COISA, CASO NÃO QUEIRA".center(INDICE120, " "))
        print("OUTRA COISINHA... CASO QUEIRA DESISTIR DO JOGO, BASTA DIGITAR 'DESISTIR' NO MOMENTO DE SELCIONAR A PEÇA".center(INDICE120, " "))
        print("PRONTO... É BASICAMENTE ISSO, COMO JÁ DISSEMOS ANTES, O JOGO É BEM INTUÍTIVO, ENTÃO NÃO PRECISA SE PREOCUPAR".center(INDICE120, " "))
        break

    if decisao == "NÃO" or decisao == "NAO":
        print("ENTÃO NESSE CASO, VAMO APRENDER ALGUMAS REGRAS DO XADREZ E COMO O JOGO FUNCIONA".center(INDICE120, " "))
        print("PARA COMEÇAR, O XADREZ É COMPOSTO POR 32 PEÇAS, SENDO 16 PARA CADA JOGADOR".center(INDICE120, " "))
        print("DESSAS 16 PEÇAS, TEMOS 8 PEÕES, 2 TORRES, 2 CAVALOS, 2 BISPOS, 1 REI E 1 RAINHA".center(INDICE120, " "))
        print("CADA PEÇA TEM UM TIPO DE MOVIMENTO ÚNICO... E É SOBRE ISSO QUE VAMOS APRENDER AGORA".center(INDICE120, " "))
        print("COMEÇANDO PELOS PEÕES... CASO SEJA A PRIMEIRA VEZ QUE UM PEÃO VÁ SE MOVER, ELE PODE IR ATÉ DUAS CASAS PARA FRENTE".center(INDICE120, " "))
        print("CASO CONTRÁRIO, ELE SÓ PODERÁ SE MOVER UMA CASA PARA FRENTE".center(INDICE120, " "))
        print("E EM CASOS DE CAPTURA, O PEÃO SÓ PODERÁ CAPTURAR PEÇAS QUE ESTEJAM NAS DIAGONÁIS À SUA FRENTE".center(INDICE120, " "))
        print("OUTRA COISA INTERESSANTE SOBRE OS PEÕES É QUE, CASO ELES CONSIGAM ATRAVESSAR TODO O TABULEIRO,".center(INDICE120, " "))
        print("ELES PODEM SER PROMOVIDOS À QUALQUER OUTRA PEÇA QUE NÃO SEJA O REI".center(INDICE120, " "))
        print("AGORA INDO PARA A TORRE... É MUITO SIMPLES, ELA PODE SE MOVER QUANTAS CASAS QUISER, MAS SOMENTE NA VERTICAL E NA HORIZONTAL".center(INDICE120, " "))
        print("O BISPO SEGUE ESSE MESMO RACIOCÍNIO, PODENDO SE MOVER QUANTAS CASAS QUISER, MAS SOMENTE PARA AS DIAGONÁIS".center(INDICE120, " "))
        print("APROVEITANDO ESSAS DUAS ÓTIMAS INFORMAÇÕES, VAMOS LOGO APRENDER COMO FUNCIONA O MOVIMENTO DA RAINHA.".center(INDICE120, " "))
        print("A MOVIMENTAÇÃO DA RAINHA É UM CONJUNTO DAS MOVIMENTAÇÕES DA TORRE E DO BISPO... SENDO ASSIM,".center(INDICE120, " "))
        print("ELA PODE SE MOVER QUANTAS CASAS QUISER, MAS TANTO NAS DIAGONAIS, QUANTO NA HORIZONTAL E NA VERTICAL".center(INDICE120, " "))
        print('AGORA É A VEZ DE APRENDER COMO FUNCIONA A MOVIMENTAÇÃO DO CAVALO!'.center(INDICE120, " "))
        print("O CAVALO PODE SE MOVER DE UMA MANEIRA BEM DIFERENTE DAS OUTRAS PEÇAS, PODENDO 'ANDAR' SOMENTE EM FORMATO DE 'L'".center(INDICE120, " "))
        print("SENDO ASSIM, ELE TEM AS OPÇÕES DE SE MOVER EM DUAS CASAS NA HORIZONTAL (ESQUERDA OU DIREITA) E UMA NA VERTICAL (CIMA OU BAIX0)".center(INDICE120, " "))
        print("OU ENTÃO, DUAS CASAS NA VERTICAL E UMA CASA NA HORIZONTAL".center(INDICE120, " "))
        print("OUTRO FATO INTERESSANTE SOBRE O CAVALO, É QUE ELE É A ÚNICA PEÇA QUE PODE PASSAR POR CIMA DAS OUTRAS".center(INDICE120, " "))
        print("SE TORNANDO ASSIM, UMA PEÇA BEM LEGAL PARA BOLAR ALGUMAS ESTRATÉGIAS".center(INDICE120, " "))
        print("E POR ÚLTIMO, MAS NÃO MENOS IMPORTANTE, TEMOS O REI, QUE TEM O MOVIMENTO MAIS SIMPLES DE TODOS.".center(INDICE120, " "))
        print("APESAR DE PODER SE MOVER PARA TODAS AS DIREÇÕES, ASSIM COMO A RAINHA, ELE SÓ PODE ANDAR UMA CASA".center(INDICE120, " "))
        print("MAS NÃO É SÓ ISSO, TAMBÉM É POSSÍVEL FAZER UMA JOGADA CHAMADA 'ROQUE' COM O REI!".center(INDICE120, " "))
        print("ESSA JOGADA CONSISTE EM MOVER O REI DUAS CASAS PARA A ESQUERDA, OU PARA A DIREITA, E APÓS ISSO,".center(INDICE120, " "))
        print("PASSA A TORRE MAIS PRÓXIMA PRO LADO CONTRÁRIO DO REI".center(INDICE120, " "))
        print("MAS CUIDADO!! NEM O REI E NEM A TORRE COM A QUAL VOCÊ DESEJA FAZER O ROQUE PODEM TER SE MOVIDO ANTES".center(INDICE120, " "))
        print("E PARA FINALIZAR ESSE BREVE RESUMO... O OBJETIVO DO JOGO É NADA MAIS, NADA MENOS, DO QUE CAPTURAR O REI ADVERSÁRIO".center(INDICE120, " "))
        print()
        print("AGORA QUE VOCÊ JÁ SABE JOGAR, VAMOS PASSAR O PASSO A PASSO DE COMO JOGAR O NOSSO PYDREZ!".center(INDICE120, " "))

        print()

        print("PODE FICAR TRANQUILO(A) QUE O JOGO É BEM INTUÍTIVO".center(INDICE120, " "))
        print("PARA COMEÇAR, O NOSSO TABULEIRO É DIVIDIDO ENTRE LINHAS, QUE VÃO DE 1 À 8, E COLUNAS, DE 'A' À 'H'".center(INDICE120, " "))
        print("PARA MOVIMENTAR AS PEÇAS, VOCÊ VAI PRECISAR ESCOLHER A CASA AONDE A PEÇA ESTÁ LOCALIZADA".center(INDICE120, " "))
        print("SEMPRE ESCOLHENDO PRIMEIRO A LINHA, E DEPOIS A COLUNA".center(INDICE120, " "))
        print("E NÃO ESQUEÇA COLOCAR NA ORDEM CORRETA, POR EXEPLO: 1d".center(INDICE120, " "))
        print("APÓS ESCOLHER A PEÇA QUE DESEJA MOVER, NOSSO PROGRAMA IRÁ TE PASSAR AS POSSÍVEIS CASAS PARA QUAL A SUA PEÇA PODE SE MOVER".center(INDICE120, " "))
        print("DAÍ, É SÓ SELECIONAR PARA QUAL DAS CASAS POSSÍVEIS VOCÊ DESEJA MOVER A SUA PEÇA".center(INDICE120, " "))
        print("CASO NÃO SEJA POSSÍVEL MOVER A PEÇA QUE VOCÊ SELECIONOU, VAMOS PEDIR PARA QUE SELECIONE OUTRA".center(INDICE120, " "))
        print("CASO QUEIRA FAZER O ROQUE, BASTA SELECIONAR O SEU REI, E SE FOR POSSÍVEL FAZER O ROQUE, VAMOS TE PERGUNTAR SE TEM CERTEZA DISSO".center(INDICE120, " "))
        print("E BASTA RESPONDER COM UM 'SIM', CASO QUEIRA, OU QUALQUER OUTRA COISA, CASO NÃO QUEIRA".center(INDICE120, " "))
        print("OUTRA COISINHA... CASO QUEIRA DESISTIR DO JOGO, BASTA DIGITAR 'DESISTIR' QUANDO FOR A SUA VEZ DE JOGAR".center(INDICE120, " "))
        print("PRONTO... É BASICAMENTE ISSO, COMO JÁ DISSEMOS ANTES, O JOGO É BEM INTUÍTIVO, ENTÃO NÃO PRECISA SE PREOCUPAR".center(INDICE120, " "))
        break
    else:
        print("ESSA NÃO É UMA OPÇÃO VÁLIDA... TENTE OUTRA COISA, POR FAVOR!")

tabuleiro = posiciona_pecas()
nome_jogador_b = input("NOME DO JOGADOR DAS PEÇAS BRANCAS: ").upper()
nome_jogador_p = input("NOME DO JOGADOR DAS PEÇAS PRETAS: ").upper()

lista_pec_b = lista_pec_b
lista_pec_p = lista_pec_p
lista_mov_b = lista_mov_b
lista_mov_p = lista_mov_p
peca = ""
li_m = INDICE0
co_m = INDICE0
cont = INDICE0
cont_tb_7 = INDICE0
cont_tb_0 = INDICE0
cont_tp_7 = INDICE0
cont_tp_0 = INDICE0
cont_rb = INDICE0
cont_rp = INDICE0
pos_re_b = "1d"
pos_re_p = "8e"

while True:
    # Imprime o tabuleiro
    cont_t = INDICE1
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
                        b = b[INDICE0]
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
                        b = b[INDICE0]
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
                        b = b[INDICE0]
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
                        b = b[INDICE0]
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
        cont_t += INDICE1
    print()
    # Abaixo desse ponto, encontram-se as condicionais que irão definir quem é o jogador da vez
    if cont % DIVISOR == INDICE0:  # Jogadas pares, indica que é a vez do jogador das peças brancas
        print("VEZ DO(A) JOGADOR(A) {}\n".format(nome_jogador_b))
        # Os laços while a seguir servem para caso a peça selecionada não seja possível ser movida, o jogador deverá
        # selecionar outra peça
        li = INDICE0
        co = INDICE0
        peca = ""
        ent = ""
        mov = ""
        while True:
            if cont > INDICE1:
                # Verifica, a cada início de jogada, se o rei está em xeque
                cheque = indentificaCheque(tabuleiro, pos_re_b, "RE_B", lista_pec_b, lista_mov_b, lista_pec_p, lista_mov_p)
                if cheque == "XEQUE":
                    print(colored("SEU REI ESTÁ EM XEQUE. CUIDADO!", "red", attrs=['bold']))
                    print()
                    while True:
                        try:
                            ent = input("EM QUE CASA ESTÁ LOCALIZADA A PEÇA QUE VOCÊ DESEJA MOVER? ").upper()
                            if ent == "DESISTIR":
                                m = "O JOGADOR {} DESISTIU, SENDO ASSIM, O JOGADOR {} VENCEU".format(nome_jogador_p,
                                                                                                     nome_jogador_b)
                                print()
                                print(colored(m, "green", attrs=['bold']))
                                exit(INDICE0)
                            li = int(ent[INDICE0]) - INDICE1
                            co = tradLet(ent[INDICE1].lower())
                            peca = tabuleiro[li][co]
                            lista_s = movimentos(tabuleiro, co, li, peca)
                            if li > INDICE7 or co > INDICE7 or li < INDICE0 or co < INDICE0:
                                print((colored("ESSA CASA NÃO ESTA CONTIDA NO TABULEIRO", "red")))
                            elif peca in PECAS_P:
                                print(colored("ESSA PEÇA É DO SEU ADVERSÁRIO. ESCOLHA UMA ALIADA.", "red"))
                            elif peca not in PECAS_B:
                                print(colored("NÃO HÁ NENHUMA PEÇA NESSA CASA. SELECIONA OUTRA.", "red"))
                            elif lista_s == []:
                                print(colored("ESSA PEÇA NÃO PODE SE MOVER, SELECIONE OUTRA.", "red"))
                            elif lista_s is True:
                                print(colored("ESSA PEÇA NÃO FOI ENCONTRADA", "red"))
                            else:
                                break
                        except (TypeError, IndexError, ValueError):
                            print(colored("JOGADA INVÁLIDA!", "red"))
                            pass
                    if peca == "RE_B":
                        # Verifica se, ao selecionar o rei, é possível fazer o roque com alguma das duas torres
                        to_e, to_d = roqueCond(tabuleiro, "RE_B", cont_rb, cont_tb_0, cont_tb_7, li, co)
                        if to_e is True and to_d is True:
                            faz_ro = input("VOCÊ GOSTARIA DE FAZER O ROQUE? ").upper()
                            if faz_ro == "SIM":
                                esc_to = input("ESCOLHA UMA TORRE:\nTO_E    TO_D").upper()
                                if esc_to == "TO_E":
                                    tabuleiro, lista_mov_b = roqueMov(tabuleiro, lista_mov_p, lista_pec_b, li, co, INDICE0, "RE_B", "TO_B")
                                    break
                                elif esc_to == "TO_D":
                                    tabuleiro, lista_mov_b = roqueMov(tabuleiro, lista_mov_p, lista_pec_b, li, co, INDICE0, "RE_B", "TO_B")
                                    break
                        elif to_e:
                            faz_ro = input("VOCÊ GOSTARIA DE FAZER O ROQUE? ").upper()
                            if faz_ro == "SIM":
                                cont_tb_0 += INDICE1
                                cont_rb += INDICE1
                                tabuleiro, lista_mov_b = roqueMov(tabuleiro, lista_mov_p, lista_pec_b, li, co, INDICE0, "RE_B", "TO_B")
                                break
                        elif to_d:
                            faz_ro = input("VOCÊ GOSTARIA DE FAZER O ROQUE? ").upper()
                            if faz_ro == "SIM":
                                cont_tb_7 += INDICE1
                                cont_rb += INDICE1
                                tabuleiro, lista_mov_b = roqueMov(tabuleiro, lista_mov_p, lista_pec_b, li, co, INDICE0, "RE_B", "TO_B")
                                break
                    lista_s = movimentos(tabuleiro, co, li, peca)
                    s = "ESSAS SÃO SUAS OPÇÕES DE MOVIMENTO\n{}".format(lista_s)
                    print((colored(s, "blue")))
                    while True:
                        try:
                            mov = input("PARA QUAL DESSAS CASAS VOCÊ DESEJA MOVER A PEÇA? ").lower()
                            li_m = int(mov[INDICE0]) - INDICE1
                            co_m = tradLet(mov[INDICE1])
                            l_m = tabuleiro[li_m][co_m]
                            if mov not in lista_s:
                                print(colored("A CASA SELECIONADA NÃO PODE SER ESCOLHIDA", "red"))
                            elif lista_s == []:
                                print(colored("ESSA PEÇA NÃO PODE SE MOVER, SELECIONE OUTRA.", "red"))
                                print()
                            elif lista_s is True:
                                print(colored("ESSA PEÇA NÃO FOI ENCONTRADA", "red"))
                            else:
                                break
                        except (TypeError, IndexError, ValueError):
                            print("JOGADA INVÁLIDA!")
                            pass
                    if peca == "RE_B":
                        # Gera uma deepcopy do tabuleiro, a qual serve para analisar as condições de xeque
                        tabuleiro_t = copy.deepcopy(tabuleiro)
                        tabuleiro_t = moverPecas(tabuleiro_t, peca, li_m, co_m, li, co)
                        pos_t_r = mov
                        cheque = indentificaCheque(tabuleiro_t, pos_t_r, "RE_B", lista_pec_b, lista_mov_b, lista_pec_p, lista_mov_p)
                        if cheque == "XEQUE":
                            print(colored("SEU REI CONTINUA EM XEQUE!", "red"))
                        elif cheque == "MATE":
                            print(colored("XEQUE MATE, SEU ADVERSÁRIO VENCEU O JOGO!", "yellow"))
                            exit(INDICE0)
                        else:
                            pos_re_b = mov  # Atualiza a posição do rei sempre que ele se move
                            tabuleiro = moverPecas(tabuleiro, peca, li_m, co_m, li, co)
                            lista_mov_b = posPecas(lista_mov_b, ent.lower(), mov)
                            if l_m in PECAS_P:
                                lista_pec_p, lista_mov_p = removPecas(lista_pec_p, lista_mov_p, mov, l_m, "P")
                            break
                    else:
                        # Gera uma deepcopy do tabuleiro, a qual serve para analisar as condições de xeque
                        tabuleiro_t = copy.deepcopy(tabuleiro)
                        tabuleiro_t = moverPecas(tabuleiro_t, peca, li_m, co_m, li, co)
                        cheque = indentificaCheque(tabuleiro_t, pos_re_b, "RE_B", lista_pec_b, lista_mov_b, lista_pec_p, lista_mov_p)
                        if cheque == "XEQUE":
                            print(colored("SEU REI CONTINUA EM XEQUE!", "red"))
                        elif cheque == "MATE":
                            print(colored("XEQUE MATE, SEU ADVERSÁRIO VENCEU O JOGO!", "yellow"))
                            exit(INDICE0)
                        else:
                            cont_rb += INDICE1
                            if peca == "PE_B" and li_m == INDICE7:
                                print(colored("SEU PEÃO FOI PROMOVIDO, ESCOLHA A PEÇA NA QUAL ELE SERÁ TRANSFORMADO: ", "green"))
                                print(colored("T, B, C, Q", "green"))
                                peca_pro = ""
                                while True:
                                    peca_pro = input().upper()
                                    if peca_pro == "T" or peca_pro == "B" or peca_pro == "C" or peca_pro == "Q":
                                        break
                                    else:
                                        print(colored("PEÇA INVÁLIDA", "red"))
                                peca_pro, lista_pec_b = promoPeao(lista_pec_b, lista_mov_b, mov, peca_pro, "B")
                            tabuleiro = moverPecas(tabuleiro, peca, li_m, co_m, li, co)
                            lista_mov_b = posPecas(lista_mov_b, ent.lower(), mov)
                            if l_m in PECAS_P:
                                lista_pec_p, lista_mov_p = removPecas(lista_pec_p, lista_mov_p, mov, l_m, "B")
                            break
                elif cheque == "MATE":
                    print(colored("XEQUE MATE, SEU ADVERSÁRIO VENCEU O JOGO!", "yellow"))
                    exit(INDICE0)
            while True:
                try:
                    # Entrada usada para que se selecione a peça que o jogador quer mover
                    ent = input("EM QUE CASA ESTÁ LOCALIZADA A PEÇA QUE VOCÊ DESEJA MOVER? ").upper()
                    if ent == "DESISTIR":
                        m = "O JOGADOR {} DESISTIU, SENDO ASSIM, O JOGADOR {} VENCEU".format(nome_jogador_p, nome_jogador_b)
                        print()
                        print(colored(m, "green", attrs=['bold']))
                        exit(INDICE0)
                    li = int(ent[INDICE0]) - INDICE1
                    co = tradLet(ent[INDICE1].lower())
                    peca = tabuleiro[li][co]
                    lista_s = movimentos(tabuleiro, co, li, peca)
                    if li > INDICE7 or co > INDICE7 or li < INDICE0 or co < INDICE0:
                        print((colored("ESSA CASA NÃO ESTA CONTIDA NO TABULEIRO", "red")))
                    elif peca in PECAS_P:
                        print(colored("ESSA PEÇA É DO SEU ADVERSÁRIO. ESCOLHA UMA ALIADA.", "red"))
                    elif peca not in PECAS_B:
                        print(colored("NÃO HÁ NENHUMA PEÇA NESSA CASA. SELECIONA OUTRA.", "red"))
                    elif lista_s == []:
                        print(colored("ESSA PEÇA NÃO PODE SE MOVER, SELECIONE OUTRA.", "red"))
                    elif lista_s is True:
                        print(colored("ESSA PEÇA NÃO FOI ENCONTRADA", "red"))
                    else:
                        break
                except (TypeError, IndexError, ValueError):
                    print(colored("JOGADA INVÁLIDA!", "red"))
            to_e, to_d = roqueCond(tabuleiro, "RE_B", cont_rb, cont_tb_0, cont_tb_7, li, co)
            if to_e is True and to_d is True:
                faz_ro = input("VOCÊ GOSTARIA DE FAZER O ROQUE? ").upper()
                if faz_ro == "SIM":
                    esc_to = input("ESCOLHA UMA TORRE:\nTO_E    TO_D").upper()
                    if esc_to == "TO_E":
                        tabuleiro, lista_mov_b = roqueMov(tabuleiro, lista_mov_p, lista_pec_b, li, co, INDICE0, "RE_B", "TO_B")
                        break
                    elif esc_to == "TO_D":
                        tabuleiro, lista_mov_b = roqueMov(tabuleiro, lista_mov_p, lista_pec_b, li, co, INDICE0, "RE_B", "TO_B")
                        break
            elif to_e:
                faz_ro = input("VOCÊ GOSTARIA DE FAZER O ROQUE? ").upper()
                if faz_ro == "SIM":
                    tabuleiro, lista_mov_b = roqueMov(tabuleiro, lista_mov_p, lista_pec_b, li, co, INDICE0, "RE_B", "TO_B")
                    break
            elif to_d:
                faz_ro = input("VOCÊ GOSTARIA DE FAZER O ROQUE? ").upper()
                if faz_ro == "SIM":
                    tabuleiro, lista_mov_b = roqueMov(tabuleiro, lista_mov_p, lista_pec_b, li, co, INDICE0, "RE_B", "TO_B")
                    break
            # Contadores de movimento das peças necessárias para a realização do roque
            if li == INDICE0 and co == INDICE0:  # Torre da esquerda
                cont_tb_0 += INDICE1
            elif li == INDICE0 and co == INDICE7:  # Torre da direita
                cont_tb_7 += INDICE1
            elif li == INDICE0 and co == INDICE3:  # Rei branco
                cont_rb += INDICE1

            s = "ESSAS SÃO SUAS OPÇÕES DE MOVIMENTO\n{}".format(lista_s)
            print((colored(s, "blue")))
            print()
            while True:
                try:
                    mov = input("PARA QUAL DESSAS CASAS VOCÊ DESEJA MOVER A PEÇA? ").lower()
                    li_m = int(mov[INDICE0]) - INDICE1
                    co_m = tradLet(mov[INDICE1])
                    l_m = tabuleiro[li_m][co_m]
                    if mov not in lista_s:
                        print(colored("A CASA SELECIONADA NÃO PODE SER ESCOLHIDA", "red"))
                    else:
                        break
                except (TypeError, IndexError, ValueError):
                    print(colored("JOGADA INVÁLIDA!", "red"))
                    pass
            lista_mov_b = posPecas(lista_mov_b, ent.lower(), mov)
            if peca == "RE_B":
                pos_re_b = mov  # Atualiza a posição do rei sempre que ele se move
            if l_m == "RE_P":
                print()
                print("REI PRETO CAPTURADO! O(A) JOGADOR(A) {} É O(A) VENCEDOR(A)!".format(nome_jogador_b))
                exit(INDICE0)
            elif mov in lista_s:
                if peca == "PE_B" and li_m == INDICE7:
                    print(colored(
                        "SEU PEÃO FOI PROMOVIDO, ESCOLHA A PEÇA NA QUAL ELE SERÁ TRANSFORMADO: ", "green"))
                    print(colored("T, B, C, Q", "green"))
                    peca_pro = ""
                    while True:
                        peca_pro = input().upper()
                        if peca_pro == "T" or peca_pro == "B" or peca_pro == "C" or peca_pro == "Q":
                            break
                        else:
                            print(colored("PEÇA INVÁLIDA", "red"))
                    peca_pro, lista_pec_b = promoPeao(lista_pec_b, lista_mov_b, mov, peca_pro, "B")
                    tabuleiro = moverPecas(tabuleiro, peca_pro, li_m, co_m, li, co)
                elif l_m in PECAS_P:
                    lista_pec_p, lista_mov_p = removPecas(lista_pec_p, lista_mov_p, mov, l_m, "P")
                    tabuleiro = moverPecas(tabuleiro, peca, li_m, co_m, li, co)
                else:
                    tabuleiro = moverPecas(tabuleiro, peca, li_m, co_m, li, co)
                break
    else:
        li = INDICE0
        co = INDICE0
        peca = ""
        ent = ""
        mov = ""
        print("VEZ DO(A) JOGADOR(A) {}\n".format(nome_jogador_p))
        while True:
            if cont > INDICE1:
                # Verifica, a cada início de jogada, se o rei está em xeque
                cheque = indentificaCheque(tabuleiro, pos_re_p, "RE_P", lista_pec_p, lista_mov_p, lista_pec_b, lista_mov_b)
                if cheque == "XEQUE":
                    print(colored("SEU REI ESTÁ EM XEQUE, CUIDADO!", "red", attrs=['bold']))
                    print()
                    while True:
                        li = INDICE0
                        co = INDICE0
                        peca = ""
                        try:
                            ent = input("EM QUE CASA ESTÁ LOCALIZADA A PEÇA QUE VOCÊ DESEJA MOVER? ").upper()
                            if ent == "DESISTIR":
                                m = "O JOGADOR {} DESISTIU, SENDO ASSIM, O JOGADOR {} VENCEU".format(nome_jogador_p, nome_jogador_b)
                                print()
                                print(colored(m, "green", attrs=['bold']))
                                exit(INDICE0)
                            li = int(ent[INDICE0]) - INDICE1
                            co = tradLet(ent[INDICE1].lower())
                            peca = tabuleiro[li][co]
                            lista_s = movimentos(tabuleiro, co, li, peca)
                            if li > INDICE7 or co > INDICE7 or li < INDICE0 or co < INDICE0:
                                print((colored("ESSA CASA NÃO ESTA CONTIDA NO TABULEIRO", "red")))
                            elif peca in PECAS_B:
                                print(colored("ESSA PEÇA É DO SEU ADVERSÁRIO. ESCOLHA UMA ALIADA.", "red"))
                            elif peca not in PECAS_P:
                                print(colored("NÃO HÁ NENHUMA PEÇA NESSA CASA. SELECIONA OUTRA.", "red"))
                            elif lista_s == []:
                                print(colored("ESSA PEÇA NÃO PODE SE MOVER, SELECIONE OUTRA.", "red"))
                                print()
                            elif lista_s is True:
                                print(colored("ESSA PEÇA NÃO FOI ENCONTRADA", "red"))
                            else:
                                break
                        except (TypeError, IndexError, ValueError):
                            print(colored("JOGADA INVÁLIDA!", "red"))
                            pass
                    if peca == "RE_P":
                        to_e, to_d = roqueCond(tabuleiro, "RE_P", cont_rp, cont_tp_0, cont_tp_7, li, co)
                        if to_e is True and to_d is True:
                            faz_ro = input("VOCÊ GOSTARIA DE FAZER O ROQUE? ").upper()
                            if faz_ro == "SIM":
                                esc_to = input("ESCOLHA UMA TORRE:\nTO_E    TO_D").upper()
                                if esc_to == "TO_E":
                                    tabuleiro, lista_mov_p = roqueMov(tabuleiro, lista_mov_p, lista_pec_p, li, co, INDICE0, "RE_P", "TO_P")
                                    break
                                elif esc_to == "TO_D":
                                    tabuleiro, lista_mov_p = roqueMov(tabuleiro, lista_mov_p, lista_pec_p, li, co, INDICE0, "RE_P", "TO_P")
                                    break
                        elif to_e:
                            faz_ro = input("VOCÊ GOSTARIA DE FAZER O ROQUE? ").upper()
                            if faz_ro == "SIM":
                                cont_tp_0 += INDICE1
                                cont_rp += INDICE1
                                tabuleiro, lista_mov_p = roqueMov(tabuleiro, lista_mov_p, lista_pec_p, li, co, INDICE0, "RE_P", "TO_P")
                                break
                        elif to_d:
                            faz_ro = input("VOCÊ GOSTARIA DE FAZER O ROQUE? ").upper()
                            if faz_ro == "SIM":
                                cont_tp_7 += INDICE1
                                cont_rp += INDICE1
                                tabuleiro, lista_mov_p = roqueMov(tabuleiro, lista_mov_p, lista_pec_p, li, co, INDICE0, "RE_P", "TO_P")
                                break
                    lista_s = movimentos(tabuleiro, co, li, peca)
                    s = "ESSAS SÃO SUAS OPÇÕES DE MOVIMENTO\n{}".format(lista_s)
                    print((colored(s, "blue")))
                    while True:
                        try:
                            mov = input("PARA QUAL DESSAS CASAS VOCÊ DESEJA MOVER A PEÇA? ").lower()
                            li_m = int(mov[INDICE0]) - INDICE1
                            co_m = tradLet(mov[INDICE1])
                            l_m = tabuleiro[li_m][co_m]
                            if mov not in lista_s:
                                print(colored("A CASA SELECIONADA NÃO PODE SER ESCOLHIDA", "red"))
                            elif lista_s == []:
                                print(colored("ESSA PEÇA NÃO PODE SE MOVER, SELECIONE OUTRA.", "red"))
                                print()
                            elif lista_s is True:
                                print(colored("ESSA PEÇA NÃO FOI ENCONTRADA", "red"))
                            else:
                                break
                        except (TypeError, IndexError, ValueError):
                            print(colored("JOGADA INVÁLIDA!", "red"))
                            pass
                    if peca == "RE_P":
                        # Gera uma deepcopy do tabuleiro, a qual serve para analisar as condições de xeque
                        tabuleiro_t = copy.deepcopy(tabuleiro)
                        tabuleiro_t = moverPecas(tabuleiro_t, peca, li_m, co_m, li, co)
                        pos_t_r = mov
                        cheque = indentificaCheque(tabuleiro_t, pos_t_r, "RE_P", lista_pec_p, lista_mov_p, lista_pec_b, lista_mov_b)
                        if cheque == "XEQUE":
                            print(colored("SEU REI CONTINUA EM XEQUE!", "yellow"))
                            pass
                        elif cheque == "MATE":
                            print(colored("XEQUE MATE, SEU ADVERSÁRIO VENCEU O JOGO!", "yellow"))
                            exit(INDICE0)
                        else:
                            pos_re_p = mov  # Atualiza a posição do rei sempre que ele se move
                            tabuleiro = moverPecas(tabuleiro, peca, li_m, co_m, li, co)
                            lista_mov_p = posPecas(lista_mov_p, ent.lower(), mov)
                            if l_m in PECAS_B:
                                lista_pec_b, lista_mov_b = removPecas(lista_pec_b, lista_mov_b, mov, l_m, "B")
                            break
                    else:
                        # Gera uma deepcopy do tabuleiro, a qual serve para analisar as condições de xeque = copy.deepcopy(tabuleiro)
                        tabuleiro_t = copy.deepcopy(tabuleiro)
                        tabuleiro_t = moverPecas(tabuleiro_t, peca, li_m, co_m, li, co)
                        cheque = indentificaCheque(tabuleiro_t, pos_re_p, "RE_P", lista_pec_p, lista_mov_p, lista_pec_b, lista_mov_b)
                        if cheque == "XEQUE":
                            print(colored("SEU REI CONTINUA EM XEQUE!", "yellow"))
                            pass
                        elif cheque == "MATE":
                            print(colored("XEQUE MATE, SEU ADVERSÁRIO VENCEU O JOGO!", "yellow"))
                            exit(INDICE0)
                        else:
                            if peca == "PE_P" and li_m == INDICE0:
                                print(colored("SEU PEÃO FOI PROMOVIDO, ESCOLHA A PEÇA NA QUAL ELE SERÁ TRANSFORMADO: ", "green"))
                                print(colored("T, B, C, Q", "green"))
                                peca_pro = ""
                                while True:
                                    peca_pro = input().upper()
                                    if peca_pro == "T" or peca_pro == "B" or peca_pro == "C" or peca_pro == "Q":
                                        break
                                    else:
                                        print(colored("PEÇA INVÁLIDA", "red"))
                                peca_pro, lista_pec_p = promoPeao(lista_pec_p, lista_mov_p, mov, peca_pro, "P")
                            tabuleiro = moverPecas(tabuleiro, peca, li_m, co_m, li, co)
                            lista_mov_p = posPecas(lista_mov_p, ent.lower(), mov)
                            if l_m in PECAS_B:
                                lista_pec_b, lista_mov_b = removPecas(lista_pec_b, lista_mov_b, mov, l_m, "B")
                            break
                elif cheque == "MATE":
                    print(colored("XEQUE MATE, SEU ADVERSÁRIO VENCEU O JOGO!", "yellow"))
                    exit(INDICE0)
            while True:
                try:
                    ent = input("EM QUE CASA ESTÁ LOCALIZADA A PEÇA QUE VOCÊ DESEJA MOVER? ").upper()
                    if ent == "DESISTIR":
                        m = "O JOGADOR {} DESISTIU, SENDO ASSIM, O JOGADOR {} VENCEU".format(nome_jogador_p, nome_jogador_b)
                        print()
                        print(colored(m, "green", attrs=['bold']))
                        exit(INDICE0)
                    li = int(ent[INDICE0]) - INDICE1
                    co = tradLet(ent[INDICE1].lower())
                    peca = tabuleiro[li][co]
                    lista_s = movimentos(tabuleiro, co, li, peca)
                    if li > INDICE7 or co > INDICE7 or li < INDICE0 or co < INDICE0:
                        print((colored("ESSA CASA NÃO ESTA CONTIDA NO TABULEIRO", "red")))
                    elif peca in PECAS_B:
                        print(colored("ESSA PEÇA É DO SEU ADVERSÁRIO. ESCOLHA UMA ALIADA.", "red"))
                    elif peca not in PECAS_P:
                        print(colored("NÃO HÁ NENHUMA PEÇA NESSA CASA. SELECIONA OUTRA.", "red"))
                    elif lista_s == []:
                        print(colored("ESSA PEÇA NÃO PODE SE MOVER, SELECIONE OUTRA.", "red"))
                        print()
                    elif lista_s is True:
                        print(colored("ESSA PEÇA NÃO FOI ENCONTRADA", "red"))
                    else:
                        break
                except (TypeError, IndexError, ValueError):
                    print(colored("JOGADA INVÁLIDA!", "red"))
                    pass
            to_e, to_d = roqueCond(tabuleiro, "RE_P", cont_rp, cont_tp_0, cont_tp_7, li, co)
            if to_e is True and to_d is True:
                faz_ro = input("VOCÊ GOSTARIA DE FAZER O ROQUE? ").upper()
                if faz_ro == "SIM":
                    esc_to = input("ESCOLHA UMA TORRE:\nTO_E    TO_D").upper()
                    if esc_to == "TO_E":
                        tabuleiro, lista_mov_p = roqueMov(tabuleiro, lista_mov_p, lista_pec_p, li, co, INDICE0, "RE_P", "TO_P")
                        break
                    elif esc_to == "TO_D":
                        tabuleiro, lista_mov_p = roqueMov(tabuleiro, lista_mov_p, lista_pec_p, li, co, INDICE0, "RE_P", "TO_P")
                        break
            elif to_e:
                faz_ro = input("VOCÊ GOSTARIA DE FAZER O ROQUE? ").upper()
                if faz_ro == "SIM":
                    tabuleiro, lista_mov_p = roqueMov(tabuleiro, lista_mov_p, lista_pec_p, li, co, INDICE0, "RE_P", "TO_P")
                    break
            elif to_d:
                faz_ro = input("VOCÊ GOSTARIA DE FAZER O ROQUE? ").upper()
                if faz_ro == "SIM":
                    tabuleiro, lista_mov_p = roqueMov(tabuleiro, lista_mov_p, lista_pec_p, li, co, INDICE0, "RE_P", "TO_P")
                    break
            # Contadores de movimento das peças necessárias para a realização do roque
            if li == INDICE7 and co == INDICE0:  # Torre da esquerda
                cont_tp_0 += INDICE1
            elif li == INDICE7 and co == INDICE7:  # Torre da direita
                cont_tp_7 += INDICE1
            elif li == INDICE7 and co == INDICE4:  # Rei preto
                cont_rp += INDICE1

            s = "ESSAS SÃO SUAS OPÇÕES DE MOVIMENTO\n{}".format(lista_s)
            print((colored(s, "blue")))
            print()
            while True:
                try:
                    mov = input("PARA QUAL DESSAS CASAS VOCÊ DESEJA MOVER A PEÇA? ").lower()
                    li_m = int(mov[INDICE0]) - INDICE1
                    co_m = tradLet(mov[INDICE1])
                    l_m = tabuleiro[li_m][co_m]
                    if mov not in lista_s:
                        print(colored("A CASA SELECIONADA NÃO PODE SER ESCOLHIDA", "red"))
                    else:
                        break
                except (TypeError, IndexError, ValueError):
                    print(colored("JOGADA INVÁLIDA!", "red"))
                    pass
            lista_mov_p = posPecas(lista_mov_p, ent.lower(), mov)
            if peca == "RE_P":
                pos_re_p = mov  # Atualiza a posição do rei sempre que ele se move
            if l_m == "RE_B":
                print()
                s = "REI BRANCO CAPTURADO! O(A) JOGADOR(A) {} É O(A) VENCEDOR(A)!".format(
                    nome_jogador_p)
                print(colored(s, "blue", attrs=['bold']))
                exit(INDICE0)
            elif mov in lista_s:
                if peca == "PE_P" and li_m == INDICE0:
                    print(colored("SEU PEÃO FOI PROMOVIDO, ESCOLHA A PEÇA NA QUAL ELE SERÁ TRANSFORMADO: ", "green"))
                    print(colored("T, B, C, Q", "green"))
                    peca_pro = ""
                    while True:
                        peca_pro = input().upper()
                        if peca_pro == "T" or peca_pro == "B" or peca_pro == "C" or peca_pro == "Q":
                            break
                        else:
                            print(colored("PEÇA INVÁLIDA", "red"))
                    peca_pro, lista_pec_p = promoPeao(lista_pec_p, lista_mov_p, mov, peca_pro, "P")
                    tabuleiro = moverPecas(tabuleiro, peca_pro, li_m, co_m, li, co)
                elif l_m in PECAS_B:
                    lista_pec_b, lista_mov_b = removPecas(lista_pec_b, lista_mov_b, mov, l_m, "B")
                    tabuleiro = moverPecas(tabuleiro, peca, li_m, co_m, li, co)
                else:
                    tabuleiro = moverPecas(tabuleiro, peca, li_m, co_m, li, co)
                break
    # Casos de empate
    cont_g_b = len(lista_pec_b)  # Contador do total de peças brancas
    cont_g_p = len(lista_pec_p)  # Contador do total de peças pretas
    cont_ca_b = lista_pec_b.count("CA_B")  # Contador da quantidade de cavalos brancos
    cont_ca_p = lista_pec_p.count("CA_P")  # Contador da quantidade de cavalos pretos
    cont_bi_p = lista_pec_p.count("BI_P")  # Contador da quantidade de bispos pretos
    cont_bi_b = lista_pec_b.count("BI_B")  # Contador da quantidade de bispos brancos
    # Condição de empate caso só sobrem os dois reis
    if cont_g_b == INDICE1 and cont_g_p == INDICE1:
        print()
        print(colored("O JOGO TERMINOU EMPATADO!", "green"))
        exit(INDICE0)
    # Condição de empate caso sobrem apenas 1 rei, contra 1 rei e 1 bispo
    elif (cont_g_b == INDICE1 and cont_g_p == INDICE2 and cont_bi_p == INDICE1) or (cont_g_p == INDICE1 and cont_g_b == INDICE2 and cont_bi_b == INDICE1):
        print()
        print(colored("O JOGO TERMINOU EMPATADO!", "green"))
        exit(INDICE0)
    # Condição de empate caso sobrem apenas 1 rei, contra 1 rei e 1 cavalo
    elif (cont_g_b == INDICE1 and cont_g_p == INDICE2 and cont_ca_p == INDICE1) or (cont_g_p == INDICE1 and cont_g_b == INDICE2 and cont_ca_b == INDICE1):
        print()
        print(colored("O JOGO TERMINOU EMPATADO!", "green"))
        exit(INDICE0)
    # Condição de empate caso sobrem apenas 1 rei, contra 1 rei e 2 cavalos
    elif (cont_g_b == INDICE1 and cont_g_p == INDICE3 and cont_ca_p == INDICE2) or (cont_g_p == INDICE1 and cont_g_b == INDICE3 and cont_ca_b == INDICE2):
        print()
        print(colored("O JOGO TERMINOU EMPATADO!", "green"))
        exit(INDICE0)
    cont += INDICE1  # Adiciona '+ 1' ao contador da quantidade de jogadas
