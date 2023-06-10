#
# Priority Queue using Linked List
#

class Node:
    def __init__(self,data,priority):
        self.data = data
        self.priority = priority
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.head = None
    def enqueue(self,data,priority):
        new_node = Node(data, priority)
        if self.isEmpty():
            self.head = new_node
        else:
            if new_node.priority > self.head.priority:
                new_node.next = self.head
                self.head = new_node
            else:
                prev = self.head
                curr = self.head.next
                while curr is not None and new_node.priority <= curr.priority:
                    prev = curr
                    curr = curr.next
                prev.next = new_node
                new_node.next = curr

    def isEmpty(self):
        return self.head is None

    def dequeue(self):
        if self.isEmpty():
            raise "The Queue is Empty!"
        else:
            data = self.head.data
            self.head = self.head.next
            return data
    def length(self):
        count = 0
        curr = self.head
        while curr is not None:
            count+=1
            curr = curr.next
        return count

    def __str__(self):
        out = ""
        curr = self.head
        while curr is not None:
            out += f"{curr.data} - {curr.priority}\n"
            curr = curr.next
        out = out[:-1]
        return out
    def peek(self):
        if self.isEmpty():
            raise "The Queue is Empty!"
        else:
            return self.head.data
def fn():
    pq = PriorityQueue()
    pq.enqueue("Moldoveanu",210)
    pq.enqueue("Negoiu",100)
    pq.enqueue("Vanatoarea lui Buteanu",80)
    pq.enqueue("Peleaga",90)
    print("Length: ",pq.length())
    print(pq)
    print("\n")
    pq.dequeue()
    print("Length: ",pq.length())
    print(pq)
fn()
