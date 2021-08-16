'''Jogo da Velha. O tabuleiro do jogo é representado por uma matriz
3x3, contendo 3 tipos de caracteres: 'X', 'O' e '-'. O primeiro está associado
ao Jogador 1, o segundo ao Jogador 2 e o último trata-se de um espaço do
tabuleiro ainda não preenchido. O objetivo do jogo é preencher em sequência 3
peças em uma linha, coluna ou diagonal. O jogador que conseguir realizar este
feito primeiro, vence o jogo. Há a possibilidade de o tabuleiro
ser todo preenchido e nenhum dos jogadores conseguir atingir este objetivo,
caracterizando um empate.'''

#Document properties
__author__ = "[Lucas Aquino]"
__copyright__ = "Copyright 2021"
__credits__ = "__author__"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Lucas Aquino" # Reponsável por manter o
                                # programa funcionando
__email__ = "lucasaquinotz@poli.ufrj.br"
__status__ = "Production"

import numpy as np

class Comunicacao:
    def __init__(self: object, jogo: list = [['-','-','-'],['-','-','-',],['-','-','-']], jogadas: int = 0, vitoria: bool = False) -> None:
        '''Método construtor'''
        self. jogo = jogo
        self.jogadas = jogadas
        self.vitoria = vitoria

        return None
        
    def leituraPosicao1(self: object) -> None:
        '''Troca o - pelo X dada as coordenadas'''
        pos1 = list(input('\n''Jogador 1 - escolha uma posição [x,y]:\n'))
        while True:
            try:
                if len(pos1) > 5:
                    raise ValueError
                elif pos1[0] != '[' or pos1[1] not in '012' or pos1[2] != ',' or pos1[3] not in '012' or pos1[4] != ']':
                    raise ValueError
                elif self.jogo[int(pos1[1])][int(pos1[3])] == 'X' or self.jogo[int(pos1[1])][int(pos1[3])] == 'O':
                    raise IndexError
                index = [int(pos1[1]),int(pos1[3])]
                np.delete(self.jogo, index)
            except IndexError:
                log = open('log.txt', 'a+')
                log.write(str.format('IndexError: Jogador 1 (X) tentou preencher uma posição que já possui uma peça: "{}"\n', ''.join(pos1)))
                log.close()
                pos1 = list(input('\n''Posição inválida. Jogador 1 - escolha uma posição [x,y]:\n'))
            except ValueError:
                log = open('log.txt', 'a+')
                log.write(str.format('ValueError: Jogador 1 (X) tentou preencher uma posição com um formato diferente de [x,y] sendo x e y de 0 a 2: "{}"\n', ''.join(pos1)))
                log.close()
                pos1 = list(input('\n''Jogador 1 - escolha uma posição no formato [x,y] com x e y de 0 a 2:\n'))
            else:
                np.insert(self.jogo[int(pos1[1])],int(pos1[3]),'X')
                historico = open('historico.txt', 'a+')
                historico.write(str.format('Jogador 1 (X) preencheu a posição: {}\n',''.join(pos1)))
                historico.close()
                break
            
        return None

    def leituraPosicao2(self: object) -> None:
        pos2 = list(input('\n''Jogador 2 - escolha uma posição [x,y]:\n'))
        while True:
            try:
                if len(pos2) > 5:
                    raise ValueError
                elif pos2[0] != '[' or pos2[1] not in '012' or pos2[2] != ',' or pos2[3] not in '012' or pos2[4] != ']':
                    raise ValueError
                elif self.jogo[int(pos2[1])][int(pos2[3])] == 'X' or self.jogo[int(pos2[1])][int(pos2[3])] == 'O':
                    raise IndexError
                del self.jogo[int(pos2[1])][int(pos2[3])]
            except IndexError:
                log = open('log.txt', 'a+')
                log.write(str.format('IndexError: Jogador 2 (O) tentou preencher uma posição que já possui uma peça: "{}"\n', ''.join(pos2)))
                log.close()
                pos2 = list(input('\n''Posição inválida. Jogador 2 - escolha uma posição [x,y]:\n'))
            except ValueError:
                log = open('log.txt', 'a+')
                log.write(str.format('ValueError: Jogador 2 (O) tentou preencher uma posição com um formato diferente de [x,y] sendo x e y de 0 a 2: "{}"\n', ''.join(pos2)))
                log.close()
                pos2 = list(input('\n''Jogador 2 - escolha uma posição no formato [x,y] com x e y de 0 a 2:\n'))
            else:
                list.insert(self.jogo)
                historico = open('historico.txt', 'a+')
                historico.write(str.format('Jogador 2 (O) preencheu a posição: {}\n',''.join(pos2)))
                historico.close()
                break

        return None
    
    def resultado(self: object) -> None:
        '''Verifica no caso de um vencedor quem ganhou e verifica se querem jogar novamente'''
        if self.vitoria == True and self.jogadas%2 == 1:
            '''Verifica se o foi o jogador 1 (X) o ganhador'''
            historico = open('historico.txt', 'a+')
            historico.write('Jogador 1 (X) ganhou\n')
            historico.close()
            jogar = input('\n''Jogador 1 venceu o jogo. Deseja iniciar uma nova partida?''\n')        
            while True:
                try:
                    if jogar != 'S' and jogar != 'N':
                        raise TypeError
                except TypeError:
                    log = open('log.txt', 'a+')
                    log.write(str.format('TypeError: Usuário digitou um caractere inválido: "{}"\n', jogar))
                    log.close()
                    jogar = input('\n''Comando inválido. Deseja iniciar uma nova partida? (S ou N)''\n')
                else:
                    if jogar == 'S':
                        historico = open('historico.txt', 'a+')
                        historico.write('Usuário digitou "S" e um novo jogo foi iniciado\n')
                        historico.close()
                        JogoDaVelha.main()
                    elif jogar == 'N':
                        historico = open('historico.txt', 'a+')
                        historico.write('Usuário digitou "N" e o programa foi encerrado\n')
                        historico.close()
                        return None
                        break
        elif  self.vitoria == True and self.jogadas%2 == 0:
            '''Verifica se foi o jogador 2 (O) o ganhador'''
            historico = open('historico.txt', 'a+')
            historico.write('Jogador 2 (O) ganhou\n')
            historico.close()
            jogar = input('\n''Jogador 2 venceu o jogo. Deseja iniciar uma nova partida?''\n')
            while True:
                try:
                    if jogar != 'S' and jogar != 'N':
                        raise TypeError
                except TypeError:
                    log = open('log.txt', 'a+')
                    log.write(str.format('TypeError: Usuário digitou um caractere inválido: "{}"\n', jogar))
                    log.close()
                    jogar = input('\n''Comando inválido. Deseja iniciar uma nova partida? (S ou N)''\n')
                else:
                    if jogar == 'S':
                        historico = open('historico.txt', 'a+')
                        historico.write('Usuário digitou "S" e um novo jogo foi iniciado\n')
                        historico.close()
                        JogoDaVelha.main()
                    elif jogar == 'N':
                        historico = open('historico.txt', 'a+')
                        historico.write('Usuário digitou "N" e o programa foi encerrado\n')
                        historico.close()
                        return None
                        break
        elif self.jogadas == 9:
            historico = open('historico.txt', 'a+')
            historico.write('O jogo terminou em empate\n')
            historico.close()
            jogar = input('\n''Empate . Deseja iniciar uma nova partida?''\n')
            while True:
                try:
                    if jogar != 'S' and jogar != 'N':
                        raise TypeError
                except TypeError:
                    log = open('log.txt', 'a+')
                    log.write(str.format('TypeError: Usuário digitou um caractere inválido: "{}"\n', jogar))
                    log.close()
                    jogar = input('\n''Comando inválido. Deseja iniciar uma nova partida? (S ou N)''\n')
                else:
                    if jogar == 'S':
                        historico = open('historico.txt', 'a+')
                        historico.write('Usuário digitou "S" e um novo jogo foi iniciado\n')
                        historico.close()
                        JogoDaVelha.main()
                    elif jogar == 'N':
                        historico = open('historico.txt', 'a+')
                        historico.write('Usuário digitou "N" e o programa foi encerrado\n')
                        historico.close()
                        return None
                        break
                    
