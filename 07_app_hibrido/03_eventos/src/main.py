import flet as ft


def main(page: ft.Page):
    # funçao do evento
    def Exibir_nome(e):
        nome_saida.value = nome.value
        nome_saida.update()


    # propriedade da pagina
    page.title = "App de manipulaçao de eventos"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT

    # declaraçao de variaveis
    nome = ft.TextField(label="Informe seu nome",on_submit=Exibir_nome)# usar a tela enter
    nome_saida = ft.Text()
    
    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("Trabalhando com Evntos", size=35, weight="bold"),
                alignment=ft.alignment.center,
            ),
            expand=True,
        ),
            nome,
            ft.ElevatedButton("enviar", on_click=Exibir_nome),
            nome_saida
        
    )


ft.app(main)
