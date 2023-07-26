from typing import Any
from src.core import Calculator, CalcParts
from src.core.memory import Memory

def test_calculator_instantiate():
    class TestMemory(Memory):
        
        def __init__(self):
            """ test """
            pass
        
        def insert(self, key: str, data: Any) -> list:
            return []
        
        def pop(self, key: str) -> Any | None:
            return "test"

    parts = CalcParts(memory=TestMemory)
    calculator = Calculator(parts=parts)
    
    assert calculator is not None
