from app.ui.App import App
import flet as ft

from app.services.getData import GetData

def print_houses(houses):
    print("=" * 50)
    print("              HOUSES DATA")
    print("=" * 50)

    for currency_id, data in houses.items():
        print(f"\n{currency_id.upper()} | {data['name']}")
        print("-" * 50)
        print(f"  Compra : {data['buy']:>8}  [{data['buy_trend']}]")
        print(f"  Venta  : {data['sell']:>8}  [{data['sell_trend']}]")

    print("=" * 50)



# print_houses(cotizations['Cambios-Chaco'])
# pprint(cotizations,width=15, compact=False,depth= 10, indent=5, sort_dicts=False)


print('Iniciando...')





app = App(GetData())

ft.run(main=app.main, assets_dir= 'assets')