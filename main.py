import flet as ft
import bubble_sort as bs
import selection_sort as ss
import insertion_sort as insertion
import shell_sort as shell
import quick_sort as quick
import merge_sort as merge
import radix_sort as radix
import heap_sort as heap
import os
import platform
import subprocess

def clear_screen():
    # Detectar el sistema operativo
    current_os = platform.system()
    
    if current_os == "Windows":
        # Para Windows
        subprocess.run("cls", shell=True)
    else:
        # Para Unix/Linux/MacOS
        subprocess.run("clear", shell=True)

#Funcion principal donde definimos elemento pagina como parametro
def main(page: ft.Page):

    def reload(e):
      txt_field_valores_ordenados.value =""
      txt_field.value =""
      pick_files_button.disabled = False
      txt_field.read_only = False
      selected_files.value =""  
      dp_selection.value=""
      clear_screen()
      print("Se han restablecido todos los campos y se ha limpiado la consola")
      page.update()

   #funciones del boton ordenar
    def btn_clicked(e):
          if dp_selection.value == "Bubble Sort":
            print("Se ha seleccionado Bubble Sort")
            values=txt_field.value
            sorted_values = bs.main(values)
            txt_field_valores_ordenados.value = sorted_values
            page.update()
        
          elif dp_selection.value =="Selection Sort":
              print("Se ha seleccionado Selection Sort")
              values=txt_field.value
              sorted_values = ss.main(values)
              txt_field_valores_ordenados.value = sorted_values
              page.update()

          elif dp_selection.value =="Insertion Sort":
              print ("Se ha seleccionado Insertion Sort")
              values = txt_field.value
              sorted_values = insertion.main(values)
              txt_field_valores_ordenados.value = sorted_values
              page.update()

          elif dp_selection.value =="Shellsort":
               print ("Se ha seleccionado Shell Sort")
               values = txt_field.value
               sorted_values = shell.main(values)
               txt_field_valores_ordenados.value = sorted_values
               page.update()

          elif dp_selection.value =="Quicksort":
              print ("Se ha seleccionado Quick Sort")
              values = txt_field.value
              sorted_values = quick.main(values)
              txt_field_valores_ordenados.value = sorted_values
              page.update()

          elif dp_selection.value == "Merge Sort":
               print ("Se ha seleccionado Merge Sort")
               values = txt_field.value
               sorted_values = merge.main(values)
               txt_field_valores_ordenados.value = sorted_values
               page.update()

          elif dp_selection.value == "Radix Sort":
               print ("Se ha seleccionado Radix Sort")
               values = txt_field.value
               sorted_values = radix.main(values)
               txt_field_valores_ordenados.value = sorted_values
               page.update()

          elif dp_selection.value == "Heap Sort":
               print ("Se ha seleccionado Heap Sort")
               values = txt_field.value
               sorted_values = heap.main(values)
               txt_field_valores_ordenados.value = sorted_values
               page.update()

          

    #Evento que escucha el campo de texto principal si tiene un elemento o no
    def on_text_change(e):
         row.disabled = bool(txt_field.value)
         page.update()

    #evento  que escucha file picker
    def pick_files_result(e: ft.FilePickerResultEvent):

        if e.files:
            # Leer el contenido del archivo seleccionado
            file = e.files[0]
            file_path = str(file.path)
            print("Se ha cargado el archivo "+file_path)
            with open(file_path, "r") as f:
                file_content = f.read()
                f.close()
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

    #evento que escucha valor seleccionado del dropdown
       

    #Seccion de Renderizado - elementos de aplicación

            
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
    page.title ="Sorting App 2.0 - Lorenzo Serbinio - 8-929-245"
    label_app_title = ft.Text(value="Metodos de Ordenamiento",theme_style=ft.TextThemeStyle.HEADLINE_SMALL)

    page.controls.append(label_app_title)
    page.update()
    
    #definiendo elemento dropdown

    dp_selection=  ft.Dropdown(
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
            #on_change =dropdown_selector,
            autofocus=True,
            

        )
    page.update()
        
  
    txt_field_valores_ordenados=ft.TextField(label="Valores Ordenados",read_only=True)
    txt_field=ft.TextField(label="Valores",on_change=on_text_change)
    btn_ordenar=ft.ElevatedButton(text="Ordenar", icon="sort",bgcolor=ft.colors.PURPLE_300,color="white", on_click=btn_clicked)
    btn_limpiar = ft.ElevatedButton(text ="Limpiar",icon="clear",color="white", bgcolor=ft.colors.PURPLE_300, on_click=reload)
    page.add(dp_selection,txt_field,row,txt_field_valores_ordenados)
    page.add(ft.Row([btn_limpiar,btn_ordenar]))



ft.app(target=main)

