"""
Neste módulo se encontram as funções usadas
para o funcionamento do Xadrez.
O módulo de interface com o usuário as utiliza para:
- Colocar as peças nos lugares corretos para o ínico da partida.
- Mostrar ao usuário quais são os movimentos possíveis
"""
from CONS import *

lista_pec_b = []
lista_pec_p = []
lista_mov_b = []
lista_mov_p = []


def montar_tabuleiro():
    """
    Esta função monta o tabuleiro de xadrez em forma de matriz de tamanho QTD_L x QTD_C
    :return: Um tauleiro como matriz
    """
    tabuleiro = []
    for x in range(INDICE0, INDICE7 + INDICE1):  # indice da linha
        linha = []
        for y in range(INDICE0, INDICE7 + INDICE1):  # indice da coluna
            linha.append("_")
        tabuleiro.append(linha)
    return tabuleiro


def peoes_lugar(n1, peca):
    """
    Esta função adiciona os Peões(variavel peca),
    na 2º linha e na 7º linha(variavel n1).
    :return: Uma lista com os Peões em suas posições que substitui as linhas 2 e 7
    """
    lista = []
    for c in range(n1):
        lista.append(("{}".format(peca)))
        if peca in PECAS_B:
            lista_pec_b.append(peca)
            lista_mov_b.append("{}{}".format(INDICE1 + 1, tradLet(c)))
        else:
            lista_pec_p.append(peca)
            lista_mov_p.append("{}{}".format(INDICE7, tradLet(c)))
    return lista


def pecas_lugar(tabuleiro, indice_linha, indice_e, indice_d, peca):
    """
    Esta função adiciona as peças torre, cavalo e bispo em suas posições no tabuleiro
    :param tabuleiro: A matriz do tabuleiro de Xadrez
    :param indice_linha: A linha que as peças devem ser adicionadas
    :param indice_e: A posição nas casas da esquerda que a peça deve ser posicionada
    :param indice_d: A posição nas casas da direita que a peça deve ser posicionada
    :param peca: A peça que deve ser adicionada ao tabuleiro
    :return: Uma lista correspondente a linha com as peças posicionadas
    """
    tabuleiro[indice_linha][indice_e] = ("{}".format(peca))
    tabuleiro[indice_linha][indice_d] = ("{}".format(peca))
    return tabuleiro[indice_linha]


def rei_rainha_lugar(tabuleiro, indice_linha, indice, peca):
    """
    Esta função adiciona as peças rei e rainha em suas posições no tabuleiro
    :param tabuleiro: A matriz do tabuleiro de Xadrez
    :param indice_linha: A linha que as peças devem ser adicionadas
    :param indice: A posição nas casas que a peça deve ser posicionada
    :param peca: A peça que deve ser adicionada ao tabuleiro
    :return: Uma lista correspondente a linha com as peças posicionadas
    """
    tabuleiro[indice_linha][indice] = ("{}".format(peca))
    return tabuleiro[indice_linha]


