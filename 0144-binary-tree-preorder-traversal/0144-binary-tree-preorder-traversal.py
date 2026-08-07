class Solution:
    def preorderTraversal(self, root):
        res = []

        def dfs(node):
            if not node:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return res