class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data
    
class LinkedList:

    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:

            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " --> ".join(nodes)

    def add_node(self,node):
        node.next = self.head
        self.head = node

    def add_after(self, target_node_data, new_node):
        if self.head == None:
            raise Exception("list empty! :( ")
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception("node with data '%s' not found! " % target_node_data)
    
        
    

if __name__ == "__main__":
    list = LinkedList()
    
    list.add_node(Node("6"))
    list.add_node(Node("9"))

    list.add_after("6", "5")

    #list.remove()

    print(list)

