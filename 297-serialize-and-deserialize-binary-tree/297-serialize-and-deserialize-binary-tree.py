# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import json
from collections import defaultdict
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        def pickle(node, serial, nodetype):
            if node is None:
                return serial.setdefault("None", {})
            serial = serial.setdefault(nodetype, {})
            serial = serial.setdefault(node.val, {})
            pickle(node.left, serial, "left")
            pickle(node.right, serial, "right")

        serialroot = dict()
        serial = serialroot
        pickle(root, serial, "root")
        
        serialroot = json.dumps(serialroot)
        return serialroot
        
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = json.loads(data)
        root = TreeNode()
        queue = []
        if 'None' in data.keys():
            return
        data = data['root']
        queue.append((root, data))
        while queue:
            d = queue.pop(0)
            node = d[0]
            data = d[1]
            for key, val in data.items():
                node.val = key
                if 'left' in data[node.val]:
                    node.left = TreeNode()
                    queue.append((node.left, data[node.val]['left']))
                if 'right' in data[node.val]:
                    node.right = TreeNode()
                    queue.append((node.right, data[node.val]['right']))
                   
        # def printNodes(root):
        #     queue = []
        #     if root is None:
        #         return
        #     queue.append(root)
        #     while queue:
        #         node = queue.pop(0)
        #         print(node.val)
        #         if node.left is not None:
        #             queue.append(node.left)
        #         if node.right is not None:
        #             queue.append(node.right)
        # # printNodes(root)
            
        return root

            
                
            
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))