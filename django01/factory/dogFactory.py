from django01.factory.factory import Factory
from django01.factory.dog import Dog


class DogFactory(Factory):

    def factory_method(self):
        return Dog()