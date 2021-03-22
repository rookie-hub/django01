from abc import ABCMeta,abstractmethod

class Animals(metaclass=ABCMeta): # 定义一个接口

    @abstractmethod
    def description(self) -> str:
        pass