class Funcionamento:
    def __init__(self: object, jogo: list = [['-','-','-'],['-','-','-',],['-','-','-']], jogadas: int = 0, vitoria: bool = False) -> None:
        '''Método construtor'''
        self. jogo = jogo
        self.jogadas = jogadas
        self.vitoria = vitoria

        return None
        
    def interface(self: object) -> None:
        '''Imprime a matriz'''
        for linha in self.jogo:
                print('')
                for elemento in linha:
                    print(str.format('{}',elemento),end=' ')
        return None
                    
    def condicaoDeVitoria(self: object) -> bool:
        '''Verifica se houve algum vencedor, retornando True pra caso haja e False pra caso contrário'''
        figuras = ['X','O']
        for f in figuras:
            if self.vitoria == False:
                '''Verifica a vitória nas linha (3 iguais na horizontal)'''
                lin = 0
                col = 0
                while lin < 3 and self.vitoria == False:
                    soma = 0
                    col = 0
                    while col < 3:
                        if self.jogo[lin][col] == f:
                            soma += 1
                        col += 1
                    lin += 1
                    if soma == 3:
                        self.vitoria = True
                '''Verifica a vitória nas colunas (3 iguais na vertical)'''
                lin = 0
                col = 0
                while col < 3 and self.vitoria == False:
                    soma = 0
                    lin = 0
                    while lin < 3:
                        if self.jogo[lin][col] == f:
                            soma += 1
                        lin += 1
                    col += 1
                    if soma == 3:
                        self.vitoria = True
                '''Verifica a primeira diagonal'''
                soma = 0
                lin = 0
                col = 2
                while lin < 3 and self.vitoria == False:
                    if self.jogo[lin][col] == f:
                        soma += 1
                    lin += 1
                    col -= 1
                if soma == 3:
                    self.vitoria = True
                '''Verifica a segunda diagonal'''
                soma = 0
                diag = 0
                while diag < 3 and self.vitoria == False:
                    if self.jogo[diag][diag] == f:
                        soma += 1
                    diag += 1
                if soma == 3:
                    self.vitoria = True
        return self.vitoria
        
