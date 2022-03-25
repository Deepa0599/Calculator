import Calculator
import unittest

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    return a / b


if __name__ == "__main__":
    num1 = int(input("Enter 1st number:"))
    num2 = int(input("Enter 2nd number:"))
    print(add(num1, num2))
    print(sub(num1, num2))
    print(mult(num1, num2))
    print(div(num1, num2))



class TestCalculator(unittest.TestCase):
    def test_add(self):
        x = 10
        y = 20
        result = Calculator.add(x, y)
        self.assertEqual(result, x + y)

    def test_sub(self):
        x = 10
        y = 20
        result = Calculator.sub(x, y)
        self.assertEqual(result, x - y)

    def test_multi(self):
        x = 10
        y = 20
        result = Calculator.mult(x, y)
        self.assertEqual(result, x * y)

    def test_div(self):
        x = 10
        y = 20
        result = Calculator.div(x, y)
        self.assertEqual(result, x / y)


if __name__ == "__main__":
    unittest.main()