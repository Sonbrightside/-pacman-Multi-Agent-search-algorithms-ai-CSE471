# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent
from pacman import GameState

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState: GameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState: GameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        
        
        closest_food_pos = min(
            (manhattanDistance(newPos, food) for food in newFood.asList()),
            default=float('inf')  # 먹이가 없을 때를 대비
        )
                
        newGhostPos = successorGameState.getGhostPosition(1)
        
        dis_score = manhattanDistance(newPos,newGhostPos)

        if(dis_score < 2) :
            dis_score =  dis_score - 1000000
        score = successorGameState.getScore() + dis_score/100 + 10/(closest_food_pos)
        print('------------------')
        print(successorGameState.getScore())
        print('============vs=======\n my function score:')
        print (score)
        print('------------------')


        "*** YOUR CODE HERE ***"
        return score

    

def scoreEvaluationFunction(currentGameState: GameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        

        value, action = self.maxValue(gameState, self.depth, 0)
        print(action)
        return action


    def maxValue(self, gameState: GameState, depth: int, agentIndex: int):

        if depth == 0 or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState), None

        best_value = -float('inf')
        best_action = gameState.getLegalActions(agentIndex)[0]

        
    
        for action in  gameState.getLegalActions(agentIndex):
            successor = gameState.generateSuccessor(agentIndex, action)
            value, _= self.minValue(successor, depth, agentIndex + 1)
            if value > best_value:
                best_value = value
                best_action = action
        print(best_action)
        return best_value, best_action


    def minValue(self, gameState: GameState, depth: int, agentIndex: int):
    
        if gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState), None

        worst_value = float('inf')
        best_action = None
        num_agents = gameState.getNumAgents()

        
        for action in gameState.getLegalActions(agentIndex):
            successor = gameState.generateSuccessor(agentIndex, action)
            if agentIndex == num_agents - 1:
                value, _ = self.maxValue(successor, depth - 1, 0, alpa, beta)
            else:  # 다음 고스트
                value, _ = self.minValue(successor, depth, agentIndex + 1)
            if value < worst_value:
                worst_value = value
                best_action = action

        return worst_value, best_action

        util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"

        value, action = self.maxValue(gameState, self.depth, 0, -float('inf'), float('inf'))
        return action
    
    def maxValue(self, gameState: GameState, depth: int, agentIndex: int, alpa: float, beta: float):

        if depth == 0 or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState), None

        best_value = -float('inf')
        best_action = None
        
        for action in  gameState.getLegalActions(agentIndex):
            successor = gameState.generateSuccessor(agentIndex, action)
            value, _= self.minValue(successor, depth, agentIndex + 1,alpa,beta)
            if value > best_value:
                best_value = value
                best_action = action
            if best_value > beta:
                return  best_value,best_action
            alpa = max(alpa, best_value)
        
        return best_value, best_action




    def minValue(self, gameState: GameState, depth: int, agentIndex: int, alpa: float, beta: float):

        if gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState), None

        worst_value = float('inf')
        best_action = None
        num_agents = gameState.getNumAgents()

        
        for action in gameState.getLegalActions(agentIndex):
            successor = gameState.generateSuccessor(agentIndex, action)
            if agentIndex == num_agents - 1:
                value, _ = self.maxValue(successor, depth - 1, 0, alpa, beta)
            else:  # 다음 고스트
                value, _ = self.minValue(successor, depth, agentIndex + 1,alpa,beta)

            if value < worst_value:
                worst_value = value
                best_action = action

            if worst_value < alpa:
                return worst_value, best_action

            beta = min(beta, worst_value)

        return worst_value, best_action
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        value, action = self.maxValue(gameState, self.depth, 0, -float('inf'), float('inf'))
        return  action
        "*** YOUR CODE HERE ***"

    def maxValue(self, gameState: GameState, depth: int, agentIndex: int, alpha: float, beta: float):
        if depth == 0 or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState), None

        best_value = -float('inf')
        best_action = None

        for action in gameState.getLegalActions(agentIndex):
            successor = gameState.generateSuccessor(agentIndex, action)
            value, _ = self.expValue(successor, depth, agentIndex + 1, alpha, beta)  # 다음 agent

            if value > best_value:
                best_value = value
                best_action = action

        return best_value, best_action


    def expValue(self, gameState: GameState, depth: int, agentIndex: int, alpha: float, beta: float):
        if gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState), None

        actions = gameState.getLegalActions(agentIndex)
        if not actions:
            return self.evaluationFunction(gameState), None

        total_value = 0
        num_agents = gameState.getNumAgents()
        probability = 1.0 / len(actions)

        for action in actions:
            successor = gameState.generateSuccessor(agentIndex, action)

            if agentIndex == num_agents - 1:
                value, _ = self.maxValue(successor, depth - 1, 0, alpha, beta)
            else:
                value, _ = self.expValue(successor, depth, agentIndex + 1, alpha, beta)

            total_value += probability * value

        return total_value, None

        