def posiciona_pecas():
    """
    Esta função posiciona todas as peças no tabuleiro
    :return: Uma matriz com o tabuleiro montado
    """
    tabuleiro = montar_tabuleiro()
    for a in PECAS_B:
        for b in range(len(tabuleiro)):
            if b == PONTO_P and a == "PE_B":
                tabuleiro[b] = peoes_lugar(QTD_C, a)
            elif b == INDICE0 and a == "TO_B":
                tabuleiro[b] = pecas_lugar(tabuleiro, b, INDICE_TORRE_E, INDICE_TORRE_D, a)
                lista_pec_b.append(a)
                lista_pec_b.append(a)
                lista_mov_b.append("{}{}".format(b + INDICE1, tradLet(INDICE_TORRE_E)))
                lista_mov_b.append("{}{}".format(b + INDICE1, tradLet(INDICE_TORRE_D)))
            elif b == INDICE0 and a == "CA_B":
                tabuleiro[b] = pecas_lugar(tabuleiro, b, INDICE_CAVALO_E, INDICE_CAVALO_D, a)
                lista_pec_b.append(a)
                lista_pec_b.append(a)
                lista_mov_b.append("{}{}".format(b + INDICE1, tradLet(INDICE_CAVALO_E)))
                lista_mov_b.append("{}{}".format(b + INDICE1, tradLet(INDICE_CAVALO_D)))
            elif b == INDICE0 and a == "BI_B":
                tabuleiro[b] = pecas_lugar(tabuleiro, b, INDICE_BISPO_E, INDICE_BISPO_D, a)
                lista_pec_b.append(a)
                lista_pec_b.append(a)
                lista_mov_b.append("{}{}".format(b + INDICE1, tradLet(INDICE_BISPO_E)))
                lista_mov_b.append("{}{}".format(b + INDICE1, tradLet(INDICE_BISPO_D)))
            elif b == INDICE0 and a == "RA_B":
                tabuleiro[b] = rei_rainha_lugar(tabuleiro, b, INDICE_REI, a)
                lista_pec_b.append(a)
                lista_mov_b.append("{}{}".format(b + INDICE1, tradLet(INDICE_REI)))
            elif b == INDICE0 and a == "RE_B":
                tabuleiro[b] = rei_rainha_lugar(tabuleiro, b, INDICE_RAINHA, a)
                lista_pec_b.append(a)
                lista_mov_b.append("{}{}".format(b + INDICE1, tradLet(INDICE_RAINHA)))
    for a in PECAS_P:
        for b in range(len(tabuleiro)):
            if b == P2_PEAO and a == "PE_P":
                tabuleiro[b] = peoes_lugar(QTD_C, a)
            elif b == INDICE7 and a == "TO_P":
                tabuleiro[b] = pecas_lugar(tabuleiro, b, INDICE_TORRE_E, INDICE_TORRE_D, a)
                lista_pec_p.append(a)
                lista_pec_p.append(a)
                lista_mov_p.append("{}{}".format(b + INDICE1, tradLet(INDICE_TORRE_E)))
                lista_mov_p.append("{}{}".format(b + INDICE1, tradLet(INDICE_TORRE_D)))
            elif b == INDICE7 and a == "CA_P":
                tabuleiro[b] = pecas_lugar(tabuleiro, b, INDICE_CAVALO_E, INDICE_CAVALO_D, a)
                lista_pec_p.append(a)
                lista_pec_p.append(a)
                lista_mov_p.append("{}{}".format(b + INDICE1, tradLet(INDICE_CAVALO_E)))
                lista_mov_p.append("{}{}".format(b + INDICE1, tradLet(INDICE_CAVALO_D)))
            elif b == INDICE7 and a == "BI_P":
                tabuleiro[b] = pecas_lugar(tabuleiro, b, INDICE_BISPO_E, INDICE_BISPO_D, a)
                lista_pec_p.append(a)
                lista_pec_p.append(a)
                lista_mov_p.append("{}{}".format(b + INDICE1, tradLet(INDICE_BISPO_E)))
                lista_mov_p.append("{}{}".format(b + INDICE1, tradLet(INDICE_BISPO_D)))
            elif b == INDICE7 and a == "RE_P":
                tabuleiro[b] = rei_rainha_lugar(tabuleiro, b, INDICE_REI, a)
                lista_pec_p.append(a)
                lista_mov_p.append("{}{}".format(b + INDICE1, tradLet(INDICE_REI)))
            elif b == INDICE7 and a == "RA_P":
                tabuleiro[b] = rei_rainha_lugar(tabuleiro, b, INDICE_RAINHA, a)
                lista_pec_p.append(a)
                lista_mov_p.append("{}{}".format(b + INDICE1, tradLet(INDICE_RAINHA)))
    return tabuleiro


def tradLet(le):
    """
    Esta função traduz as letras das posições em números e os números em letras
    :param le: O número ou letra
    :return: A tradução seja uma letra ou número
    """
    if le == "a":
        n = INDICE0
        return n
    elif le == "b":
        n = INDICE1
        return n
    elif le == "c":
        n = INDICE2
        return n
    elif le == "d":
        n = INDICE3
        return n
    elif le == "e":
        n = INDICE4
        return n
    elif le == "f":
        n = INDICE5
        return n
    elif le == "g":
        n = INDICE6
        return n
    elif le == "h":
        n = INDICE7
        return n
    elif le == INDICE0:
        l = "a"
        return l
    elif le == INDICE1:
        l = "b"
        return l
    elif le == INDICE2:
        l = "c"
        return l
    elif le == INDICE3:
        l = "d"
        return l
    elif le == INDICE4:
        l = "e"
        return l
    elif le == INDICE5:
        l = "f"
        return l
    elif le == INDICE6:
        l = "g"
        return l
    elif le == INDICE7:
        l = "h"
        return l


