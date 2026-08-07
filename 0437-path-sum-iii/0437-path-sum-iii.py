class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1

        def dfs(node, curr_sum):
            if not node:
                return 0

            curr_sum += node.val

            count = prefix[curr_sum - targetSum]

            prefix[curr_sum] += 1

            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)

            # Backtrack
            prefix[curr_sum] -= 1

            return count

        return dfs(root, 0)