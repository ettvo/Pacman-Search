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
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    # from game import Directions
    # n = Directions.NORTH
    # e = Directions.EAST
    # s = Directions.SOUTH
    # w = Directions.WEST
    # stop = Directions.STOP
    # fringe as LIFO stack
    # return a list of actions (solution) --> need to process the tree within here
    # 

    from util import Stack, Queue
    # fringe = Stack() # tuple (state, actions so far, cost) --> each fringe item = (successor, actions_so_far for path)
    fringe = Stack()
    closed_set = set()
    actions_so_far = list()

    # def expand_node(state, action, fringe: Stack, closed_set: set):
    # returns True if goal state
    def expand_nodes(state, action, cost, actions_so_far, fringe, closed_set):
        # check goal state
        if (problem.isGoalState(state)):
            return True
            # if (action is None):
            #     return list()
            # return list(action) # double-check this
        # add current node to CLOSED SET (just the node, not the route or anything else)
        
        if ((state, action) in closed_set):
            return False # already expanded
        closed_set.add((state, action)) 
        
        # expand current node
        next = problem.getSuccessors(state) # use func in pacman.py instead
        # add successors to fringe
        if (next == []):
            return False
        if (action is not None):
            actions_so_far.append(action)
        for x in next:
            # if ((x[0], x[1]) not in closed_set):
            #     fringe.push([x, actions_so_far.copy()])
            fringe.push([x, actions_so_far.copy()])
            # print("Fringe push: ", actions_so_far + action)
        return False

    # return state
    actions_so_far = list()
    if (expand_nodes(problem.getStartState(), None, 0, actions_so_far, fringe, closed_set)):
        return actions_so_far
    
    while(not fringe.isEmpty()): # currently does not do DFS?
        successor = fringe.pop()
        status = expand_nodes(successor[0][0], successor[0][1], successor[0][2], successor[1], fringe, closed_set)
        if (status):
            successor[1].append(successor[0][1])
            print(successor[1])
            return successor[1]
    
    return None # error, exist exists but is not detected
    

    # step 1: expand current node to get successors
    # step 2: add current node to CLOSED SET (just the node, not the route or anything else)
    # step 3: add successors to fringe 
    # step 4: pop first successor in fringe to expand
    # step 5: expand successor
    # step 6: add successor to closed set
    # step 7: repeat
    
    # check first node
    # while fringe is not empty and no solution (check that return is empty list; append to list of actions)
    # 


    # prev code here VVVVV

    # def isOpposite(action1, action2):
    #     if (action1 == n and action2 == s) or (action1 == w and action2 == e) \
    #         or (action2 == n and action1 == s) or (action2 == w and action1 == e):
    #         return True
    #     return False
    # # issue of looping


    # from pacman import GameState
    # def checkNode(state, action, cost):
    #     # successor = new location, action taken, cost
    #     # keep going left
    #     if (problem.isGoalState(state)):
    #         if (action is None):
    #             return []
    #         return [action]
    #     # else, keep going left
    #     next = problem.getSuccessors(state)
    #     print("Current's successors:", next)
    #     if (next == []): 
    #         # no more possible states from current situation
    #         # indicates no success on route
    #         return None
    #     for successor in next:
    #         if (not isOpposite(action, successor[1])):
    #             fringe.push(successor)
    #             solution = checkNode(successor[0], successor[1], successor[2])
    #             if (solution is not None):
    #                 return [action].append(solution)
    #             fringe.pop()

    # # initial nodes
    # successfulActions = checkNode(problem.getStartState(), None, 0) # first move
    # return successfulActions
    
    # cycle:
    # get legal actions at level --> if [], return current list of actions as the solution 
    # get successor for those legal actions
    # branch 
    # keep going on stack through deep left side to get answer
    

    #util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
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

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
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
