import flet as ft

def main(page: ft.Page):

    # Definindo o título da página
    page.title = "Minha primeira aplicação com Flet"

    def add_task(e):
        # Adicionando uma nova tarefa
        print(new_tesk2.value)
    
    # Título da página     
    new_tesk = ft.Text(value='Página inicial')
    page.add(new_tesk)

    # Inserindo Tarefa
    new_tesk2 = ft.TextField(hint_text='Insira ima terefa')
    page.add(new_tesk2)

    # Botão de adicionar tarefa
    new_button = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_task)
    page.add(new_button)

    page.update()   


ft.app(target=main)