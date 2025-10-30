import flet as ft

def main(page: ft.Page):
    page.title = "Multi-Counter App"
    page.padding = 20
    page.window_width = 520
    page.window_height = 600

    name_tf = ft.TextField(hint_text="Enter counter name", expand=True)
    counters_col = ft.Column(spacing=10, expand=True)

    def create_counter_row(counter_name: str) -> ft.Row:
        value_tf = ft.TextField(value="0", width=70, text_align="center", read_only=True)
        name_lbl = ft.Text(counter_name, expand=True)

        def inc(_):
            value_tf.value = str(int(value_tf.value) + 1)
            page.update()

        def dec(_):
            value_tf.value = str(int(value_tf.value) - 1)
            page.update()

        def delete_row(_):
            counters_col.controls.remove(row)
            page.update()

        row = ft.Row(
            controls=[
                name_lbl,
                ft.IconButton(icon="remove", tooltip="Decrement", on_click=dec),
                value_tf,
                ft.IconButton(icon="add", tooltip="Increment", on_click=inc),
                ft.IconButton(icon="delete", tooltip=f"Delete '{counter_name}'", on_click=delete_row),
            ],
            alignment=ft.MainAxisAlignment.START,
        )
        return row

    def add_counter(_):
        name = name_tf.value.strip()
        if not name:
            return
        counters_col.controls.append(create_counter_row(name))
        name_tf.value = ""
        page.update()

    add_btn = ft.ElevatedButton(text="+", width=50, tooltip="Add counter", on_click=add_counter)

    page.floating_action_button = ft.FloatingActionButton(
        icon="add",
        tooltip="Add counter",
        on_click=add_counter,
    )

    page.add(
        ft.Row([name_tf, add_btn]),
        ft.Divider(),
        counters_col,
    )

ft.app(target=main, view=ft.AppView.FLET_APP)
