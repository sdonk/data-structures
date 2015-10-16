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
    assert stack.is_empty is False
    assert stack.size == 2


def test_stack_pop_elements():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.size == 1


def test_queue_enqueue_elements():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.items == [1, 2]
    assert queue.is_empty is False
    assert queue.size == 2


def test_queue_dequeue_elements():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    assert queue.size == 1
