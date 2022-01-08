from typing import List

from LinkedListHeaps.LinkedListHeaps import *


def print_main_selection_menu():
    print("Select type of heaps to create:\n"
          "\t1 - Sorted Linked Lists\n"
          "\t2 - Unsorted Linked Lists\n"
          "\t3 - Unsorted Foreign Linked Lists\n"
          "\texit - to quit")


def print_heaps(heaps: List[AbstractLinkedListHeap]):
    for i in range(len(heaps)):
        print(f"Heap {i}:\n{str(heaps[i])}")


def run_sorted():
    run = True
    heaps: List[SortedLinkedListHeap] = []
    while run:
        print_heaps(heaps)
        heap_operation = input()
        if heap_operation == "MakeHeap":
            new_heap = SortedLinkedListHeap()
            heaps.append(new_heap)
        elif heap_operation.startswith("Insert"):
            if not heaps:
                print("No heap to insert the value into")
            heap = heaps[-1]
            try:
                heap.insert_node(int(heap_operation.split(" ")[1]))
            except IndexError:
                print("*** Invalid user input ***")
                continue
        elif heap_operation == "Union":
            # This operation merges all the heaps created in the current operation
            # It leaves a single heap with all the previous heaps merged into it
            if not heaps:
                # If there are no heaps alert the user
                print("*** No heaps ***")
                continue

            while len(heaps) != 1:
                # Union all the heaps. If we have only one heap the loop will never be called
                heaps[0].union_heaps(heaps[1])
                heaps.pop(1)  # Pop the merged heap
        elif heap_operation == "ExtractMin":
            if not heaps:
                # If there are no heaps alert the user
                print("*** No heaps ***")
                continue
            try:
                print(f"The minimum value extracted is {heaps[-1].extract_min()}")
            except ValueError as e:
                print(e)
        elif heap_operation == "Minimum":
            if not heaps:
                # If there are no heaps alert the user
                print("*** No heaps ***")
                continue
            print(f"The minimum value is {heaps[-1].get_min()}")
        elif heap_operation == "exit":
            run = False
        else:
            print("*** Invalid user input ***")


def run_unsorted():
    run = True
    heaps: List[UnsortedLinkedListHeap] = []
    while run:
        print_heaps(heaps)
        heap_operation = input()
        if heap_operation == "MakeHeap":
            new_heap = UnsortedLinkedListHeap()
            heaps.append(new_heap)
        elif heap_operation.startswith("Insert"):
            if not heaps:
                print("No heap to insert the value into")
            heap = heaps[-1]
            try:
                heap.insert_node(int(heap_operation.split(" ")[1]))
            except IndexError:
                print("*** Invalid user input ***")
                continue
        elif heap_operation == "Union":
            # This operation merges all the heaps created in the current operation
            # It leaves a single heap with all the previous heaps merged into it
            if not heaps:
                # If there are no heaps alert the user
                print("*** No heaps ***")
                continue

            while len(heaps) != 1:
                # Union all the heaps. If we have only one heap the loop will never be called
                heaps[0].union_heaps(heaps[1])
                heap_to_del = heaps.pop(1)  # Pop the merged heap
                del heap_to_del             # Delete the merged heap
        elif heap_operation == "ExtractMin":
            if not heaps:
                # If there are no heaps alert the user
                print("*** No heaps ***")
                continue
            try:
                print(f"The minimum value extracted is {heaps[-1].extract_min()}")
            except ValueError as e:
                print(e)
        elif heap_operation == "Minimum":
            if not heaps:
                # If there are no heaps alert the user
                print("*** No heaps ***")
                continue
            print(f"The minimum value is {heaps[-1].get_min()}")
        elif heap_operation == "exit":
            run = False
        else:
            print("*** Invalid user input ***")



def check_value_in_all_heaps(heaps, val):
    """
    Check that value val is not found in any of the existing heaps
    :param val:         The value to check
    :return:            True if the value exists, False otherwise
    """
    for curr_heap in heaps:
        curr_node = curr_heap.head
        while curr_node:
            if curr_node.val == val:
                return True
            curr_node = curr_node.next

    return False


def run_unsorted_unique():
    run = True
    heaps: List[UnsortedUniqueLinkedListHeap] = []
    while run:
        print_heaps(heaps)
        heap_operation = input()
        if heap_operation == "MakeHeap":
            new_heap = UnsortedUniqueLinkedListHeap()
            heaps.append(new_heap)
        elif heap_operation.startswith("Insert"):
            if not heaps:
                print("No heap to insert the value into")
            heap = heaps[-1]
            try:
                value = int(heap_operation.split(" ")[1])
                if not check_value_in_all_heaps(heaps, value):
                    heap.insert_node(value)
                else:
                    print(f"*** Value {value} exists in one of the heaps ***")
            except IndexError:
                print("*** Invalid user input ***")
                continue
        elif heap_operation == "Union":
            # This operation merges all the heaps created in the current operation
            # It leaves a single heap with all the previous heaps merged into it
            if not heaps:
                # If there are no heaps alert the user
                print("*** No heaps ***")
                continue

            while len(heaps) != 1:
                # Union all the heaps. If we have only one heap the loop will never be called
                heaps[0].union_heaps(heaps[1])
                heap_to_del = heaps.pop(1)  # Pop the merged heap
                del heap_to_del  # Delete the merged heap
        elif heap_operation == "ExtractMin":
            if not heaps:
                # If there are no heaps alert the user
                print("*** No heaps ***")
                continue
            try:
                print(f"The minimum value extracted is {heaps[-1].extract_min()}")
            except ValueError as e:
                print(e)
        elif heap_operation == "Minimum":
            if not heaps:
                # If there are no heaps alert the user
                print("*** No heaps ***")
                continue
            print(f"The minimum value is {heaps[-1].get_min()}")
        elif heap_operation == "exit":
            run = False
        else:
            print("*** Invalid user input ***")


def main():
    run = True
    while run:
        print_main_selection_menu()
        user_input = input()
        if user_input == "1":
            run_sorted()
        elif user_input == "2":
            run_unsorted()
        elif user_input == "3":
            run_unsorted_unique()
        elif user_input == "exit":
            run = False
        else:
            print("*** Invalid input! ***")


if __name__ == "__main__":
    main()
