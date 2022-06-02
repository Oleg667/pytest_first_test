import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self): #тест проверки умножения
        assert self.calc.multiply(self, 2, 2)==4

