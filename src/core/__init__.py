from dataclasses import dataclass
from src.core.memory import Memory

@dataclass
class CalcParts:
    memory: Memory

class Calculator:
    def __init__(self, parts: CalcParts) -> None:
        self.parts = parts
        
    