def movPeao(tabuleiro, co, li, peca):
    """
    Esta função indentifica quais são as movimentações possiveis do peão
    :param tabuleiro: A matriz do tabuleiro de Xadrez
    :param co: A coluna em que o Peão se encontra
    :param li: A linha em que o Peão se encontra
    :param peca: A peça movimentada, se é um Peão branco ou preto
    :return: Uma lista com as casas possiveis
    """
    lista_m = []
    if peca[INDICE3] == "B":
        if li == INDICE1:
            lista_m.append("{}{}".format(LINHA_PEAO_2, co))
            lista_m.append("{}{}".format(LINHA_PEAO_3, co))
        elif li != INDICE7 and tabuleiro[li + INDICE1][co] not in PECAS_P and tabuleiro[li + INDICE1][
            co] not in PECAS_B:
            lista_m.append("{}{}".format(li + INDICE1, co))
        if li != INDICE7 and co != INDICE7 and tabuleiro[li + INDICE1][co + INDICE1] in PECAS_P:
            lista_m.append("{}{}".format(li + INDICE1, co + INDICE1))
        if li != INDICE7 and co != INDICE0 and tabuleiro[li + INDICE1][co - INDICE1] in PECAS_P:
            lista_m.append("{}{}".format(li + INDICE1, co - INDICE1))

    if peca[INDICE3] == "P":
        if li == 6:
            lista_m.append("{}{}".format(LINHA_PEAO_4, co))
            lista_m.append("{}{}".format(LINHA_PEAO_5, co))
        elif li != INDICE0 and tabuleiro[li - INDICE1][co] not in PECAS_P and tabuleiro[li - INDICE1][
            co] not in PECAS_B:
            lista_m.append("{}{}".format(li - INDICE1, co))
        if li != INDICE0 and co != INDICE7 and tabuleiro[li - INDICE1][co + INDICE1] in PECAS_B:
            lista_m.append("{}{}".format(li - INDICE1, co + INDICE1))
        if li != INDICE0 and co != INDICE0 and tabuleiro[li - INDICE1][co - INDICE1] in PECAS_B:
            lista_m.append("{}{}".format(li - INDICE1, co - INDICE1))
    num = len(lista_m)
    for a in range(num):
        lista_m[a] = list(lista_m[a])
        lista_m[a][INDICE0] = str(int(lista_m[a][INDICE0]) + INDICE1)
        lista_m[a][INDICE1] = tradLet(int(lista_m[a][INDICE1]))
        v = ""
        for b in lista_m[a]:
            v += b
        lista_m[a] = v

    return lista_m


def movTorre(tabuleiro, co, li, peca):
    """
    Esta função indentifica quais são as movimentações possiveis da torre
    :param tabuleiro: A matriz do tabuleiro de Xadrez
    :param co: A coluna em que a Torre se encontra
    :param li: A linha em que a Torre se encontra
    :param peca: A peça movimentada, se é uma Torre branca ou preta
    :return: Uma lista com as casas possiveis
    """
    aliados = []
    oponente = []
    lista_m = []
    if peca[INDICE3] == "B":
        aliados = PECAS_B
        oponente = PECAS_P
    elif peca[INDICE3] == "P":
        aliados = PECAS_P
        oponente = PECAS_B
    for a in range(co + INDICE1, INDICE7 + INDICE1):
        casa = tabuleiro[li][a]
        if casa in aliados:
            break
        if casa not in aliados:
            lista_m.append("{}{}".format(li, a))
            if casa in oponente:
                break
    for b in range(co - INDICE1, INDICE0 - INDICE1, -INDICE1):
        casa = tabuleiro[li][b]
        if casa in aliados:
            break
        if casa not in aliados:
            lista_m.append("{}{}".format(li, b))
            if casa in oponente:
                break
    for c in range(li + INDICE1, INDICE7 + INDICE1):
        casa = tabuleiro[c][co]
        if casa in aliados:
            break
        if casa not in aliados:
            lista_m.append("{}{}".format(c, co))
            if casa in oponente:
                break
    for d in range(li - INDICE1, INDICE0 - INDICE1, -INDICE1):
        casa = tabuleiro[d][co]
        if casa in aliados:
            break
        if casa not in aliados:
            lista_m.append("{}{}".format(d, co))
            if casa in oponente:
                break
    num = len(lista_m)
    for a in range(num):
        lista_m[a] = list(lista_m[a])
        lista_m[a][INDICE0] = str(int(lista_m[a][INDICE0]) + INDICE1)
        lista_m[a][INDICE1] = tradLet(int(lista_m[a][INDICE1]))
        v = ""
        for b in lista_m[a]:
            v += b
        lista_m[a] = v
    return lista_m


