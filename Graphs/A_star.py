'''
Code implementation inspired & modified from sample of AI textbook "Artificial Intelligence: Foundations of Computational Agents"

# searchGeneric.py - Generic Searcher, including depth-first and A*
# AIFCA Python3 code Version 0.7.6 Documentation at http://aipython.org

# Artificial Intelligence: Foundations of Computational Agents
# http://artint.info
# Copyright David L Poole and Alan K Mackworth 2017.
# This work is licensed under a Creative Commons
# Attribution-NonCommercial-ShareAlike 4.0 International License.
# See: http://creativecommons.org/licenses/by-nc-sa/4.0/deed.en
'''
import heapq 

class Astar_searcher(object):

    def __init__(self, problem):
        """creates a searcher from a problem
        """
        self.problem = problem
        self.initialize_frontier()
        self.num_expanded = 0
        self.add_to_frontier(Path(problem.start_node()))
        super().__init__()

    def initialize_frontier(self):
        self.frontier = FrontierPQ()
        
    def empty_frontier(self):
        return self.frontier.empty()
        
    def add_to_frontier(self,path):
        value = path.cost+self.problem.heuristic(path.end())
        self.frontier.add(path, value)

    def search(self):
        """returns (next) path from the problem's start node

        """
        tmp = ''
        output_paths = []
        while not self.empty_frontier():

            path = self.frontier.pop()

            self.num_expanded += 1
            if self.problem.is_goal(path.end()):   

                self.solution = path   # store the optimal path

                write_output(start, output_paths, self.solution, f_output) # write output all
                return path
            else: # solution not found, keep searching
                neighs = self.problem.neighbors(path.end())
                
                for arc in reversed(neighs):
                    # check cycle path: 
                  
                    if str(arc)[-1] in str(tmp): 
                        continue
                    self.add_to_frontier(Path(path,arc))
  
        
            sorted_paths_cost = self.frontier.sort()
            
            sorted_paths = []
            for (_, _, path) in sorted_paths_cost:
                sorted_paths.append(path)


            output_paths.append(sorted_paths)

            last_node = str(sorted_paths[-1])[-1]
            
            for path_name in sorted_paths[:-1]:

                if last_node in str(path_name):

                    try:
                        self.frontier.remove(sorted_paths_cost[-1])
                        remove_duplicate_sorted = self.frontier.sort()
                        tmp4 = []
                        for (_, _, visited_path) in remove_duplicate_sorted:
                            tmp4.append(visited_path)

                        output_paths.append(tmp4)

                        (_, _, tmp) = remove_duplicate_sorted[0]
                        
                    except: 
                        ValueError
                        
                    break
                    


class Search_problem(object):
  

    def start_node(self):
        raise NotImplementedError("start_node")   
    
    def is_goal(self,node):
        raise NotImplementedError("is_goal")  

    def neighbors(self,node):
        raise NotImplementedError("neighbors")   

    def heuristic(self,n):
        
        return 0


class Arc(object):
    def __init__(self, from_node, to_node, cost=1):
        assert cost >= 0, ("Cost cannot be negative for"+
                           str(from_node)+"->"+str(to_node)+", cost: "+str(cost))
        self.from_node = from_node
        self.to_node = to_node
        self.cost=cost

    def __repr__(self):
        return str(self.from_node)+str(self.to_node) 
        
class Search_graph(Search_problem):


    def __init__(self, nodes, arcs, start=None, goals=set(), hmap={}):
        self.neighs = {}
        self.nodes = nodes
        for node in nodes:
            self.neighs[node]=[]
        self.arcs = arcs
        self.start = start
        for arc in arcs:
            # check cycle path
            if arc.to_node is not self.start: # check if go back start_node
                self.neighs[arc.from_node].append(arc)
        
        self.goals = goals
        self.hmap = hmap

    def start_node(self):
        return self.start
    
    def is_goal(self,node):
        return node in self.goals

    def is_start(self, node):
        return node == self.start

    def neighbors(self,node):
        return self.neighs[node]

    def heuristic(self,node):
        """Gives the heuristic cost of node n.
        """
        if node in self.hmap:
            return self.hmap[node]
        else:
            return 0
        
    def __repr__(self):
        res=""
        for arc in self.arcs:
            res += str(arc)+".  "
        return res

    def neighbor_nodes(self,node):
        
        return (path.to_node for path in self.neighs[node])


