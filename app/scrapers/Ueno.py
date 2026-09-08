import re

import requests
from bs4 import BeautifulSoup

from app.models.Currency import Currency
from app.models.ExchangeType import ExchangeType


def parse_price(value: str) -> int:
    numbers = re.sub(r"\D", "", value)

    if not numbers:
        return 0

    return int(numbers)






def get_cotization(
    url="https://www.ueno.com.py/cambio-de-moneda/"
):
    """
    Gets the actual cotizations from the App (not cash).
    """

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        currencies = {}

        cards = soup.select(".divisas-card")

        for card in cards:

            currency = card.get("data-currency")
            subtitle = card.get("data-subtitle")

            if not currency or not subtitle:
                continue
            if currency == 'EUR' and subtitle == 'en transferencias':
                continue



            
            # Buscar Compra
            buy_label = None

            for span in card.find_all("span"):
                if span.get_text(strip=True) == "Compra":
                    buy_label = span
                    break

            # Buscar Venta
            sell_label = None



            for span in card.find_all("span"):
                if span.get_text(strip=True) == "Venta":
                    sell_label = span
                    break

            
            if not buy_label or not sell_label:
                continue




            
            buy_span = buy_label.find_next_sibling("span")
            sell_span = sell_label.find_next_sibling("span")

            if not buy_span or not sell_span:
                continue

            buy = str(parse_price(buy_span.get_text(strip= True)))
            sell = str(parse_price(sell_span.get_text(strip= True)))

            subtitle = subtitle.split("en ")[-1].replace('-', '')    #type: ignore




            exchange_type = ExchangeType.CASH


            # solo el Dolar tiene la opcion de -cash y -app. Para ponerle Nombre USD-efectivo
            if currency != 'EUR':
                currency = f"{currency}-{subtitle}"

            # ponerle el exchange_type si es de la app
            if subtitle.find('app'):
                exchange_type = ExchangeType.APP



            currencies[currency] = Currency(
                name=currency,  #type: ignore
                buy=buy,
                sell=sell,
                buy_trend=None,
                sell_trend=None,
                exchange_type= exchange_type
            )

        # Ordenar por precio de compra
        currencies = dict(
            sorted(
                currencies.items(),
                key=lambda e: e[1].buy
                if e[1].buy
                else 0,
                reverse=True
            )
        )


        usd_cash = 'USD-efectivo'
        usd_app = 'USD-tu app'


        # Agarra el mas grande entre USD-app y USD-cash y solo deja en currencies como USD
        if usd_cash in currencies and usd_app in currencies:
            usd_app_value = currencies.pop(usd_app)
            usd_cash_value = currencies.pop(usd_cash)


            if usd_app_value.buy > usd_cash_value.buy:
                currencies['USD'] = usd_app_value

            else:
                currencies['USD'] = usd_cash_value


        
        return currencies

    except requests.RequestException as e:
        print(f"Error to get the page: {e}")
        return None

    except Exception as e:
        print(f"Error: {e} in {__file__}")
        return None


def test_get_cotization_from_app():
    result = get_cotization()

    

    if result:
        print("Cotizaciones desde la App:")
        print(result)
        # for currency, data in result.items():
        #     print(
        #         f"{currency}: "
        #         f"Compra = {data.buy}, "
        #         f"Venta = {data.sell}"
        #     )

    else:
        print("No se pudieron obtener las cotizaciones")


if __name__ == "__main__":
    test_get_cotization_from_app()