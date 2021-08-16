import math
def absoluto (num):
    '''Retorna o valor absoluto de um número
    inteiro ou decimal, positivo ou negativo(num); float'''
    if num > 0:
        return num
    else:
        return -num
def f(x):
    ''' Funcao teste para questao 2
    float->float'''
    return x**3 - 4*x

def f_tem_Raiz(a,b):
    '''informa se uma raiz em um intervalo entre 'a' e 'b' em uma função predefinida;
    float -> string'''
    if (f(a) > 0 and f(b)< 0) or (f(a) < 0 and f(b) > 0):
        return 'TEM RAIZ'
    else:
        return 'INCONCLUSIVO'

def delta (a,b,c):
    '''calcula o delta(discriminante) de um
    polinômio do 2º grau dado a, b e c.'''
    return b**2 - 4*a*c

def raiz_Real1 (a,b,c):
    '''calcula a primeira raiz real de uma
    equação do 2º grau, dados seus coeficientes a, b e c;
    float, float, float -> float'''
    return (-b + math.sqrt(delta(a,b,c)))/(2*a)

def raiz_Real2 (a,b,c):
    '''calcula a segunda raiz real de uma
    equação do 2º grau, dados seus coeficientes a, b e c.
    float, float, float -> float'''
    return (-b - math.sqrt(delta(a,b,c)))/(2*a)

def num_Raizes (a,b,c):
    '''calcula o número de raízes reais de uma
    equação do 2º grau, dados seus coeficientes a, b e c.
    float, float, float -> int'''
    if delta (a,b,c) < 0:
        return 0
    elif raiz_Real1 (a,b,c) == raiz_Real2 (a,b,c):
        return 1
    else:
        return 2

def spam (frase , n):
    '''recebe como entrada um texto e o número n de repetições
    desejado e retorne uma sequência de caracteres composta por
    n repetições deste texto; string, int -> string'''
    return (frase + ' ')* n

def data (dia, mes, ano):
    '''recebe como entrada três números inteiros de até 2 dígitos
    representando, respectivamente, dia, mês e ano e retorna
    uma sequência de caracteres com estas informações formatadas
    no padrão usual de notação de datas: "DD/MM/AAAA";
    int, int, int -> string '''
    if dia > 31 or mes > 12:
        return 'data inválida'
    elif dia < 10 and mes < 10:
        return f'0{dia}/0{mes}/20{ano}'
    elif dia < 10:
        return f'0{dia}/{mes}/20{ano}'
    elif mes < 10:
        return f'{dia}/0{mes}/20{ano}'
    else:
        return f'{dia}/{mes}/20{ano}'

def INSS (bruto):
    '''calcula o valor do INSS dado o salário bruto;
    float -> float'''
    if bruto <= 2000:
        return 0.06 * bruto
    elif bruto <= 3000:
        return 0.08 * bruto
    else:
        return 0.1 * bruto

def IR (bruto):
    '''calcula o valor do Imposto de Renda dado o salário bruto;
    float -> float'''
    if bruto <= 2500:
        return 0.11 * bruto
    elif bruto <= 5000:
        return 0.15 * bruto
    else:
        return 0.22 * bruto

def liq (bruto):
    '''calcula o valor do salário líquido dado o salário bruto;
    float -> float'''
    return bruto - (IR(bruto) + INSS(bruto))
