class House:
    houses_history = []

    def __new__(cls, *args,**kwargs):
        instance = super().__new__(cls)
        cls.houses_history.append(args)
        return instance

    def __init__(self, *args,**kwargs):
        self.args = args
        self.kwargs = kwargs

    def __del__(self):
        print(f"{self.args} снесён, но он останется в истории")

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)