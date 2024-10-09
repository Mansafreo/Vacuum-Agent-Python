# This is the file that houses a given agent , it's functions and how it interacts with the environment
# The agent is a simple agent that can move around the environment and clean the dirt in the environment
from agent import Agent
import random
class Bogo_Agent(Agent):
    def __init__(self):
        super().__init__()
    #The agent has a location in the environment but it doesn't know yet
    #The perceive function that will contain most of the robot's logic
    def think(self):
        actions=["move_up","move_down","move_left","move_right","clean","idle"]
        #The agent will randomly choose an action
        action=random.choice(actions)
        return self.act(action)

    #A function that implements hypothetical sensors that the agent uses to perceive the environment
    def perceive():
        pass

    def sense(self,stimuli):
        pass

