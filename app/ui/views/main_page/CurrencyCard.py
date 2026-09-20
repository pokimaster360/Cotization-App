import flet as ft


class CurrencyCard:

    def __init__(
        self,
        currency: str,
        on_click
    ) -> None:

        self.currency = currency
        self.on_click = on_click

    def build(self) -> ft.Control:
        animation_config = ft.Animation(
            350, ft.AnimationCurve.EASE_OUT
        )
        # ---------------------------------------------------------
        # Elementos que vamos a modificar con el hover
        # ---------------------------------------------------------

        icon_container = ft.Container(
            width=42,
            height=42,
            border_radius=10,
            bgcolor=ft.Colors.WHITE_10,
            alignment=ft.Alignment.CENTER,
            animate= animation_config

        )

        icon = ft.Icon(
            ft.Icons.CURRENCY_EXCHANGE,
            size=23,
            color=ft.Colors.WHITE_70,
            animate_opacity= animation_config
        )

        icon_container.content = icon

        arrow = ft.Icon(
            ft.Icons.ARROW_FORWARD_IOS,
            size=15,
            color=ft.Colors.WHITE_30,
        )

        card_content = ft.Container(
            width=240,
            height=135,
            padding=20,
            border_radius=14,

            bgcolor=ft.Colors.WHITE_10,

            border=ft.Border.all(
                width=1,
                color=ft.Colors.WHITE_12,
            ),

            content=ft.Column(
                [
                    ft.Row(
                        [
                            icon_container,
                            ft.Container(expand=True),
                            arrow,
                        ],
                    ),

                    ft.Container(height=5),

                    ft.Text(
                        self.currency,
                        size=27,
                        weight=ft.FontWeight.BOLD,
                        font_family="Consolas",
                        color=ft.Colors.WHITE,
                    ),

                    ft.Text(
                        "Ver cotización",
                        size=12,
                        color=ft.Colors.WHITE_54,
                    ),
                ],
                spacing=0,
            ),

            on_click=lambda e: self.on_click(self.currency),
            animate= animation_config

        )



        card = ft.Card(
            elevation=3,
            margin=5,
            content=card_content,
        )

        


        # ---------------------------------------------------------
        # Hover
        # ---------------------------------------------------------

        def on_hover(e: ft.Event[ft.Container]):
            if e.data == True:
                # Mouse entra
                card_content.border = ft.Border.all(
                    width=1,
                    color=ft.Colors.WHITE_54,
                )

                card.elevation = 50

                card_content.bgcolor = ft.Colors.WHITE_10

                icon_container.bgcolor = ft.Colors.WHITE_24
                icon.color = ft.Colors.WHITE

                arrow.color = ft.Colors.WHITE_70

            else:
                # Mouse sale
                card_content.border = ft.Border.all(
                    width=1,
                    color=ft.Colors.WHITE_12,
                )


                card.elevation = 3

                card_content.bgcolor = ft.Colors.WHITE_10

                icon_container.bgcolor = ft.Colors.WHITE_10
                icon.color = ft.Colors.WHITE_70

                arrow.color = ft.Colors.WHITE_30

            card_content.update()

        card_content.on_hover = on_hover

        return card