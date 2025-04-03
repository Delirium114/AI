import flet as ft


def main(page: ft.Page):
    def add_clicked(event):
        task_view.controls.append(ft.Checkbox(label=add_new_task_input.value, expand=True))
        add_new_task_input.value = ''
        # delete_task_button = ft.FloatingActionButton(icon=ft.Icons.DELETE)
        view.update()

    def display_view(e):
        display = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                edit_name,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.CREATE_OUTLINED,
                            tooltip="Edit To-Do",
                            #on_click=edit_clicked, #
                        ),
                        ft.IconButton(
                            ft.icons.DELETE_OUTLINE,
                            tooltip="Delete To-Do",
                            #on_click=delete_clicked,
                        ),
                    ],
                ),
            ],
        ),


    # Основные элементы
    # delete_task_button = ft.FloatingActionButton(icon=ft.Icons.DELETE)
    #edit_task_button = ft.
    add_new_task_input = ft.TextField(label="Какую задачу вы хотите добавить?")  # отвечает за поле ввода
    add_button = ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_clicked)
    # check_box_field = ft.Checkbox(label=add_new_task_input.value, expand=True)
    edit_name = ft.TextField(expand=1)
    task_view = ft.Column()

    view = ft.Column(
        width=600,
        controls=[
            ft.Row(
                controls=[
                    add_new_task_input, add_button
                ],
            ),
            task_view
        ],
    )

    # Вывод на экран
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(view)


ft.app(main)