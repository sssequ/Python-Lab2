from ipv6 import is_valid_ipv6


# точка входа: ввод адреса и вывод результата
def main():
    address = input("введите ipv6-адрес: ").strip()
    if is_valid_ipv6(address):
        print("адрес корректен")
    else:
        print("адрес некорректен")


if __name__ == "__main__":
    main()
