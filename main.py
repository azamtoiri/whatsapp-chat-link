import requests


def get_link(number: int):
    r = requests.get(f"https://wa.me/{number}")
    print(r.url)


def main():
    number = int(input("Enter number: "))
    get_link(number)


if __name__ == "__main__":
    main()
