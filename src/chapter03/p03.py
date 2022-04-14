from chapter03.stack_and_queue import Stack


class QueueFromStacks:
    def __init__(self):
        self.new_stack = Stack()
        self.old_stack = Stack()

    def _shift_new_to_old(self):
        while not self.new_stack.is_empty:
            self.old_stack.push(self.new_stack.pop())

    def pop(self):
        if self.old_stack.is_empty:
            self._shift_new_to_old()
        return self.old_stack.pop()

    def add(self, data):
        self.new_stack.push(data)

    def peek(self):
        if self.old_stack.is_empty:
            self._shift_new_to_old()
        return self.old_stack.peek()

    def add_multiple(self, *data):
        for d in data:
            self.add(d)
