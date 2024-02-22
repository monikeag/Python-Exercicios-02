#na aula 10 - desafio 28, fiz assim:
brin = str(input('Vamos brincar de advinhação? ')).upper()
if brin == 'SIM':
     print('Oba! Então vamos começar!!🤪')
     num = str(input('Me diz aí, um número de 01 a 12. Qual estou pensando? 🫣  '))
     if num == '8':
        print('Uhu! Você acertou! Parabéns 🔥')
     else:
        print('Ixi! Tenta de novo, você consegue!')
else:
    print('Poxa! Fiquei triste :/')