def movBispo(tabuleiro, co, li, peca):
    """
    Esta função indentifica quais são as movimentações possiveis do bispo
    :param tabuleiro: A matriz do tabuleiro de Xadrez
    :param co: A coluna em que o Bispo se encontra
    :param li: A linha em que o Bispo se encontra
    :param peca: A peça movimentada, se é um Bispo branco ou preto
    :return: Uma lista com as casas possiveis
    """
    aliados = []
    oponente = []
    lista_m = []
    if peca[INDICE3] == "P":
        aliados = PECAS_P
        oponente = PECAS_B
    elif peca[INDICE3] == "B":
        aliados = PECAS_B
        oponente = PECAS_P
    # Coeficientes utilizados para cada direção diagonal:
    co_e = co  # Diagonal esquerda + cima
    co_d = co  # Diagonal direita + cima
    co_e_b = co  # Diagonal esquerda + baixo
    co_d_b = co  # Diagonal direita + baixo
    if li != INDICE0:  # Essa condição é utilizada caso o bispo não esteja na linha 0 do tabuleiro
        for a in range(li - INDICE1, -INDICE1, -INDICE1):
            if co_e == LIMITE_CO_D:
                break
            co_d += INDICE1
            casa = tabuleiro[a][co_d]
            if casa in aliados:
                break
            if casa not in aliados:
                lista_m.append("{}{}".format(a, co_d))
                if casa in oponente or co_d == LIMITE_CO_D:
                    break
        for b in range(li - INDICE1, -INDICE1, -INDICE1):
            if co_e == LIMITE_CO_E:
                break
            co_e -= INDICE1
            casa = tabuleiro[b][co_e]
            if casa in aliados:
                break
            if casa not in aliados:
                lista_m.append("{}{}".format(b, co_e))
                if casa in oponente:
                    break
    if li != INDICE7:  # Essa condição é utilizada caso o bispo não esteja na linha 7 do tabuleiro
        for c in range(li + INDICE1, INDICE7 + INDICE1):
            if co_e_b == LIMITE_CO_E:
                break
            co_e_b -= INDICE1
            casa = tabuleiro[c][co_e_b]
            if casa in aliados:
                break
            if casa not in aliados:
                lista_m.append("{}{}".format(c, co_e_b))
                if casa in oponente:
                    break
        for d in range(li + INDICE1, INDICE7 + INDICE1):
            if co_d_b == LIMITE_CO_D:
                break
            co_d_b += INDICE1
            casa = tabuleiro[d][co_d_b]
            if casa in aliados:
                break
            if casa not in aliados:
                lista_m.append("{}{}".format(d, co_d_b))
                if casa in oponente:
                    break
    num = len(lista_m)
    for a in range(num):
        lista_m[a] = list(lista_m[a])
        lista_m[a][0] = str(int(lista_m[a][0]) + INDICE1)
        lista_m[a][INDICE1] = tradLet(int(lista_m[a][INDICE1]))
        v = ""
        for b in lista_m[a]:
            v += b
        lista_m[a] = v
    return lista_m


def movRei(tabuleiro, co, li, peca):
    """
    Esta função indentifica quais são as movimentações possiveis do rei
    :param tabuleiro: A matriz do tabuleiro de Xadrez
    :param co: A coluna em que o Rei se encontra
    :param li: A linha em que o Rei se encontra
    :param peca: A peça movimentada, se é um Rei branco ou preto
    :return: Uma lista com as casas possiveis
    """
    aliados = []
    lista_m = []
    if peca[INDICE3] == "B":
        aliados = PECAS_B
    elif peca[INDICE3] == "P":
        aliados = PECAS_P

    if li != INDICE7 and tabuleiro[li + INDICE1][co] not in aliados:
        lista_m.append("{}{}".format(li + INDICE1, co))
    if li != INDICE0 and tabuleiro[li - INDICE1][co] not in aliados:
        lista_m.append("{}{}".format(li - INDICE1, co))
    if co != INDICE7 and tabuleiro[li][co + INDICE1] not in aliados:
        lista_m.append("{}{}".format(li, co + INDICE1))
    if co != INDICE0 and tabuleiro[li][co - INDICE1] not in aliados:
        lista_m.append("{}{}".format(li, co - INDICE1))
    if li != INDICE7 and co != INDICE7 and tabuleiro[li + INDICE1][co + INDICE1] not in aliados:
        lista_m.append("{}{}".format(li + INDICE1, co + INDICE1))
    if li != INDICE7 and co != INDICE0 and tabuleiro[li + INDICE1][co - INDICE1] not in aliados:
        lista_m.append("{}{}".format(li + INDICE1, co - INDICE1))
    if li != INDICE0 and co != INDICE7 and tabuleiro[li - INDICE1][co + INDICE1] not in aliados:
        lista_m.append("{}{}".format(li - INDICE1, co + INDICE1))
    if li != INDICE0 and co != INDICE0 and tabuleiro[li - INDICE1][co - INDICE1] not in aliados:
        lista_m.append("{}{}".format(li - INDICE1, co - INDICE1))
    num = len(lista_m)
    for a in range(num):
        lista_m[a] = list(lista_m[a])
        lista_m[a][0] = str(int(lista_m[a][INDICE0]) + INDICE1)
        lista_m[a][INDICE1] = tradLet(int(lista_m[a][INDICE1]))
        v = ""
        for b in lista_m[a]:
            v += b
        lista_m[a] = v
    return lista_m


