from chapter03.p02 import SetOfStacks


def test_set_of_stacks():
    setofstacks = SetOfStacks(max_size=3)
    setofstacks.push(1)
    assert setofstacks.number_of_stacks == 1
    assert setofstacks.first.current_size == 1
    setofstacks.push_multiple(2, 3, 4)
    print(setofstacks)
    assert setofstacks.number_of_stacks == 2


def test_set_of_stacks_pop_at_specific_substack_index():
    setofstacks = SetOfStacks(max_size=3)

    setofstacks.push_multiple(1, 2, 3, 4, 5)
    setofstacks.pop_at(1)
    assert setofstacks.first.next.is_full() is False
