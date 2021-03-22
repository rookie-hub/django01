from abc import ABCMeta,abstractmethod
from django01.factory.animals import Animals
class Factory(metaclass=ABCMeta): # 定义一个抽象类

    @abstractmethod
    def factory_method(self) -> Animals:
        pass

    def myinvoke(self) -> str:
        fac = self.factory_method()
        if any(fac):
            return fac.description()
        else:
            print('空对象')
