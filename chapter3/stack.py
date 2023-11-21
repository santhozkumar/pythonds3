class Stack():
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def is_empty(self):
        return not bool(self._items)

    def size(self):
        return len(self._items)

    def __str__(self) -> str:
        return f'{self._items}'
    def __len__(self):
        return len(self._items)


def revstring(my_str):
    stac = Stack()
    i = 0 
    while i < len(my_str):
        stac.push(my_str[i])
        i = i + 1

    new_s = ''
    j = 0
    while j < len(my_str):
        new_s += stac.pop()
        j = j + 1

    return new_s

def rev_string(my_str):
    stac = Stack()
    for c in my_str:
        stac.push(c)
    
    new_s = ''
    while not stac.is_empty():
        new_s += stac.pop()

    return new_s


def main():
    s = Stack()
    print(s.size())
    print(s.is_empty())
    s.push(1)
    s.push(True)
    s.push('John')
    print(s.peek())

    print("before pop ", s)
    s.pop()
    print("after pop ", s)
    print(s.size())
    print(s.is_empty())
    print(len(s), "find len")


if __name__ == "__main__":
    main()
    print(revstring("apple"))
    print(rev_string("apple"))


