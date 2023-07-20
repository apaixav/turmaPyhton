def mediaPar(med):
    soma = 0
    med = 1
    i = 0
    while(med != 0):
        med = int(input('Informe um número: '))
        if (med % 2 == 0):
            soma += med
            i += 1
    return('A média dos números é: {}'.format(soma/i))


