import flet as ft


def main(page: ft.Page):
    
    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("minha primeira aplicaçao.", size=30, weight="blod"),
                alignment=ft.alignment.center,
            )
        ),
        ft.Container(
        ft.Image(
            src="02_texto_e_imagem/src/assets/pexels-kostas-dimopoulos-119583302-29613922 (1).jpg",
            fit=ft.ImageFit.CONTAIN,
            error_content=ft.Text("nao foi possivel carregar a imagem.")
        ),
        alignment=ft.alignment.center,
        expand=True

        )
    
    )
    


ft.app(main)
