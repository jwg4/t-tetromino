import logging

logging.basicConfig(level=logging.INFO)

class TTetromino(object):
    @staticmethod
    def doubles(s):
        ms = [ sum(x) for x in zip(s, [0 - min(s)] * len(s)) ]
        if ms == [0, 1]:
            yield [ sum(x) for x in zip(s, [3, 1]) ]
        if ms == [1, 0]:
            yield [ sum(x) for x in zip(s, [1, 3]) ]

    @staticmethod
    def triples(s):
        ms = [ sum(x) for x in zip(s, [0 - min(s)] * len(s)) ]
        if ms == [1, 0, 1]:
            yield [ sum(x) for x in zip(s, [1, 2, 1]) ]
        if ms == [0, 0, 0]:
            yield [ sum(x) for x in zip(s, [1, 2, 1]) ]

def make_frame_class(w):
    class FrameTemplate(object):
        width = w
        _heights = None

        def __init__(self, *values):
            if len(values) != self.width:
                raise Exception()
            logging.debug(values)
            self._heights = tuple(values)

        @property
        def _offsets(self):
            adjust = 0 - min(self._heights)
            adjust = [adjust] * self.width
            a = tuple([ sum(x) for x in zip(self._heights, adjust) ])
            return a

        def __hash__(self):
            return hash(self._offsets)

        def __eq__(self, other):
            return self._offsets == other._offsets

        def __repr__(self):
            return str(self._heights)

        def __str__(self):
            return str(self._heights)

        def _is_valid(self):
            if self._heights[0] + 1 < self._heights[1]:
                return False
            if self._heights[-1] + 1 < self._heights[-2]:
                return False
            for i in range(1, self.width - 1):
                if ((self._heights[i] + 1 < self._heights[i+1]) and
                      (self._heights[i] + 1 < self._heights[i-1])):
                    return False
                if ((self._heights[i] + 6 < self._heights[i+1]) or
                      (self._heights[i+1] + 6 < self._heights[i])):
                    return False
            return True

        def generate_new_frames(self):
            n = []
            a = list(self._heights)
            for i in range(self.width-1):
                for s in TTetromino.doubles(a[i:i+2]):
                    b = a[:]
                    b[i:i+2] = s
                    n.append(FrameTemplate(*b))
            for i in range(self.width-2):
                for s in TTetromino.triples(a[i:i+3]):
                    b = a[:]
                    b[i:i+3] = s
                    n.append(FrameTemplate(*b))
            return n

        def find_repeated_frame(self):
            frames = set([self])
            old_frames = set()
            previous = frames
            while frames != old_frames:
                l = [ x for f in previous for x in f.generate_new_frames() ]
                l = [ f for f in l if f._is_valid() ]
                l = set(l)
                logging.info(l)
                if l & frames:
                    match = list(l & frames)[0]
                    matches = [set([match]) & l] + [set([match]) & frames]
                    return matches
                old_frames = frames
                previous = l
                frames = frames | l
            return None
    return FrameTemplate

if __name__ == '__main__':
    width = 5
    Frame = make_frame_class(width)
    starting_frame = Frame(0, 0, 0, 0, 0)
    print str(starting_frame)
    print starting_frame.find_repeated_frame()
