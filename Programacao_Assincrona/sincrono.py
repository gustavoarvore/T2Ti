# Objetivos da aula:
#Explicar os conceitos fundamentais de programaçãp assincrona e mostrar quando e por que ela deve ser utilizada. Ao final da aula, os alunos terão clareza sobre a diferença entre programação sincrona e assincrona e entenderão os beneficios do codigo nao bloqueante

import time 

def tarefa_sincrona(nome, tempo):
    print(f'iniciar a tarefa {nome}')
    time.sleep(tempo)
    print(f'iniciar a tarefa {nome} foi finalizada')

inicio = time.time()
tarefa_sincrona('tarefa 01', 3)
tarefa_sincrona('tarefa 02', 2)
tarefa_sincrona('tarefa 03', 1)
fim = time.time()

print(f'tempo total para xecutar as tarefas = {fim-inicio: .2f} segundos.')