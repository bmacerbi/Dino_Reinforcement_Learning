import random

def first(x):
    return x[0]

class KeyTreeClassifier():
    def __init__(self, state):
        self.state = state

    def keySelector(self, distance, obHeight, speed, obType, nextObDistance, nextObHeight, nextObType):
        self.state = sorted(self.state, key=first)
        for s, d in self.state:
            if speed < s:
                limDist = d
                break

        if distance <= limDist:
            if isinstance(obType, Bird) and obHeight < 83:
                return "K_UP"
            elif not isinstance(obType, Bird):
                return "K_UP"
            
        return "K_DOWN"

    def updateState(self, state):
        self.state = state