from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        a = 123
        b = 54
        cal = Calculator()

        result = cal.subtract(a, b)

        expected = 69
        assert result == expected

    def test_multiply(self):
        a = 7
        b = 10
        cal = Calculator()

        result = cal.multiply(a, b)

        expected = 70
        assert result == expected

    def test_divide(self):
        a = 50
        b = 5
        cal = Calculator()
        
        result = cal.divide(a, b)

        expected = 10
        assert result == expected