def movCavalo(tabuleiro, co, li, peca):
    """
    Esta função indentifica quais são as movimentações possiveis do cavalo
    :param tabuleiro: A matriz do tabuleiro de Xadrez
    :param co: A coluna em que o Cavalo se encontra
    :param li: A linha em que o Cavalo se encontra
    :param peca: A peça movimentada, se é um Cavalo branco ou preto
    :return: Uma lista com as casas possiveis
    """
    lista_m = []
    if peca[INDICE3] == "B":
        aliados = PECAS_B
    else:
        aliados = PECAS_P
    if li + INDICE2 <= INDICE7 and co + INDICE1 <= INDICE7:
        if tabuleiro[li + INDICE2][co + INDICE1] in tabuleiro[li + INDICE2] and tabuleiro[li + INDICE2][
            co + INDICE1] not in aliados:
            lista_m.append("{}{}".format(li + INDICE2, co + INDICE1))
    if co - INDICE1 >= INDICE0 and li + INDICE2 <= INDICE7:
        if tabuleiro[li + INDICE2][co - INDICE1] in tabuleiro[li + INDICE2] and tabuleiro[li + INDICE2][
            co - INDICE1] not in aliados:
            lista_m.append("{}{}".format(li + INDICE2, co - INDICE1))
    if co - INDICE2 >= INDICE0 and li + INDICE1 <= INDICE7:
        if tabuleiro[li + INDICE1][co - INDICE2] in tabuleiro[li + INDICE1] and tabuleiro[li + INDICE1][
            co - INDICE2] not in aliados:
            lista_m.append("{}{}".format(li + INDICE1, co - INDICE2))
    if li + INDICE1 <= INDICE7 and co + INDICE2 <= INDICE7:
        if tabuleiro[li + INDICE1][co + INDICE2] in tabuleiro[li + INDICE1] and tabuleiro[li + INDICE1][
            co + INDICE2] not in aliados:
            lista_m.append("{}{}".format(li + INDICE1, co + INDICE2))
    if li - INDICE1 >= INDICE0 and co + INDICE2 <= INDICE7:
        if tabuleiro[li - INDICE1][co + INDICE2] in tabuleiro[li - INDICE1] and tabuleiro[li - INDICE1][
            co + INDICE2] not in aliados:
            lista_m.append("{}{}".format(li - INDICE1, co + INDICE2))
    if li - INDICE1 >= INDICE0 and co - INDICE2 >= INDICE0:
        if tabuleiro[li - INDICE1][co - INDICE2] in tabuleiro[li - INDICE1] and tabuleiro[li - INDICE1][
            co - INDICE2] not in aliados:
            lista_m.append("{}{}".format(li - INDICE1, co - INDICE2))
    if li - INDICE2 >= INDICE0 and co - INDICE1 >= INDICE0:
        if tabuleiro[li - INDICE2][co - INDICE1] in tabuleiro[li - INDICE2] and tabuleiro[li - INDICE2][
            co - INDICE1] not in aliados:
            lista_m.append("{}{}".format(li - INDICE2, co - INDICE1))
    if li - INDICE2 >= INDICE0 and co + INDICE1 <= INDICE7:
        if tabuleiro[li - INDICE2][co + INDICE1] in tabuleiro[li - INDICE2] and tabuleiro[li - INDICE2][
            co + INDICE1] not in aliados:
            lista_m.append("{}{}".format(li - INDICE2, co + INDICE1))
    num = len(lista_m)
    for a in range(num):
        lista_m[a] = list(lista_m[a])
        lista_m[a][INDICE0] = str(int(lista_m[a][INDICE0]) + INDICE1)
        lista_m[a][INDICE1] = tradLet(int(lista_m[a][INDICE1]))
        v = ""
        for b in lista_m[a]:
            v += b
        lista_m[a] = v
    return lista_m


