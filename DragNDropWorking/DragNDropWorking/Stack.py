class stack:

    class node:
        data = None
        pointer = None

    stack_pointer = None

    def push(self,item):
        #Check stack overflow
        try:
            #Push the item
            new_node = stack.node()
            new_node.data = item
            new_node.pointer = self.stack_pointer
            self.stack_pointer = new_node
            return True
        except:
            return False

    def pop(self):
        #Check stack underflow
        if self.stack_pointer != None:
            #Pop the item
            popped = self.stack_pointer.data
            self.stack_pointer = self.stack_pointer.pointer
            return popped
        else:
            return None
        
    def peek(self):
        #Check stack underflow
        if self.stack_pointer != None:
            #Peek the item
            return self.stack_pointer.data
        else:
            return None

#Main program starts here            
items = ["Florida","Georgia","Delaware","Alabama","California"]
s = stack()

for index in range(0,len(items)):
    s.push(items[index])

print(s.pop())

print(s.peek())
