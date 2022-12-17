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


#if __name__ == "__main__":
#    main()
