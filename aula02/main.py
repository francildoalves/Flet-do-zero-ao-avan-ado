import flet as ft

def main(page: ft.Page):
    new_tesk = ft.Text(value='Página inicial')
    page.add(new_tesk)
    page.update()   
ft.app(target=main)