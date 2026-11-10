import json

from ipv6 import find_ipv6_addresses, is_valid_ipv6


# точка входа: консольное меню, ввод и вывод
MENU = """
1. проверить ipv6-адрес
2. найти ipv6-адреса в файле
0. выйти из программы
"""


# сохраняет результат последнего действия в json
def save_result(result):
    with open("result.json", "w", encoding="utf-8") as file:
        json.dump(result, file, ensure_ascii=False, indent=4)
    print("результат сохранён в result.json")


def main():
    while True:
        try:
            print(MENU)
            choice = input("выберите действие: ").strip()

            if choice == "0":
                print("программа завершена")
                break

            elif choice == "1":
                address = input("введите ipv6-адрес: ").strip()
                is_valid = is_valid_ipv6(address)
                if is_valid:
                    print("адрес корректен")
                else:
                    print("адрес некорректен")
                save_result({"адрес": address, "корректен": is_valid})

            elif choice == "2":
                filename = input("путь к файлу: ").strip()
                with open(filename, encoding="utf-8") as file:
                    addresses = find_ipv6_addresses(file.read())
                if not addresses:
                    print("ipv6-адреса не найдены")
                for address in addresses:
                    print(address)
                save_result({"файл": filename, "адреса": addresses})

            else:
                print("такого действия нет, выберите пункт меню")

        # ошибки не закрывают меню, можно попробовать ещё раз
        except (OSError, UnicodeError) as error:
            print(f"ошибка работы с файлом: {error}")
        except (EOFError, KeyboardInterrupt):
            print("\nпрограмма завершена")
            break


if __name__ == "__main__":
    main()
