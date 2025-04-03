from asyncio import create_task

import flet as ft

def task_create(task_name,delet_task):


        def delete_task(event):
            delet_task(task_container)


        checkbox = ft.Checkbox(value=False, label=task_name)

        checkbox = ft.Checkbox(value=False)
        display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                checkbox,  # Галочка
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(  # Кнопка удаления
                            ft.icons.DELETE_OUTLINE,
                            tooltip="Delete To-Do",
                            on_click=delete_task,
                        ),
                    ],
                ),
            ],
        )



        task_container = ft.Column(controls=[display_view])  ## Контейнер для задачи
        return task_container, checkbox




def main(page: ft.Page):


    def add_task(event):

        if new_task_input.value:
            task_container, task_checkbox = task_create(
                new_task_input.value, delete_clicked
            )
            task_view.controls.append(task_container)
            new_task_input.value = ''
            page.update()


        #task_view.controls.append(ft.Checkbox(label=add_new_task_input.value,expand=True))
        #add_new_task_input.value = ''
        #view.update()




    def delete_clicked(task):
        task_view.controls.remove(task)
        page.update()


    # Основные элементы
    new_task_input = ft.TextField(label="Какую задачу вы хотите добавить?", on_submit=add_task)
    #add_button = ft.FloatingActionButton(icon = ft.Icons.ADD, on_click=add_task)

    task_view = ft.Column()


    view = ft.Column(
        width=600,
        controls=[
            ft.Row(
                controls=[
                    new_task_input,
                    ft.FloatingActionButton(icon = ft.Icons.ADD, on_click=add_task)#add_button
                ],
            ),
            ft.Column(
                spacing=25,
                controls=[
                    task_view
                ],
            ),
        ],
    )

    # Вывод на экран
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(view)


ft.app(main)