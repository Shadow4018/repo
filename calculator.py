class Calculator:
    def __init__(self):
        print("Calculator initialized.")

    def add(self, a, b):
        """Додавання"""
        return a + b

    def subtract(self, a, b):
        """Віднімання"""
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        """Ділення з перевіркою на 0"""
        """Ділення з перевіркою на 0"""
        """Ділення з перевіркою на 0"""
        """Ділення з перевіркою на 0"""
        

    def power(self, a, b):
        """Піднесення до степеня"""
        

    def modulo(self, a, b):
        """Остача від ділення"""
        


# Приклад використання (можна помістити у файл main.py)
if __name__ == "__main__":
    calc = Calculator()

    print("5 + 3 =", calc.add(5, 3))
    print("5 - 3 =", calc.subtract(5, 3))
    print("5 * 3 =", calc.multiply(5, 3))
    print("10 / 2 =", calc.divide(10, 2))
    print("2 ** 4 =", calc.power(2, 4))
    print("10 % 3 =", calc.modulo(10, 3))
