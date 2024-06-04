class Stack:
    """
    This class sample of stack LIFO method in here
    data last entry, first out
    """

    def __init__(self):
        """
        In here I entered attributes
        """
        self.stack = []

    def items(self):
        """
        In here we can take data from []
        :return: stack[]
        """
        return self.stack

    def isEmpty(self) -> bool:
        """
        This function check the empty of list
        :return:true or false
        """
        return self.stack == []

    def push(self, item):
        """
        This function add item to stack[]
        :param item:
        :return: stack[]
        """
        self.stack.append(item)
        return self.stack

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self) -> int:
        """
        This function return the size of stack[]
        :return: len(stack)
        """
        return len(self.stack)


stack = Stack()
print(stack.isEmpty())
stack.push(15)
print(stack.isEmpty())
stack.push("Nodirbek")
print(stack.isEmpty())
print(stack.size())
print(stack.items())
print(stack.peek())
print(stack.items())
