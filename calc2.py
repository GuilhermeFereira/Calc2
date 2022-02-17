from re import sub
from time import sleep
import time
g1 = int(input('digite o 1 número: '))
g2 = int(input('digite o 2 número: '))
terminar = False
while not terminar:
    menu = int(input('''selecione oque você quer fazer com os números, digitando o número em seu teclado
    [1] somar
    [2] multiplicar
    [3]subtração
    [4]divisão
    [5] maior
    [6] novos números (nessa opção você coloca núemros novos para somar)
    [7] fechar programa 
    selecione qual operação você quer fazer acima:'''))
    soma = g1 + g2
    mult = g1 * g2
    sub = g1 - g2
    div = g1 / g2
    maiorvalor = ''
    if menu == 1:
        print('a soma de {} e {} é = {}'.format(g1,g2,soma))
        time.sleep(2)
    if menu == 2:
        print('a multiplicação entre os eles são {}'.format(mult))
        time.sleep(2)
    if menu == 3:
        print('a subtração de {} menos {} é = {}'.format(g1,g2,sub))
        time.sleep(2)
    if menu == 4:
        print('{} dividido por {} é igual a {}'.format(g1,g2,div))
        time.sleep(2)
    if menu == 5:
        if  g1 > g2:
            maiorvalor = g1
            print('0 maior entre eles é = {}'.format(maiorvalor))
        if g2 > g1:
            maiorvalor = g2
            print('o maior entre eles é = {}.'.format(maiorvalor))
        if g2 == g1:
            print('os valores são iguais')
            time.sleep(2)
    if menu == 6:
        print('coloque os novos valores a baixo')
        g1 = int(input('insira o primeiro número: '))
        g2 = int(input('insira o segundo número: '))
        time.sleep(2)
    if menu == 7:
        print('O programa está acabando por aqui, feito por GuiR <3')
        terminar = True
        time.sleep(2)
    print('-='*50)
