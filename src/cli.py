#Este archivo define la interfaz de línea de comandos utilizando click.

import click
from tasks.task_manager import TaskManager

task_manager = TaskManager()

@click.group()        #Define un grupo de comandos
def cli():
    pass

@click.command()
@click.argument('description')
def add(description):        #Define un comando para añadir una tarea
    '''Add a new task'''
    task_manager.add_task(description)
    click.echo(f'Task added: {description}')
    
@click.command()
def list():          #Define un comando para listar todas las tareas
    '''List all tasks'''
    tasks = task_manager.list_tasks()
    for i, task in enumerate(tasks):
        click.echo(f"{i}. {task['description']} - {task['status']}")
        
@click.command()
@click.argument('index', type=int)
@click.argument('status')
def update(index, status):          #Define un comando para actualizar el estado de una tarea
    '''Update the status of a task'''
    task_manager.update_task(index, status)
    click.echo(f'Task {index} updated to {status}')
    
#Añade los comandos al grupo
cli.add_command(add)      
cli.add_command(list)          
cli.add_command(update)         

if __name__ == '__main__':     #Ejecuta la interfaz de línea de comandos
    cli()