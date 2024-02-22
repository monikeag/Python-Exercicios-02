from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('='*20)
    print('''    [1] Somar;
    [2] Multiplicar;
    [3] Maior;
    [4] Novos números;
    [5] Sair do programa.''')
    print('=' * 20)
    opção = int(input('Qual é a sua opção?: '))
    print('=' * 20)
    sleep(3)
    if opção == 1:
        soma = n1+ n2
        print('A soma entre {} + {} é igual a {}'.format(n1, n2, soma))

    elif opção == 2:
        vezes = n1 * n2
        print ('Multipiclando {} * {} é igual a {}'.format(n1, n2, vezes))

    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {}, o maior valor é {}'.format(n1, n2, maior))

    elif opção == 4:
        vezes = n1 * n2
        print('Digite os novos números: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))

    elif opção == 5:
        print('Finalizando...')

    else:
        print('Opção inválida! Tente novamente ')
    sleep(3)
    print('*' * 20)
    print('Fim do programa! Volte Sempre!')
    print('*' * 20)
    sleep(3)

