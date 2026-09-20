from pathlib import Path
from app.models.currency import Currency


# from app.services.currency_conversion import ConvertCurrencies
from app.repositories.currency import CurrencyRepository


FILE_DIR = Path(__file__).resolve()
BASE_DIR = FILE_DIR.parent.parent

DATA_DIR = BASE_DIR / 'data' / 'market-rates.json'



repository = CurrencyRepository()


def GetAllData() -> list[Currency]:
    return repository.get_all()

def GetLatestData() -> dict[tuple[str,str], Currency]:
    return repository.get_current()