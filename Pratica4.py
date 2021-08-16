def SIGA (nome, n1, n2, n3):
    '''Calcula a média do aluno e retorna a média com uma casa decimal
    e a situação do aluno (aprovado ou reprovado);
    tupla (string, float, float, float) -> tupla (string, float)'''
    media = round((n1 + n2 + n3)/3,1)
    if media >= 7:
        return nome, media,'Aprovado', 'Parabéns!'
    elif media >= 5:
        return nome, media,'Aprovado'
    else:
        return nome, media,'Reprovado'

def quadrante(angulo,RadOuGraus):
    '''Dado um ângulo qualquer e um booleano indicando se o ângulo está em
    Graus (True) ou Radianos (False), retorna um inteiro entre 1 e 4
    que represente em qual quadrante este ângulo se encontra;
    tupla (float, bool) -> int'''
    if RadOuGraus == True and angulo <0:
        angulo = 360 + angulo
    if RadOuGraus == False and angulo <0:
        angulo = 2 + angulo
    if RadOuGraus == True and angulo <= 360:
        if angulo <= 90 and angulo >= 0 or angulo == 360:
            return 1
        elif angulo > 90 and angulo <= 180:
            return 2
        elif angulo > 180 and angulo <= 270:
            return 3
        elif angulo > 270 and angulo < 360:
            return 4
    elif RadOuGraus == True and angulo > 360:
        if angulo%360 <= 90:
            return 1
        elif angulo%360 > 90 and angulo%360 <= 180:
            return 2
        elif angulo%360 > 180 and angulo%360 <= 270:
            return 3
        elif angulo%360 > 270 and angulo%360 < 360:
            return 4
    elif RadOuGraus == False and angulo <= 2:
        if angulo <= 0.5 and angulo >= 0 or angulo == 2:
            return 1
        elif angulo > 0.5 and angulo <= 1:
            return 2
        elif angulo > 1 and angulo <= 1.5:
            return 3
        elif angulo > 1.5 and angulo < 2:
            return 4
    else:
        if angulo%2 <= 0.5:
            return 1
        elif angulo%2 > 0.5 and angulo%2 <= 1:
            return 2
        elif angulo%2 > 1 and angulo%2 <= 1.5:
            return 3
        elif angulo%2 > 1.5 and angulo%2 < 2:
            return 4
    
        
