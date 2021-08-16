import math
print(max(3,2.8,3.9))
print(min(7,2,4,1,0))

def media(n1,n2,n3):
    '''calcula a média de 3 números inteiros.'''
    return (n1 + n2 + n3)/3

def diferenca(n1,n2,n3):
    '''calcula a diferença entre o maior número e a média.'''
    return max(n1,n2,n3) - media(n1,n2,n3)

def soma (n1,n2,n3):
    '''calcula a soma do menor número com a média.'''
    return min(n1,n2,n3) + media(n1,n2,n3)

def delta (a,b,c):
    '''calcula o delta(discriminante) de um
    polinômio do 2º grau dado a, b e c.'''
    return b**2 - 4*a*c

def raiz_Real1 (a,b,c):
    '''calcula a primeira raiz real de uma
    equação do 2º grau, dados seus coeficientes a, b e c.'''
    return (-b + math.sqrt(delta(a,b,c)))/(2*a)

def raiz_Real2 (a,b,c):
    '''calcula a segunda raiz real de uma
    equação do 2º grau, dados seus coeficientes a, b e c.'''
    return (-b - math.sqrt(delta(a,b,c)))/(2*a)

def NumeroDeTermos(A1,An,r):
    '''calcula o ńumero de termos dados os
    valores inicial e final e a raz̃ao.'''
    return (An + r - A1)/r

def SomaPA(A1,An,r):
    '''calcula a soma da PA dados os valores
    inicial, final e a razão.'''
    return (NumeroDeTermos(A1,An,r)*(A1 + An))/2

def hipotenusa(cat1,cat2):
    '''calcula a hipotenusa de um triângulo retângulo dados os catetos.'''
    return math.hypot(cat1, cat2)

def distância_2pontos(X1,Y1,X2,Y2):
    '''calcule a distˆancia entre dois pontos em um plano
    dadas suas coordenadas.'''
    return math.hypot(X1-X2,Y1-Y2)

def perímetro_Triângulo(cat1, cat2):
    '''calcula o perímetro de um triângulo reto dados os catetos.'''
    return hipotenusa(cat1,cat2) + cat1 + cat2

def soma_sen_cos(x):
    '''calcula a soma do quadrado do seno com o
    quadrado do cosseno de um ângulo.'''
    return math.sin(x)**2 + math.cos(x)**2

def comprimento_círculo(r):
    '''calcula o comprimento do c ́ırculo dado o raio.'''
    return 2 * math.pi * r
    
def areaSetorCircular(raio,ang=360):
    '''́calcula a área de um setor circular,
    dados o raio e o ângulo. Caso o valor do ângulo não seja passado
    ele será igual ao círculo inteiro (360º).'''
    return (ang * 3.14 * raio**2)/360 
