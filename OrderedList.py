from Node import Node


class OrderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        if self.is_empty():
            return 0
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.getNext()
        return count

    def add(self, node):
        cur = self.head
        previous = None
        stop = False
        while cur is not None and not stop:
            if repr(cur.getData()) > repr(node):
                stop = True
            else:
                previous = cur
                cur = cur.getNext()
        temp = Node(node)
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(cur)
            previous.setNext(temp)

    def search(self, node):
        cur = self.head
        if repr(cur.getData()) == node:
            return True

        while cur.getNext() is not None and repr(cur.getData()) <= node:
            if repr(cur.getData()) == node:
                return True
            cur = cur.proximo
        return False

    def remove(self, node):
        if self.is_empty():
            return False

        cur = self.head
        if repr(cur.getData()) == node:
            self.head = cur.getNext()
            return True

        while cur.getNext() is not None and repr(cur.getData()) <= node:
            if repr(cur.getData()) == node:
                cur.setNext(cur.getNext().getNext())
                return True
            cur = cur.proximo
        return False

    def __str__(self):
        cur = self.head
        out = ""
        while cur is not None:
            out += str(cur.getData()) + " -> "
            cur = cur.getNext()
        return out[:-3]