class JogoDaVelha(Comunicacao, Funcionamento):
    def __init__(self: object, jogo : list = [['-','-','-'],['-','-','-',],['-','-','-']], jogadas: int = 0, vitoria: bool = False) -> None:
        '''Método construtor'''
        Comunicacao.__init__(self, jogo, jogadas, vitoria)
        Funcionamento.__init__(self, jogo, jogadas, vitoria)
        self.__atributos = {'jogo','jogadas','vitoria', 'dicionario'}
        self.__metodos = {
            'leituraPosicao1', 'leituraPosicao2', 'resultado', 'interface',
            'condicaoDeVitoria', 'getAtributos', 'getMetodos'
            }
        
        return None

    def manualUsuario(self: object) -> dict:
        '''Retorna um dicionário contendo todos os métodos e atributos e suas respectivas funcionalidades'''
        dicionario = {
            'jogo':'(list) Tabuleiro do jogo',
            'jogadas':'(int) Número de jogadas',
            'vitoria':'(bool) Representa se houve um vencedor. True = Houve vencedor e False = Ainda não houve um vencedor',
            'atributos':'(set) Armazena todos os atributos utilizados pelas classes do programa',
            'metodos':'(set) Armazena todos os métodos utilizados pelas classes do programa',
            'dicionario':'(dict) Armazena um dicionario contendo todos os métodos e atributos e suas respectivas funcionalidades'
            }
        for i in self.__metodos:
            dicionario[i] = eval('self.%s.__doc__'%i)
        return dicionario

    def getAtributos(self: object) -> set:
        '''Retorna o nome de todos os atributos'''
        return self.__atributos

    def getMetodos(self: object) -> set:
        '''Retorna o nome de todos os métodos'''
        return self.__metodos

    def __str__(self: object):
        output = ''
        dicio = self.manualUsuario()
        for chave, valor in dicio.items():
            output += str.format('{}:{}\n',chave, valor)
        return output

    def main():
        '''Função Principal'''
        jogo = JogoDaVelha(np.array([['-','-','-'],['-','-','-',],['-','-','-']]))
        jogo.interface()
        while jogo.jogadas < 9 and jogo.vitoria == False:
            jogo.leituraPosicao1()
            jogo.jogadas += 1
            jogo.condicaoDeVitoria()
            '''Verifica se o jogador 1 ganhou'''
            jogo.interface()
            if jogo.jogadas < 9 and jogo.vitoria == False:
                jogo.leituraPosicao2()
                jogo.jogadas += 1
                jogo.condicaoDeVitoria()
                '''Verifica se o jogador 2 ganhou'''
                jogo.interface()
        jogo.resultado()
        '''Verifica o resultado'''
    
if __name__ == '__main__':
   JogoDaVelha.main()
