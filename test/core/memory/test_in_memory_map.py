from src.core.memory.in_memory_map import InMemoryMapMemory


def test_in_memory_map_initial_insert():
    in_memory_map = InMemoryMapMemory()
    new_stack = in_memory_map.insert("number", 10)
    assert new_stack == [10]

def test_in_memory_map_subsequent_insert():
    in_memory_map = InMemoryMapMemory()
    in_memory_map.insert("number", 10)
    new_stack = in_memory_map.insert("number", 20)
    assert new_stack == [10, 20]
    
def test_in_memory_map_pop_with_value():
    in_memory_map = InMemoryMapMemory()
    in_memory_map.insert("number", 10)
    in_memory_map.insert("number", 20)
    value = in_memory_map.pop("number")
    assert value == 20
