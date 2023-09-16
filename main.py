import funcoes as func
import listas as lista

while True:
    print('''
    ========================================
    MENU - To Do List
    ========================================
    [0] - Finalizar Programa
    [1] - Cadastrar Tarefa
    [2] - Alterar Tarefa
    [3] - Deletar Tarefa
    [4] - Apresentar Tarefa (Listar)
    [5] - Alterar Estado de Tarefa
    ========================================''')
    opcao = input('Escolha: ')
    if opcao == "0":
        print("Finalizando...")
        print("Operações Finalizadas!")
        break
    elif opcao == "1":
        func.cadastrar_tarefa()
    elif opcao == "2":
        func.alterar_tarefa(lista.tarefas)
    elif opcao == "3":
        func.deletar_tarefa(lista.tarefas)
    elif opcao == "4":
        func.listar_tarefa()
    elif opcao == "5":
        func.alterar_estado_tarefa(lista.tarefas)
    else:
        print("=" * 24)
        print("Valor inválido!")
        print("=" * 24)