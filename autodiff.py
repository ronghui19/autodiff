import numpy as np

class Node:
    def __init__(self):
        self.inputs = []
        self.op = None
        self.const_attr = None
        self.name = ""

    def __add__(self, other):
        if isinstance(other, Node):
            new_node = add_op(self, other)
        else:
            new_node = add_byconst_op(self, other)
        return new_node

    def __mul__(self, other):
        if isinstance(other, Node):
            new_node = mul_op(self, other)
        else:
            new_node = mul_byconst_op(self, other)
        return new_node

class Op:
    def __call__(self):
        new_node = Node()
        new_node.op = self
        return new_node

    def compute(self, node, input_vals):
        raise NotImplementedError

    def gradient(self, node, output_grad):
        raise NotImplementedError

class AddOp(Op):
    def __call__(self, node_A, node_B):
        new_node = Op.__call__(self)
        new_node.inputs = [node_A, node_B]
        new_node.name = "(%s+%s)" % (node_A.name, node_B.name)



class AddByConstOp:
    def __call__(self, *args, **kwargs):
        pass

class MulOp:
    def __call__(self, *args, **kwargs):
        pass

class MulByConstOp:
    def __call__(self, *args, **kwargs):
        pass

add_op = AddOp()
mul_op = MulOp()
add_byconst_op = AddByConstOp()
mul_byconst_op = MulByConstOp()