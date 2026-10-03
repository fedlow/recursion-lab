class Stack:
    def __init__(self):
        self._items = []

    def push(self, value):
        self._items.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop из пустого стека")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek из пустого стека")
        return self._items[-1]

    def is_empty(self):
        """True, если стек пуст, иначе False."""
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f"Stack({self._items})"