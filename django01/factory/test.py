from django01.factory.rabbitFactory import RabbitFactory
from django01.factory.dogFactory import DogFactory

def test():
    s = '饿'
    obj = None

    if s in '饥饿':
        obj = RabbitFactory()
    else:
        obj = DogFactory()
    return obj.factory_method()

if __name__ == "__main__":
   animal = test()
   print(animal.description())