from chapter03.stack_and_queue import Stack


class FixedSizeStack(Stack):
    def __init__(self, max_size, next_stack=None):
        self.max_size = max_size
        self.current_size = 0
        self.next = next_stack
        super().__init__()

    def push(self, data):
        if self.is_full():
            self.pop()
        super().push(data)
        self.current_size += 1

    def pop(self):
        current = super().pop()
        self.current_size -= 1
        return current

    def is_full(self):
        if self.current_size >= self.max_size:
            return True
        return False

    def is_empty(self):
        return self.current_size == 0


class SetOfStacks(Stack):
    def __init__(self, max_size):
        super().__init__()
        self.max_size = max_size
        self.first = FixedSizeStack(max_size)
        self.number_of_stacks = 1

    def push(self, data):
        if self.first.is_full():
            self.first = FixedSizeStack(self.max_size, self.first)
            self.number_of_stacks += 1
        self.first.push(data)

    def pop(self):
        current = self.first.pop()
        if self.first.is_empty():
            self.first = self.first.next
            self.number_of_stacks -= 1
        return current

    def pop_at(self, idx: int):
        for stack_idx, stack in enumerate(self):
            if idx == stack_idx:
                return stack.pop()

    def __iter__(self):
        stack = self.first
        while stack:
            yield stack
            stack = stack.next

    def __repr__(self):
        stacks = " -> ".join(
            f"Stack({stack.current_size}/{stack.max_size})" for stack in self
        )
        return stacks
