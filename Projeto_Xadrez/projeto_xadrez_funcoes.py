"""
Neste módulo se encontram as funções usadas
para o funcionamento do Xadrez.
O módulo de interface com o usuário as utiliza para:
- Colocar as peças nos lugares corretos para o ínico da partida.
- Mostrar ao usuário quais são os movimentos possíveis
"""
from CONS import *


def montar_tabuleiro():
    """
    Esta função monta o tabuleiro de xadrez em forma de matriz de tamanho QTD_L x QTD_C
    :return: Um tauleiro como matriz
    """
    tabuleiro = []
    for x in range(INDICE0, INDICE7 + INDICE1):  # indice da linha
        linha = []
        for y in range(INDICE0, INDICE7 + INDICE1):  # indice da coluna
            linha.append("{},{}".format(x, y))
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
            elif b == INDICE0 and a == "CA_B":
                tabuleiro[b] = pecas_lugar(tabuleiro, b, INDICE_CAVALO_E, INDICE_CAVALO_D, a)
            elif b == INDICE0 and a == "BI_B":
                tabuleiro[b] = pecas_lugar(tabuleiro, b, INDICE_BISPO_E, INDICE_BISPO_D, a)
            elif b == INDICE0 and a == "RA_B":
                tabuleiro[b] = rei_rainha_lugar(tabuleiro, b, INDICE_REI, a)
            elif b == INDICE0 and a == "RE_B":
                tabuleiro[b] = rei_rainha_lugar(tabuleiro, b, INDICE_RAINHA, a)
    for a in PECAS_P:
        for b in range(len(tabuleiro)):
            if b == P2_PEAO and a == "PE_P":
                tabuleiro[b] = peoes_lugar(QTD_C, a)
            elif b == INDICE7 and a == "TO_P":
                tabuleiro[b] = pecas_lugar(tabuleiro, b, INDICE_TORRE_E, INDICE_TORRE_D, a)
            elif b == INDICE7 and a == "CA_P":
                tabuleiro[b] = pecas_lugar(tabuleiro, b, INDICE_CAVALO_E, INDICE_CAVALO_D, a)
            elif b == INDICE7 and a == "BI_P":
                tabuleiro[b] = pecas_lugar(tabuleiro, b, INDICE_BISPO_E, INDICE_BISPO_D, a)
            elif b == INDICE7 and a == "RE_P":
                tabuleiro[b] = rei_rainha_lugar(tabuleiro, b, INDICE_REI, a)
            elif b == INDICE7 and a == "RA_P":
                tabuleiro[b] = rei_rainha_lugar(tabuleiro, b, INDICE_RAINHA, a)
    return tabuleiro


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
    if peca == "PE_B":
        if li == 1:
            lista_m.append(tabuleiro[LINHA_PEAO_2][co])
            lista_m.append(tabuleiro[LINHA_PEAO_3][co])
        elif tabuleiro[li + 1][co] not in PECAS_P and tabuleiro[li + 1][co] not in PECAS_B:
            lista_m.append(tabuleiro[li + 1][co])
        if co != 7 and tabuleiro[li + 1][co + 1] in PECAS_P:
            lista_m.append(tabuleiro[li + 1][co + 1])
        if co != 0 and tabuleiro[li + 1][co - 1] in PECAS_P:
            lista_m.append(tabuleiro[li + 1][co - 1])
    if peca == "PE_P":
        if li == 6:
            lista_m.append(tabuleiro[LINHA_PEAO_4][co])
            lista_m.append(tabuleiro[LINHA_PEAO_5][co])
        elif tabuleiro[li - 1][co] not in PECAS_P and tabuleiro[li - 1][co] not in PECAS_B:
            lista_m.append(tabuleiro[li - 1][co])
        if co != 7 and tabuleiro[li - 1][co + 1] in PECAS_B:
            lista_m.append(tabuleiro[li - 1][co + 1])
        if co != 0 and tabuleiro[li - 1][co - 1] in PECAS_B:
            lista_m.append(tabuleiro[li - 1][co - 1])
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
    for a in range(co + 1, INDICE7 + 1):
        casa = tabuleiro[li][a]
        if casa in aliados:
            break
        if casa not in aliados:
            lista_m.append(casa)
            if casa in oponente:
                break
    for b in range(co - 1, INDICE0 - 1, -1):
        casa = tabuleiro[li][b]
        if casa in aliados:
            break
        if casa not in aliados:
            lista_m.append(casa)
            if casa in oponente:
                break
    for c in range(li + 1, INDICE7 + 1):
        casa = tabuleiro[c][co]
        if casa in aliados:
            break
        if casa not in aliados:
            lista_m.append(casa)
            if casa in oponente:
                break
    for d in range(li - 1, INDICE0 - 1, -1):
        casa = tabuleiro[d][co]
        if casa in aliados:
            break
        if casa not in aliados:
            lista_m.append(casa)
            if casa in oponente:
                break
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
        for a in range(li - 1, -1, -1):
            if co_e == LIMITE_CO_D:
                break
            co_d += 1
            casa = tabuleiro[a][co_d]
            if casa in aliados:
                break
            if casa not in aliados:
                lista_m.append(tabuleiro[a][co_d])
                if casa in oponente or co_d == LIMITE_CO_D:
                    break
        for b in range(li - 1, -1, -1):
            if co_e == LIMITE_CO_E:
                break
            co_e -= 1
            casa = tabuleiro[b][co_e]
            if casa in aliados:
                break
            if casa not in aliados:
                lista_m.append(tabuleiro[b][co_e])
                if casa in oponente:
                    break
    if li != INDICE7:  # Essa condição é utilizada caso o bispo não esteja na linha 7 do tabuleiro
        for c in range(li + 1, 7+1):
            if co_e_b == LIMITE_CO_E:
                break
            co_e_b -= 1
            casa = tabuleiro[c][co_e_b]
            if casa in aliados:
                break
            if casa not in aliados:
                lista_m.append(tabuleiro[c][co_e_b])
                if casa in oponente:
                    break
        for d in range(li + 1, 7+1):
            if co_d_b == LIMITE_CO_D:
                break
            co_d_b += 1
            casa = tabuleiro[d][co_d_b]
            if casa in aliados:
                break
            if casa not in aliados:
                lista_m.append(tabuleiro[d][co_d_b])
                if casa in oponente:
                    break
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
    if peca == "RE_B":
        aliados = PECAS_B
    elif peca == "RE_P":
        aliados = PECAS_P
    if li != INDICE7 and tabuleiro[li + 1][co] not in aliados:
        lista_m.append(tabuleiro[li + 1][co])
    if li != INDICE0 and tabuleiro[li - 1][co] not in aliados:
        lista_m.append(tabuleiro[li - 1][co])
    if co != INDICE7 and tabuleiro[li][co + 1] not in aliados:
        lista_m.append(tabuleiro[li][co + 1])
    if co != INDICE0 and tabuleiro[li][co - 1] not in aliados:
        lista_m.append(tabuleiro[li][co - 1])
    if li != INDICE7 and co != INDICE7 and tabuleiro[li + 1][co + 1] not in aliados:
        lista_m.append(tabuleiro[li + 1][co + 1])
    if li != INDICE7 and co != INDICE0 and tabuleiro[li + 1][co - 1] not in aliados:
        lista_m.append(tabuleiro[li + 1][co - 1])
    if li != INDICE0 and co != INDICE7 and tabuleiro[li - 1][co + 1] not in aliados:
        lista_m.append(tabuleiro[li - 1][co + 1])
    if li != INDICE0 and co != INDICE0 and tabuleiro[li - 1][co - 1] not in aliados:
        lista_m.append(tabuleiro[li - 1][co - 1])
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
    if peca == "CA_B":
        aliados = PECAS_B
    else:
        aliados = PECAS_P
    if li + INDICE2 <= INDICE7 and co + INDICE1 <= INDICE7:
        if tabuleiro[li + INDICE2][co + INDICE1] in tabuleiro[li + INDICE2] and tabuleiro[li + INDICE2][
            co + INDICE1] not in aliados:
            lista_m.append(tabuleiro[li + INDICE2][co + INDICE1])
    if co - INDICE1 >= INDICE0 and li + INDICE2 <= INDICE7:
        if tabuleiro[li + INDICE2][co - INDICE1] in tabuleiro[li + INDICE2] and tabuleiro[li + INDICE2][
            co - INDICE1] not in aliados:
            lista_m.append(tabuleiro[li + INDICE2][co - INDICE1])
    if co - INDICE2 >= INDICE0 and li + INDICE1 <= INDICE7:
        if tabuleiro[li + INDICE1][co - INDICE2] in tabuleiro[li + INDICE1] and tabuleiro[li + INDICE1][
            co - INDICE2] not in aliados:
            lista_m.append(tabuleiro[li + INDICE1][co - INDICE2])
    if li + INDICE1 <= INDICE7 and co + INDICE2 <= INDICE7:
        if tabuleiro[li + INDICE1][co + INDICE2] in tabuleiro[li + INDICE1] and tabuleiro[li + INDICE1][
            co + INDICE2] not in aliados:
            lista_m.append(tabuleiro[li + INDICE1][co + INDICE2])
    if li - INDICE1 >= INDICE0 and co + INDICE2 <= INDICE7:
        if tabuleiro[li - INDICE1][co + INDICE2] in tabuleiro[li - INDICE1] and tabuleiro[li - INDICE1][
            co + INDICE2] not in aliados:
            lista_m.append(tabuleiro[li - INDICE1][co + INDICE2])
    if li - INDICE1 >= INDICE0 and co - INDICE2 >= INDICE0:
        if tabuleiro[li - INDICE1][co - INDICE2] in tabuleiro[li - INDICE1] and tabuleiro[li - INDICE1][
            co - INDICE2] not in aliados:
            lista_m.append(tabuleiro[li - INDICE1][co - INDICE2])
    if li - INDICE2 >= INDICE0 and co - INDICE1 >= INDICE0:
        if tabuleiro[li - INDICE2][co - INDICE1] in tabuleiro[li - INDICE2] and tabuleiro[li - INDICE2][
            co - INDICE1] not in aliados:
            lista_m.append(tabuleiro[li - INDICE2][co - INDICE1])
    if li - INDICE2 >= INDICE0 and co + INDICE1 <= INDICE7:
        if tabuleiro[li - INDICE2][co + INDICE1] in tabuleiro[li - INDICE2] and tabuleiro[li - INDICE2][
            co + INDICE1] not in aliados:
            lista_m.append(tabuleiro[li - INDICE2][co + INDICE1])
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
    tabuleiro[li_m][co_m] = peca
    tabuleiro[li][co] = "{},{}".format(li, co)
    return tabuleiro


def roqueCasV(tabuleiro, li, co, la):
    mensagem = True
    if la == 0:
        for a in range(co - 1, 0, -1):
            casa = tabuleiro[li][a]
            if casa in PECAS_B or casa in PECAS_P:
                break
            elif a == 1:
                return mensagem
    elif la == 7:
        for a in range(co + 1, 7):
            casa = tabuleiro[li][a]
            if casa in PECAS_B or casa in PECAS_P:
                break
            elif a == 6:
                return mensagem


def roqueMov(tabuleiro, li, co, la, re, to):
    if la == 0:
        tabuleiro[li][co - 2] = re
        tabuleiro[li][co - 1] = to
        tabuleiro[li][co] = "{},{}".format(li, co)
        tabuleiro[li][la] = "{},{}".format(li, la)
    elif la == 7:
        tabuleiro[li][co + 2] = re
        tabuleiro[li][co + 1] = to
        tabuleiro[li][co] = "{},{}".format(li, co)
        tabuleiro[li][la] = "{},{}".format(li, la)
    return tabuleiro


def indentificaCheque(tabuleiro, li_f, co_f, peca, rei):
    cheque = False
    lista = movimentos(tabuleiro, co_f, li_f, peca)
    if rei in lista:
        cheque = True
    return cheque

