class Road:
    __ro_asphalt = 25

    def __init__(self, width, length):
        self.__width = width
        self.__length = length

    def mass(self, thickness):
        weight = self.__length * self.__width * Road.__ro_asphalt * thickness
        return weight


road = Road(20, 5000)
thick = int(input('Введите толщину укладываемого асфальта, см: '))
print(f"Требуемая масса асфальта: {road.mass(thick) / 1000} тонн")
