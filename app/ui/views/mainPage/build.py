import flet as ft


class MainPage:
    @staticmethod

    def build():
        ''' builds the main Page and returns It'''

        column = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=15,
            margin= 100,
        )

        # ---------------------------------------------------------
        # HEADER
        # ---------------------------------------------------------

        header = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "MARKET QUOTES",
                        size=38,
                        weight=ft.FontWeight.BOLD,
                        font_family="Consolas",
                        color=ft.Colors.WHITE,
                    ),

                    ft.Container(
                        width=70,
                        height=3,
                        bgcolor=ft.Colors.WHITE,
                    ),

                    ft.Text(
                        "Cotizaciones de monedas",
                        size=15,
                        font_family="Consolas",
                        color=ft.Colors.WHITE_60,
                    ),
                ],
                spacing=8,
            ),
            padding=ft.Padding.only(
                left=10,
                top=20,
                bottom=15,
            ),
        )

        column.controls.append(header)

        # ---------------------------------------------------------
        # SEPARATOR
        # ---------------------------------------------------------

        column.controls.append(
            ft.Divider(
                color=ft.Colors.WHITE_30,
                thickness=1,
            )
        )

        # ---------------------------------------------------------
        # CURRENCIES TITLE
        # ---------------------------------------------------------

        currencies_title = ft.Row(
            [
                ft.Text(
                    "CURRENCIES",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    font_family="Consolas",
                    color=ft.Colors.WHITE,
                ),

                ft.Container(
                    expand=True,
                ),

                ft.Text(
                    "EXCHANGE RATES",
                    size=12,
                    font_family="Consolas",
                    color=ft.Colors.WHITE_54,
                ),
            ],
        )

        column.controls.append(currencies_title)

        return column