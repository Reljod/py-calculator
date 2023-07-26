from dataclasses import dataclass
from src.core.memory import Memory
from src.core.operations import Operator


@dataclass
class CalcParts:
    memory: Memory
    operator: Operator


class Calculator:
    def __init__(self, parts: CalcParts) -> None:
        self.parts = parts
