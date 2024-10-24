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
from game import Directions
from typing import List

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




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


dfs_path = []
fridge = set()
def depthFirstSearch(problem: SearchProblem, current_state=None, first = True) -> List[Directions]:
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
    global dfs_path,fridge
    if first:
        dfs_path = []
        fridge = set()
    if current_state:
        state = current_state
    else:
        state = problem.getStartState()
        fridge.add(state)

    if problem.isGoalState(state):
        return dfs_path
    successors = problem.getSuccessors(state)
    for successor in successors:
        successor, action, stepCost = successor
        if successor in fridge:
            continue
        dfs_path.append(action)
        fridge.add(successor)
        print(dfs_path)
        if depthFirstSearch(problem,successor,False):
            return dfs_path
        del dfs_path[-1]



def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue
    q = Queue()
    start = problem.getStartState()
    q.push([start])
    fridge = set()
    fridge.add(start)
    while not q.isEmpty():
        search_paths = q.pop()
        last_node = search_paths[-1]
        last_action = search_paths[:-1]
        if problem.isGoalState(last_node):
            return last_action
        successors = problem.getSuccessors(last_node)
        for successor in successors:
            successor, action, stepCost = successor
            if successor in fridge:
                continue
            new_path = last_action+[action,successor]
            fridge.add(successor)
            q.push(new_path)


def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    start = problem.getStartState()
    pq = PriorityQueue()
    pq.push([[],start,0],-0)
    fridge = set()
    while not pq.isEmpty():
        search_paths = pq.pop()
        last_node = search_paths[1]
        last_cost = search_paths[2]
        last_action = search_paths[0]
        if last_node in fridge:
            continue
        else:
            fridge.add(last_node)
        if problem.isGoalState(last_node):
            return last_action
        successors = problem.getSuccessors(last_node)
        for successor in successors:
            successor, action, stepCost = successor
            new_path = last_action + [action]
            new_cost = stepCost+last_cost
            pq.update([new_path,successor,new_cost],new_cost)

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
