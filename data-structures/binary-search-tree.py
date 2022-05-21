# Binary Search Tree for numbers.
# *insert, delete
# *traversal, traverse, find (dft,bft)
# get_node, get_height, get_successor
# min, max
# level, height

from collections import deque
from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        node = Node(val)
        if not self.root:
            self.root = node
            return
        current = self.root
        parent = self.root
        while current:
            parent = current
            if val >= current.val:
                current = current.right
                if not current:
                    parent.right = node
                    return
            else:
                current = current.left
                if not current:
                    parent.left = node
                    return

    def delete_recursive(self, root, val):
        # The idea is to rewrite left/right child on each iteration, with new changes included
        # so when we get back to the first recursion, we have the root of the newly changed tree.
        # in each iteration, we're either returning the root itself, or whatever we've put in its place after deletion.
        if not root:
            return
        # Traversal
        if val < root.val:
            root.left = self.delete_recursive(root.left, val)
        elif val > root.val:
            root.right = self.delete_recursive(root.right, val)
        else:
            # node with val=val is found.

            # no child
            if not root.right and not root.left:
                root = None
            # 2 children
            elif root.right and root.left:
                succ = self.min(root.right)
                root.val = succ.val
                root.right = self.delete_recursive(root.right, succ.val)
            # 1 child, right
            elif root.right:
                root = root.right
            # 1 child, left
            elif root.left:
                root = root.left

        return root

    def delete_iterative(self, val: Optional[Node]):
        # we could also get the root, so that we can have a reursive call when we want to delete the inorder successor.
        # we could also make the traversal part recursive

        # traverse and find the node, keep track of parent
        current = self.root
        parent = self.root

        while current:
            if val == current.val:
                break
            parent = current
            if val > current.val:
                current = current.right
            else:
                current = current.left

        # if there is no node in tree or the value is not found, just return.
        if not current:
            return

        # handle case by case based on num of node's children. put the 1-child condition
        # at the end, so that we can just write 'else' for it!

        # no child on node:
        if not current.left and not current.right:
            if parent.left == current:
                parent.left = None
            if parent.right == current:
                parent.right = None

        # two children on node:
        elif current.left and current.right:
            # get the successor. since the node has two children, its successor will def be in its right subtree
            succ_parent = current
            succ = current.right
            while succ:
                if not succ.left:
                    break
                succ_parent = succ
                succ = succ.left
            current.val = succ.val

            # the successor can either have no child, or just the right child
            if succ_parent.left == succ:
                succ_parent.left = succ.right
            if succ_parent.right == succ:
                succ_parent.right = succ.right

        # one chid on node:
        else:
            child = current.left if current.left else current.right
            if parent.left == current:
                parent.left = child
            if parent.right == current:
                parent.right == child

    def traverse(self, method=0):
        """Available Methods:
        0 - inorder, depth-first, recursive
        1 - preorder, depth-first, recursive
        2 - postorder, depth-first, recursive
        3 - breadth-first
        """
        methods = {
            0: self._traverse_inorder,
            1: self._traverse_preorder,
            2: self._traverse_postorder,
            3: self._traverse_breadth_first,
            4: self._traverse_inorder_stack_recursive,
        }

        return methods.get(method, 0)(self.root)

    def _traverse_inorder(self, node):
        if not node:
            return
        self._traverse_inorder(node.left)
        print(node.val)
        self._traverse_inorder(node.right)

    def _traverse_preorder(self, node):
        if not node:
            return
        print(node.val)
        self._traverse_preorder(node.left)
        self._traverse_preorder(node.right)

    def _traverse_postorder(self, node):
        if not node:
            return
        self._traverse_postorder(node.left)
        self._traverse_postorder(node.right)
        print(node.val)

    def _traverse_breadth_first(self, node, queue=deque()):

        if node:
            print(node.val)
            queue.append(node.left)
            queue.append(node.right)
        if queue:
            self._traverse_breadth_first(queue.popleft())

    def _traverse_inorder_stack_recursive(self, node, stack=[]):
        if not node and not stack:
            return
        if node:
            stack.append(node)
            new_node = node.left
        elif stack:
            new_node = stack.pop()
            print(new_node.val)
            new_node = new_node.right

        self._traverse_inorder_stack_recursive(new_node, stack)

    def is_in_tree(self, val):
        current = self.root
        while current:
            if val == current.val:
                return True
            elif val > current.val:
                current = current.right
            else:
                current = current.left
        return False

    def min(self, node=None):
        if not node:
            if not self.root:
                return
            node = self.root

        parent = node
        current = node
        while current:
            parent = current
            current = current.left
        return parent

    def max(self, node=None):
        if not node:
            if not self.root:
                return
            node = self.root

        parent = node
        current = node
        while current:
            parent = current
            current = current.right
        return parent

    def get_successor(self, node):
        if not node:
            return
        # If there is a right subtree, successor is the min value in there (left-most)
        if node.right:
            return self.min(node.right)

        # If not, one of the ancestors is the successor, so we traverse from root to find it.
        current = self.root
        # if node is the greatest value in tree, successor will be Null, so we prepare an empty node.
        suc = Node(None)
        while current and current.val != node.val:

            # if current is smaller than our node, we need to go to right to get to bigger values.
            if current.val < node.val:
                current = current.right
            # if current is bigger than our node, we go to left and update successor with
            # what comes up. Once we get to None or the node itself, we have the successor.
            elif current.val > node.val:
                suc = current
                current = current.left
        return suc

    def get_predecessor(self, node):
        if not node:
            return
        # if there is a left subtree, pred is the max node in it (right-most)
        if node.left:
            return self.max(node.left)

        # if not, its an ancestor. so we start from the root.
        current = self.root
        # In case node is also the min and predeccessor is null...
        pred = Node(None)

        while current:
            if current.val < node.val:
                pred = current
                current = current.right
            elif current.val > node.val:
                current = current.left
            else:
                # we got to predecessor. since it didn't have a left subtree (checked at step 1),
                # we've found the predecessor.
                break
        return pred

    def get_height(self, node):
        # max number of edges from root to a leaf
        if not node or (not node.left and not node.right):
            return 0

        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)

        return max(left_height, right_height) + 1

    def get_size(self, node):
        # count of all nodes in tree

        if not node:
            return 0
        left_size = self.get_size(node.left)
        right_size = self.get_size(node.right)
        return right_size + left_size + 1

    def get_level(self, root, node):
        # if only root, level = 1. root's children are level 2, and so on.
        if not node:
            return 0
        if root.val == node.val:
            return 1
        if node.val < root.val:
            return 1 + self.get_level(root.left, node)
        if node.val > root.val:
            return 1 + self.get_level(root.right, node)


t = BinarySearchTree()
a = [12, 5, 14, 15, 3, 7, 1, 2, 6, 7.5, 7.25, 7.26, 9, 8.5, 10]
for i in a:
    t.insert(i)

print("traversing...")
t.t(t.root)
