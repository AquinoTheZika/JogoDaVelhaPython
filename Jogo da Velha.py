def jogoDaVelha():
    jogo = [['-','-','-'],['-','-','-',],['-','-','-']]
    jogadas = 0
    vitoria = False
    interface(jogo)
    while jogadas < 9 and condicaoDeVitoria(jogo,vitoria,jogadas) != False:
        leituraPosicao1(jogo)
        '''Troca o - pelo X '''
        jogadas = jogadas + 1
        condicaoDeVitoria(jogo,vitoria,jogadas)
        '''Verifica se o jogador 1 ganhou'''
        interface(jogo)
        if jogadas < 9 and condicaoDeVitoria(jogo,vitoria,jogadas) != False:
            leituraPosicao2(jogo)
            '''Troca o - pelo O '''
            jogadas = jogadas + 1
            condicaoDeVitoria(jogo,vitoria,jogadas)
            '''Verifica se o jogador 2 ganhou'''
            interface(jogo)
    resultado(jogadas,jogo,vitoria)
    '''Verifica o resultado'''
def interface(jogo):
    '''Imprime a matriz'''
    for linha in jogo:
            print('')
            for elemento in linha:
                print(str.format('{}',elemento),end=' ')
    
def condicaoDeVitoria(jogo,vitoria,jogadas):
    '''Verifica se houve algum ganhador'''
    figuras = ['X','O']
    for f in figuras:
        if vitoria == False:
            '''Verifica a vitória nas linha (3 iguais na horizontal)'''
            lin = 0
            col = 0
            while lin < 3 and vitoria == False:
                soma = 0
                col = 0
                while col < 3:
                    if jogo[lin][col] == f:
                        soma = soma + 1
                    col = col + 1
                lin = lin + 1
                if soma == 3:
                    vitoria = True
            '''Verifica a vitória nas colunas (3 iguais na vertical)'''
            lin = 0
            col = 0
            while col < 3 and vitoria == False:
                soma = 0
                lin = 0
                while lin < 3:
                    if jogo[lin][col] == f:
                        soma = soma + 1
                    lin = lin + 1
                col = col + 1
                if soma == 3:
                    vitoria = True
            '''Verifica a primeira diagonal'''
            soma = 0
            lin = 0
            col = 2
            while lin < 3 and vitoria == False:
                if jogo[lin][col] == f:
                    soma = soma + 1
                lin = lin + 1
                col = col - 1
            if soma == 3:
                vitoria = True
            '''Verifica a segunda diagonal'''
            soma = 0
            diag = 0
            while diag < 3 and vitoria == False:
                if jogo[diag][diag] == f:
                    soma = soma + 1
                diag = diag + 1
            if soma == 3:
                vitoria = True
            if vitoria == True:
                return False
def leituraPosicao1(jogo):
    '''Troca o - pelo X dada as coordenadas e  verifica se o espaço esta vazio e se as coordenadas são válidas '''
    pos1 = list(input('\n''Jogador 1 - escolha uma posição [x,y]:\n'))
    while pos1[0] != '[' or pos1[1] not in '012' or pos1[2] != ',' or pos1[3] not in '012' or pos1[4] != ']':
        pos1 = list(input('\n''Posição inválida. Jogador 1 - escolha uma posição [x,y]:\n'))
    while jogo[int(pos1[1])][int(pos1[3])] == 'X' or jogo[int(pos1[1])][int(pos1[3])] == 'O':
        pos1 = list(input('\n''Posição inválida. Jogador 1 - escolha uma posição [x,y]:\n'))
    del jogo[int(pos1[1])][int(pos1[3])]
    list.insert(jogo[int(pos1[1])],int(pos1[3]),'X')

def leituraPosicao2(jogo):
    '''Troca o - pelo O dada as coordenadas e  verifica se o espaço esta vazio e se as coordenadas são válidas '''
    pos2 = list(input('\n''Jogador 2 - escolha uma posição [x,y]:\n'))
    while pos2[0] != '[' or pos2[1] not in '012' or pos2[2] != ',' or pos2[3] not in '012' or pos2[4] != ']':
        pos2 = list(input('\n''Posição inválida. Jogador 2 - escolha uma posição [x,y]:\n'))
    while jogo[int(pos2[1])][int(pos2[3])] == 'X' or jogo[int(pos2[1])][int(pos2[3])] == 'O':
        pos2 = list(input('\n''Posição inválida. Jogador 2 - escolha uma posição [x,y]:\n'))
    del jogo[int(pos2[1])][int(pos2[3])]
    list.insert(jogo[int(pos2[1])],int(pos2[3]),'O')

def resultado(jogadas,jogo,vitoria):
    if condicaoDeVitoria(jogo,vitoria,jogadas) == False and jogadas%2 == 1:
        '''verifica se foi o jogador 1 (X) o ganhador'''
        jogar = input('\n''Jogador 1 venceu o jogo. Deseja iniciar uma nova partida?''\n')
        while jogar != 'S' and jogar != 'N':
            jogar = input('\n''Comando inválido. Deseja iniciar uma nova partida?''\n')
        if jogar == 'S':
            jogoDaVelha()
        elif jogar == 'N':
            return None
    elif  condicaoDeVitoria(jogo,vitoria,jogadas) == False and jogadas%2 == 0:
        '''verifica se foi o jogador 2 (O) o ganhador'''
        jogar = input('\n''Jogador 2 venceu o jogo. Deseja iniciar uma nova partida?''\n')
        while jogar != 'S' and jogar != 'N':
            jogar = input('\n''Comando inválido. Deseja iniciar uma nova partida?''\n')
            if jogar == 'S':
                jogoDaVelha()
            elif jogar == 'N':
                return None
    elif jogadas == 9:
        jogar = input('\n''Empate . Deseja iniciar uma nova partida?''\n')
        while jogar != 'S' and jogar != 'N':
            jogar = input('\n''Comando inválido. Deseja iniciar uma nova partida?''\n')
        if jogar == 'S':
            jogoDaVelha()
        elif jogar == 'N':
            return None
