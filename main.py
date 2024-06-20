import flet as ft


def main(page: ft.Page):
     page.title ="Sorting App 1.0 - Lorenzo Serbinio - CEDULA"
     label_app_title = ft.Text(value="Metodos de Ordenamiento", color="white")
     page.controls.append(label_app_title)
     page.update()

    #añadiendo dropdown
     page.add(
        ft.Dropdown(
            label="",
            hint_text="Seleccione el Metodo de Ordenamiento",
            options=[
                ft.dropdown.Option("Bubble Sort"),
                ft.dropdown.Option("Selection Sort"),
                ft.dropdown.Option("Insertion Sort"),
                ft.dropdown.Option("Shellsort"),
                ft.dropdown.Option("Quicksort"),
                ft.dropdown.Option("Merge Sort"),
                ft.dropdown.Option("Radix Sort"),
                ft.dropdown.Option("Heap Sort"),

            ],
            autofocus=True,
            

        )
   


    )
     txt_field=ft.TextField(label="Valores")
     txt_field_valores_ordenados=ft.TextField(label="Valores Ordenados", read_only=True)
     btn_ordenar=ft.ElevatedButton(text="Ordenar")
     page.add(txt_field,txt_field_valores_ordenados)
     page.add(btn_ordenar)



ft.app(target=main)

