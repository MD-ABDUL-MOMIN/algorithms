## Maximum sum path of binary tree. 
##MD ABDUL MOMIN
#30-05-18

class Node:
     
 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def findMaxTree(root):
     
  
    if root is None:
        return 0
 
  
    l = findMaxTree(root.left)
    r = findMaxTree(root.right)
     

    max_single = max(max(l, r) + root.data, root.data)
     
    max_top = max(max_single, l+r+ root.data)

    findMaxTree.res = max(findMaxTree.res, max_top)

    return max_single
 

def findMaxSum(root):
     
  
    findMaxTree.res = float("-inf")
     
    
    findMaxTree(root)
    return findMaxTree.res
 
# Driver program 
root = Node(10)
root.left = Node(2)
root.right   = Node(10);
root.left.left  = Node(20);
root.left.right = Node(1);
root.right.right = Node(-25);
root.right.right.left   = Node(3);
root.right.right.right  = Node(4);
print("Max path sum is " ,findMaxSum(root));
 