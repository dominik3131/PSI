from town import *


class State:
    def __init__(self, towns, all_towns):
        self.towns = towns
        self.distance = self.find_distance()
        self.heuristic = self.calculate_f(all_towns)

    def find_distance(self):
        dis = 0
        for i in range(0, len(self.towns) - 1):
            dis += self.towns[i].distance(self.towns[i + 1])
        return dis

    def calculate_f(self, towns):
        temp = 999999999999
        this_towns_len = len(self.towns)
        other_towns_len = len(towns)
        if this_towns_len == other_towns_len:
            self.heuristic = self.distance + self.towns[-1].distance(
                self.towns[0]) * 0.95
        else:
            multiplier = other_towns_len - this_towns_len
            for x in towns:
                last_town = self.towns[-1]
                if x not in self.towns:
                    dist = last_town.distance(x)
                    if dist < temp:
                        temp = dist
            self.heuristic = self.distance + temp * multiplier * 0.95
        return self.heuristic

    def __repr__(self):
        stateString = ""
        for i in range(0, len(self.towns)):
            stateString += str(self.towns[i]) + "\n"
        stateString += "distance = " + str(self.distance)
        return stateString
