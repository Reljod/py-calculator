from abc import ABC, abstractmethod


class AddOperator(ABC):
    @abstractmethod
    def add(self, *args: int | float) -> int | float:
        pass


class SimpleAddOperator(AddOperator):
    def add(self, *args: int | float) -> int | float:
        return sum(args)
