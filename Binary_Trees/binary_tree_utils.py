import collections
import sys

def binary_tree_to_string(tree):
    result = ''
    q = collections.deque()
    visited = set()
    first = True
    null_nodes_pending = 0

    result += '['
    q.append(tree)

    while q:
        node = q.popleft()
        if id(node) in visited:
            raise RuntimeError('Detected a cycle in the tree')
        if node:
            if first:
                first = False
            else:
                result += ', '

            while null_nodes_pending:
                result += 'null, '
                null_nodes_pending -= 1

            result += '"{}"'.format(node.data)

            visited.add(id(node))
            q.append(node.left)
            q.append(node.right)
        else:
            null_nodes_pending += 1

    result += ']'
    return result


def binary_tree_height(tree):
    if not tree:
        return -1
    return 1 + max(
        binary_tree_height(tree.left), binary_tree_height(tree.right))