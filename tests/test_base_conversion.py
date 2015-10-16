import pytest

from algodata.algorithms.base_conversion import iterative_base_conversion, stack_iterative_base_conversion, \
    list_iterative_base_conversion


@pytest.mark.parametrize(('number', 'base', 'expected_result'), [
    (521, 8, '1011'),
    (43545, 2, '1010101000011001'),
    (43545, 16, 'aa19'),
    (100, 10, '100'),
])
def test_iterative_base_conversion(number, base, expected_result):
    assert iterative_base_conversion(number, base) == expected_result


@pytest.mark.parametrize(('number', 'base', 'expected_result'), [
    (521, 8, '1011'),
    (43545, 2, '1010101000011001'),
    (43545, 16, 'aa19'),
    (100, 10, '100'),
])
def test_stack_iterative_base_conversion(number, base, expected_result):
    assert stack_iterative_base_conversion(number, base) == expected_result


@pytest.mark.parametrize(('number', 'base', 'expected_result'), [
    (521, 8, '1011'),
    (43545, 2, '1010101000011001'),
    (43545, 16, 'aa19'),
    (100, 10, '100'),
])
def test_list_iterative_base_conversion(number, base, expected_result):
    assert list_iterative_base_conversion(number, base) == expected_result
