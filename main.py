import os
from pathlib import Path

from repository.task_repository import TaskRepository
from service.task_service import TaskService
from ui.app_window import AppWindow


def _configure_tk_paths() -> None:
    python_dir = Path(os.__file__).resolve().parent.parent
    tcl_dir = python_dir / "tcl"

    tcl_library = tcl_dir / "tcl8.6"
    tk_library = tcl_dir / "tk8.6"

    if tcl_library.exists():
        os.environ["TCL_LIBRARY"] = str(tcl_library)
    if tk_library.exists():
        os.environ["TK_LIBRARY"] = str(tk_library)


def main() -> None:
    _configure_tk_paths()
    repository: TaskRepository = TaskRepository()
    service: TaskService = TaskService(repository)
    app: AppWindow = AppWindow(service)

    app.mainloop()

if __name__ == "__main__":
    main()
