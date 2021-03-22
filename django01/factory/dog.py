from django01.factory.animals import Animals

class Dog(Animals):
    def description(self):
        return '单身狗是不吃狗粮的！！！'
