from Node import Node
from timeit import default_timer as timer


def fill_list():         #Method for populating the array of the total number of user
    activision_users = []
    vivendi_users = []
    activisionfile = open("activision.txt", "r")
    vivendifile = open("vivendi.txt", "r")
    number_lines_activision = sum(1 for line in open("activision.txt"))
    number_lines_vivendi = sum(1 for line in open("vivendi.txt"))

    for i in range(number_lines_activision):
        activision_users.append(int(activisionfile.readline()))
    for i in range(number_lines_vivendi):
        vivendi_users.append(int(vivendifile.readline()))
    all_users = activision_users + vivendi_users
    return all_users


def create_linkedlist(user): #Method for populating the linkedList with the user list
    x = Node(None, None)        #Initiating a Node with .item=None and .next=None
    for i in range(len(user)):
        x = Node(user[i], x)
    return x


def display_menu():
    users = fill_list()
    user_list = create_linkedlist(users)
    menu = {}
    menu['1'] = "Compare every element(Unsorted LinkedList) nested loops"
    menu['2'] = "Bubble sort / Duplicates(Sorted LinkedList)"
    menu['3'] = "Merge sort / Duplicates(Sorted LinkedList)"
    menu['4'] = "True-False / Duplicates(Sorted LinkedList)"
    menu['5'] = "Exit"
    while True:
        user_list.print_list()
        options = menu.keys()

        for entry in options:
            print(entry, menu[entry])
        selection = input("Please Select:")

        if selection == '1':
            print("Loading...Please wait")
            user_list.print_list()
            unsorted_start_timer = timer()
            find_duplicates_unsorted(user_list)
            unsorted_end_timer = timer()
            total_time = (unsorted_end_timer - unsorted_start_timer)
            print("Time for duplicates in unsorted array: ", total_time)
            print("Done")
            print("\n")

        elif selection == '2':
            user_list_bubble_sort = create_linkedlist(users)
            user_list_bubble_sort.print_list()
            print("Loading...Please wait")
            bubble_sort_start_timer = timer()
            bubble_sort(user_list_bubble_sort)
            bubble_sort_end_timer = timer()
            total_time_bubble_sort = (bubble_sort_end_timer - bubble_sort_start_timer)
            user_list_bubble_sort.print_list()
            print("Time for bubble sort: ", total_time_bubble_sort)
            sorted_start_timer = timer()
            find_duplicates_sorted(user_list_bubble_sort)
            sorted_end_timer = timer()
            total_time_sorted = (sorted_end_timer - sorted_start_timer)
            print(total_time_sorted)
            print("Done")
            print("\n")

        elif selection == '3':
            user_list_merge_sort = create_linkedlist(users)
            user_list_merge_sort.print_list()
            print("Loading...Please wait")
            merge_sort(user_list_merge_sort)
            user_list_merge_sort.print_list()
            print("Done")
            print("\n")
        elif selection == '4':
            user_list_boolean = create_linkedlist(users)
            user_list_boolean.print_list()
            print("Loading...Please wait")
            Boolean_start_timer = timer()
            boolean_list = check_Boolean(user_list_boolean)
            Boolean_end_timer = timer()
            total_time_Boolean = (Boolean_end_timer - Boolean_start_timer)
            print(boolean_list)
            check_boolean_list(boolean_list)
            print(total_time_Boolean)
            print("Done")
            print("\n")

        elif selection == '5':
            print("Bye!")
            break
        else:
            print("Unknown Option Selected!")


def find_duplicates_unsorted(list):         #This method would find duplicates in a unsorted list
    x1 = list
    duplicate_elements = []
    while x1 is not None:
        x2 = x1.next
        while x2 is not None:
            if x1.item == x2.item:
                duplicate_elements.append(x1.item)
            x2 = x2.next
        x1 = x1.next
    print("Duplicates: ", duplicate_elements)


def find_duplicates_sorted(list):
    x1 = list
    duplicate_elements = []
    while x1 is not None:
        if x1.next is None:
            break
        if x1.item == x1.next.item:
            duplicate_elements.append(x1.item)
        x1 = x1.next
    print("Duplicates: ", duplicate_elements)


def bubble_sort(list):
    for i in range(list.length()):
        x1 = list
        x2 = x1.next
        while x2 is not None:
            if x2.item is None:
                break
            if x1.item > x2.item:
                swap(x1, x2)
            x2 = x2.next
            x1 = x1.next


def swap(node1, node2):
    temp = node1.item
    node1.item = node2.item
    node2.item = temp


def merge_sort(list):
    if list is None or list.next is None:
        return list
    middle = get_middle(list)
    right_half = middle.next
    middle.next = None

    return merge_list(merge_sort(list), merge_sort(right_half))

def merge_list(left_half, right_half):
    result = Node(None, None)

    while left_half.item is not None:
        if left_half.next is None:
            return right_half
        if right_half.next is None:
            return left_half
        if left_half.item <= right_half.item:
            result = (left_half.item, result)
            result.print_list()
            left_half = left_half.next
        else:
            result = (right_half.item, result)
            left_half = left_half.next
        right_half = right_half.next

    return result


def get_middle(list):
    if list is None:
        return list
    slow = list
    fast = list
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


def check_Boolean(list):
    seen = [False]*(list.length()+1)
    x1 = list
    x2 = x1.next
    while x2 is not None:
        if x1.item == x2.item:
            seen[x1.item] = True
        x1 = x1.next
        if x1 == x2:
            x2 = x2.next
            x1 = list
    return seen


def check_boolean_list(boolean_list):
    duplicates = []
    for i in range(len(boolean_list)):
        if boolean_list[i] == True:
            duplicates.append(i)
    print("Duplicates: ", duplicates)


def main():
    display_menu() #Display the menu with the options
    #usuarios = [1, 0, 0, 3, 2, 3, 1]
    #usuarios_lista = create_linkedlist(usuarios)
    #usuarios_lista.print_list()


main()