def movimentos(tabuleiro, co, li, peca):
    """
    Esta função retorna as possiveis casas de movimento
    :param tabuleiro: A matriz do tauleiro com as peças posicionadas
    :param co: O indice da coluna
    :param li: O indice da linha
    :param peca: A peça a ser movimentada
    :return: Uma lista com as casas possiveis de movimento
    """
    peca_errada = True
    # Condição que será utilizada, caso a peça selecionada seja um peão (seja ele branco ou preto)
    if peca == "PE_B" or peca == "PE_P":
        return movPeao(tabuleiro, co, li, peca)
    # Condição que será utilizada, caso a peça selecionada seja uma torre (seja ela branca ou preta)
    elif peca == "TO_B" or peca == "TO_P":
        return movTorre(tabuleiro, co, li, peca)
    # Condição que será utilizada, caso a peça selecionada seja um bispo preto
    elif peca == "BI_P" or peca == "BI_B":
        return movBispo(tabuleiro, co, li, peca)
    elif peca == "RE_B" or peca == "RE_P":
        return movRei(tabuleiro, co, li, peca)
    elif peca == "CA_B" or peca == "CA_P":
        return movCavalo(tabuleiro, co, li, peca)
    elif peca == "RA_B" or peca == "RA_P":
        b = movBispo(tabuleiro, co, li, peca)
        t = movTorre(tabuleiro, co, li, peca)
        s = (b + t)
        return s
    else:
        return peca_errada


def moverPecas(tabuleiro, peca, li_m, co_m, li, co):
    """
    Esta função move as peças no tabuleiro
    :param tabuleiro: Uma matriz com o tabuleiro
    :param peca: A peça que esta sendo movida
    :param li_m: A linha de movimento
    :param co_m: A coluna de movimento
    :param li: A linha inicial
    :param co: A coluna inicial
    :return: O tabuleiro atualizado
    """
    tabuleiro[li_m][co_m] = peca
    tabuleiro[li][co] = "_"
    return tabuleiro


def roqueCasV(tabuleiro, li, co, la):
    """
    Esta função verifica se o espaço entre o rei e a torre esta vazio
    :param tabuleiro: Uma matriz com o tabuleiro
    :param li: A linha em que o rei se encontra
    :param co: A coluna em que o rei se encontra
    :param la: O lado em que a torre está
    :return: Uma variável booleana, dizendo se a casa está vazia ou não
    """
    mensagem = True
    if la == INDICE0:
        for a in range(co - INDICE1, INDICE0, -INDICE1):
            casa = tabuleiro[li][a]
            if casa in PECAS_B or casa in PECAS_P:
                break
            elif a == INDICE1:
                return mensagem
    elif la == INDICE7:
        for a in range(co + INDICE1, INDICE7):
            casa = tabuleiro[li][a]
            if casa in PECAS_B or casa in PECAS_P:
                break
            elif a == INDICE6:
                return mensagem


def roqueCond(tabuleiro, rei, cont_r, cont_t_e, cont_t_d, li, co):
    """
    Esta função analisa as condições para acontecer o roque
    :param tabuleiro: Uma matriz com o tabuleiro
    :param rei: O rei
    :param cont_r: O contador de movimentos do rei
    :param cont_t_e: O contador de movimentos da torre esquerda
    :param cont_t_d: O contador de movimentos da torre direita
    :param li: A linha em que o rei esta localizado
    :param co: A coluna em que o rei esta localizado
    :return: Duas variáveis booleanas em relação a torre esquerda e direita
    """
    to_e = False
    to_d = False
    if rei == "RE_B" and cont_r == INDICE0:
        if rei == "RE_B" and li == INDICE0 and co == INDICE3:
            if tabuleiro[INDICE0][INDICE0] == "TO_B":
                if cont_t_e == INDICE0:
                    vazio = roqueCasV(tabuleiro, li, co, INDICE0)
                    if vazio:
                        to_e = True
            elif tabuleiro[INDICE0][INDICE7] == "TO_B":
                if cont_t_d == INDICE0:
                    vazio = roqueCasV(tabuleiro, li, co, INDICE0)
                    if vazio:
                        to_d = True
    if rei == "RE_P" and cont_r == INDICE0:
        if rei == "RE_P" and li == INDICE7 and co == INDICE4:
            if tabuleiro[INDICE7][INDICE0] == "TO_P":
                if cont_t_e == INDICE0:
                    vazio = roqueCasV(tabuleiro, li, co, INDICE0)
                    if vazio:
                        to_e = True
            elif tabuleiro[INDICE7][INDICE7] == "TO_P":
                if cont_t_d == INDICE0:
                    vazio = roqueCasV(tabuleiro, li, co, INDICE7)
                    if vazio:
                        to_d = True
    return to_e, to_d


