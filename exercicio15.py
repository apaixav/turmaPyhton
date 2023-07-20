def miss():
    nota = 1
    v = 0
    for i in range(nota, 17):
        nome = input('Informe o nome da candidata: ')
        nota = int(input('informe a nota da {}° candidata: '.format(i)))
        if (i != 16):
            if(v == 0):
                maior = nota
                v = 1

            if(nota > maior):
                maior = nota
                nomeMaior = nome

    return ('A vencedora do concurso é: {}, nota {}'.format(nomeMaior, maior))


