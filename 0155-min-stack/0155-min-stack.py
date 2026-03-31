class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        
        # If min_stack is empty, the current val is the min.
        # Otherwise, compare val with the current top of min_stack.
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            new_min = min(val, self.min_stack[-1])
            self.min_stack.append(new_min)

    def pop(self):
        """
        :rtype: None
        """
        # Both stacks must stay in sync
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]