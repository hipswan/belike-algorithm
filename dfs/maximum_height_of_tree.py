from common import TreeNode, build_tree

def maximum_height_of_tree(root):
    def dfs(node):
        if not node:
            return 0
        left_height = dfs(node.left)
        right_height = dfs(node.right)
        return max(left_height, right_height) + 1

    if isinstance(root, list):
        root = build_tree(root)
    return dfs(root)
# Test cases
def test_maximum_height_of_tree():
    # Test 1: Empty tree
    assert maximum_height_of_tree(None) == 0

    # Test 2: Single node
    root = TreeNode(5)
    assert maximum_height_of_tree(root) == 1

    # Test 3: Complete binary tree
    #      1
    #     / \
    #    2   3
    #   / \
    #  4   5
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3)
    assert maximum_height_of_tree(root) == 3

    # Test 4: Left-skewed tree
    #   1
    #  /
    # 2
    #/
    #3
    root = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert maximum_height_of_tree(root) == 3

    # Test 5: Right-skewed tree
    # 1
    #  \
    #   2
    #    \
    #     3
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    assert maximum_height_of_tree(root) == 3
if __name__ == "__main__":
    test_maximum_height_of_tree()
    print("All tests passed.")