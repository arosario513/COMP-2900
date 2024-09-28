# venv/bin/python3
'''caesar chipher'''

from menu import Menu


def main() -> None:
    '''main function'''
    try:
        menu: Menu = Menu()
        menu.run()

    except ValueError:
        print("[-] Enter a valid input")
    except KeyboardInterrupt:
        print("\n[!] Exiting...")


if __name__ == "__main__":
    main()
