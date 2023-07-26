
from abc import ABC, abstractmethod
from typing import Any


class Memory(ABC):
    
    @abstractmethod
    def insert(self, key: str, data: Any) -> list:
        pass
    
    @abstractmethod
    def pop(self, key: str) -> Any | None:
        pass
