from collections import deque

# Complete this Queue function that adds and removes queues
class Queue:
    def __int__(self, container=None):
        if container is None:
            container = deque()
        self.container = container

    def add(self, element):
        self.container.append(element)

    def remove(self):
        if not self.isEmpty():
            return self.container.popleft()
        else:
            raise IndexError("Queue empty")

    def isEmpty(self):
        return len(self.container) == 0