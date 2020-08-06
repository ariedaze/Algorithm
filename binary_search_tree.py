from tree_node import TreeNode


class BinarySearchTree:
    # root만 저장함을 기억하자!
    root = None

    def __init__(self):
        pass

    def insert(self, value, node=None):
        if node is None:
            node = self.root

        if self.root is None:
            self.root = TreeNode(value, None)
            return
        if value == node.get_value():
            return

        if value > node.get_value():
            if node.get_rhs() is None:
                node.set_rhs(TreeNode(value, node.get_rhs()))
            else:
                self.insert(value, node.get_rhs())

        if value < node.get_value():
            if node.get_lhs() is None:
                node.set_lhs(TreeNode(value, node.get_lhs()))
            else:
                self.insert(value, node.get_lhs())
        return
