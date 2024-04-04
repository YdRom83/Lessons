#                       MVC (Model View Controller)
# ------------------------------------------------------------------------#
# class CalculatorModel:
#     def add(self, num1, num2):
#         return num1 + num2
#
#     def subtrack(self, num1, num2):
#         return num1 - num2
#
# c = CalculatorModel()
# print(c.add(5, 5))
# print(c.subtrack(5, 5))


import tkinter as tk


# Model

class Model:
    def __init__(self):
        self.data = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data


# View
class View:
    def __init__(self, root):
        self.label = tk.Label(root, text="Data: ")
        self.label.pack()

    def show_data(self, data):
        self.label.config(text=f'Data: {data}')


# Controller
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def set_data(self, data):
        self.model.set_data(data)

    def update_view(self):
        data = self.model.get_data()
        self.view.show_data(data)


# Usage

root = tk.Tk()
model = Model()
view = View(root)
controller = Controller(model, view)


def update_data():
    data = entry.get()
    controller.set_data(data)
    controller.update_view()


entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text='Update Data', command=update_data)
button.pack()

root.mainloop()
