from algodata.datastructures.basics import ParentStructure, Stack, Queue


def test_empty_data_structure():
    data_structure = ParentStructure()
    assert data_structure.is_empty
    assert data_structure.size == 0

def test_stack_add_elements():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.items == [1, 2]


def test_queue_add_elements():
    pass
