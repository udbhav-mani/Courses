from node import Node
from tree import Tree


binary_tree = Tree(Node(5))


binary_tree.add_node(Node(6))
binary_tree.add_node(Node(4))
binary_tree.add_node(Node(7))
binary_tree.add_node(Node(1))
binary_tree.add_node(Node(13))

binary_tree.find_node(7)

binary_tree.print_tree()

binary_tree.delete_node(7)
print()
binary_tree.print_tree()
