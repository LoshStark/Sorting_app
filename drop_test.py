import flet as ft

def main(page: ft.Page):
    def dropdown_changed(e):
        selected_value.value = f"Selected value: {dropdown.value}"
        if dropdown.value == "Option 1":
            print("Se ha seleccionado la opcion 1")
        

        page.update()

    dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option("Option 1"),
            ft.dropdown.Option("Option 2"),
            ft.dropdown.Option("Option 3"),
        ],
        on_change=dropdown_changed
    )

    selected_value = ft.Text(value="Selected value: None")

          

    page.add(dropdown, selected_value)

ft.app(target=main)