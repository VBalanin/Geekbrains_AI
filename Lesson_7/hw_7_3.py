class Cell:
    def __init__(self, qty):
        self.qty = int(qty)

    def __str__(self):
        return f"{self.qty * '*'}"

    def __add__(self, other):
        return Cell(self.qty + other.qty)

    def __sub__(self, other):  # вместо вывода сообщения об отрицательном результате меняем аргументы
        return Cell(self.qty - other.qty) if self.qty - other.qty > 0 else Cell(other.qty - self.qty)

    def __mul__(self, other):
        return Cell(self.qty * other.qty)

    def __truediv__(self, other):
        return Cell(int(self.qty // other.qty))

    def make_order(self, num_cell):
        for i in range(int(self.qty // num_cell)):
            print(f"{num_cell * '*'}")
        print(f"{(self.qty % num_cell) * '*'}")


a = Cell(15)
b = Cell(10)
print(f"Клетка А:")
a.make_order(5)
print(f"Клетка Б:")
b.make_order(5)
print(f"Клетка А+Б: {a + b} ")
print(f"Клетка А-Б: {a - b} ")
print(f"Клетка А*Б: {a * b} ")
print(f"Клетка А/Б: {a / b} ")

