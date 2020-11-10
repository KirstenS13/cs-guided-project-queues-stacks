"""
You've encountered a situation where you want to easily be able to pull the
largest integer from a stack.

You already have a `Stack` class that you've implemented using a dynamic array.

Use this `Stack` class to implement a new class `MaxStack` with a method
`get_max()` that returns the largest element in the stack. `get_max()` should
not remove the item.

*Note: Your stacks will contain only integers. You should be able to get a
runtime of O(1) for push(), pop(), and get_max().*
"""
class Stack:
    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]

# UNDERSTAND
# to move through a stack, we hanve to remove items
# we would need to store them somewhere else so we don't lose them
# we should not directly use a linked list or an array
# we should build off of the Stack class

class MaxStack:
    def __init__(self):
        # Your code here
        self.stack = Stack()
        # more stuff here?


    def push(self, item):
        """Add a new item onto the top of our stack."""
        # Your code here
        self.stack.push(item)
        # update max as necessary
        if self.max < item:
            self.max = item


    def pop(self):
        """Remove and return the top item from our stack."""
        # Your code here
        item = self.stack.pop()
        # check if we're removing the max
        if item == max:
            # if so, we need to update self.max
            new_max = self.find_max()
            self.max = new_max
        return item


    def get_max(self):
        """The last item in maxes_stack is the max item in our stack."""
        # Your code here
        # we can't go inside the stack so...
        # Approach 1: pop everything off, find the max, and push it back on
        # trick: when we push it back on, we want everything to stay in the same order
        # we can't change the order of the stack in any way
        # values = []
        # element = self.stack.pop()
        # cur_max = None
        # while element is not None:
            # values.append(element)
        #     if cur_max is None or cur_max < element:
        #         cur_max = element
        #     element = self.stack.pop()

        # # loop:
        # for i in range(len(values) -1, -1, -1):
        #     # start with i = len(values) - 1, go up to (but not including) i = -1, decrement i by -1 on each loop
        #     # JS translation: for (int i = len(values) - 1; i > -1; i--)
        #     # we're going backwards through the range
        #     element = values[i]
        #     self.push(element)

        
        # # stack: 1, 2, 3
        # # values = [3, 2, 1], stack = []
        # return cur_max

        # This works but it's pretty slow

        # Approach 2: we change push so that it keeps track of max

# What we want the code to do
# we make a stack with values
max_stack = MaxStack()
max_stack.push(1)
max_stack.push(2)
max_stack.push(3)
# this should give us the maximum value (which should be at the top)
max = max_stack.get_max()
# the print statement should be true
print(max == 3)

# if we remove the top value, the next one should be the max
max_stack.pop()
# the print statement should be true
print(max_stack.get_max() == 2)