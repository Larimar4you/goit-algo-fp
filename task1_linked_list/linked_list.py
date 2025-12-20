class Node:
    """Node class for a singly linked listj"""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Singly linked list"""

    def __init__(self):
        self.head = None

    def append(self, data):
        """Append a new node to the end of the list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        """Print all nodes in the list"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        """Reverse the linked list"""
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def sort(self):
        """Sort the linked list using insertion sort"""
        if not self.head or not self.head.next:
            return

        sorted_head = None
        current = self.head

        while current:
            next_node = current.next
            sorted_head = self._sorted_insert(sorted_head, current)
            current = next_node

        self.head = sorted_head

    def _sorted_insert(self, head, node):
        """Insert node into sorted list"""
        if not head or node.data < head.data:
            node.next = head
            return node

        current = head
        while current.next and current.next.data < node.data:
            current = current.next

        node.next = current.next
        current.next = node
        return head


def merge_sorted_lists(l1, l2):
    """Merge two sorted linked lists"""
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 if l1 else l2
    return dummy.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(5)
    ll.append(2)
    ll.append(8)
    ll.append(1)

    print("Original list:")
    ll.print_list()

    ll.sort()
    print("Sorted list:")
    ll.print_list()

    ll.reverse()
    print("Reversed list:")
    ll.print_list()

    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(5)
    list1.sort()

    list2 = LinkedList()
    list2.append(2)
    list2.append(4)
    list2.append(6)
    list2.sort()

    merged_list = LinkedList()
    merged_list.head = merge_sorted_lists(list1.head, list2.head)

    print("Merged sorted lists:")
    merged_list.print_list()


"""
Original list:
5 -> 2 -> 8 -> 1 -> None
Sorted list:
1 -> 2 -> 5 -> 8 -> None
Reversed list:
8 -> 5 -> 2 -> 1 -> None
Merged sorted lists:
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
"""
