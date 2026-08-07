class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(node, remaining, path):
            if not node:
                return

            path.append(node.val)
            remaining -= node.val

            # Check if it's a leaf and the sum matches
            if not node.left and not node.right and remaining == 0:
                result.append(path[:])   # Store a copy of the path

            dfs(node.left, remaining, path)
            dfs(node.right, remaining, path)

            # Backtrack
            path.pop()

        dfs(root, targetSum, [])
        return result