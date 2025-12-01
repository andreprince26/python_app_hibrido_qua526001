import flet as ft
from pytubefix import youtube

import os
import threading


def main(page: ft.Page):
    page.title = "YouTube Downloader"
    page. theme_mode = ft.ThemeMode.LIGHT
    page.window.icon = "assets/youtube.png"


    # cria as pastas caso nao existam/////////////
    caminho_videos = 'videos'
    caminho_audios = 'audios'
    os.makedirs(caminho_videos, exist_ok=True)
    os.makedirs(caminho_audios, exist_ok=True)

    # componetes da interfaxe grafica///////////////
    titulo = ft.Text("Use uma URL", color=ft.colors.Black, size=20, weight=ft.FontWeight.BOLD)
    url = ft.TextField(
        label="cole a url do video do YouTube aqui",
        width=400,
        border_radius=10
    )
    base_path = os.path.dirname(__file__)
    logo_path = os.path.join(base_path, "assets", "youtube.png")
    logo_cabecalho = ft.image(src=logo_path, width=300, height=200)
    
    #componete para mostra informacoes do video/////////////
    video_info = ft.Container(
        content=ft.Column([]),
        visible=False,
        padding=10,
        bgcolor=ft.Colors.BLUE_GREY_50,
        border_radius=10,
        width=400

    )

    # barra de progresso////////////
    progress_bar = ft.ProgressBar(
        visible=False,
        width=400,
        color=ft.Colors.BLUE,
        bgcolor=ft.Colors.BLUE_GREY_100
    )

    # texto de status///////////
    status_text = ft.Text(
        "",
        color=ft.Colors.BLACK,
        size=14,
        text_align=ft.TextAlign.CENTER
    )

    # MOSTRA AS INFORMAÇOES DE VIDEOS NA INTERFACE////////
    def mostrar_info_videos(yt):
        try:
            # LIMPA O CONTAINER
            video_info.content.controls.clear()

            # adicione informaçoes do video ////////////
            video_info.content.controls.extend(
                [
                    ft.Text(f"Titulo: {yt.title}", size=14, weight=ft.FontWeight.BOLD),
                    ft.Text(f"Canal: {yt.author}", size=12),
                    ft.Text(f"Duraçao: {yt.length/60}:{yt.length%60:02d}", size=12),
                    ft.Text("Visualizaçoes: {yt.views:,}", size=12),
                ]
            )
            video_info.visible = True
            page.update()

        except Exception as e:
            status_text.value = f"Erro ao obter informaçoes: {str(e)}."
            status_text.color = ft.Colors.RED
            page.update()

    # funçao para baixar videos///////////////
    def baixar_video(e):
        if not url.value.strip():
            status_text.value = "por favor, insira uma url valido."
            status_text.color = ft.Colors.ORANGE
            page.update()

        def donwload_thread():
            try:
                # mostra progresso
                progress_bar.visible = True
                status_text.value = "Analisando video..."
                status_text.color = ft.colors.BLUE
                page.update()

                # cria objeto do youtube
                yt = youtube(url.value.strip())

                # mostrar as informaçoes do video
                mostrar_info_videos(yt)

                # inciar download
                status_text,value = f"Baixando video: {yt.title}..."
                page.update()

                # pega a maior resoluçao possivel
                stream = yt.streams.get_highest_resolution()

                # TODO
                
            except Exception as e:
                progress_bar.visible = False
                status_text.value = f"Erro (str(e))."
                status_text.color = ft.Colors.RED
                page.update()

        # executa em tread separada para nao travar a interface///////////////
        threading.Thread(target=donwload_thread, daemon=True).start()
    
           
 
    page.add(
        ft.SafeArea(
            ft.Container(
             
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )


ft.app(main)
