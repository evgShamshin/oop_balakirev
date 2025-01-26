import sys


class Player:
    def __init__(self, name, old, score):
        if type(name) == str:
            self.name = name
        if str(old).isdigit():
            self.old = old
        if str(score).isdigit():
            self.score = score

    def __bool__(self):
        return int(self.score) > 0


lst_in = list(map(str.strip, sys.stdin.readlines()))
players = [Player(*i.split("; ")) for i in lst_in]
players_filtered = list(filter(bool, players))
[print(i.__dict__) for i in players_filtered]