import unittest

def fib(n):
    n = abs(n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


class MyTest(unittest.TestCase):
    def test_type_error(self):
        self.assertRaises(TypeError, fib, None)

    def test_value_error(self):
        self.assertRaises(TypeError, fib, 'aoeu')

    def test_number_is_zero(self):
        self.assertEqual(fib(0), 0)

    def test_number_is_one(self):
        self.assertEqual(fib(1), 1)

    def test_number_is_ten(self):
        self.assertEqual(fib(10), 55)


if __name__ == "__main__":
    unittest.main()
