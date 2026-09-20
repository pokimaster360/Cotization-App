from app.ui.App import App
from app.data.connection import initialize_database
import flet as ft


def print_houses(houses):
    print("=" * 50)
    print("              HOUSES DATA")
    print("=" * 50)

    for currency_id, data in houses.items():
        print(f"\n{currency_id.upper()} | {data['name']}")
        print("-" * 50)
        print(f"  buy : {data['buy']:>8}  [{data['buy_trend']}]")
        print(f"  sell  : {data['sell']:>8}  [{data['sell_trend']}]")

    print("=" * 50)







def main():
    initialize_database()

    app = App()

    ft.run(main=app.main, assets_dir= 'app/assets')


if __name__ == '__main__':
    main()