from abc import ABCMeta, abstractmethod
from typing import List


class Node:
    def __init__(self, val: int, forward=None):
        """
        An implementation of a singly linked list with INT values
        :param val:             The value of the node
        :param forward:         The next node in the linked list
        """
        self.val = val
        self.next = forward


class AbstractLinkedListHeap(metaclass=ABCMeta):
    def __init__(self):
        """
        An implementation of a Heap using a linked lists
        Runtime:
            * O(1)
        """
        self.head: Node = None

    def __str__(self):
        linked_list_list: List[str] = []
        if self.head:
            curr_node = self.head
            while curr_node:
                linked_list_list.append(str(curr_node.val))
                curr_node = curr_node.next

        return "->".join(linked_list_list)

    @abstractmethod
    def insert_node(self, val: int):
        """
        An abstract method for the different types of linked lists implementations to override
        :param val:         The value of the new node to be inserted
        :return:            Changes the linked list of the heap in accordance to its type
        """
        raise NotImplementedError("Method insert_node is not implemented!!!")

    @abstractmethod
    def get_min(self) -> int:
        raise NotImplementedError("Method get_min is not implemented!!!")

    @abstractmethod
    def extract_min(self) -> int:
        """
        A function that returns the minimum value of the heap
        :return:
        """
        raise NotImplementedError("Method extract_min is not implemented!!!")

    @abstractmethod
    def union_heaps(self, heap_to_union):
        """
        A function that merges two heaps
        :param heap_to_union:       The heap to union with
        :return:                    None
        """
        raise NotImplementedError("Method union_heaps is not implemented!!!")


class SortedLinkedListHeap(AbstractLinkedListHeap):
    def insert_node(self, val: int):
        """
        As we're implementing a sorted linked list here we'll just insert the node in it's correct position
        Runtime:
            * O(n)
        """
        new_node = Node(val=val)
        if not self.head:
            self.head = new_node
        else:
            if val <= self.head.val:
                new_node.next = self.head
                self.head = new_node
                return

            curr_node = self.head
            while curr_node.next and curr_node.next.val:
                curr_node = curr_node.next

            new_node.next = curr_node.next
            curr_node.next = new_node

    def get_min(self) -> int:
        """
        Get the minimum value of the heap
        :return:        The min val of the heap
        """
        if not self.head:
            raise ValueError("The heap is empty!")
        return self.head.val

    def extract_min(self) -> int:
        """
        Since we have a sorted linked list we'll just return the first value of the linked list
        Runtime analysis:
            * O(1)
        :return:            Minimum value of the heap
        """
        if not self.head:
            raise ValueError("The heap is empty!")
        min_val = self.head.val
        node_to_del = self.head
        self.head = self.head.next
        del node_to_del
        return min_val

    def union_heaps(self, heap_to_merge):
        """

        :param heap_to_merge:
        :return:
        """
        new_list: Node = None
        curr_node_self: Node = self.head
        curr_node_to_merge: Node = heap_to_merge.head

        while curr_node_self and curr_node_to_merge:
            if curr_node_self.val <= curr_node_to_merge.val:
                # If the new_list is None initiate it with the first value of the merge
                if not new_list:
                    new_list = curr_node_self
                    # Set the head to be the new list's first element
                    curr_node_self = curr_node_self.next
                    self.head = new_list
                else:
                    # Insert the next value in the next node of the linked list and move all
                    # the pointers
                    new_list.next = curr_node_self
                    curr_node_self = curr_node_self.next
                    new_list = new_list.next
            else:
                # If the new_list is None initiate it with the first value of the merge
                if not new_list:
                    new_list = curr_node_to_merge
                    # Set the head to be the new list's first element
                    curr_node_to_merge = curr_node_to_merge.next
                    self.head = new_list
                else:
                    # Insert the next value in the next node of the linked list and move all
                    # the pointers
                    new_list.next = curr_node_to_merge
                    curr_node_to_merge = curr_node_to_merge.next
                    new_list = new_list.next

        if curr_node_self:
            new_list.next = curr_node_self
        else:
            new_list.next = curr_node_to_merge


class UnsortedLinkedListHeap(AbstractLinkedListHeap):
    def __init__(self):
        super().__init__()
        self.last = None

    def insert_node(self, val: int):
        """
        As we're dealing with an unsorted linked list we'll just prepend the new value to the currently existing list
        Runtime analysis:
            * O(1)
        :param val:             The new value to insert
        """
        new_node = Node(val)
        if not self.head:
            self.last = new_node
        new_node.next = self.head
        self.head = new_node

    def extract_min(self, is_unique=False) -> int:
        """
        We extract all the minimum value nodes from the heap.
        Runtime complexity:
            * O(n)
        :return:        The minimum value extracted
        """
        min_val = self.get_min()  # Get the min value

        while self.head and self.head.val == min_val:
            # If the head is the minimum value unlink it and set the new head
            node_to_del = self.head
            if self.last == node_to_del:
                # If the node we're deleting from the head is the last one as well
                # set the ptr to the last node to None
                self.last = None
            self.head = self.head.next
            del node_to_del
            if is_unique:
                return min_val

        if not self.head:
            return min_val

        curr_node = self.head

        while curr_node.next:
            # Find all the nodes with the minimum value and unlink them
            if curr_node.next.val == min_val:
                node_to_del = curr_node.next
                if self.last == node_to_del:
                    # If the node we're about to delete is the last one, we move the ptr to the last
                    # node to be the current node
                    self.last = curr_node
                curr_node.next = curr_node.next.next
                del node_to_del     # Delete the node with the minimum value
                if is_unique:
                    return min_val
            else:
                curr_node = curr_node.next

    def get_min(self) -> int:
        """
        Runtime analysis:
            * O(n)
        """
        if not self.head:
            raise ValueError("The heap is empty!")
        min_val: int = self.head.val
        curr_node: Node = self.head.next
        while curr_node:
            if curr_node.val < min_val:
                min_val = curr_node.val
            curr_node = curr_node.next

        return min_val

    def union_heaps(self, heap_to_union):
        """
        Union the heaps. We're keeping track of the last node, so we just switch the pointers around
        Now the last is linked to the merged head, and the last is pointed to the merged last node
        Runtime analysis:
            * O(n)
        Note:
            If I would've used a doubly linked list with the first and last node connected the union
            operation would've been done in a runtime complexity of O(1)
        :param heap_to_union:           The heap to union
        """
        self.last.next = heap_to_union.head
        self.last = heap_to_union.last


class UnsortedUniqueLinkedListHeap(UnsortedLinkedListHeap):

    def extract_min(self, is_unique=True) -> int:
        return super().extract_min(is_unique)
