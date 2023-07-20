def tabuada(num, n):
    for i in range(1, n+1, 1):
        print('{} * {} = {}'.format(num, i, num*i))


def coletar():
    num = int(input('Informe um número '))
    while(num < 0):
        print('Erro!! Informe um número positivo ')
        num = int(input('Informe um número '))
    return num
