from pathlib import Path
import importlib.util
# from dataclasses import dataclass, asdict


# from app.services.currency_conversion import Currencies_To_Dic
from app.repositories.currency import CurrencyRepository




debugging = False




CURRENT_DIR = Path(__file__)
BASE_DIR =  CURRENT_DIR.parent.parent
DATA_DIR = BASE_DIR / 'data' / 'market-rates.json'
SCRAPERS_DIR = BASE_DIR / 'scrapers'






repository = CurrencyRepository()





def UpdteData():
    '''
    It Updates the data from data/market-rates.json, within all the house exchanges from obtain_exchanges
    '''
    # with open('program/core/dataBase.json', 'r', encoding= 'utf-8') as file:
    #     dataBase = json.load(file)


    houses = {}
    currencies = {}


    carpeta = SCRAPERS_DIR

    for archivo in carpeta.glob('*.py'):
        if archivo.name == '__init__.py':
            continue
        
        # Importar el módulo
        spec = importlib.util.spec_from_file_location(archivo.stem, archivo)

        if spec is None or spec.loader is None:
            print('Spec is None')

            continue



        
        if debugging: print(spec)



        
        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo)
        
        # Ejecutar get_cotization() si existe
        if hasattr(modulo, 'get_cotization'):
            currencies = modulo.get_cotization()

            # print(modulo, currencies)

            if currencies is not None:
                currencies = {
                    'USD': currencies['USD'],
                    'EUR': currencies['EUR'],
                }
            else:
                print(f'Empty Currencies Dict: {modulo}, ScrapService File: {__file__}')
                currencies = {}


            houses[archivo.stem] = currencies
            # print(houses)

            
        else:
            print(f'module: {modulo} unkown Function while Scraping {__file__}')



    for currencies in houses.values():
        for currency in currencies.values():
            # print(currency)
            repository.save(currency)


    if debugging:
        print('dumpeado')