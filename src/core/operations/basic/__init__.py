from dataclasses import dataclass
from .addition import AddOperator


@dataclass
class BasicOperatorPlugins:
    add: AddOperator
