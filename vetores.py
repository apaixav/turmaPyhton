notas = [] #  Vetor Global = Todas as funções podem vizualizar/usar esse vetor

def preencherVetor(fim):
    for i in range(fim):
        num =  int(input('Informe a {}ª nota: '.format(i+1)))
        notas.append(num) #Adicionando notas no vetor

def consultarVetor(fim):
    for i in range(fim):
        print('{}ª posição: {}'.format(i+1, notas[i]))

def apagarPosicao(posicao):
    if (len(notas) < posicao):
        print('Impossivel remover, pois o tamanho é manor que a posição')
    else:
        del(notas[posicao]) #Exclundo um dado do vetor
        print('Removido com sucesso')