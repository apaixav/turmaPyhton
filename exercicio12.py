def vinteInteiro():
    soma = 0
    num = 1
    i = 0
    negativo = 0
    while( i < 20):
        num =int(input('Informe um número: '))
        if(num > 0):
            soma += num

        if(num < 0):
            negativo += 1
        i += 1

    return'A Soma dos números é {} e a quantidade de números negativos é {}'.format(soma,negativo)
