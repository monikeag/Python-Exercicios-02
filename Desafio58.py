from random import randint
from time import sleep
comput = randint (0, 10)
print('Sou seu computador... Acabei de pensar em número entre 0 e 10.')
sleep (2)
print ('Vamos ver se consegue adivinhar, qual escolhi! 👀')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1 #palpite recebe + 1
    if jogador == comput:
        acertou = True
    else:
        if jogador < comput:
            print('É mais! Tenta de novo.')
        elif jogador > comput:
            print('Menos que isso! Tente de novo.')
print('Acertou com {} tentativas. Parabéns 🔥'.format(palpites))




