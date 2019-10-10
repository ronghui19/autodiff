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
        new_node = Node()  # create Node instance
        new_node.op = self  # bind op with node
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
        return new_node

    def compute(self, node, input_vals):
        assert len(input_vals) == 2
        return input_vals[0] + input_vals[1]

    def gradient(self, node, output_grad):
        return [output_grad, output_grad]

class AddByConstOp(Op):
    def __call__(self, node_A, const_val):
        new_node = Op.__call__(self)
        new_node.inputs = [node_A]
        new_node.const_attr = const_val
        new_node.name = "(%s+%s)" % (node_A.name, str(const_val))
        return new_node

    def compute(self, node, input_vals):
        assert len(input_vals) == 2
        return input_vals[0] + node.const_attr

    def gradient(self, node, out_grad):
        return [out_grad]

class MulOp(Op):
    def __call__(self, node_A, node_B):
        new_node = Op.__call__(self)
        new_node.inputs = [node_A, node_B]
        new_node.name = "(%s*%s)" % (node_A.name, node_B.name)
        return new_node

    def compute(self, node, input_vals):
        assert len(input_vals) == 2
        return input_vals[0] * input_vals[1]

    def gradient(self, node, output_grad):



class MulByConstOp:
    def __call__(self, *args, **kwargs):
        pass

add_op = AddOp()
mul_op = MulOp()
add_byconst_op = AddByConstOp()
mul_byconst_op = MulByConstOp()