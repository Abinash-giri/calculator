import math

class Calculator:
    """Calculator class"""
    def __init__(self, value1, value2) -> None:
        self._v1 = value1
        self._v2 = value2

    def addition(self):
        return self._v1 + self._v2

    def substraction(self):
        return self._v1 - self._v2

    def multiplication(self):
        return self._v1 * self._v2

    def divison(self):
        return self._v1 / self._v2


def main():
    print("***** Prcoessing start *****")
    value1, value2 = [int(x) for x in input('Enter two values for operation: ').split()]
    print(f'First variable = {value1}, Second variable = {value2}')
    cal_obj = Calculator(value1, value2)
    print(f'''
        Addition = {cal_obj.addition()},
        Substraction = {cal_obj.substraction()},
        Multiplication = {cal_obj.multiplication()},
        Division = {cal_obj.divison()}
        ''')


if __name__ == "__main__":
    main()
