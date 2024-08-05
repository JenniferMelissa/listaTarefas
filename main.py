#lista
tarefas = []

#inicio do loop
while True:
    print('1 - Inserir nova tarefa: ')
    print('2 - Listar tarefas: ')
    print('3 - Sair do programa.')

    #usuario seleciona opcao desejada
    opcao = input('Insira a opção desejada: ')
    

    match opcao:
        case '1':
            nova_tarefa = input('Insira nova tarefa: ')
            posicao = int(input('Informe a posição da nova tarefa: '))
            tarefas.insert(posicao,nova_tarefa)
            print(tarefas)
            print('Lista inserida com sucesso.\n')
            continue
        case '2':
            print('\nLista de Tarefas:\n')
            for tarefa in tarefas:
                print(tarefa)
            continue
        case '3':
            print('Programa encerrado. Obrigada por ajudar nossa comunidade!')
            break