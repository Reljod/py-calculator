from src.core.operations.basic import AddOperator
from src.core.operations.basic.addition import SimpleAddOperator


def add(*args: int | float) -> int | float:
    add_operator: AddOperator = SimpleAddOperator()
    return add_operator.add(*args)
