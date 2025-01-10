class Track:
    def __init__(self, *args):
        if len(args) == 1:

    def add_track(self, tr):


class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        if type(to_x) in [int, float]:
            self.to_x = to_x
        if type(to_y) in [int, float]:
            self.to_y = to_y
        if type(max_speed) == int:
            self.max_speed = max_speed