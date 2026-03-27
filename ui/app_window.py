import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from uuid import UUID
from service.task_service import TaskService

class AppWindow(tk.Tk):

    def __init__(self, task_service: TaskService) -> None:
        super().__init__()
        self._task_service = task_service

        self.title("Gestor de Tareas")
        self.geometry("820x560")
        self.resizable(False, False)

        # Widgets
        self.create_widgets()

    def create_widgets(self) -> None:
        main_frame = tk.Frame(self, padx=24, pady=24)
        main_frame.pack(fill="both", expand=True)

        header_frame = tk.Frame(main_frame, padx=20, pady=18)
        header_frame.pack(fill="x")

        title_label = tk.Label(
            header_frame,
            text="Panel de tareas",
            font=("TkDefaultFont", 16, "bold"),
        )
        title_label.pack(anchor="w")

        subtitle_label = tk.Label(
            header_frame,
            text="Crea, visualiza y elimina tareas desde una sola ventana.",
        )
        subtitle_label.pack(anchor="w", pady=(6, 0))

        form_frame = tk.Frame(main_frame, padx=20, pady=20)
        form_frame.pack(fill="x", pady=(18, 16))

        label_title = tk.Label(
            form_frame,
            text="Titulo de la tarea",
        )
        label_title.grid(row=0, column=0, sticky="w")
        self.title_input = tk.Entry(
            form_frame,
            width=34,
        )
        self.title_input.grid(row=1, column=0, sticky="ew", pady=(6, 14), padx=(0, 14))

        label_description = tk.Label(
            form_frame,
            text="Descripcion de la tarea",
        )
        label_description.grid(row=0, column=1, sticky="w")
        self.description_input = tk.Entry(
            form_frame,
            width=40,
        )
        self.description_input.grid(row=1, column=1, sticky="ew", pady=(6, 14))

        button_frame = tk.Frame(form_frame)
        button_frame.grid(row=2, column=0, columnspan=2, sticky="w")

        button = tk.Button(
            button_frame,
            text="Registrar tarea",
            command=self.create_task,
            padx=18,
            pady=10,
        )
        button.pack(side="left", padx=(0, 10))

        delete_button = tk.Button(
            button_frame,
            text="Eliminar seleccionada",
            command=self.delete_task,
            padx=18,
            pady=10,
        )
        delete_button.pack(side="left")

        form_frame.columnconfigure(0, weight=1)
        form_frame.columnconfigure(1, weight=1)

        table_frame = tk.Frame(main_frame, padx=16, pady=16)
        table_frame.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(
            table_frame,
            columns=("id", "title", "description"),
            show="headings",
        )
        self.tree.heading("id", text="ID")
        self.tree.heading("title", text="Titulo")
        self.tree.heading("description", text="Descripcion")

        self.tree.column("id", width=220, anchor="center")
        self.tree.column("title", width=180, anchor="w")
        self.tree.column("description", width=330, anchor="w")
        self.tree.pack(fill="both", expand=True)

        self.load_tasks()

    def create_task(self) -> None:
        title = self.title_input.get().strip()
        description = self.description_input.get().strip()

        if not title or not description:
            messagebox.showwarning(
                "Campos requeridos",
                "Debes completar el titulo y la descripcion de la tarea.",
            )
            return

        self._task_service.create_one_task(title, description)
        self.clear_inputs()
        self.load_tasks()
        messagebox.showinfo("Tarea registrada", "La tarea fue registrada correctamente.")

    def load_tasks(self) -> None:
        self.clear_table()
        tasks = self._task_service.get_all_task()

        for index, task in enumerate(tasks):
            self.tree.insert(
                "",
                "end",
                values=(str(task.uuid), task.title, task.description),
            )

    def delete_task(self) -> None:
        selected_items = self.tree.selection()
        if not selected_items:
            messagebox.showwarning(
                "Seleccion requerida",
                "Debes seleccionar una tarea para eliminarla.",
            )
            return

        values = self.tree.item(selected_items[0], "values")
        if not values:
            messagebox.showerror(
                "Error de seleccion",
                "No se pudo obtener la tarea seleccionada.",
            )
            return

        task_uuid = UUID(values[0])
        self._task_service.delete_one_task(task_uuid)
        self.load_tasks()
        messagebox.showinfo("Tarea eliminada", "La tarea fue eliminada correctamente.")

    def clear_table(self) -> None:
        for item in self.tree.get_children():
            self.tree.delete(item)

    def clear_inputs(self) -> None:
        self.title_input.delete(0, "end")
        self.description_input.delete(0, "end")
