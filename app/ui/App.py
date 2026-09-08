import flet as ft
from pathlib import Path

# Services
from app.services.getData import GetData
from app.services.ScrapService import UpdteData


# UI
from app.ui.views.mainPage.CurrencyCard import CurrencyCard

from app.ui.views.mainPage.build import MainPage
from app.ui.views.currencyDetails.build import CurrencyPage




# Assets_DIR = Path(__file__).parent.parent / 'Assets'



CURRENCY_ORDER = [
    "USD",
    "EUR",
    "BRL",
    "ARS",
    "CLP",
]






class App:
    def __init__(self, currencies: dict) -> None:
        self.page = None
        self.currencies = currencies

    def main(self, page: ft.Page):
        self.page = page

        # page.fonts = {}



        self.config_page()
        self.show_main_page()
        # self.show_currency('USD')







    # ------------------------------------------------
    #   Page Rendering
    # ------------------------------------------------

    def show_main_page(self):
        if self.page is None:
            return
            
    
        page = self.page
        page.clean()

        main_content = MainPage().build()

        total_currencies = self.total_currencies()

        column = ft.Column(
            scroll=ft.ScrollMode.AUTO,
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            height= 800
        )


        container = ft.Container(
            content=column,
            padding=20,
            alignment=ft.Alignment.CENTER,
            expand=True,
        )

        main_content.controls.append(container)


        max_per_row = 6
        row = None

        for index, currency in enumerate(total_currencies):

            if index % max_per_row == 0:
                row = ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=15,
                )

                column.controls.append(row)

            if row == None: return

            row.controls.append(
                CurrencyCard(
                    currency,
                    self.show_currency
                ).build()
            )


        page.add(main_content)
        page.update()

    
    def show_currency(self, currency, arg = None):
        if self.page is None:
            return


        self.page.clean()


        if arg == 'reload':
            UpdteData()
            self.currencies = GetData()

        
        currency_fromAll_houses = {}

        for house in self.currencies:
            data = self.get_currency_from_house(house, currency)
            # print(data, house)
            if data is None:
                # print(house, self.get_currency_from_house(house, currency))
                
                continue

            currency_fromAll_houses[house] = self.get_currency_from_house(house, currency)


        main_content = CurrencyPage().build(currency, currency_fromAll_houses, self.show_main_page, self.show_currency)


        self.page.add(main_content)








    # --------------------------------------------------------
    # HELPERS
    # --------------------------------------------------------

    
    def get_currency_from_house(self,house, currency):
        if house in self.currencies and currency in self.currencies[house]:
            return self.currencies[house][currency]
        else:
            return None


    def total_currencies(self) -> list[str]:
        available = set()


        for exchange_house in self.currencies.values():
            available.update(exchange_house.keys())

        available= sorted(available)


        new_order = []


        # Appends all the main Currencys in CURRENCY_ORDER    || first ||
        for currency in range(len(CURRENCY_ORDER)):
            new_order.append(CURRENCY_ORDER[currency])

        # All the Others..,   except of the ones that already were append
        for currency in range(len(available) - len(CURRENCY_ORDER)):
            if available[currency] in CURRENCY_ORDER:
                continue

            new_order.append(available[currency])

        
        return new_order


    def config_page(self):
            if self.page == None:
                return

            
            self.page.title = 'Market Quotes'
            self.page.padding = 20
            self.page.theme_mode = ft.ThemeMode.DARK

            self.page.window.height = 800
            self.page.window.width = 1200

            self.page.window.maximized = True

            self.page.window.icon = 'icons/MainIcon.ico'
        




# app = App(GetData())

# ft.run(main=app.main)