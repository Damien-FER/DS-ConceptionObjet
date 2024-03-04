class MyEmptyStackException(Exception):
    """Exception levée lorsqu'une tentative est faite pour dépiler d'une pile vide."""
    pass

class MyOutOfSizeException(Exception):
    """Exception pour ajouter à une pile pleine."""
    pass

class StackNode:
    """Noeud de la pile."""
    def __init__(self, item, next_node=None):
        self.item = item
        self.next_node = next_node
 
class MyStack:
    """Classe représentant une pile."""
    def __init__(self, max_size):
        self.top = None
        self.size = 0
        self.max_size = max_size

    def add_to_stack(self, item):
        if self.size >= self.max_size:
            raise MyOutOfSizeException("Impossible d'ajouter à une pile pleine")
        new_node = StackNode(item, self.top)
        self.top = new_node
        self.size += 1

    def pop_from_stack(self):
        if self.size == 0:
            raise MyEmptyStackException("Impossible de dépiler d'une pile vide")
        item = self.top.item
        self.top = self.top.next_node
        self.size -= 1
        return item

    def is_full(self):
        return self.size >= self.max_size

    def is_empty(self):
        return self.size == 0

# Test du code fourni
if __name__ == '__main__':
    myStack = MyStack(3)
    myStack.add_to_stack('hello')
    myStack.add_to_stack('hello')
    print(myStack.is_full()) # False
    myStack.add_to_stack('hello')
    print(myStack.is_full()) # True
    
    try:
        myStack.add_to_stack('hello') # MyOutOfSizeException
    except MyOutOfSizeException as e:
        print(e)
    
    print(myStack.pop_from_stack()) # hello
    print(myStack.is_empty()) # False
    print(myStack.pop_from_stack()) # hello
    print(myStack.is_empty()) # False
    print(myStack.pop_from_stack()) # hello
    print(myStack.is_empty()) # True
    
    try:
        print(myStack.pop_from_stack()) # MyEmptyStackException
    except MyEmptyStackException as e:
        print(e)