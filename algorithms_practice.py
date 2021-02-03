###################################################################################################################################################################
#Linear Search Algorithm runs in Linear Complexity
def linear_search(list, item):
    found = False
    for i in range(len(list)):
        if list[i] == item:
            found = True
    return found
###################################################################################################################################################################

#NOTE THAT THIS ALGORITHM WORKS ONLY IF THE INPUT LIST IN SORTED 
#Binary Search
def binary_search(list, item):
    start = 0
    end  =  len(list) - 1
    while start <= end:
        middle =  (start +  end) // 2
        if list[middle] == item:
            return middle
        elif item >  list[middle]:
            start =  middle + 1
        else:
            end =  middle - 1
    return None
###################################################################################################################################################################

def QuickSort(list):
    #length of list
    length_list =  len(list)
    #if there is less than 1 item in list return list
    if length_list <=  1:
        return list
    #define pivot
    else:
        pivot =  list.pop() #Last item as pivot

    #2 Lists which will hold the values of compared elements
    itemsLower = []
    itemsGreater = []
    #iterate through  list
    for item in list:
        if item < pivot:
            itemsLower.append(item)
        else:
            itemsGreater.append(item)
    #recursively return the function
    return QuickSort(itemsLower) + [pivot] + QuickSort(itemsGreater)

###################################################################################################################################################################
#Finding Characters frequency in a string
string =  "Today the weather is so beautiful,therefore I want to go for walk!"
def chars_frequency(list):
    chars = {}   #Start
    for i in list:
        if i not in chars:
            chars[i] = 0
        chars[i] +=1
    return chars

#Finding Word frequency in a string basically same algorithm except you split the string and convert it to list
string =  "Today the weather is so beautiful,therefore I want to go for walk and walking is so healthy !"
def word_frequency(string):
    words = {}   #Start
    for i in string.split():
        if i not in chars:
            words[i] = 0
        words[i] +=1
    return words
###################################################################################################################################################################
#Comparing 2 strings and finding how many times a single character of one string occurs in another

def str_frequency(a,b):
    str =  a + b
    characters =  {}
    for i in str:
        if i not in characters:
            characters[i] = 0
        characters[i] +=1
    return characters

###################################################################################################################################################################

#Recursion
def is_array_sorted(array):
    if len(array) == 1:
        return True
    else:
        return array[0] <= array[1]  and is_array_sorted(array[1:])
###################################################################################################################################################################
# Singly Linked List

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head =  Node()


    def append(self, new_element):
        new_node =  Node(data =  new_element) # new created node holds the passed data to it
        current_node =  self.head           #left most point head node of the list
        while current_node.next != None:    # iterating untill the last element of the list as long
            current_node = current_node.next    #as it is not empty add the new node to the next
        else:
            current_node.next =  new_node          #otherwise assign new node to the current node

    def __len__(self):
        current =  self.head
        counter = 0
        while current != None:
            counter += 1
            current = current.next
        return counter

    def traverse(self):
        current =  self.head
        elements = []
        while current.next != None:
            current =  current.next
            elements.append(current)
        else:
            return elements


    def has_value(self, value):
        current =  self.head
        while current.next != None:
            current = current.next
            if current == value:
                return f"Found {value}"
            else:
                return f"Not found"

    def pop(self, index):
        if index >= self.__len__():
            return("Index exceeded the length of the list")
        else:
            current_index =  0
            current_node =  self.head
            while current_node.next != None:
                current_node = current_node.next
                if current_index ==  index:
                    current_index += 1
                else:
                    return current_node.data

    def delete_node(self, index):
        if index >= self.__len__():
            print("Exceeded the length")
            return None
        else:
            current =  self.head
            while True:
                last_node = current
                current =  current.next
                if current== index:
                    last_node.next =  current.next
                else:
                    index += 1

