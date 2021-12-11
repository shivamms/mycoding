import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    # define your fields here
    
    def evaluate(self) -> int:
        pass

class opNode(Node):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    def evaluate(self):
        if self is None:
            return
        if self.left is not None:
            left = self.left.evaluate()
        if self.right is not None:
            right = self.right.evaluate()
        if self.val == '+':
            return left + right
        elif self.val == '-':
            return left - right
        elif self.val == '*':
            return left * right
        elif self.val == '/':
            return int(left / right)
        else:
            return int(self.val)
"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        if len(postfix) > 0:
            val = postfix.pop()
            if val in ('+', '-', '*', '/'):
                node = opNode(val)
                node.right = self.buildTree(postfix)
                node.left = self.buildTree(postfix)
                return node
            else:
                return opNode(val)
		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        