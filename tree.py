import random
from copy import deepcopy

class Node:
    def __init__(self, value:int):
        self.value = value
        self.parent = None
        self.leftChild = None
        self.rightChild = None
        self.amLeft = None

class BST:
    def __init__(self, elem:list):
        elements = deepcopy(elem)
        #random.shuffle(elements)

        self.root = None

        while elements != []:
            while self.search(elements[0]) != None:
                elements[0] += 1
            self.addNode(Node(elements.pop(0)))
        
    def addNode(self, newNode):
        #If tree is empty
        if self.root == None:
            self.root = newNode
            return
        
        #Start at the root
        currentNode = self.root

        while True:
            #If value is smaller go left
            if newNode.value < currentNode.value:
                if currentNode.leftChild == None:
                    currentNode.leftChild = newNode

                    newNode.parent = currentNode
                    newNode.amLeft = True

                    break
                else:
                    currentNode = currentNode.leftChild
            #Else is higher and go right
            else:
                if currentNode.rightChild == None:
                    currentNode.rightChild = newNode

                    newNode.parent = currentNode
                    newNode.amLeft = False

                    break
                else:
                    currentNode = currentNode.rightChild

    def findMin(self, start = None):
        #Start at the root unless specified
        currentNode = self.root
        if start != None:
            currentNode = start

        #Go left
        while currentNode.leftChild != None:
            currentNode = currentNode.leftChild

        return currentNode
    
    def search(self, value):
        #Start at the root
        currentNode = self.root

        while currentNode != None and currentNode.value != value:
            #Go left if value is smaller
            if value < currentNode.value:
                currentNode = currentNode.leftChild
            #Go right if value is higher
            else:
                currentNode = currentNode.rightChild

        return currentNode
    
    def delete(self, value):
        #Find node to delete
        node = self.search(value)
        isRoot = (node == self.root)

        #Node exists in the tree
        if node != None:
            #Has no children
            if node.leftChild == None and node.rightChild == None:
                if isRoot:
                    self.root = None
                elif node.amLeft:
                    node.parent.leftChild = None
                else:
                    node.parent.rightChild = None
            #Has only left child
            elif node.rightChild == None:
                if isRoot:
                    self.root = node.leftChild
                    node.leftChild.parent = None
                elif node.amLeft:
                    node.parent.leftChild = node.leftChild
                    node.leftChild.parent = node.parent #cursed
                else:
                    node.parent.rightChild = node.leftChild
                    node.leftChild.parent = node.parent
            #Has only right child
            elif node.leftChild == None:
                if isRoot:
                    self.root = node.rightChild
                    node.rightChild.parent = None
                elif node.amLeft:
                    node.parent.leftChild = node.rightChild
                    node.rightChild.parent = node.parent
                else:
                    node.parent.rightChild = node.rightChild
                    node.rightChild.parent = node.parent
            #Has both children - find min of the right child
            else:
                rightMin = self.findMin(node.rightChild, print = False)

                node.value = rightMin.value
                if rightMin.parent == node: #Delete rightMin
                    node.rightChild = None
                else:
                    rightMin.parent.leftChild = None

        return

    def successor(self, value):
        #Find node
        node = self.search(value)

        successor = None
        
        #If node exists in the tree
        if node != None:
            #If node doesn't have the right child
            if node.rightChild == None:
                currentNode = node
                #Find the ancestor that is bigger
                while currentNode != None:
                    if currentNode.value > node.value:
                        successor = currentNode
                        break
                    else:
                        currentNode = currentNode.parent
            #Find the smallest descendant that is bigger than himself (go right)
            else:
                successor = self.findMin(node.rightChild, print = False)
        
        return successor
        
    def getDepth(self, node = None, maxDepth = 0):
        if node == None:
            node = self.root

        maxLeft = 0
        maxRight = 0

        if node.leftChild != None:
            maxLeft = self.getDepth(node.leftChild, maxDepth + 1)
        if node.rightChild != None:
            maxRight = self.getDepth(node.rightChild, maxDepth + 1)

        return max(maxDepth, maxLeft, maxRight)

    def printLeft(self, offset, size = 1):
        for _ in range((int(offset / 2) * (size + 1))):
                print(' ', end='')
        for _ in range((int(offset / 2) * (size + 1))):
            print('_', end='')

    def printRight(self, offset, size = 1):
        '''Handles -1'''
        for _ in range((int(offset / 2) - 1 * (size + 1))):
                print('_', end='')
        for _ in range((int(offset / 2) - 1) * (size + 1)):
            print(' ', end='')

    def printEmpty(self, offset, size = 1):
        for _ in range(offset * (size + 1)):
            print(' ', end='')

    """ def print(self): #Root is at (0, 0), leaves are 1 unit appart. Everything else is calculated and drawn from the root down
        #If tree is empty
        if self.root == None:
            return

        #Calculate offset 2^(depth - 1)
        depth = self.getDepth()
        offset = 2 ** (depth - 1)
        level = 0
        queue = []
        
        #0 case
        queue.append(self.root.leftChild)
        if self.root.leftChild != None:
            #Draw edge
            self.printLeft(offset)
        else:
            self.printEmpty(offset)

        print(self.root.value, end='')

        queue.append(self.root.rightChild)
        if self.root.rightChild != None:
            print('_', end='')
            #Draw edge
            self.printRight(offset) # handles -1
        else:
            print(' ', end='')
            self.printEmpty(offset - 1)
        
        print()

        offset = int(offset / 2)
        level += 1
        currentNode = None
        tempqueue = []

        while level < depth:
            for _ in range(2 ** level):
                currentNode = queue.pop(0)
                tempqueue.append(currentNode)
                self.printEmpty(offset)
                #print buffer
                if currentNode:
                    if currentNode.amLeft:
                        print('/', end='')
                    else:
                        print('\\', end='')
                print(' ', end='')
                self.printEmpty(offset - 1)

            print()

            for _ in range(2 ** level):
                currentNode = tempqueue.pop(0)
                if currentNode == None:
                    self.printEmpty(offset * 2)
                    queue.append(None)
                    queue.append(None)

                queue.append(currentNode.leftChild)
                if currentNode.leftChild != None:
                    #Draw edge
                    self.printLeft(offset)
                else:
                    self.printEmpty(offset)

                print(currentNode.value, end='')

                queue.append(self.root.rightChild)
                if currentNode.rightChild != None:
                    print('_', end='')
                    #Draw edge
                    self.printRight(offset) # handles -1
                else:
                    print(' ', end='')
                    self.printEmpty(offset - 1)

            print()
            offset = int(offset / 2)
            level += 1
            
        while queue != []:
            currentNode = queue.pop(0)
            if currentNode == None:
                self.printEmpty(1)
            else:
                print(currentNode.value, end='')
                print(' ', end='')

        print()
 """
    def print_tree(self):
        def display(root):
            """Returns list of strings, width, height, and horizontal coordinate of the root."""
            # No child.
            if root.rightChild is None and root.leftChild is None:
                line = '%s' % root.value
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            # Only leftChild child.
            if root.rightChild is None:
                lines, n, p, x = display(root.leftChild)
                s = '%s' % root.value
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            # Only rightChild child.
            if root.leftChild is None:
                lines, n, p, x = display(root.rightChild)
                s = '%s' % root.value
                u = len(s)
                first_line = s + x * '_' + (n - x) * ' '
                second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            # Two children.
            leftChild, n, p, x = display(root.leftChild)
            rightChild, m, q, y = display(root.rightChild)
            s = '%s' % root.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                leftChild += [n * ' '] * (q - p)
            elif q < p:
                rightChild += [m * ' '] * (p - q)
            zipped_lines = zip(leftChild, rightChild)
            lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2

        lines, *_ = display(self.root)
        for line in lines:
            print(line)

