import flet as ft

#Funcion principal donde definimos elemento pagina como parametro
def main(page: ft.Page):

    #funcion que escucha el campo de texto principal si tiene un elemento o no
    def on_text_change(e):
         row.disabled = bool(txt_field.value)
         page.update()

    #funcion que escucha file picker
    def pick_files_result(e: ft.FilePickerResultEvent):

        if e.files:
            # Leer el contenido del archivo seleccionado
            file = e.files[0]
            with open(file.path, "r") as f:
                file_content = f.read()

            # Mostrar el contenido en el cuadro de texto y establecerlo como solo lectura
            txt_field.value = file_content
            txt_field.read_only = True
            page.update()



        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelado!"
        )
        selected_files.update()


    # Resultado de la selección del archivo
    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()

    page.overlay.append(pick_files_dialog)
    
    def on_pick_files(e):
        pick_files_dialog.pick_files(allow_multiple=False,allowed_extensions=["txt"])

    # Crear el botón y asignarlo a una variable
    pick_files_button = ft.ElevatedButton(
        "Seleccionar Archivo",
        icon=ft.icons.UPLOAD_FILE,
        on_click=on_pick_files
    )

    # Crear un widget texto para mostrar los archivos seleccionados
    selected_files = ft.Text("")

    # Crear el Row con el botón y otros elementos
    row = ft.Row(
        [
            pick_files_button,
            selected_files,
        ]
    )


    page.theme_mode="light"
    page.theme = ft.Theme(color_scheme_seed="purple")
    page.title ="Sorting App 1.0 - Lorenzo Serbinio - CEDULA"
    label_app_title = ft.Text(value="Metodos de Ordenamiento",theme_style=ft.TextThemeStyle.HEADLINE_SMALL)

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
    txt_field=ft.TextField(label="Valores",on_change=on_text_change)
    txt_field_valores_ordenados=ft.TextField(label="Valores Ordenados", read_only=True)
    btn_ordenar=ft.ElevatedButton(text="Ordenar", icon="sort",bgcolor="purple",color="white")
    page.add(txt_field,row,txt_field_valores_ordenados)
    page.add(btn_ordenar)



ft.app(target=main)

