import unittest
from main import remainder  # add, subtract, multiply, divide


class TestRemainder(unittest.TestCase):
    def test_remainder_success(self):
        # Проверяем корректные результаты
        self.assertEqual(remainder(10, 3), 1)
        self.assertEqual(remainder(15, 5), 0)
        self.assertEqual(remainder(7, 2), 1)

    def test_remainder_by_zero(self):
        # Проверяем выброс ошибки при делении на 0
        with self.assertRaises(ValueError):
            remainder(10, 0)


if __name__ == '__main__':
    unittest.main()


# class TestMath(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(add(2, 5), 7)
#         self.assertNotEqual(add(3, 5), 7)
#
#     def test_subtract(self):
#         self.assertEqual(subtract(7, 4), 3)
#         self.assertEqual(subtract(4, 2), 1)
#
#     def test_multiply(self):
#         self.assertEqual(multiply(2, 5), 10)
#         self.assertEqual(multiply(3, 6), 18)
#
#     def test_divide(self):
#         self.assertEqual(divide(4, 2), 2)
#         self.assertEqual(divide(20, 5), 15)
