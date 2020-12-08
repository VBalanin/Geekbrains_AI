class Matrix:
    def __init__(self, args=None):
        if args is None:
            args = []
        self.matrix = args
      
    def __str__(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print(f" {self.matrix[i][j]} ", end='')
            print()

        return f""

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            raise ValueError('Разные размеры матриц!')
        elif len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError('Разные размеры матриц!')
        else:
            new_args = []
            for i in range(len(self.matrix)):
                new_str = list(map(lambda x, y: x + y, self.matrix[i], other.matrix[i]))
                new_args.append(new_str)
            c = Matrix(new_args)
        return c


a = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
b = Matrix([[3, 2, 1], [3, 2, 1], [3, 2, 1]])
print(a)
print(b)
print(a + b)
