import classes as classe
import listas as lista

def cadastrar_tarefa():
    print("=" * 20)
    print("Cadastro de Tarefas")
    print("=" * 20)

    tarefa = classe.Tarefa()

    lista.tarefas.append(tarefa)

    print("=" * 20)
    print("Tarefa Cadastrada")
    print("=" * 20)

def alterar_tarefa(lista):
    print("=" * 20)
    print("Alterar Tarefa")
    print("=" * 20)

    listar_tarefa()

    while True:
        try:
            id = int(input('Digite a ID da tarefa desejada: '))

            for i in lista:
                if i.get_tarefa_id() == id:
                    nova_descricao = input("Digite a nova descrição: ").upper()
                    i.descricaoTarefa = nova_descricao
                    print("=" * 20)
                    print("Tarefa Alterada")
                    print("=" * 20)

            return lista

        except:
            print("=" * 20)
            print("Valor inválido")
            print("=" * 20)

def deletar_tarefa(lista):
    print("=" * 20)
    print("Deletar Tarefa")
    print("=" * 20)

    listar_tarefa()

    while True:
        try:
            id = int(input('Digite a ID da tarefa desejada: '))

            for i in lista:
                if i.get_tarefa_id() == id:
                    lista.remove(i)
                    print("=" * 20)
                    print("Tarefa removida")
                    print("=" * 20)
            return lista

        except:
            print("=" * 20)
            print("Valor inválido")
            print("=" * 20)
     
def listar_tarefa():
    print("=" * 140)
    print("To Do List - Lista de Tarefas".center(140," "))
    print("=" * 140)
    print("|", "ID".center(10," "), "|", "Descrição".center(80," "), "|", "Estado".center(40," "), "|")
    
    for i in lista.tarefas:
        print("|", str(i.get_tarefa_id()).center(10," "), "|", str(i.get_descricao_tarefa()).center(80," "), "|", str(i.get_estado()).center(40," "), "|")

def alterar_estado_tarefa(lista):
    print("=" * 20)
    print("Alterar Estado de Tarefa")
    print("=" * 20)

    listar_tarefa()

    while True:
        try:
            id = int(input("Digite a ID da tarefa desejada: "))

            for i in lista:
                if i.get_tarefa_id() == id:
                    if i.get_estado() == "INCONCLUÍDO":
                        i.estado = "CONCLUÍDO"
                        print("=" * 20)
                        print("Tarefa concluída")
                        print("=" * 20)
                    elif i.get_estado() == "CONCLUÍDO":
                        i.estado = "INCONCLUÍDO"
                        print("=" * 20)
                        print("Tarefa inconcluída")
                        print("=" * 20)
                
            return lista

        except:
            print("=" * 20)
            print("Valor inválido")
            print("=" * 20)