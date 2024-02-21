sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0] #o zero  é pra informa que so a 1º letra vai ser considerada
while sexo not in 'MmFf':
     sexo = str(input('Dados inválidos. Por favor, informe o seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com Sucesso!'.format(sexo))