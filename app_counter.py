import flet as ft

def main(page: ft.Page):
    page.title = "2^n Counter"
    txt_number = ft.Text("1", size=50)  # 2^0 = 1
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
                ft.IconButton(icon="remove", on_click=decrement),  # بدّلنا ft.icons.REMOVE بـ "remove"
                txt_number,
                ft.IconButton(icon="add", on_click=increment),     # و ft.icons.ADD بـ "add"
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main, view=ft.AppView.FLET_APP)
