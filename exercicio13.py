def fatorial():

    f = int(input('Informe o número: '))
    fatorial = f
    for i in range(f,1,-1):
        f -= 1
        fatorial *= f

    return'O fatorial do número {} é: {} '.format(f, fatorial)
