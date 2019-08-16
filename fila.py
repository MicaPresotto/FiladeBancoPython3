print('Bem-vindo ao PythonBank,hoje é dia 09/08/2019.')
print('Insira  a opçao: ')
clientes = 0
senha =  0
filaidosos = []
filagestantes = []
filanormal = []

rodando = True


while rodando == True:
    x = int(input(' 1- Idosos - pessoas com mais de 60 anos\n 2- Gestantes - mulheres grávidas\n 3- Normais - resto da população\n 4- Retirar da fila \n 5- Mostrar filas \n 6- Mostrar a quantidade de clientes\n 7- Sair \n Qual sua opção?: '))
    
    if  x == 1:
        print('Você está na fila dos idosos')
        senha += 1
        filaidosos.append(senha)
        print('Sua senha é',senha)
        clientes += 1
        
    elif x == 2:
        print('Você está na fila dos gestantes')
        senha += 1
        filagestantes.append(senha)
        print('Sua senha é',senha)
        clientes += 1
       
    elif x == 3:
        print('Você está na fila normal')
        senha += 1
        filanormal.append(senha)
        print('Sua senha é',senha)
        clientes += 1

    elif x == 4:
        if len(filaidosos) > 0:
            print  ('Senha removida foi: ',filaidosos.pop(0))
            clientes = clientes - 1
        elif len(filagestantes) > 0:
            print  ('Senha removida foi: ',filagestantes.pop(0))
            clientes = clientes - 1
        elif len(filanormal) > 0:
            print  ("Senha removida foi:", filanormal.pop(0))
            clientes = clientes - 1
        else:
            print('Nao há senha para remover')
        
    
    elif x == 5:
        print('A fila dos idosos tem',len(filaidosos),'idosos com as senhas',filaidosos)
        print('A fila dos gestantes tem',len(filagestantes),'gestantes com as senhas',filagestantes)
        print('A fila normal tem',len(filanormal),'pessoas com as senhas',filanormal)
    elif x == 6:
        print('O total de clientes é',clientes)

            
        
    elif x == 7:
        print('A equipe PythonBank agradece pela preferência,volte sempre.')
        rodando = False
    else:
        print('Dado inválido,digite um número correto: ')
