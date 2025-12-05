import flet as ft


# -----------------------------
# Componente de Tarefa
# -----------------------------
class Task(ft.Column):
    def __init__(self, task_name, task_delete_callback):
        super().__init__()
        self.task_delete_callback = task_delete_callback

        self.display_task = ft.Checkbox(value=False, label=task_name)
        self.edit_name = ft.TextField(expand=1)

        # Modo de exibição
        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.display_task,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.CREATE_OUTLINED,
                            tooltip="Editar tarefa",
                            on_click=self.edit_clicked,
                        ),
                        ft.IconButton(
                            ft.Icons.DELETE_OUTLINE,
                            tooltip="Excluir tarefa",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )

        # Modo de edição
        self.edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                ft.IconButton(
                    icon=ft.Icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.Colors.GREEN,
                    tooltip="Salvar",
                    on_click=self.save_clicked,
                ),
            ],
        )

        self.controls = [self.display_view, self.edit_view]

    def edit_clicked(self, e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def delete_clicked(self, e):
        self.task_delete_callback(self)


# -----------------------------
# Aplicativo To-Do
# -----------------------------
class TodoApp(ft.Column):
    def __init__(self, title="Lista"):
        super().__init__()
        self.title = title

        self.new_task = ft.TextField(
            hint_text=f"Adicionar tarefa em {self.title}...",
            expand=True
        )

        self.tasks = ft.Column()

        self.controls = [
            ft.Text(self.title, size=20, weight=ft.FontWeight.BOLD),
            ft.Row(
                controls=[
                    self.new_task,
                    ft.FloatingActionButton(
                        icon=ft.Icons.ADD,
                        on_click=self.add_clicked
                    ),
                ]
            ),
            self.tasks
        ]

    def add_clicked(self, e):
        if not self.new_task.value.strip():
            return

        task = Task(self.new_task.value, self.delete_task)
        self.tasks.controls.append(task)
        self.new_task.value = ""

        self.update()

    def delete_task(self, task):
        self.tasks.controls.remove(task)
        self.update()


# -----------------------------
# Main
# -----------------------------
def main(page: ft.Page):
    page.title = "To-Do App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    Python_list = TodoApp("Python")
    Java_list = TodoApp("Java")
   

    page.add(Python_list, Java_list)


ft.app(main)