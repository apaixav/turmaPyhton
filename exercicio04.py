def somaInteiro():
    soma=0
    for i in range(1, 101, 2):
        print(i)
        soma += i

    return 'A soma dos elementos entre 1 e 100 é: {}'.format(soma)
