from town import *
class State:
    def __init__(self,towns):
        self.towns = towns
        self.distance=self.findDistance()
    def findDistance(self):
        dis=0
        for i in range(0, len(self.towns)-1):
            dis+=self.towns[i].distance(self.towns[i+1])
        return dis
    def add_town(self,town):
        self.towns.append(town)
        self.distance+=self.towns[-1].distance(self.towns[-2])
    def delete_last_town(self):
        self.distance-=self.towns[-1].distance(self.towns[-2])
        self.towns.pop()
    def calculate_f(self,towns):
        temp=999999999999
        if len(self.towns)==len(towns):
            return self.distance+self.towns[-1].distance(self.towns[0])*0.1
        multiplier=len(towns)-len(self.towns)
        for x in towns:
            if x not in self.towns:
                dist=self.towns[-1].distance(x)
                if dist<temp:
                    temp=dist
        return self.distance+temp*multiplier*0.9

    def __repr__(self):
        stateString=""
        for i in range(0,len(self.towns)):
            stateString+=str(self.towns[i])+"\n"
        stateString+="distance = " + str(self.distance)
        return stateString

    
