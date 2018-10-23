from Node import Node
import sys


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
            find_duplicates_unsorted(user_list)
            print("Done")

        elif selection == '2':
            user_list_bubble_sort = create_linkedlist(users)
            user_list_bubble_sort.print_list()
            print("Loading...Please wait")
            bubble_sort(user_list_bubble_sort)
            user_list_bubble_sort.print_list()
            find_duplicates_sorted(user_list_bubble_sort)
            print("Done")

        elif selection == '3':
            user_list_merge_sort = create_linkedlist(users)
            user_list_merge_sort.print_list()
            print("Loading...Please wait")
            merge_Sort(user_list_merge_sort)
            user_list_merge_sort.print_list()
            print("Done")
        elif selection == '4':
            break

        elif selection == '5':
            print("Bye!")
            break
        else:
            print("Unknown Option Selected!")


def find_duplicates_unsorted(list):
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
    middle = get_middle2(list)
    rhalf = middle.next
    middle.next = None

    return merge_list(merge_sort(list), merge_sort(rhalf))

def merge_list(lhalf, rhalf):
    result = Node(None, None)

    while lhalf.item is not None:
        if lhalf.next is None:
            return rhalf
        if rhalf.next is None:
            return lhalf
        if lhalf.item <= rhalf.item:
            result = (lhalf.item, result)
            result.print_list()
            lhalf = lhalf.next
        else:
            result = (rhalf.item, result)
            lhalf = lhalf.next
        rhalf = rhalf.next

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




def merge_Sort(list):
    x1 = list
    while x1 is not None:
        x2 = x1.next
        while x2 is not None:
            if x2.item is None:
                break
            if x1.item > x2.item:
                swap(x1, x2)
            x2 = x2.next
        x1 = x1.next


def main():
    sys.setrecursionlimit(1000000)
    display_menu() #Display the menu with the options
    #usuarios = [5, 3, 2, 4, 1, 4,5]
    #usuarios_lista = create_linkedlist(usuarios)
    #usuarios_lista.print_list()
    #bubble_sort(usuarios_lista)
    #usuarios_lista.print_list()
    #find_duplicates_sorted(usuarios_lista)






main()
