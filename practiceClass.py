class ItemName():
    def __init__(self, name=None, price=0):
        self.name = name
        self.price = price
        self.__list = []

    def __str__(self):
        return f'{self.name}, {self.price}'

    def __iter__(self):
        for x in self.__list:
            yield x