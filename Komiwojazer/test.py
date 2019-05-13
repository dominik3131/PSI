from town import *
from state import *
import copy
import itertools
import time

class Test:
    def __init__(self):
        self.towns = list()
        self.towns = self.load_towns()
        optimal_start=time.time()
        self.optimal=self.find_with_shortest()
        optimal_end=time.time()
        brute_start=time.time()
        self.brute=self.brute_force()
        brute_end=time.time()
        star_start=time.time()
        self.star=self.a_star()
        star_end=time.time()
        self.brute_time=brute_end-brute_start
        self.optimal_time=optimal_end-optimal_start
        self.star_time=star_end-star_start

    def load_towns(self):
        lista = list()
        filepath = 'towns.txt'
        with open(filepath) as fp:
            for cnt, line in enumerate(fp):
                splitted = line.split()
                lista.append(Town(splitted[0],splitted[1],splitted[2]))

        return lista
    def find_with_shortest(self):
        temp_towns=self.towns[:]
        path=list()
        path.append(temp_towns[0])
        temp_towns.remove(path[0])
        while len(temp_towns)>1:
            index=0
            for i in range(1,len(temp_towns)):
                if path[-1].distance(temp_towns[index])>path[-1].distance(temp_towns[i]):
                    index=i
            path.append(temp_towns.pop(index))
        path.append(temp_towns.pop(0))
        path.append(path[0])
        return State(path)
    def brute_force(self):
        #permutations = list(itertools.permutations(self.towns[1:]))
        permutations = list(self.all_perms(self.towns[1:]))
        paths=list()
        for i in range(0,len(permutations)):
            temp_list=list(permutations[i])
            temp_list.insert(0,self.towns[0])
            #temp_list.append(self.towns[0])
            paths.append(State(temp_list))
        bestPath=paths[0]
        for i in range(1,len(paths)):
            if bestPath.distance>paths[i].distance:
                bestPath=paths[i]
        return bestPath
    def all_perms(self,elements):
        if len(elements) <=1:
            yield elements
        else:
            for perm in self.all_perms(elements[1:]):
                for i in range(len(elements)):
                    yield perm[:i] + elements[0:1] + perm[i:]
    def a_star(self):
        states=list()
        for i in self.towns[1:]:
            states.append(State([self.towns[0],i]))
        #found=False
        while True:
            state_to_expand=self.find_with_best_heuristic(states)
            states.remove(state_to_expand)
            expanded_states=self.expand_state(state_to_expand)
            if len(expanded_states[0].towns)==len(self.towns):
                return expanded_states[0]
            states.extend(expanded_states) 
    def expand_state(self,state):
        states=list()
        if len(state.towns)==len(self.towns):
            states.append(State(state.towns[:]+[state.towns[0]]))
        else:
            for x in self.towns:
                if x not in state.towns:
                    states.append(State(state.towns[:]+[x]))
        print(states)       
        
    
        return states   
    def find_with_best_heuristic(self,states):
        best_state=states[0]
        best_heuristic=best_state.calculate_f(self.towns)
        for i in range(1,len(states)):
            temp_heuristic=states[i].calculate_f(self.towns)
            if temp_heuristic<best_heuristic:
                best_heuristic=temp_heuristic
                best_state=states[i]
        return best_state
    

if __name__ == '__main__':
    test = Test()
    print("result choosing shortest path each time \n"+str(test.optimal)+ "time: "+str(test.optimal_time))
    print("result using brute force \n"+str(test.brute) + "time: "+str(test.brute_time))
    print("result using astar \n"+str(test.star)+ "time: "+str(test.star_time))

