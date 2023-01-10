import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_calculate_correctly(self):
        assert self.calc.division(self, 8, 2) == 4

    def test_catculation_filed(self):
        assert self.calc.division(self, 6, 0)

    def test_summa_correctly(self):
        assert self.calc.adding(self, 9, 4) == 13

    def test_summa_filed(self):
        assert self.calc.adding(self, 6, 4) == 9

    def test_subtract_correctly(self):
        assert self.calc.subtraction(self, -5, 6) == -11

    def test_subtraction_filed(self):
        assert self.calc.subtraction(self, 20, 10) == 5
