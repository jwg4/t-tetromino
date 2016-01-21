def make_frame_class(w):
    class FrameTemplate(object):
        width = w
        _heights = None

        def __init__(self, *values):
            if len(values) != self.width:
                raise Exception()
            self._heights = tuple(values)

        def __hash__(self):
            adjust = 0 - min(self._heights)
            adjust = [adjust] * self.width
            a = tuple([ sum(x) for x in zip(self._heights, adjust) ])
            return hash(a)

        def __str__(self):
            return str(self._heights)

        def _is_valid(self):
            return True

        def generate_new_frames(self):
            n = []
            for i in range(self.width-1):
                if self._heights[i] == self._heights[i+1] + 1:
                    a = list(self.values)
                    a[i] = a[i] + 1
                    a[i+1] = a[i+1] + 3
                    n.append(FrameTemplate(*a))
                if self._heights[i] == self._heights[i+1] - 1:
                    a = list(self._heights)
                    a[i] = a[i] + 3
                    a[i+1] = a[i+1] + 1
                    n.append(FrameTemplate(*a))
            return n

        def find_repeated_frame(self):
            frames = set([self])
            old_frames = set()
            while frames != old_frames:
                l = [ x for x in generate_new_frames(f) for f in frames ]
                l = [ f for f in l if f._is_valid() ]
                l = set(l)
                if l & frames:
                    match = [l & frames][0]
                    matches = [set(match) & l] + [set(match) & frames]
                    return matches
                old_frames = frames
                frames = frames | l
            return None
    return FrameTemplate

if __name__ == '__main__':
    width = 5
    Frame = make_frame_class(width)
    starting_frame = Frame(0, 0, 0, 0, 0)
    print str(starting_frame)
    print starting_frame.find_repeated_frame()
