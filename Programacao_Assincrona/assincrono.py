# Objetivos da aula:
#Explicar os conceitos fundamentais de programaçãp assincrona e mostrar quando e por que ela deve ser utilizada. Ao final da aula, os alunos terão clareza sobre a diferença entre programação sincrona e assincrona e entenderão os beneficios do codigo nao bloqueante
import asyncio
import time 

async def tarefa_assincrona(nome, tempo):
    print(f'iniciar a tarefa {nome}')
    await asyncio.sleep(tempo)
    print(f'iniciar a tarefa {nome} foi finalizada')

async def main():
    inicio = time.time()

    await asyncio.gather(
        tarefa_assincrona('tarefa 01', 3),
        tarefa_assincrona('tarefa 02', 2),
        tarefa_assincrona('tarefa 03', 1)
    )

    fim = time.time()

    print(f'tempo total para executar as tarefas = {fim-inicio: .2f} segundos.')

asyncio.run(main())
