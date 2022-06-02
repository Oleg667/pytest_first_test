import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc=Calculator
    class TestCalc: # названиекласса тестов
        def setup(self): # подключаем тестируемый объект Калькулятор
            self.calc=Calculator

        def test_multiply_calculate_correctly(self): #тест проверки умножения
            assert self.calc.multiply(self, 2, 2)==4

        def test_multiply_calculate_failed(self): #тест проверки умножения
            assert self.calc.division(self, 6, 2)==3