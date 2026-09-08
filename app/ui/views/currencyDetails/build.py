import flet as ft

from app.models.Currency import Currency
from app.models.Trend import Trend

from .CurrencyCard import CurrencyCard


from math import pi
from typing import cast

import asyncio



class CurrencyPage:

    @staticmethod
    def build(currency_type: str, currencies: dict[str, Currency], on_return, on_reload):
        """Builds the Currency Page and returns it."""



        currencies = dict(
            sorted(
                currencies.items(),
                key=lambda item:
                    # Agarra el Currency de cada Casa, si es None el Buy, lo pone como "0".
                    # Y le cambia la "," por un "." y dsps lo convierte en Numero para que el Sorted Funcione
                    float((item[1].buy or "0").replace(',', '.')),
                reverse= True
            )
        )






        # ---------------------------------------------------------
        # Main container
        # ---------------------------------------------------------

        main_content = ft.Column(
            spacing=25,
            scroll=ft.ScrollMode.AUTO,
        )

        # ---------------------------------------------------------
        # Header
        # ---------------------------------------------------------

        header = ft.Container(
            content=ft.Row(
                [
                    ft.Column(
                        [
                            ft.Text(
                                "Cotización",
                                size=16,
                                color=ft.Colors.WHITE_70,
                            ),
                            ft.Text(
                                currency_type,
                                size=42,
                                weight=ft.FontWeight.BOLD,
                                font_family="Consolas",
                                color=ft.Colors.WHITE,
                            ),
                        ],
                        spacing=2,
                    ),
                ],
            ),
            padding=ft.Padding.symmetric(
                horizontal=30,
                vertical=25,
            ),
            border_radius=16,
            gradient=ft.LinearGradient(
                begin=ft.Alignment.TOP_LEFT,
                end=ft.Alignment.BOTTOM_RIGHT,
                colors=[
                    "#545DD6",
                    "#7B4FD4",
                ],
            ),
        )

        main_content.controls.append(header)

        # ---------------------------------------------------------
        # Section title
        # ---------------------------------------------------------
        

        # update_icon = ft.Icon(
        #     ft.Icons.RESTART_ALT,
        #     size= 20
        # )



        def UpdateButton_on_focus(e: ft.Event[ft.IconButton]):
            if e.data:
                e.control.icon_size = 30
                e.control.icon_color = ft.Colors.TEAL_600
            else:
                e.control.icon_size = 25
                e.control.icon_color = ft.Colors.WHITE_54

            e.control.update()

        async def UpdateButton_on_click(e: ft.Event[ft.IconButton]):
            current_rotation = cast(float, e.control.rotate or 0)
            e.control.rotate = current_rotation + 2 * pi

            e.control.update()


            await asyncio.sleep(0.3)

            on_reload(currency_type, 'reload')


        main_content.controls.append(
            ft.Row(
                [
                    ft.Text(
                        "Casas de cambio",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Container(expand=True),
                    ft.Button(
                        ft.Text('Main Page', size= 15, margin=10),
                        margin= ft.Margin.symmetric(horizontal= 150),
                        on_click= on_return
                    ),
                    ft.IconButton(
                        icon= ft.Icons.RESTART_ALT,
                        icon_size= 25,
                        on_hover= UpdateButton_on_focus,
                        icon_color = ft.Colors.WHITE_54,
                        on_click= UpdateButton_on_click,
                        rotate= 0,
                        animate_rotation= ft.Animation(
                            duration= 500,
                            curve= ft.AnimationCurve.EASE_OUT
                        )

                    ),
                    ft.Text(
                        f"{len(currencies)} casas",
                        size=14,
                        color=ft.Colors.WHITE_60,
                    ),
                ]
            )
        )


        # ---------------------------------------------------------
        # Currency cards
        # ---------------------------------------------------------

        cards = ft.Row(
            wrap=True,
            spacing=15,
            run_spacing=15,
        )

        for house_name, currency in currencies.items():
            card = CurrencyCard.build(house_name, currency)


            cards.controls.append(card)

        main_content.controls.append(cards)



       

        return ft.Container(
            expand=True,
            content=main_content,
        )