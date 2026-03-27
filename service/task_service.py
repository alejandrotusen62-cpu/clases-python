"""
Esta clase se encarga de la logica de la aplicacion.
Se conecta con los datos a traves del repositorio.
"""

from uuid import UUID

from model.task import Task
from repository.task_repository import TaskRepository


class TaskService:
    def __init__(self, task_repository: TaskRepository) -> None:
        self._task_repository = task_repository

    def get_all_task(self) -> list[Task]:
        """Retorna todas las tareas."""
        return self._task_repository.get_all()

    def delete_one_task(self, uuid: UUID) -> None:
        """Elimina una tarea por su identificador."""
        self._task_repository.delete_one(uuid)

    def create_one_task(self, title: str, description: str) -> Task:
        """Crea una tarea y retorna el resultado."""
        return self._task_repository.create_one(title, description)

    def update_one_task(
        self, uuid: UUID, title: str, description: str, complete: bool
    ) -> Task | None:
        """Actualiza una tarea existente."""
        return self._task_repository.update_one(uuid, title, description, complete)
