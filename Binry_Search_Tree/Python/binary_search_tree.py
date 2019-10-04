class Node:
    lft = None
    rgt = None
    def __init__(self, key, val):
        self.key = key
        self.val = val

def insert(node, key, val):
    if node is None:
        return Node(key, val) # empty leaf: add node here
    if node.key == key:
        node.val = val # found the key: replace val
    elif key < node.key:
        node.lft = insert(node.lft, key, val) # go left
    else:
        node.rgt = insert(node.rgt, key, val) # go right
    return node

def search(node, key):
    if node is None:
        raise KeyError # empty leaf: it's not here
    if node.key == key:
        return node.val # found key: return val
    elif key < node.key:
        return search(node.lft, key) # go left
    else:
        return search(node.rgt, key) # go right

def traverse_recursively(node):
    """Perform an in-order traversal recursively"""
    
    nodes = []
    
    if node is not None:
        nodes.extend(traverse_recursively(node.lft))
        nodes.append(node)
        nodes.extend(traverse_recursively(node.rgt))
        
    return nodes

def traverse_stack(node):
    """Perform an in-order traversal iteratively using a stack"""
    
    nodes = []
    
    stack = []
    while True:
        while node is not None:
            stack.append(node)
            node = node.lft

        if len(stack) == 0:
            break

        node = stack.pop()
        nodes.append(node)
        node = node.rgt
        
    return nodes

class Tree:
    # a simple wrapper
    root = None
    def __setitem__(self, key, val):
        self.root = insert(self.root, key, val)
    def __getitem__(self, key):
        return search(self.root, key)
    def __contains__(self, key):
        try:
            search(self.root, key)
        except KeyError:
            return False
        return True
    def rtraverse(self):
        return traverse_recursively(self.root)
    def straverse(self):
        return traverse_stack(self.root)
