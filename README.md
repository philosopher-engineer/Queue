# Queue
Queue implementation based on 2 stacks.
Stack s1 is to write (add) and stack s2 is to get (remove/peek).

In this implementation:
1. In add operation, the new element is entered at the top of stack s1. 
2. In remove operation, if stack s2 is empty then all elements are moved to stack s2 and finally top of stack s2 is returned.
3. Peek operation is supported. Retrieves the top of stack s2.
4. Length retrieves total elements of the queue. 
