from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_calculate_correctly(self):
        assert self.calc.division(self, 8, 2) == 4

    def test_summa_correctly(self):
        assert self.calc.adding(self, 9, 4) == 13

    def test_subtract_correctly(self):
        assert self.calc.subtraction(self, -5, 6) == -11


