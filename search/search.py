# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def generalSearch(problem: SearchProblem, index: int):
    # 0 = dfs
    # 1 = bfs
    # 2 = ucs
    # 3 = a*
    from util import Stack, Queue, PriorityQueue
    match index:
        case 0: # dfs
            fringe = Stack()
        case 1: # bfs
            fringe = Queue()
        case 2: # ucs
            fringe = PriorityQueue() # low priority popped first
        case _:
            return None 
    closed_set = set()
    actions_so_far = list()
    if (index < 2):
        fringe.push([problem.getStartState(), actions_so_far, None]) # fringe = state, current path, next action
    else:
        print("a")
        fringe.push([problem.getStartState(), actions_so_far, None, 0], 0) # fringe = state, current path, next action, total cost of actions; priority represents cumulative cost
    
    while(True): # fringe = state, current path, next action, cost; append next action before adding to fringe
        if (fringe.isEmpty()):
            print("b")
            return None # no answer exists
        curr = fringe.pop()
        if (problem.isGoalState(curr[0])):
            print("c")
            return curr[1]
        if (curr[0] not in closed_set):
            closed_set.add(curr[0])
            next = problem.getSuccessors(curr[0]) # successor = tuple (state, action, cost)
            print("d")
            for successor in next: 
                print("next: ", next)
                if ((successor[0], successor[1]) not in closed_set):
                    print("f")
                    new_path = curr[1].copy()
                    new_path.append(successor[1])
                    if (index < 2):
                        fringe.push([successor[0], new_path, successor[1]])
                    else:
                        print("g")
                        if (successor[2] != 999999):
                            print("h")
                            total_cost = successor[2] + curr[3]
                            fringe.push([successor[0], new_path, successor[1], total_cost], total_cost)



def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    return generalSearch(problem, 0)
    from util import Stack
    fringe = Stack()
    closed_set = set()
    actions_so_far = list()
    fringe.push([problem.getStartState(), actions_so_far, None, 0]) # None = direction; need to add cost to
    while(True): # fringe = state, current path, next action, cost; append next action before adding to fringe
        if (fringe.isEmpty()):
            return None # no answer exists
        curr = fringe.pop()
        if (problem.isGoalState(curr[0])):
            return curr[1]
        if (curr[0] not in closed_set):
            closed_set.add(curr[0])
            next = problem.getSuccessors(curr[0]) # successor = tuple (state, action, cost)
            for successor in next: 
                if ((successor[0], successor[1]) not in closed_set):
                    new_path = curr[1].copy()
                    new_path.append(successor[1])
                    fringe.push([successor[0], new_path, successor[1], successor[2]])


    from util import Stack
    # fringe = Stack() # tuple (state, actions so far, cost) --> each fringe item = (successor, actions_so_far for path)
    fringe = Stack()
    closed_set = set()
    actions_so_far = list()
    fringe.push([problem.getStartState(), actions_so_far, None, 0]) # None = direction; need to add cost to
    while(True): # fringe = state, current path, next action, cost; append next action before adding to fringe
        if (fringe.isEmpty()):
            # print("empty fringe")
            return None # no answer exists
        curr = fringe.pop()
        if (problem.isGoalState(curr[0])):
            # print("got goal")
            return curr[1]
        # print("curr: ", curr)
        #if ((curr[0], curr[2]) not in closed_set):
        if (curr[0] not in closed_set):
            closed_set.add(curr[0])
            next = problem.getSuccessors(curr[0])
            # print("next: ", next)
            for successor in next: # (state, action, cost)
                # while (not leaf_reached):    
                if ((successor[0], successor[1]) not in closed_set):
                    new_path = curr[1].copy()
                    new_path.append(successor[1])
                    # print("new path: ", new_path)
                    fringe.push([successor[0], new_path, successor[1], successor[2]])
 
def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    # util.raiseNotDefined()
    return generalSearch(problem, 1)

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    return generalSearch(problem, 2)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    from game import Directions
    n = Directions.NORTH
    e = Directions.EAST
    s = Directions.SOUTH
    w = Directions.WEST
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
