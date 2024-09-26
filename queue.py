class ListQueue:
    def __init__(self):
        self.queue_list = []


    def enqueue(self, value):
        self.queue_list.append(value)


    def dequeue(self):
        return self.queue_list.pop(0)

    def get_size(self):
        return len(self.queue_list)