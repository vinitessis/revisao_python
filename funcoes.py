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

#    for i in lista.tarefas:
#        print(i.get_tarefaid())
#        print(i.get_descricaoTarefa())
#        print(i.get_estado())

def alterar_tarefa(lista):
    print("=" * 20)
    print("Alterar Tarefa")
    print("=" * 20)

    listar_tarefa()

    id = input('Digite a ID da tarefa desejada: ')

    for i in lista:
        if i.get_tarefaid() == id:
            novaDescricao = input("Digite a nova descrição: ")
            i.descricaoTarefa = novaDescricao
            return lista
        else:
            print('deu ruim')

def deletar_tarefa():
    print("=" * 20)
    print("Deletar Tarefa")
    print("=" * 20)

    listar_tarefa()

    id = input('Digite a ID da tarefa desejada: ')
        
def listar_tarefa():
    print("=" * 140)
    print("To Do List - Lista de Tarefas".center(140," "))
    print("=" * 140)
    print("|", "ID".center(10," "), "|", "Descrição".center(80," "), "|", "Estado".center(40," "), "|")
    for i in lista.tarefas:
        print("|", str(i.get_tarefaid()).center(10," "), "|", str(i.get_descricaoTarefa()).center(80," "), "|", str(i.get_estado()).center(40," "), "|")
