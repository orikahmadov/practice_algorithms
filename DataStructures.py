
# Singly Linked List

class Node:
    def __init__(self, data =  None):
        self.data =  data
        self.next=  None


class Linked_List:
    def __init__(self):
        self.head =  Node()

    def append_data(self, new_element):
        new_node =  Node(data=new_element)
        current_node  =  self.head
        while current_node.next != None:
            current_node =  current_node.next
        else:
            current_node.next =  new_node


    def length(self):
        counter =  0
        current_node =  self.head
        while current_node != None:
            current_node =  current_node.next
            counter += 1
        return counter


    def has_value(self, value):
        current_node =  self.head
        while current_node.next != None:
            current_node =  current_node.next
            if current_node.data == value:
                return True
        else:
            return False
    
    def pop_item(self, element):
        current =  self.head
        while current.next != None:
            current =  current.next
            if current.data == element:
                return element
        else:
            return None

    def traverse_list(self):
        current_node =  self.head
        while current_node.next != None:
            current_node  = current_node.next
            print(current_node.data)

    def delete_item(self, index):
        if index >= self.length():
            print("List length is exceeded")
        current_index = 0
        current_node =  self.head
        while True:
            last_node = current_node
            current_node =  current_node.next
            if current_index == index:
                last_node.next =  current_node.next
                return
            current_index += 1
