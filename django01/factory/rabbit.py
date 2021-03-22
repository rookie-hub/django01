from django01.factory.animals import Animals
class Rabbit(Animals):

    def description(self):
        return '兔子是用来填饱肚子的！！！'