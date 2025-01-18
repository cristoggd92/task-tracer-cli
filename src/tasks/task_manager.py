#Este archivo contiene la lógica para gestionar las tareas. Incluye métodos para cargar, guardar, añadir, listar y actualizar tareas.

import json
import os

TASKS_FILE = 'tasks.json'

class TaskManager:   #Clase que gestiona las tareas
    def __init__(self):                #Inicializa la clase cargando las tareas desde el archivo.
        self.tasks = self.load_tasks()
        
    def load_tasks(self):           #Carga las tareas desde el archivo tasks.json
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, 'r') as file:
                return json.load(file)
        return[]
    
    def save_tasks(self):                 #Guarda las tareas en el archivo tasks.json
        with open(TASKS_FILE, 'w') as file:
            json.dump(self.tasks, file, indent=4)
            
    def add_task(self, description):             #Añade una tarea a la lista de tareas y guarda los cambios.
        task = {
            'description': description,
            'status': 'to-do'
        }
        self.tasks.append(task)
        self.save_tasks()
        
    def list_tasks(self):           #Devuelve la lista de tareas
        return self.tasks
    
    def update_task(self, index, status):        #Actualiza el estado de una tarea en la lista y guarda los cambios.
        if 0 <= index < len(self.tasks):
            self.tasks[index]['status'] = status
            self.save_tasks()