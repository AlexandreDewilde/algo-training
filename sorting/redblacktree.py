import random


RED = 1
BLACK = 2


class Node:
    def __init__(self, key, val, color):
        self.key = key
        self.val = val
        self.color = color
        self.left = None
        self.right = None

class RedBlackTree:
    def __init__(self):   
        self.root = None
    
    def rotate_left(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = RED
        return x
    def rotate_right(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = RED

        return x
    def add(self, key, val):
        self.root = self.add_util(self.root, key, val)
        self.root.color = BLACK
    def add_util(self, node, key, val):
        if node == None:
            return Node(key, val, RED)
        if key < node.key:
            node.right = self.add_util(node.right, key, val)
        elif key > node.key:
            node.left = self.add_util(node.left, key, val)
        else:
            node.val = val

        if node.right and node.left and node.right.color == RED and not node.left.color != RED:
            node = self.rotate_left(node)
        if node.left and node.left.color == RED and (node.left.left and not node.left.left.color == RED):
            node = self.rotate_right(node)
        if node.left and node.right and node.left.color == RED and node.right.color == RED:
            node.color = RED
            node.left.color = BLACK
            node.right.color = BLACK
        return node

def dfs(node):
    if node:
        print(node.key)
        dfs(node.left)
        dfs(node.right) 

if __name__ == "__main__":
    tree = RedBlackTree()

    for _ in range(100):
        tree.add(random.randrange(100), 0)
    dfs(tree.root)
