from common import TreeNode, build_tree

def sum_of_all_nodes(root):

    def dfs(node):
        if not node:
            return 0
        return node.val + dfs(node.left) + dfs(node.right)

    if isinstance(root, list):
        root = build_tree(root)
    return dfs(root)

# Test cases
def test_sum_of_all_nodes():
    # Test 1: Empty tree
    assert sum_of_all_nodes(None) == 0

    # Test 2: Single node
    root = TreeNode(5)
    assert sum_of_all_nodes(root) == 5

    # Test 3: Complete binary tree
    #      1
    #     / \
    #    2   3
    #   / \
    #  4   5
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3)
    assert sum_of_all_nodes(root) == 15

    # Test 4: Left-skewed tree
    #   1
    #  /
    # 2
    #/
    #3
    root = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert sum_of_all_nodes(root) == 6

    # Test 5: Right-skewed tree
    # 1
    #  \
    #   2
    #    \
    #     3
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    assert sum_of_all_nodes(root) == 6

if __name__ == "__main__":
    test_sum_of_all_nodes()
    print("All tests passed.")

