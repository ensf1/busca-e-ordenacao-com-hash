from time import sleep


class Node:
    def __init__(self, node):
        self._node = node
        self._next = None

    def getData(self):
        return self._node

    def getNext(self):
        return self._next

    def setData(self, node):
        self._node = node

    def setNext(self, next):
        self._next = next


