def j():
    jogo = [['-','-','-'],['-','-','-',],['-','-','-']]
    jogadas = 0
    for elemento in jogo:
        print(str.format('{:.2f}',i, end='\t')
    pos1 = list(input('Jogador 1 - escolha uma posição [x,y]:\n'))
    del jogo[int(pos1[1])][int(pos1[3])]
    list.insert(jogo[int(pos1[1])],int(pos1[3]),'X')
    pos2 = list(input('Jogador 2 - escolha uma posição [x,y]:\n'))
    del jogo[int(pos2[1])][int(pos2[3])]
    list.insert(jogo[int(pos2[1])],int(pos2[3]),'O')
