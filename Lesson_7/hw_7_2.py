from abc import ABC


class Clothes(ABC):

    def __init__(self, name, size, number):
        self.name = name
        self.size = size
        self.number = number

    @property
    def cloth(self):
        return self.cloth

    @property
    def total_cloth(self):
        return self.cloth * self.number


class Jacket(Clothes):
    @property
    def cloth(self):
        v = self.size * 2 + 0.3
        return v


class Coat(Clothes):
    @property
    def cloth(self):
        v = self.size / 2 + 6.5
        return v


j = []
c = []
total_j = 0
total_c = 0
j.append(Jacket('jacket', 5, 10))
j.append(Jacket('jacket', 6, 10))
c.append(Coat('coat', 6, 10))
c.append(Coat('coat', 8, 10))
for i in range(len(j)):
    total_j += j[i].total_cloth
for i in range(len(c)):
    total_c += c[i].total_cloth
print(f"Общий расход ткани - {total_j + total_c}, расход на костюмы - {total_j}, расход на пальто - {total_c}")
