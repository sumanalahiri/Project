class queue:

    class node:
        data = None
        pointer = None

    front_pointer = None
    back_pointer = None

    def enqueue(self,item):
        #Check queue overflow
        try:
            #Push the item
            new_node = queue.node()
            new_node.data = item
            #Empty queue
            if self.back_pointer == None:
                self.front_pointer = new_node
            else:
                self.back_pointer.pointer = new_node
            self.back_pointer = new_node
            return True
        except:
            return False

    def dequeue(self):
        #Check queue underflow
        if self.front_pointer != None:
            #Dequeue the item
            popped = self.front_pointer.data
            self.front_pointer = self.front_pointer.pointer
            #When the last item is dequeued reset the pointers
            if self.front_pointer == None:
                self.back_pointer = None
            return popped
        else:
            return None
        
    def peek(self):
        #Check queue underflow
        if self.front_pointer != None:
            #Peek the item
            return self.front_pointer.data
        else:
            return None

#Main program starts here            
items = ["Florida","Georgia","Delaware","Alabama","California"]
q = queue()
for index in range(0,len(items)):
    q.enqueue(items[index])
print(q.dequeue())
print(q.peek())

