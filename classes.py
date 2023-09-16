import listas as lista
import funcoes as func

##### CONTADOR ID #####
id = 0
#######################

class Tarefa():

    def __init__(self, tarefaid = None, descricaoTarefa = None, estado = None):
        self.tarefaid = self.set_tarefaid()
        self.descricaoTarefa = self.set_descricaoTarefa()
        self.estado = self.set_estado()

    def set_tarefaid(self):
        global id
        id = id + 1
        return id
    
    def get_tarefaid(self):
        return self.tarefaid

    def set_descricaoTarefa(self):
        descricao = input("Digite a descrição da tarefa: ").upper()
        return descricao

    def get_descricaoTarefa(self):
        return self.descricaoTarefa

    def set_estado(self):
        estado = ('INCONCLUÍDO')
        return estado

    def get_estado(self):
        return self.estado