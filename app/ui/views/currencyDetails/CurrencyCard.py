import flet as ft

from app.models.currency import Currency
from app.models.Trend import Trend

class CurrencyCard:
    @staticmethod
    def build(house_name: str,currency: Currency) -> ft.Card:
        def trend_icon(trend: Trend | None):
                if trend == Trend.UP:
                    return ft.Icons.TRENDING_UP
    
                if trend == Trend.DOWN:
                    return ft.Icons.TRENDING_DOWN
    
                if trend == Trend.EQUAL:
                    return ft.Icons.REMOVE
    
                return ft.Icons.HORIZONTAL_RULE
    
        def trend_text(trend: Trend | None):
            if trend == Trend.UP:
                return "Subiendo"

            if trend == Trend.DOWN:
                return "Bajando"

            if trend == Trend.EQUAL:
                return "Sin cambios"

            return "Sin datos"

        def trend_color(trend: Trend | None):
            if trend == Trend.UP:
                return ft.Colors.GREEN_400

            if trend == Trend.DOWN:
                return ft.Colors.RED_400

            if trend == Trend.EQUAL:
                return ft.Colors.AMBER_400

            return ft.Colors.GREY_400
        


        buy_color = trend_color(currency.buy_trend)
        sell_color = trend_color(currency.sell_trend)

        exchange_type_icon = ft.Icon(
            ft.Icons.MONETIZATION_ON       if currency.exchange_type == 'cash' else ft.Icons.APP_SHORTCUT,
            color= ft.Colors.GREEN_200  if currency.exchange_type == 'cash' else ft.Colors.YELLOW_900,
            size=  20
        )



        card = ft.Card(
            elevation=4,
        )


        # House name
        row_house_name = ft.Row(
            [
                ft.Icon(
                    ft.Icons.STORE,
                    size=22,
                    color=ft.Colors.BLUE_300,
                ),
                ft.Text(
                    house_name,
                    size=18,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Row(
                    [
                        ft.Text(
                            currency.exchange_type, #type: ignore
                            size = 13,
                            weight= ft.FontWeight.W_400,
                        ),
                        exchange_type_icon
                    ],
                    alignment= ft.MainAxisAlignment.END,
                    expand= True
                )
            ],
            spacing=10,
        )
        column_divider =  ft.Divider(
            color=ft.Colors.WHITE_10,
        )
        # Buy / Sell
        row_buy_sell =  ft.Row(
            [
                ft.Column(
                    [
                        ft.Text(
                            "Compra",
                            size=13,
                            color=ft.Colors.WHITE_60,
                        ),
                        ft.Text(
                            currency.buy or "---",
                            size=25,
                            weight=ft.FontWeight.BOLD,
                        ),
                        # Si es en Efectivo o App
                        ft.Row(
                            [
                                ft.Icon(
                                    trend_icon(
                                        currency.buy_trend
                                    ),
                                    size=16,
                                    color=buy_color,
                                ),
                                ft.Text(
                                    trend_text(
                                        currency.buy_trend
                                    ),
                                    size=12,
                                    color=buy_color,
                                ),
                            ],
                            spacing=4,
                        ),
                    ],
                    spacing=4,
                ),

                ft.Container(
                    width=1,
                    height=80,
                    bgcolor=ft.Colors.WHITE_10,
                ),
                

                ft.Column(
                    [
                        ft.Text(
                            "Venta",
                            size=13,
                            color=ft.Colors.WHITE_60,
                        ),
                        ft.Text(
                            currency.sell or "---",
                            size=25,
                            weight=ft.FontWeight.BOLD,
                        ),
                        ft.Row(
                            [
                                ft.Icon(
                                    trend_icon(
                                        currency.sell_trend
                                    ),
                                    size=16,
                                    color=sell_color,
                                ),
                                ft.Text(
                                    trend_text(
                                        currency.sell_trend
                                    ),
                                    size=12,
                                    color=sell_color,
                                ),
                            ],
                            spacing=4,
                        ),
                    ],
                    spacing=4,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )



        
        card_container = ft.Container(
            width=330,
            padding=22,
            border_radius=14,
            bgcolor=ft.Colors.WHITE_10,
            content= ft.Column(
                controls= [
                   row_house_name,
                   column_divider,
                   row_buy_sell
                ]
            )
        )



        card.content = card_container




        return card