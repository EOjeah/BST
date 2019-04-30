

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
            return self.root

        node = self.root

        while True:
            if value < node.value:
                if node.left is None:
                    node.left = Node(value)
                    return node.left
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = Node(value)
                    return node.right
                else:
                    node = node.right

    def findvalue(self, value):
        node = self.root
        while node.value:
            if value < node.value:
                if node.left is None:
                    return ("Value {} not found!".format(value))
                else:
                    node = node.left
                    # return self.left.findvalue(value)
            elif value > node.value:
                if node.right is None:
                    return ("Value {} not found!".format(value))
                else:
                    node = node.right
            elif value == node.value:
                return "found {}".format(value)

        return ("Value {} not found".format(value))



myTree = Tree()
myTree.insert(9)
myTree.insert(4)
myTree.insert(10)
myTree.insert(3)
print(myTree.findvalue(10))
print(myTree.findvalue(21))
