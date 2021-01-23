import logging

from collections import defaultdict


class ShapeDict(object):
    def __init__(self):
        self.d = dict() 
        self.dd = defaultdict(set)

    def get_root(self, node):
        p = node
        seen = set([node])
        while self.d[p] != p:
            p = self.d[p]
            if p in seen:
                raise Exception("Found circular refs: %s" % (seen, ))
            else:
                seen.add(p)
        return p

    def add_new(self, x):
        logging.debug("add_new(%s)" % (x, ))
        self.d[x] = x
        self.dd[x].add(x)

    def add_connected(self, leaf, branch):
        logging.debug("add_connected(%s, %s)" % (leaf, branch))
        self.d[leaf] = branch
        root = self.get_root(leaf)
        self.dd[root].add(leaf)

    def add_connection(self, a, b):
        logging.debug("add_connection(%s, %s)" % (a, b))
        old_root = self.get_root(a)
        b_root = self.get_root(b)
        self.d[old_root] = b_root
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
