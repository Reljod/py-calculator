from typing import Any, Dict
from . import Memory

class InMemoryMapMemory(Memory):
    def __init__(self) -> None:
        self.memory_map: Dict[str, list[Any]] = {}
        
    def _create_initial_stack(self, key: str):
        self.memory_map[key] = []
        
    def _is_stack_exists(self, key: str):
        return self.memory_map.get(key) is not None
        
    def insert(self, key: str, data: Any) -> None:
        if not self._is_stack_exists(key):
            self._create_initial_stack(key)
            
        self.memory_map[key].append(data)
        return self.memory_map.get(key)

    def pop(self, key: str) -> Any | None:
        if not self._is_stack_exists(key):
            return None
        return self.memory_map[key].pop()
