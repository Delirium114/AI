import flet as ft


def main(page: ft.Page):


    def add_clicked(event):

        task_view.controls.append(ft.Checkbox(label=add_new_task_input.value))
        add_new_task_input.value = ''
        view.update()


    # Основные элементы
    add_new_task_input = ft.TextField(label="Какую задачу вы хотите добавить?") # отвечает за поле ввода
    add_button = ft.FloatingActionButton(icon = ft.Icons.ADD, on_click=add_clicked)
    #check_box_field = ft.Checkbox(label=add_new_task_input.value, expand=True)
    task_view = ft.Column()

    view = ft.Column(
        width=600,
        controls=[
            ft.Row(
                controls=[
                    add_new_task_input,add_button
                ],
            ),
            task_view
        ],
    )

    # Вывод на экран
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(view)


ft.app(main)