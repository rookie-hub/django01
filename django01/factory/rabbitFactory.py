from django01.factory.factory import Factory
from django01.factory.rabbit import Rabbit


class RabbitFactory(Factory):

    def factory_method(self):
        return Rabbit()