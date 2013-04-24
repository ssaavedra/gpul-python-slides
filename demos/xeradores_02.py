class Node(object):
    def __init__(self, value="U", left=None, right=None):
        self.left = left
        self.right = right
        self.value = value
        # Anything else...

    def get_inorder_list(self):
        '''
        Returns a list of the order in
        in-order position
        '''
        if self.left:
            for elt in self.left.get_inorder_list():
                # Yield all elements before me, inorder
                yield elt

        yield self # Yield ourselves

        if self.right:
            for elt in self.right.get_inorder_list():
                # Yield all elements after me, inorder
                yield elt

    def __str__(self):
        return self.value



if __name__ == '__main__':
    a = Node("A")
    c = Node("C")
    b = Node("B", left=a, right=c)

    e = Node("E")
    g = Node("G")
    f = Node("F", left=e, right=g)

    d = Node("D", left=b, right=f)

    print map(lambda s: str(s), list(d.get_inorder_list()))

