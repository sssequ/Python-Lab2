import re


# одна группа ipv6: от одного до четырёх символов 0–9 и a–f
HEX_GROUP = r"[0-9a-fA-F]{1,4}"

# одно число ipv4: от 0 до 255
IPV4_PART = r"(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])"

# четыре числа ipv4, разделённые точками
IPV4_ADDRESS = rf"{IPV4_PART}(?:\.{IPV4_PART}){{3}}"

# конец адреса: две группы ipv6 или встроенный адрес ipv4
LAST_GROUPS = rf"(?:{HEX_GROUP}:{HEX_GROUP}|{IPV4_ADDRESS})"

# полная и сокращённые формы ipv6, включая адреса со встроенным ipv4
# :: заменяет одну или несколько нулевых групп, ipv4 занимает место двух групп
IPV6_PATTERN = re.compile(
    rf"(?:"
    rf"(?:{HEX_GROUP}:){{6}}{LAST_GROUPS}|"  # 8 групп, без сокращения
    rf"::(?:{HEX_GROUP}:){{5}}{LAST_GROUPS}|"  # :: в начале, после него 7 групп
    rf"(?:{HEX_GROUP})?::(?:{HEX_GROUP}:){{4}}{LAST_GROUPS}|"  # до :: не больше 1 группы, после — 6
    rf"(?:(?:{HEX_GROUP}:){{0,1}}{HEX_GROUP})?::(?:{HEX_GROUP}:){{3}}{LAST_GROUPS}|"  # до :: не больше 2 групп, после — 5
    rf"(?:(?:{HEX_GROUP}:){{0,2}}{HEX_GROUP})?::(?:{HEX_GROUP}:){{2}}{LAST_GROUPS}|"  # до :: не больше 3 групп, после — 4
    rf"(?:(?:{HEX_GROUP}:){{0,3}}{HEX_GROUP})?::{HEX_GROUP}:{LAST_GROUPS}|"  # до :: не больше 4 групп, после — 3
    rf"(?:(?:{HEX_GROUP}:){{0,4}}{HEX_GROUP})?::{LAST_GROUPS}|"  # до :: не больше 5 групп, после — 2
    rf"(?:(?:{HEX_GROUP}:){{0,5}}{HEX_GROUP})?::{HEX_GROUP}|"  # до :: не больше 6 групп, после — 1
    rf"(?:(?:{HEX_GROUP}:){{0,6}}{HEX_GROUP})?::"  # :: в конце, до него не больше 7 групп
    rf")"
)


# проверяет адрес целиком, а не только его часть
def is_valid_ipv6(address):
    return IPV6_PATTERN.fullmatch(address) is not None


# ищет в тексте адреса, отделённые пробелами или знаками препинания
def find_ipv6_addresses(text):
    candidates = re.findall(r"[\w:.]+", text)
    addresses = []
    for candidate in candidates:
        candidate = candidate.strip(".")
        if is_valid_ipv6(candidate):
            addresses.append(candidate)
    return addresses
