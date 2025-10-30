import flet as ft

def main(page: ft.Page):
    txt_number = ft.Text("0", size=50)
    n = 0

    def increment(e):
        nonlocal n
        n += 1
        txt_number.value = str(2 ** n)
        page.update()

    def decrement(e):
        nonlocal n
        n -= 1
        txt_number.value = str(2 ** n)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=decrement),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=increment),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main, view=ft.AppView.FLET_APP)
