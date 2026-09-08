from pathlib import Path
from app.models.currency import Currency
import json


from app.services.currency_conversion import ConvertCurrencies


FILE_DIR = Path(__file__).resolve()
BASE_DIR = FILE_DIR.parent.parent

DATA_DIR = BASE_DIR / 'data' / 'market-rates.json'



def GetData() -> dict:

    with open(DATA_DIR, 'r', encoding= 'utf-8') as file:
        database = json.load(file)

    database = ConvertCurrencies(database)    


    return database