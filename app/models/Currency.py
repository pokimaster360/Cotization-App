from dataclasses import dataclass
from .Trend import Trend
from .ExchangeType import ExchangeType

@dataclass
class Currency:
    name: str
    buy: str | None
    sell: str | None
    buy_trend: Trend | None
    sell_trend: Trend | None
    exchange_type: ExchangeType = ExchangeType.CASH