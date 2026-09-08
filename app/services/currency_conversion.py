from app.models.Currency import Currency
from app.models.Trend import Trend

from dataclasses import asdict



def ConvertCurrencies(data: dict):
    '''
    Convert an Diccionary into an obj Currency
    example:
    'soup' = {
        "name" = ...    -->   'soup' = Currrency(...)
    }
    '''
    currencies = {}


    # "CambiosChaco": {
    #     "USD": {
    #         "name": "USD",
    #         "buy": "5870",
    #         "sell": "5940",
    #         "buy_trend": 1,
    #         "sell_trend": 0
    #     }
    # },


    
    # Source -> Casa =  "cambiosChaco"
    # Data -> Casa.Currencies =  {USD, RLS...}

    for source, data in data.items():
        currencies[source] = {}

        if data is None:
            continue
        

        for key in data:
            data_currency = data[key]

            currencies[source][key] = Currency(
                name=           data_currency['name'],
                buy=            data_currency['buy'],
                sell=           data_currency['sell'],
                buy_trend=      (Trend(data_currency['buy_trend'])          if data_currency['buy_trend'] is not None else None),
                sell_trend=     (Trend(data_currency['sell_trend'])         if data_currency['sell_trend'] is not None else None),
                exchange_type=           data_currency['exchange_type']
            )

    return currencies


def Currencies_To_Dic(data: dict[str,Currency]):
    conversion_data = {}

    # print(data)

    # graps properties:   name, buy, sell, ...

    if data is None:
        return

    for item in data:
        conversion_data[item] = asdict(data[item])

        # print(item ,conversion_data[item])

        conversion_data[item]['exchange_type'] = data[item].exchange_type.value

        # print(conversion_data[item]['exchange_type'])


    return conversion_data