class Path(object):
    
    
    def __init__(self,initial,arc=None):
        
        self.initial = initial
        self.arc=arc
        if arc is None:
            self.cost=0
        else:
            self.cost = initial.cost+arc.cost

    def end(self):
        
        if self.arc is None:
            return self.initial
        else:
            return self.arc.to_node

    def nodes(self):
     
        current = self
        while current.arc is not None:
            yield current.arc.to_node
            current = current.initial
        yield current.initial

    def initial_nodes(self):
      
        if self.arc is not None:
            for nd in self.initial.nodes(): yield nd     
        
    def __repr__(self):
        if self.arc is None:
            return str(self.initial)
        else:
            return str(self.initial)+str(self.arc.to_node)

      
class FrontierPQ(object):


    def __init__(self):
        
        self.frontier_index = 0  
        self.frontierpq = []  

    def empty(self):
        return self.frontierpq == []

    def add(self, path, value):
     
        self.frontier_index += 1    
        heapq.heappush(self.frontierpq,(value, -self.frontier_index, path))

    def remove(self, duplicate_max_path):
        self.frontierpq.remove(duplicate_max_path)

    def sort(self):
        "sort paths from min to max cost"

        visited_paths = []
        for data in self.frontierpq:
            heapq.heappush(visited_paths, data)

        sorted_paths = []
        while visited_paths:
            sorted_paths.append(heapq.heappop(visited_paths))

        return sorted_paths

    def pop(self):

        (_,_,path) = heapq.heappop(self.frontierpq)
        return path 

# I/O files
f_input = 'A_star_input.txt'
f_output = 'A_star_output.txt'

def read_input(file):
    f = open(file, 'r+')
    data = f.read()
    data = data.split('\n')
    f.close()
    start = data[0]
    goal = data[1]
    return start, goal

def write_output(start_node, path_char_list, optimal_path, file):
    f = open(file, 'w+')
    f.write(str(start_node))
    f.write('\n')
    for visited_route in path_char_list:

        for idx, char in enumerate(visited_route):
            str_char = str(char)
            f.write(str_char)
            
            if idx == (len(visited_route) -1):
                
                f.write('\n')
            else:
                
                f.write(', ')
    f.write(str(optimal_path))    
    f.close()

start, goal = read_input(f_input)

# set graph
hw1 = Search_graph(
    {'a', 'b', 'c', 'd', 'e', 'f', 'z'},
    [Arc('a', 'b', 9), Arc('b', 'a', 9),
    Arc('a', 'c', 4), Arc('c', 'a', 4),
    Arc('a', 'd', 7), Arc('d', 'a', 7),
    Arc('b', 'e', 11), Arc('e', 'b', 11),
    Arc('c', 'e', 17), Arc('e', 'c', 17),
    Arc('c', 'f', 12), Arc('f', 'c', 12),
    Arc('d', 'f', 14), Arc('f', 'd', 14),
    Arc('e', 'z', 5), Arc('z', 'e', 5),
    Arc('f', 'z', 9), Arc('z', 'f', 9)],
    start = start,
    goals = {goal},
    hmap = {
        'a': 21,
        'b': 14,
        'c': 18,
        'd': 18,
        'e': 5,
        'f': 8,
        'z': 8
        }

    )


if __name__ == "__main__":
    #print(hw1)
    Astar = Astar_searcher(hw1)  
    Astar.search()
    print('A start search finished!')