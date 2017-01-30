# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html
"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""
import time
import util
import game
import searchAgents
import copy
"""
a=PriorityQueue()
a.push(1,2)
print a.dic()
"""
class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first
  [2nd Edition: p 75, 3rd Edition: p 87]
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm 
  [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"
  """
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  frontier=util.Stack()
  explored={}
  startstate=problem.getStartState()
  frontier.push((startstate,"Stop",0))
  explored[startstate[0]]=startstate[1]
  
  succ=[]
  if problem.isGoalState(problem.getStartState()):
    goalnode=problem.getStartState()
    return []
  while frontier.isEmpty()==False:
      node=frontier.pop()
      succ=problem.getSuccessors(node[0])
      print explored
      for elem in succ:
        if problem.isGoalState(elem[0]):
          # print elem
          goalnode=elem
          goal=goalnode
          explored[elem[0]]=elem[1]
          return findpath1(startstate,explored,elem[0]) 
        elif elem[0] not in explored:
          explored[elem[0]]=elem[1]
          frontier.push(elem)
           
  util.raiseNotDefined()

def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]
  """
  "*** YOUR CODE HERE ***"
  frontier=util.Queue()
  explored={}
  startstate=problem.getStartState()
  frontier.push((startstate,"Stop",0))
  explored[startstate[0]]=startstate[1]
  #print explored
  succ=[]
  #print problem.corners
  if problem.isGoalState(problem.getStartState()):
    goalnode=problem.getStartState()
  while frontier.isEmpty()==False:
      node=frontier.pop()
      #print node[0]
      succ=problem.getSuccessors(node[0])
      #print succ
      for elem in succ:
        if problem.isGoalState(elem[0]):
          explored[elem[0]]=elem[1]
          print "sucess" 
          if problem.type==1:
            return findpath1(problem.getStartState(),explored,elem[0])
          #print explored
          #print len(explored)
          return findpath2(problem.getStartState(),explored,elem[0],problem) 
        elif elem[0] not in explored:
          explored[elem[0]]=elem[1]
          #print explored[0]
          #print explored[1]
          frontier.push(elem)
        else:
          print "state explored"
        
def findpath1(startstate,explored,endstate):
  print "findpath\n"
  print explored
  print "startstate\n"
  print startstate
  path=[]
  node=(endstate,explored[endstate])
  path.insert(0,node[1])
  dx, dy = game.Actions.directionToVector(game.Directions.REVERSE[node[1]])
  x,y=node[0]
  nextx, nexty = int(x + dx), int(y + dy)
  while((nextx,nexty)!=startstate):
    print (nextx,nexty)
    print "->\n"
    node=((nextx,nexty),explored[(nextx,nexty)])
    print(node)
    path.insert(0,node[1])
    dx, dy = game.Actions.directionToVector(game.Directions.REVERSE[node[1]])
    x,y=node[0]
    nextx, nexty = int(x + dx), int(y + dy)
  print len(path)
  return path

def findpath2(startstate,explored,endstate,problem):
  path=[]
  node=(endstate,explored[endstate])
  #print node[0]
  
  print("Startstate")
  print startstate
  path.insert(0,node[1])
  x,y=node[0][0]
  dx,dy=game.Actions.directionToVector(game.Directions.REVERSE[node[1]])
  nextx,nexty=int(x+dx),int(y+dy)
  newgoals=set(node[0][1])
  if (x,y) in problem.corners:
      newgoals.add((x,y))
  nextstate=((nextx,nexty),tuple(newgoals))
  #print nextstate

  while((nextstate[0],set(nextstate[1]))!=(startstate[0],set(startstate[1]))):
    print nextstate
    #time.sleep(0.05)
    #print explored[index][0]
    node=(nextstate,explored[nextstate])
    print node
    path.insert(0,node[1])
    x,y=node[0][0]
    dx,dy=game.Actions.directionToVector(game.Directions.REVERSE[node[1]])
    #print dx,x
    nextx,nexty=int(x+dx),int(y+dy)
    #print nextx
    newgoals=set(node[0][1])
    if (x,y) in problem.corners:
        newgoals.add((x,y))
    nextstate=((nextx,nexty),tuple(newgoals))
    #print nextstate
    #print "end"
  return path

def findpath3(startstate,explored,endstate,problem):
  path=[]
  nextstate=0
  index=len(explored)-1
  state=endstate
  #print node[0]
  path.insert(0,explored[state])
  x,y=state[0]
  print explored[state]
  grid=copy.deepcopy(state[1])
  print(state)
  dx,dy=game.Actions.directionToVector(game.Directions.REVERSE[explored[state]])
  nextx,nexty=int(x+dx),int(y+dy)
  if problem.start[1][x][y]==True:
    grid[x][y]=True
    if(((nextx,nexty),grid) not in explored):
        grid[x][y]=False
  nextstate=((nextx,nexty),grid)
  #print nextstate
  while(nextstate!=startstate):
    node=(nextstate,explored[nextstate])
    path.insert(0,node[1])
    x,y=node[0][0]
    grid=copy.deepcopy(node[0][1])
    print(str(x)+" "+str(y)+"  "+node[1]+"\n")
    dx,dy=game.Actions.directionToVector(game.Directions.REVERSE[node[1]])
    #print dx,x
    nextx,nexty=int(x+dx),int(y+dy)
    #print nextx
    if problem.start[1][x][y]==True:
      grid[x][y]=True
      if((nextx,nexty),grid) not in explored:
          grid[x][y]=False
    nextstate=((nextx,nexty),grid)
    #print nextstate
    #print "end"
  return path

def uniformCostSearch(problem):
  frontier=util.PriorityQueue()
  explored={}
  startstate=problem.getStartState()
  frontier.push((problem.getStartState(),"Stop",0),0)
  explored[startstate[0]]=startstate[1]
  while frontier.isEmpty()==False:
      node=frontier.pop()
      explored[node[0]]=node[1]
      if problem.isGoalState(node[0]):
        return findpath1(problem.getStartState(),explored,node[0])
      succ=problem.getSuccessors(node[0])
      for elem in succ:
          if(elem[0] not in explored):
            frontier.push((elem[0],elem[1],node[2]+elem[2]),node[2]+elem[2])
  
    
              
        
def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  frontier=util.PriorityQueue()
  frontier.push((problem.getStartState(),"Stop",0),heuristic(problem.getStartState(),problem))
  #explored.append((problem.getStartState(),"Stop",0,heuristic(problem.getStartState(),problem)))
  explored={}
  print(problem.getStartState())
  #time.sleep(2)
  i=0
  while frontier.isEmpty()==False:
      #print "before pop"
      #print frontier.heap
      node=frontier.pop()
      #print "after pop"
      #print frontier.heap
      #print "node :"+str(node)
      if(node[0] in explored):
          continue
      explored[node[0]]=node[1]
      #time.sleep(0.5)
      #print("explored"+str(len(explored))+"\n")
      if problem.isGoalState(node[0]):
        print "success\n"
        if(problem.type==1):
          return findpath1(problem.getStartState(),explored,node[0])
        elif(problem.type==2):
          return findpath2(problem.getStartState(),explored,node[0],problem)
        if(problem.type==3):
          return findpath3(problem.getStartState(),explored,node[0],problem)
      i=i+1
      succ=problem.getSuccessors(node[0])
      #print succ
      for elem in succ:
        #newh=node[2]+elem[2]+heuristic(elem[0],problem)
        if(elem[0] not in explored):
              #print ((elem[0],elem[1],node[2]+1),node[2]+1+heuristic(elem[0],problem))
              frontier.push((elem[0],elem[1],node[2]+elem[2]),node[2]+elem[2]+heuristic(elem[0],problem))

  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

