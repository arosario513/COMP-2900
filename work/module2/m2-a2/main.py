#!venv/bin/python
'''cities'''


def main() -> None:
    '''main function'''

    cities: tuple = ("Barceloneta", "Ponce", "San Juan",
                     "Vega Baja", "Guaynabo")
    cities2: tuple = ("Cabo Rojo", "Arecibo", "Aguadilla")
    first_two_cities: tuple = cities[:2]
    all_cities: tuple = cities + cities2

    print(f"Cities 1:        {cities}")
    print(f"Cities 2:        {cities2}")

    print(f"City at index 2: {cities[2]}")
    print(f"First 2 cities:  {first_two_cities}")
    print(f"All cities:      {all_cities}")


if __name__ == "__main__":
    main()

# Tuples are immutable, which means they can't be modified
