import pytest

from chapter03.stack_and_queue import MultiStackFixedSize, StackIsFullError


def test_multistack_fixed_size():
    multistack = MultiStackFixedSize(3, 8)
    assert multistack.max_size == 8
    assert multistack.number_of_stacks == 3
    assert multistack.is_full(0) is False
    assert multistack.is_full(1) is False
    assert multistack.is_full(2) is False


def test_check_current_size_multistack():
    multistack = MultiStackFixedSize(3, 8)
    assert multistack.current_size[1] == 0
    multistack.add(1, 10)
    assert multistack.current_size[1] == 1


def test_add_test_is_full_multistack():
    multistack = MultiStackFixedSize(3, 8)
    with pytest.raises(StackIsFullError):
        for d in range(1, 10):
            multistack.add(1, d)