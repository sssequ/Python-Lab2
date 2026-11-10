import re


# части адреса: шестнадцатеричная группа и адрес ipv4
HEX_GROUP = r"[0-9a-fA-F]{1,4}"
IPV4_PART = r"(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])"
IPV4_ADDRESS = rf"{IPV4_PART}(?:\.{IPV4_PART}){{3}}"
LAST_GROUPS = rf"(?:{HEX_GROUP}:{HEX_GROUP}|{IPV4_ADDRESS})"

# полная и сокращённые формы ipv6, включая адреса со встроенным ipv4
IPV6_PATTERN = re.compile(
    rf"(?:"
    rf"(?:{HEX_GROUP}:){{6}}{LAST_GROUPS}|"
    rf"::(?:{HEX_GROUP}:){{5}}{LAST_GROUPS}|"
    rf"(?:{HEX_GROUP})?::(?:{HEX_GROUP}:){{4}}{LAST_GROUPS}|"
    rf"(?:(?:{HEX_GROUP}:){{0,1}}{HEX_GROUP})?::(?:{HEX_GROUP}:){{3}}{LAST_GROUPS}|"
    rf"(?:(?:{HEX_GROUP}:){{0,2}}{HEX_GROUP})?::(?:{HEX_GROUP}:){{2}}{LAST_GROUPS}|"
    rf"(?:(?:{HEX_GROUP}:){{0,3}}{HEX_GROUP})?::{HEX_GROUP}:{LAST_GROUPS}|"
    rf"(?:(?:{HEX_GROUP}:){{0,4}}{HEX_GROUP})?::{LAST_GROUPS}|"
    rf"(?:(?:{HEX_GROUP}:){{0,5}}{HEX_GROUP})?::{HEX_GROUP}|"
    rf"(?:(?:{HEX_GROUP}:){{0,6}}{HEX_GROUP})?::"
    rf")"
)


# проверяет адрес целиком, а не только его часть
def is_valid_ipv6(address):
    return IPV6_PATTERN.fullmatch(address) is not None
