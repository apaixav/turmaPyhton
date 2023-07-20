def volei():
    num=1
    soma = 0
    media = 0
    for i in range(num, 13):
        num = int(input('Informe a altura do {}° jogador: '.format(i)))
        while (i < 12):
            soma += num
            i += 1
    media = soma/i
    return ('A altura média do time é: {}'.format(media))