from pathlib import Path
import importlib.util
from dataclasses import dataclass, asdict


from app.services.currency_conversion import Currencies_To_Dic


import json



debugging = False




CURRENT_DIR = Path(__file__)
BASE_DIR =  CURRENT_DIR.parent.parent
DATA_DIR = BASE_DIR / 'data' / 'market-rates.json'
SCRAPERS_DIR = BASE_DIR / 'scrapers'



def UpdteData():
    '''
    It Updates the data from data/market-rates.json, within all the house exchanges from obtain_exchanges
    '''
    # with open('program/core/dataBase.json', 'r', encoding= 'utf-8') as file:
    #     dataBase = json.load(file)


    houses = {}


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


            currencies = {
                'USD': currencies['USD']
            }


            currencies = Currencies_To_Dic(currencies)


            houses[archivo.stem] = currencies

            
        else:
            print(f'module: {modulo} unkown Function while Scraping {__file__}')


    with open(DATA_DIR, 'w', encoding= 'utf-8') as file:
            

        # for key, currency in currencys.items():
        #     print("KEY:", key)
        #     print("VALUE:", currency)
        #     print("TYPE:", type(currency))

        json.dump(houses, file, indent= 4, ensure_ascii= False)

        if debugging:
            print('dumpeado')