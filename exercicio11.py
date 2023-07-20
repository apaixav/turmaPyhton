def maiorMenor():
    m = 1
    i = 0
    while(m != 0):
        m = int(input('Informe um número: '))
        if(m != 0):
            if(i == 0):
                maior = m
                menor = m
                i = 1

            if(m > maior):
                maior = m

            if(m < menor):
                menor = m


    return('O número {} é o maior e o {} o menor'.format(maior, menor))
