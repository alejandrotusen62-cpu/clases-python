"""
Esta clase manipula los datos de las tareas.
"""

from dataclasses import replace
from uuid import UUID

from model.task import Task


class TaskRepository:
    def __init__(self) -> None:
        self._tasks: list[Task] = [
            Task("Leer un libro", "Debo leer el libro 'El diario de Ana Frank'."),
            Task("Practicar programacion", "Debo practicar mucho Python."),
            Task("Ver anime", "Debo dedicar solo media hora a Dragon Ball Z."),
        ]

    def get_all(self) -> list[Task]:
        """Recupera todas las tareas."""
        return [replace(task) for task in self._tasks]

    def delete_one(self, uuid: UUID) -> None:
        """Elimina una tarea por su identificador."""
        self._tasks = [task for task in self._tasks if task.uuid != uuid]

    def create_one(self, title: str, description: str) -> Task:
        """Crea una tarea y retorna una copia segura de la misma."""
        task = Task(title, description)
        self._tasks.append(task)
        return replace(task)

    def update_one(
        self, uuid: UUID, title: str, description: str, complete: bool
    ) -> Task | None:
        """Actualiza una tarea y retorna una copia si fue encontrada."""
        for index, task in enumerate(self._tasks):
            if task.uuid == uuid:
                updated_task = Task(title, description, complete, uuid)
                self._tasks[index] = updated_task
                return replace(updated_task)

        return None
