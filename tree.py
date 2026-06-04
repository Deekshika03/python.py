#univalued tree
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return True

            if node.val != root.val:
                return False

            return dfs(node.left) and dfs(node.right)

        return dfs(root)


#traversal
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #inorderTraversal=left->root->right
        ans=[]
        def inorder(node):
            if not node:
                return 
            inorder(node.left)     
            ans.append(node.val)   # ans  se  store root node ki val append krne k liye
            inorder(node.right)    
        inorder(root)
        return ans


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def preorder(node):
            if not node:
                return
            ans.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return ans

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def postorder(node):
            if not node:
                return

            postorder(node.left)
            postorder(node.right)
            ans.append(node.val)

        postorder(root)
        return ans
