import flet as ft

def main(page: ft.Page):
    page.title = "Text fields, Button, Column and Dialog"
    page.window_width = 420
    page.window_height = 520
    page.padding = 20

    
    name_tf = ft.TextField(label="Name", hint_text="Name")
    uni_tf  = ft.TextField(label="University", hint_text="University")

   
    items_col = ft.Column(spacing=4)

    
    def print_list(e):
        name = name_tf.value.strip()
        uni  = uni_tf.value.strip()
        if not name or not uni:
            return  
        items_col.controls.append(ft.Text(f"Hello {name} from {uni}"))
        page.update()

   
    dlg = ft.AlertDialog(modal=True)

    def print_dialog(e):
        name = name_tf.value.strip()
        uni  = uni_tf.value.strip()
        if not name or not uni:
            return
        dlg.content = ft.Container(
            content=ft.Text(f"Hello {name} from {uni}", size=22),
            padding=20
        )
        page.dialog = dlg
        dlg.open = True
        page.update()

    
    btn_list   = ft.ElevatedButton(text="Print List", on_click=print_list)
    btn_dialog = ft.ElevatedButton(text="Print Dialog", on_click=print_dialog)

   
    page.add(
        name_tf,
        uni_tf,
        ft.Row([btn_list, btn_dialog], spacing=10),
        items_col,
    )

ft.app(target=main, view=ft.AppView.FLET_APP)
