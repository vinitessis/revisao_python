import listas as lista
import funcoes as func

##### CONTADOR ID #####
id = 0
#######################

class Tarefa():

    def __init__(self, tarefaid = None, descricaoTarefa = None, estado = None):
        self.tarefa_id = self.set_tarefa_id()
        self.descricao_tarefa = self.set_descricao_tarefa()
        self.estado = self.set_estado()

    def set_tarefa_id(self):
        global id
        id = id + 1
        return id
    
    def get_tarefa_id(self):
        return self.tarefa_id

    def set_descricao_tarefa(self):
        descricao = input("Digite a descrição da tarefa: ").upper()
        return descricao

    def get_descricao_tarefa(self):
        return self.descricao_tarefa

    def set_estado(self):
        estado = ('INCONCLUÍDO')
        return estado

    def get_estado(self):
        return self.estado