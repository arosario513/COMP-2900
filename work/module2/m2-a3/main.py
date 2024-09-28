#!venv/bin/python3
'''Module 2, Lesson 4, Exercise 3'''

from prettytable import PrettyTable


table: PrettyTable = PrettyTable()
table.field_names = ["Product", "Price (USD)"]

products: dict[str, float] = {
    "Playstation 5 Pro": 699.99,
    "Playstation 5 Diskless": 449.99,
    "Xbox Series X": 499.99
}


def show_table(ptable: PrettyTable, d: dict) -> None:
    '''Prints the dictionary as a Table'''
    ptable.clear_rows()
    for product, price in d.items():
        ptable.add_row([product, f"${price}"])
    print(table)


def main() -> None:
    '''Main function'''

    show_table(table, products)

    products.update({"Nintendo Switch": 299.99})
    products.pop("Playstation 5 Diskless")

    show_table(table, products)

    products.update({"Nintendo Switch": 239.99})

    show_table(table, products)


if __name__ == "__main__":
    main()
