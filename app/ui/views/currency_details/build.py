import flet as ft

from app.models.currency import Currency
from app.models.Trend import Trend
from .CurrencyCard import CurrencyCard

from math import pi
from typing import cast
import asyncio


class CurrencyPage:

    @staticmethod
    def build(
        page: ft.Page,
        currency_type: str,
        currencies: dict[str, Currency],
        on_return,
        on_reload
    ):
        """Builds the Currency Page and returns it."""

        currencies = dict(
            sorted(
                currencies.items(),
                key=lambda item:
                    float((item[1].buy or "0").replace(',', '.')),
                reverse=True
            )
        )

        # ---------------------------------------------------------
        # Main container
        # ---------------------------------------------------------

        main_content = ft.Row(
            expand=True,
            spacing=25,
            vertical_alignment=ft.CrossAxisAlignment.STRETCH
        )

        # ---------------------------------------------------------
        # Responsive sizes
        # ---------------------------------------------------------

        def get_icon_size():
            return max(
                14,
                min(page.width or 1 * 0.015, 30)
            )

        def get_sidebar_icon_size():
            return max(
                14,
                min(page.width * 0.02, 35)
            )

        # ---------------------------------------------------------
        # Sidebar
        # ---------------------------------------------------------

        home_button = ft.IconButton(
            icon=ft.Icons.HOME_OUTLINED,
            icon_size=get_sidebar_icon_size(),
        )

        main_page_list = ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            home_button
                        ]
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH
            ),
            width=100,
            expand=1,
            gradient=ft.LinearGradient(
                begin=ft.Alignment.TOP_LEFT,
                end=ft.Alignment.BOTTOM_RIGHT,
                colors=[
                    "#D67254",
                    "#B87C23",
                ],
            ),
        )

        # ---------------------------------------------------------
        # Houses / Quotes PAGE
        # ---------------------------------------------------------

        main_currencies_view = ft.Container(
            expand=30,
        )

        currencies_view = ft.Column(
            spacing=25,
            scroll=ft.ScrollMode.AUTO,
        )

        main_currencies_view.content = currencies_view

        main_content.controls.append(main_page_list)
        main_content.controls.append(main_currencies_view)


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

        currencies_view.controls.append(header)

        # ---------------------------------------------------------
        # Update button
        # ---------------------------------------------------------

        def UpdateButton_on_focus(e: ft.Event[ft.IconButton]):

            if e.data:
                e.control.icon_size = 30
                e.control.icon_color = ft.Colors.TEAL_600

            else:
                e.control.icon_size = 25
                e.control.icon_color = ft.Colors.WHITE_54

            e.control.update()

        async def UpdateButton_on_click(e: ft.Event[ft.IconButton]):

            current_rotation = cast(
                float,
                e.control.rotate or 0
            )

            e.control.rotate = current_rotation + 2 * pi

            e.control.update()

            await asyncio.sleep(0.3)

            on_reload(currency_type, 'reload')

        # ---------------------------------------------------------
        # Section title
        # ---------------------------------------------------------

        currencies_view.controls.append(
            ft.Row(
                [
                    ft.Text(
                        "Casas de cambio",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                    ),

                    ft.Container(
                        expand=True
                    ),

                    # Return Main Page Button
                    ft.Button(
                        ft.Container(
                            ft.Row(
                                [
                                    ft.Icon(
                                        ft.Icons.ARROW_BACK
                                    ),

                                    ft.Text(
                                        "Main Page",
                                        size=15,
                                        margin=ft.Margin.symmetric(
                                            vertical=12
                                        ),
                                        color=ft.Colors.LIGHT_BLUE_ACCENT_200,
                                    ),
                                ]
                            )
                        ),

                        margin=ft.Margin.symmetric(
                            horizontal=150
                        ),

                        on_click=on_return
                    ),

                    # Update Button
                    ft.IconButton(
                        icon=ft.Icons.RESTART_ALT,
                        icon_size=25,
                        on_hover=UpdateButton_on_focus,
                        icon_color=ft.Colors.WHITE_54,
                        on_click=UpdateButton_on_click,
                        rotate=0,
                        animate_rotation=ft.Animation(
                            duration=500,
                            curve=ft.AnimationCurve.EASE_OUT
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

            card = CurrencyCard.build(
                house_name,
                currency
            )

            cards.controls.append(card)

        currencies_view.controls.append(cards)

        # ---------------------------------------------------------
        # Return
        # ---------------------------------------------------------

        return ft.Container(
            expand=True,
            content=main_content,
        )