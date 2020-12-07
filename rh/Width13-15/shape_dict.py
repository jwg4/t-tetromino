from collections import defaultdict


class ShapeDict(object):
    def __init__(self):
        self.d = dict() 
        self.dd = defaultdict(set)

    def get_root(self, node):
        p = node
        while self.d[p] != p:
            p = self.d[p]
        return p

    def add_new(self, x):
        self.d[x] = x
        self.dd[x].add(x)

    def add_connected(self, leaf, branch):
        self.d[leaf] = branch
        root = self.get_root(leaf)
        self.dd[root].add(leaf)

    def add_connection(self, a, b):
        old_root = self.get_root(a)
        self.d[old_root] = b
        new_root = self.get_root(a)
        self.dd[new_root].update(self.dd[old_root])

    @property
    def components(self):
        done = set()
        for k in self.d:
            root = self.get_root(k)
            if root not in done:
                yield self.dd[root]
                done.add(root)
