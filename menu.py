from exercicio04 import somaInteiro
from exercicio05 import tabuada
from exercicio05 import coletar
from exercicio06 import algoritmo
from exercicio07 import parImpar
from exercicio08 import numInteiro
from exercicio09 import ateZero
from exercicio10 import mediaPar
from exercicio11 import maiorMenor
from exercicio12 import vinteInteiro
from exercicio13 import fatorial
from exercicio14 import volei
from exercicio15 import miss
from exercicio16 import eleitores
from vetores import preencherVetor
from vetores import consultarVetor
from vetores import apagarPosicao
def mostrarMenu():
    print('\n\n\nEscolha umas das opções abaixo: ' +
          '\n0. SAIR' +
          '\n1. Exercicio 01' +
          '\n2. Exercicio 02' +
          '\n3. Exercicio 03' +
          '\n4. Exercicio 04' +
          '\n5. Exercicio 05' +
          '\n6. Exercicio 06' +
          '\n7. Exercicio 07' +
          '\n8. Exercicio 08' +
          '\n9. Exercicio 09' +
          '\n10. Exercicio 10' +
          '\n11. Exercicio 11' +
          '\n12. Exercicio 12' +
          '\n13. Exercicio 13' +
          '\n14. Exercicio 14' +
          '\n15. Exercicio 15' +
          '\n16. Exercicio 16' +
          '\n17. Exercicio 17' +
          '\n18. Exercicio 18' +
          '\n19. Exercicio 19' +
          '\n20. Exercicio 20' +
          '\n21. Preencher Vetor' +
          '\n22. Consultar Vetor' +
          '\n23. Apagar posição Vetor')

def operacao():
    opcao = 1 #Instanciar
    while(opcao != 0):
        # Chamar o método de cima
        mostrarMenu()
        # Coletar a opção do usuário
        opcao = int(input('Digite aqui o número da opção escolhida: '))

        # Executo a ação
        if(opcao == 0):
            # Instruções do exercício 1
            print ('Obrigado!')

        elif(opcao == 1):
            return
        elif (opcao == 2):
            return
        elif (opcao == 3):
            return
        elif (opcao == 4):
            # Utilizar o exercício04
             print('\n Exercício 04')
             print(somaInteiro())

        elif (opcao == 5):
            # Exercício05
             print('\n Exercício 05')
             num = int(input('Informe um número '))
             n = coletar()
             tabuada(num, n)

        elif (opcao == 6):
            # Exercício06
             print('\n Exercício 06')
             num = int(input('Informe o início '))
             n = int(input('Informe o fim '))
             algoritmo(num, n)

        elif (opcao == 7):
            # Exercício07
             print('\n Exercício 07')
             print(parImpar())
        elif (opcao == 8):
            # Exercício08
             print('\n Exercício 08')
             n = int(input('Informe um número'))
             print(numInteiro(n))

        elif (opcao == 9):
            # Exercício09
            print('\n Exercício 09')
            num = int(input('Informe um número: '))
            print(ateZero(num))

        elif (opcao == 10):
            # Exercício010
             print('\n Exercício 10')
             med = int(input('Informe um número: '))
             print(mediaPar(med))

        elif (opcao == 11):
            # Exercício011
            print('\n Exercício 11')
            print(maiorMenor())
        elif (opcao == 12):
            # Exercício012
            print('\n Exercício 12')
            print(vinteInteiro())
        elif (opcao == 13):
            # Exercício013
            print('\n Exercício 13')
            print(fatorial())
        elif (opcao == 14):
            print('\n Exercício 14')
            print(volei())
        elif (opcao == 15):
            print('\n Exercício 15')
            print(miss())
        elif (opcao == 16):
            print('\n Exercício 16')
            print(eleitores())
        elif (opcao == 17):
            return
        elif (opcao == 18):
            return
        elif (opcao == 19):
            return
        elif (opcao == 20):
            return
        elif (opcao == 21):
            num = int(input('Informe o tamanho do vetor: '))
            preencherVetor(num)
        elif (opcao == 22):
            num = int(input('Informe o tamanho do vetor: '))
            consultarVetor(num)
        elif (opcao == 23):
            posicao = int(input('Informe a posição que deseja apagar: '))
            apagarPosicao(posicao-1)
        else:
            print( 'Opção escolhida não é válida, digite novamente!!')