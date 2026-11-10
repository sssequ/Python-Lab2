import unittest

from ipv6 import find_ipv6_addresses, is_valid_ipv6


# проверяет правильные и неправильные формы ipv6
class TestIPv6(unittest.TestCase):
    def test_full_addresses(self):
        addresses = [
            "2001:0db8:0000:0000:0000:0000:0000:0001",
            "ABCD:EF01:2:3:4:5:6:7",
            "1:2:3:4:5:6:192.0.2.1",
        ]
        for address in addresses:
            with self.subTest(address=address):
                self.assertTrue(is_valid_ipv6(address))

    def test_shortened_addresses(self):
        addresses = [
            "::", "::1", "::1:2:3:4:5:6:7", "1::2:3:4:5:6:7",
            "1:2::3:4:5:6", "1:2:3::4:5:6", "1:2:3:4::5:6",
            "1:2:3:4:5::6", "1:2:3:4:5:6::7", "1:2:3:4:5:6:7::",
            "2001:db8::1", "::ffff:192.0.2.1",
        ]
        for address in addresses:
            with self.subTest(address=address):
                self.assertTrue(is_valid_ipv6(address))

    def test_invalid_addresses(self):
        addresses = [
            "", "1:2:3:4:5:6:7", "1:2:3:4:5:6:7:8:9",
            "2001::db8::1", "12345::1", "gggg::1", ":1:2:3:4:5:6:7",
            "1:2:3:4:5:6:7:8:", "1:2:3:4:5:6:7::8",
            "::ffff:256.0.2.1", "::ffff:192.168.01.1", "::1extra",
        ]
        for address in addresses:
            with self.subTest(address=address):
                self.assertFalse(is_valid_ipv6(address))

    # поиск возвращает адреса целиком и сохраняет их порядок
    def test_find_addresses(self):
        text = "адреса: (::1), 2001:db8::1. ::ffff:192.0.2.1; ::1"
        self.assertEqual(
            find_ipv6_addresses(text),
            ["::1", "2001:db8::1", "::ffff:192.0.2.1", "::1"],
        )

    def test_find_no_addresses(self):
        text = "нет адресов: 2001::db8::1 12345::1 1:2:3:4:5:6:7:8:9"
        self.assertEqual(find_ipv6_addresses(text), [])
        self.assertEqual(find_ipv6_addresses(""), [])


if __name__ == "__main__":
    unittest.main()