def roqueMov(tabuleiro, lista_m, lista_p, li, co, la, re, to):
    """
    Esta função move as peças do roque no tabuleiro e atualiza suas posições
    :param tabuleiro: Uma matriz com o tabuleiro
    :param lista_m: Uma lista com as posições das peças
    :param lista_p: Uma lista com as peças
    :param li: A linha em que o rei se encontra
    :param co: A coluna em que o rei se encontra
    :param la: O lado, sendo quais das duas torres
    :param re: O rei
    :param to: A torre
    :return: O tabuleiro e a lista de movimentos atualizados
    """
    i_t = lista_p.index(to)
    i_r = lista_p.index(re)
    if la == INDICE0:
        tabuleiro[li][co - INDICE2] = re
        tabuleiro[li][co - INDICE1] = to
        lista_m[i_t] = "{}{}".format(li + INDICE1, tradLet(co - INDICE1))
        lista_m[i_r] = "{}{}".format(li + INDICE1, tradLet(co - INDICE2))
        tabuleiro[li][co] = "_"
        tabuleiro[li][la] = "_"
    elif la == 7:
        tabuleiro[li][co + INDICE2] = re
        tabuleiro[li][co + INDICE1] = to
        lista_m[i_t + INDICE1] = "{}{}".format(li + INDICE1, tradLet(co + INDICE1))
        lista_m[i_r] = "{}{}".format(li + INDICE1, tradLet(co + INDICE2))
        tabuleiro[li][co] = "_"
        tabuleiro[li][la] = "_"
    return tabuleiro, lista_m


def indentificaCheque(tabuleiro, pos_r, rei, lista_pecas_a, lista_m_a, lista_pecas_o, lista_m_o):
    """
    Esta função identifica se o rei esta em xeque ou em xeque mate
    :param tabuleiro: Uma matriz com o tabuleiro
    :param pos_r: A posição do rei
    :param rei: O rei a ser analisado
    :param lista_pecas_a: Uma lista com as peças aliadas
    :param lista_m_a: Uma lista com as posições das peças aliadas
    :param lista_pecas_o: Uma lista com as peças do oponente
    :param lista_m_o: Uma lista com as posições das peças do oponente
    :return: Uma variável com a palavra XEQUE ou MATE
    """
    m = "MATE"
    Mate = True
    ch = "XEQUE"
    cont_cheque = INDICE0
    li = int(pos_r[INDICE0]) - INDICE1
    co = tradLet((pos_r[INDICE1].lower()))
    cor_o = ""
    lista_cheques = []
    lista_pos_che = []
    if rei == "RE_B":
        cor_o = "P"
    elif rei == "RE_P":
        cor_o = "B"
    pos_p_o = descPos(lista_pecas_o, lista_m_o, "PE_{}".format(cor_o))
    pos_t_o = descPos(lista_pecas_o, lista_m_o, "TO_{}".format(cor_o))
    pos_b_o = descPos(lista_pecas_o, lista_m_o, "BI_{}".format(cor_o))
    pos_ca_o = descPos(lista_pecas_o, lista_m_o, "CA_{}".format(cor_o))
    pos_ra_o = descPos(lista_pecas_o, lista_m_o, "RA_{}".format(cor_o))
    try:
        lista_pe = movPeao(tabuleiro, co, li, rei)
        for mo in pos_p_o:
            if mo in lista_pe:
                cont_cheque += INDICE1
                lista_cheques += lista_pe
                lista_pos_che += pos_p_o
        lista_to = movTorre(tabuleiro, co, li, rei)
        for mo in pos_t_o:
            if mo in lista_to:
                cont_cheque += INDICE1
                lista_cheques += lista_to
                lista_pos_che += pos_t_o
        for mo in pos_ra_o:
            if mo in lista_to:
                cont_cheque += INDICE1
                lista_cheques += lista_to
                lista_pos_che += pos_ra_o
        lista_bi = movBispo(tabuleiro, co, li, rei)
        for mo in pos_b_o:
            if mo in lista_bi:
                cont_cheque += INDICE1
                lista_cheques += lista_bi
                lista_pos_che += pos_b_o
        for mo in pos_ra_o:
            if mo in lista_bi:
                cont_cheque += INDICE1
                lista_cheques += lista_bi
                lista_pos_che += pos_ra_o
        lista_ca = movCavalo(tabuleiro, co, li, rei)
        for mo in pos_ca_o:
            if mo in lista_ca:
                cont_cheque += INDICE1
                lista_cheques += lista_ca
                lista_pos_che += pos_ra_o
        lista_re = movRei(tabuleiro, co, li, rei)
        cont_mate = INDICE0
        if cont_cheque >= INDICE1:
            for casa in lista_re:
                if casa in lista_cheques:
                    cont_mate += INDICE1
            for i in range(len(lista_pecas_a)):
                pos = lista_m_a[i]
                l = int(pos[INDICE0]) - INDICE1
                c = tradLet(pos[INDICE1])
                peca = tabuleiro[l][c]
                if peca != rei:
                    lista_pec_m = movimentos(tabuleiro, c, l, lista_pecas_a[i])
                    for mo in lista_pec_m:
                        if mo in lista_cheques:
                            Mate = False
                else:
                    lista_pec_m = movimentos(tabuleiro, c, l, lista_pecas_a[i])
                    for mo in lista_pec_m:
                        if mo in lista_pos_che:
                            Mate = False
            tam = len(lista_re)
            if cont_mate > INDICE0 and cont_mate == tam and Mate:
                return m
            else:
                return ch
    except TypeError:
        pass


