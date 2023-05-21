from Queues import MyQueue
from stacks import MyStack


def reverseK(queue, k):
    use_stack = MyStack()
    num = k
    # Write your code here
    if k > queue.size() or k < 0 or queue.is_empty():
        return None
    for i in range(k):
        use_stack.push(queue.dequeue())
    while(use_stack.is_empty() is False):
        queue.enqueue(use_stack.pop())
    size = queue.size()
    for i in range(size-k):
        queue.enqueue(queue.dequeue())
    return queue
        

        