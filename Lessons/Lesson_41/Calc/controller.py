from model import CalculatorModel
from view import CalculatorView


class CalculatorController:
    def __init__(self):
        self.model = CalculatorModel()
        self.view = CalculatorView()

    def add_numbers(self, num1, num2):
        result = self.model.add(num1, num2)
        self.view.display_result(result)

    def subtract_numbers(self, num1, num2):
        result = self.model.subtrack(num1, num2)
        self.view.display_result(result)