def descPos(lista_p, lista_m, peca):
    """
    Esta função descobre a posição da peça de acordo com a lista de posições
    :param lista_p: Lista de peças aliadas
    :param lista_m: Lista de posições das peças
    :param peca: Peça para descobrir as posições
    :return: Uma lista com as posições das peças
    """
    lista_s = []
    for i in range(len(lista_p)):
        if lista_p[i] == peca:
            lista_s.append(lista_m[i])
    return lista_s


def removPecas(lista_p, lista_m, mov, peca, cor):
    """
    Esta função remove as peças das listas de movimento e peças com base no indice do mov na lista
    :param lista_p: Lista de peças aliadas
    :param lista_m: Lista de posições das peças
    :param mov: A posição
    :param peca: A peça
    :param cor: A cor da peça
    :return: A lista de peças e a lista de movimentos atualizada
    """
    t = "TO_{}".format(cor)
    ca = "CA_{}".format(cor)
    b = "BI_{}".format(cor)
    pe = "PE_{}".format(cor)
    ra = "RA_{}".format(cor)
    i = lista_m.index(mov)
    if peca == t:
        lista_p.pop(i)
        lista_m.pop(i)
    elif peca == ca:
        lista_p.pop(i)
        lista_m.pop(i)
    elif peca == b:
        lista_p.pop(i)
        lista_m.pop(i)
    elif peca == pe:
        lista_p.pop(i)
        lista_m.pop(i)
    elif peca == ra:
        lista_p.pop(i)
        lista_m.pop(i)
    return lista_p, lista_m


def posPecas(lista_m, ent, mov):
    """
    Esta função atualiza a lista de posição
    :param lista_m: Lista de movimento das peças aliadas
    :param ent: A entrada é posição inicial
    :param mov: O movimento é a posição final
    :return: A lista atualizada
    """
    i = lista_m.index(ent)
    lista_m[i] = mov
    return lista_m


def promoPeao(lista_p, lista_m, mov, peca_pro, cor):
    """
    Esta função realiza a promoção do peão, alterando e a peca na lista e no tabuleiro
    :param lista_p: Lista de peças aliadas
    :param lista_m: Lista de posições das peças
    :param mov: Último movimento
    :param peca_pro: A peça escolhida pra a promoção
    :param cor: A cor das peças aliadas
    :return: A peça promovida e a lista de peças atualizada
    """
    pe_p = ""
    if peca_pro == "T":
        pe_p = "TO_{}".format(cor)
    elif peca_pro == "B":
        pe_p = "BI_{}".format(cor)
    elif peca_pro == "C":
        pe_p = "CA_{}".format(cor)
    elif peca_pro == "Q":
        pe_p = "RA_{}".format(cor)
    i_mov = lista_m.index(mov)
    lista_p[i_mov] = pe_p
    return pe_p, lista_p
