from Queues import MyQueue

def find_num(number):
    if number ==0:
        return 0
    elif(number<0):
        return None
    queue = MyQueue()
    final = []
    queue.enqueue(1)
    for i in range(number):
        final.append(str(queue.dequeue()))
        sum1 = final[i] + "0"
        sum2 = final[i] + "1"
        queue.enqueue(sum1)
        queue.enqueue(sum2)
    return final

print(find_num(5))
