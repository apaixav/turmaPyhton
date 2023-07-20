def coletarPositivoInteiro():
    num = int(input())
    while(num <= 0):
        print('Erro!! Informe um valor positivo')
        num= int(input('Informe um número: '))
        return num

def transformarPercentual(num, total):
    percentual= (total/num)*100
    return percentual


def eleitores():
    print('informe o total de votos nulos: ')
    n = coletarPositivoInteiro()
    print('informe o total de votos válidos: ')
    v = coletarPositivoInteiro()
    print('informe o total de votos brancos: ')
    b = coletarPositivoInteiro()
    print('informe o total de eleitores: ')
    x = coletarPositivoInteiro()

    if(n+v+b) == x:

        pb = transformarPercentual(b, x)
        pn = transformarPercentual(n, x)
        pv = transformarPercentual(v, x)

        return 'Votos Brancos: {}\nVotos Nulos: {}\nVotos Válidos: {}'.format(pb, pn, pv)
    else:
        return'Número de brancos, válidos e nulos é diferente do total de eleitores'
