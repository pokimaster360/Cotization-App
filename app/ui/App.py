import flet as ft
from pathlib import Path

# Services
from app.services.getData import GetLatestData
from app.services.ScrapService import UpdteData


# Models
from app.models.currency import Currency


# UI
from app.ui.views.main_page.CurrencyCard import CurrencyCard

from app.ui.views.main_page.build import MainPage
from app.ui.views.currency_details.build import CurrencyPage




# Assets_DIR = Path(__file__).parent.parent / 'Assets'



CURRENCY_ORDER = [
    "USD",
    "EUR",
    "BRL",
    "ARS",
    "CLP",
]





debugging = False




class App:
    def __init__(self) -> None:
        self.page = None
        self.currencies: dict[tuple[str, str], Currency] = GetLatestData()      #("MyD","USD") = Currency
        self.actual_page = 'main'

        if debugging: print(f'File: {__file__} | Obtained Data: {self.currencies}')

    def main(self, page: ft.Page):
        self.page = page

        # page.fonts = {}



        self.config_page()
        # self.show_main_page()
        self.show_currency('USD')







    # ------------------------------------------------
    #   Page Rendering
    # ------------------------------------------------

    def show_main_page(self):
        if self.page is None:
            return
            
    
        page = self.page
        page.clean()

        main_content = MainPage().build()

        total_currencies = self.available_currencies()

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

    
    def show_currency(self, currency_to_show, arg = None):
        if self.page is None:
            return


        self.page.clean()
        self.actual_page = 'currency'

        if arg == 'reload':
            UpdteData()
            self.currencies = GetLatestData()

            if debugging: print(f'File: {__file__} | Obtained Data: {self.currencies}')

        
        currency_fromAll_houses = {}

        for house in self.available_houses():         #("MyD","USD") = Currency
            # print(house)
            data = self.house_data(house, currency_to_show)
            # print(data, house)
            if data is None:
                print(f'Trying to show Currency Page, but - Row - Data is None: {house} |  {__file__}')
                
                continue

            currency_fromAll_houses[house] = data


        main_content = CurrencyPage().build(self.page, currency_to_show, currency_fromAll_houses, self.show_main_page, self.show_currency)


        self.page.add(main_content)








    # --------------------------------------------------------
    # HELPERS
    # --------------------------------------------------------

    # get Currency from a House with a Specific Currency: USD, EUR..
    def house_data(self,house, currency) -> Currency | None:
        '''
        Gets the Currency Data, from a especific House, and his specific currency
        '''

        return self.currencies.get((house, currency))

    # All the total Currencies that are Available, USD, EUR etc
    def available_currencies(self) -> list[str]:
        '''
        Gets all available Houses in the Database
        '''
        available = set()


        for exchange_house in self.currencies:      # ("Ueno", "USD") = Currency
            available.update(exchange_house[1])

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

    # All The Houses that are in the DataBase Currently
    def available_houses(self) -> list[str]:
        available = set()

        for exchange_house in self.currencies:
            # print(exchange_house[0])
            available.update([exchange_house[0]])

        return list(available)

    def config_page(self):
        if self.page == None:
            return

        
        self.page.title = 'Market Quotes'
        # self.page.padding = 20
        self.page.theme_mode = ft.ThemeMode.DARK

        self.page.window.height = 800
        self.page.window.width = 1200

        self.page.window.maximized = True

        self.page.window.icon = 'icons/MainIcon.ico'

        self.page.window.update()
        




# app = App(GetData())

# ft.run(main=app.main)