class Tree:
    def __init__(self, head) -> None:
        self.head = head

    def add_node(self, new_node):
        current_node = self.head
        while current_node:
            if current_node.value > new_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    break
            else:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    break

    def _print_inorder(self, node):
        if not node:
            return
        self._print_inorder(node.left)
        print(node)
        self._print_inorder(node.right)

    def print_tree(self):
        self._print_inorder(self.head)

    def _find_inorder(self, node, value):
        if not node:
            return

        self._find_inorder(node.left, value)
        if node.value == value:
            print("Node found!!")
        self._find_inorder(node.right, value)

    def find_node(self, value):
        # self._find_inorder(self.head, value=value)
        current_node = self.head
        while current_node:
            if current_node.value == value:
                print(f"Node found -> {current_node}.")
                break
            elif current_node.value > value:
                current_node = current_node.left
            else:
                current_node = current_node.right

    def delete_node(self, value: int):
        current_node = self.head
        while current_node:
            print(f"delete - {current_node}")
            if current_node.value == value:
                print("EQUAL ")
                if not current_node.left:
                    print("This one ")
                    # print(f"{current_node.right}")
                    current_node = current_node.right
                    break
                elif not current_node.right:
                    current_node = current_node.left
                    break
                else:
                    break
            elif current_node.value > value:
                current_node = current_node.left
            else:
                current_node = current_node.right
