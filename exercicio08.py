def numInteiro(n):
    soma = 0
    for i in range(n):
        num = int(input('{} ° número: '.format(i+1)))
        soma += num

    return('A soma dos elementos é: {}'.format(soma))