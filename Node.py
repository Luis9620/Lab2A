class Node(object):
    def __init__(self, item, next):
        self.item = item
        self.next = next

    def print_list(self):
        elements = []
        node = self  # start from the head node
        while node is not None:
            elements.append(node.item)  # access the node value
            node = node.next  # move on to the next node
        print(elements)

    def length(self):
        cur = self
        total = 0
        while cur.next is not None:
            total += 1
            cur = cur.next
        return total