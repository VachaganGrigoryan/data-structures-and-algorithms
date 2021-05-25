import logging as log

log.basicConfig(filename='text.log', filemode='w', format='%(levelname)s::%(message)s', level=log.DEBUG)

class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def __str__(self):
        return f'[{self.value}, (L({self.value}):{self.left}, (R({self.value}):{self.right}]'

class BeTree:

    def __init__(self, node=None):
        self._root = node
    
    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, root):
        self._root = root

    @root.deleter
    def root(self):
        self._root = None

    def add(self, value):
        def __add(node, value, direct=None):
            log.debug(f"__add({node}, {value}, {direct})")
            if value > node.value:
                if node.right is None:
                    node.right = Node(value)
                    log.info(f"Added new value({value}) Right")
                else:
                    log.debug("Right Call")
                    node.right = __add(node.right, value, direct or "R")      
            elif value < node.value:
                if node.left is None:
                    node.left = Node(value)
                    log.info(f"Added new value({value}) Left")
                else:
                    log.debug("Left Call")
                    node.left = __add(node.left, value, direct or "L")
            log.debug(f"End __add({node}, {value})")
            log.info(f"Start checking node ({node})")
            return BeTree.check(node, direct)
    
        if self.root is None:
            self.root = Node(value)
            log.info(f"Add new root value({value})\n")
        else:
            log.info(f"Start adding value({value})")
            self.root = __add(self.root, value)
            log.info(f"End adding value({value})\n")

    @staticmethod 
    def level(node):
        if node is None:
            return 0
        return max(BeTree.level(node.left), BeTree.level(node.right)) + 1

    @staticmethod    
    def check(node, direct=None):
        log.warning(f"_check({node})")
        ll = BeTree.level(node.left)
        lr = BeTree.level(node.right)    
        diff = lr-ll
        log.warning(f"Left({ll}) Right({lr}) Diff({diff}) Direct({direct})")

        if diff > 1 or (ll == 1 and lr == 2 and direct == "L"):
            node_right = node.right
            node.right = None
            log.info(f"Left Node")
            node = BeTree.__add_node_left(node_right, node)

        elif diff < -1 or (lr == 1 and ll == 2 and direct == "R"):
            node_left = node.left
            node.left = None
            log.info(f"Right Node")
            node = BeTree.__add_node_right(node_left, node)
 
        log.warning(f'End _check({node})')
        return node

    @staticmethod
    def __add_node_left(node, tmp):
        log.critical(f'__add_node_left(NODE:{node}, TMP:{tmp})')
        if node.left is None:
            node.left = tmp
        else:
            node.left = BeTree.__add_node_left(node.left, tmp)
        log.critical(f"Added Left Node ({node})")
        log.info(f"Send to _check({node})")
        return BeTree.check(node)

    @staticmethod
    def __add_node_right(node, tmp):
        log.critical(f'__add_node_right(NODE:{node}, TMP:{tmp})')
        if node.right is None:
            node.right = tmp
        else:
            node.right = BeTree.__add_node_right(node.right, tmp)
        log.critical(f"Added Right Node ({node})")
        log.info(f"Send to _check({node})")
        return BeTree.check(node)


    def remove(self, x):
        log.error(f"Start remove({x}, {self.root})")
        def __remove(x, node):
            log.error(f"__remove({x}, {node})")
            if x > node.value:
                log.info(f"Right Node")
                if node.right:
                    log.error(f"__remove({x}, {node.right})")
                    node.right = __remove(x, node.right)
            elif x < node.value:
                log.info(f"Left Node")
                if node.left:
                    log.error(f"__remove({x}, {node.left})")
                    node.left = __remove(x, node.left)
            else:
                log.error(f"Node found ({node})")
                if node.left == node.right:
                    return None
                
                if node.left is None or node.right is None:
                    return node.left or node.right

                if BeTree.level(node.left) > BeTree.level(node.right):
                    return BeTree.__add_node_right(node.left, node.right)
                return BeTree.__add_node_left(node.right, node.left)
            
            # log.error(f"End __remove({x}, {node})")
            log.error(f"Send to Check({node})")
            return BeTree.check(node)
            
        if self.root:
            self.root = __remove(x, self.root)
            log.error(f"End removing({x}, {self.root})")
         
    def find(self, x):
        def __find(x, node):
            if x == node.value:
                return BeTree(node)
            elif x < node.value:
                if node.left is None:
                    return BeTree()
                else:
                    return __find(x, node.left)
            elif x > node.value:
                if node.right is None:
                    return BeTree()
                else:
                    return __find(x, node.right)

        if(self.root == None):
            return self
        else:
            return __find(x, self.root)
       
    def __repr__(self):
        return str(self.to_list())

    def __str__(self):
        return str(self.root)

    def to_list(self, key='sort'):
        def _tree(node):
            if node:
                self.list.append(node.value)
                _tree(node.left)
                _tree(node.right)
            
        def _sort(node):
            if node:
                _sort(node.left)
                self.list.append(node.value)
                _sort(node.right)
        try:
            self.list = []
            __func = eval(f'_{key}')
            __func(self.root)
        except NameError:
            return self.list
        return self.list

    


if __name__ == '__main__':
    
    tree = BeTree()

    tree.add(13)
    tree.add(15)
    tree.add(10)
    tree.add(16)
    tree.add(11)
    tree.add(5)
    tree.add(4)
    tree.add(6)
    tree.add(7)
    tree.remove(15)
    # tree.remove(35)
    
    print(tree)
    print(tree.level(tree.root))
    


