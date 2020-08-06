class TreeNode:
    # 4개의 reference를 가진다.
    nodeLHS = None
    nodeRHS = None
    nodeParent = None
    value = None

    def __init__(self, value, node_parent):
        self.value = value
        self.nodeParent = node_parent

    def get_lhs(self):
        return self.nodeLHS

    def get_rhs(self):
        return self.nodeRHS

    def get_value(self):
        return self.value

    def get_parent(self):
        return self.nodeParent

    def set_lhs(self, lhs):
        self.nodeLHS = lhs

    def set_rhs(self, rhs):
        self.nodeRHS = rhs

    def set_value(self, value):
        self.value = value

    def set_parent(self, parent):
        self.nodeParent = parent
