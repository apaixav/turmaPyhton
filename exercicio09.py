def ateZero(num):
    soma = 0
    num = 1
    while(num != 0):
        num = int(input('Informe um número: '))
        soma += num
    return ('A soma dos números é: {}'.format(soma))


