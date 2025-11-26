import flet as ft


def main(page: ft.Page):
    page.title = "App Flex Fuel"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT

    gasolina = ft.TextField(
        label="valor da gasolina",
        prefix_text="R$ ",
        keyboard_type=ft.KeyboardType.NUMBER
    )
    etanol = ft.TextField(
        label="valor da gasolina",
        prefix_text="R$ ",
        keyboard_type=ft.KeyboardType.NUMBER
    )
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("melhor abastecimento com:"),

        content=ft.Text(size=20, weight="bold"),
        actions=[ft.TextButton("OK", on_click=lambda e:page.close(dlg_modal))],
        actions_alignment=ft.MainAxisAlignment.END
    )
    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("Flex Fuel", size=35, weight="bold"),
                
                alignment=ft.alignment.center,
            ),
            #expand=True,
        ),
        ft.ResponsiveRow(
            [
                ft.Container(gasolina, col={"sm": 6, "md": 4, "xl": 2}), # 'col' e um dicionario//////
                ft.Container(etanol, col={"sm": 6, "md": 4, "xl": 2})
            ]
        )
    )


ft.app(main)
