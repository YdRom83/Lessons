from controller import CalculatorController


def main():
    controller = CalculatorController()

    num1 = 10
    num2 = 5
    controller.add_numbers(num1, num2)
    controller.subtract_numbers(num1, num2)


if __name__ == "__main__":
    main()
