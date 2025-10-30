import flet as ft

def main(page: ft.Page):
    page.title = "Flet app"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "start"

    def show_login():
        email = ft.TextField(label="Email", width=300)
        password = ft.TextField(label="Password", password=True, can_reveal_password=True, width=300)
        error_text = ft.Text("", color="red")

        def handle_login(e):
            if not email.value or not password.value:
                error_text.value = "Email or password is missing!"
                page.update()
            else:
                show_form()

        page.controls.clear()
        page.add(
            ft.AppBar(title=ft.Text("Flet app")),
        )
        page.add(
            ft.Column(
                [
                    email,
                    password,
                    ft.ElevatedButton("Log in", on_click=handle_login),
                    error_text,
                ],
                horizontal_alignment="start",
                tight=True,
            )
        )
        page.update()

    def show_form():
        name = ft.TextField(label="Name", width=350)
        dob = ft.DatePicker()
        dob_field = ft.TextField(label="Date of birth", width=350, read_only=True, on_focus=lambda e: page.open(dob))
        gender = ft.RadioGroup(
            content=ft.Column(
                [
                    ft.Radio(value="Male", label="Male"),
                    ft.Radio(value="Female", label="Female"),
                ]
            ),
            value="Male",
        )
        address = ft.TextField(label="Address", width=350, multiline=True, min_lines=2)
        country = ft.Dropdown(
            label="Country",
            width=200,
            options=[
                ft.dropdown.Option("Finland"),
                ft.dropdown.Option("Sweden"),
                ft.dropdown.Option("Norway"),
                ft.dropdown.Option("Denmark"),
            ],
            value="Finland",
        )

        def change_dob(e):
            if dob.value:
                dob_field.value = dob.value.strftime("%Y-%m-%d")
                page.update()

        dob.on_change = change_dob

        def submit_form(e):
            data = {
                "name": name.value,
                "dob": dob_field.value,
                "gender": gender.value,
                "address": address.value,
                "country": country.value,
            }
            show_result(data)

        page.controls.clear()
        page.add(
            ft.AppBar(
                title=ft.Text("Form"),
                leading=ft.IconButton(icon="arrow_back", on_click=lambda e: show_login()),
            )
        )
        page.add(
            ft.Column(
                [
                    name,
                    dob_field,
                    gender,
                    address,
                    country,
                    ft.ElevatedButton("Submit", on_click=submit_form),
                    dob,
                ],
                scroll=ft.ScrollMode.AUTO,
            )
        )
        page.update()

    def show_result(data: dict):
        name = data.get("name", "")
        dob = data.get("dob", "")
        gender = data.get("gender", "")
        address = data.get("address", "")
        country = data.get("country", "")

        card = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text(f"Name: {name}", weight="bold"),
                        ft.Text(f"Date of Birth: {dob}"),
                        ft.Text(f"Gender: {gender}"),
                        ft.Text(f"Address: {address}"),
                        ft.Text(f"Country: {country}"),
                    ],
                    tight=True,
                    spacing=5,
                ),
                padding=20,
            )
        )

        page.controls.clear()
        page.add(
            ft.AppBar(
                title=ft.Text("Result"),
                leading=ft.IconButton(icon="arrow_back", on_click=lambda e: show_form()),
            )
        )
        page.add(card)
        page.add(
            ft.ElevatedButton("Go back", on_click=lambda e: show_form())
        )
        page.update()

    show_login()

ft.app(target=main)
