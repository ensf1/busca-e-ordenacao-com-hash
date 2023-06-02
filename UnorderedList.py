from Node import Node


class UnorderedList:
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
        head = Node(node)
        head.setNext(self.head)
        # print('head', repr(self.head))
        # print('aux', repr(head))
        self.head = head

    def search(self, node):
        cur = self.head
        while cur is not None:
            if repr(cur.getData()) == node:
                return True
            else:
                cur = cur.getNext()
        return False

    def remove(self, node):
        if self.is_empty():
            return False
        cur = self.head
        if repr(cur.getData()) == node:
            self.head = cur.getNext()
            return True

        after = self.head.getNext()

        # print('antes', repr(cur.getData()))
        while after is not None and repr(cur.getData()) != node:
            if repr(after.getData()) == node:
                cur.setNext(after.getNext())
                return True
            cur = after
            after = after.getNext()
            # print('durante', repr(cur.getData()))
        # print('depois', repr(cur.getData()))



    def __str__(self):
        cur = self.head
        out = ""
        while cur is not None:
            out += str(cur.getData()) + " -> "
            cur = cur.getNext()
        return out[:-3]


