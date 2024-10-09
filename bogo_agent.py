# This is the file that houses a given agent , it's functions and how it interacts with the environment
# The agent is a simple agent that can move around the environment and clean the dirt in the environment
from agent import Agent
import random
class Bogo_Agent(Agent):
    def __init__(self):
        #The agent has a location in the environment but it doesn't know yet
        self.x = None
        self.y = None
        #The agent has a record of how much energy it uses
        self.energy_consumed=0
        self.map={}
    
    #Function to set the agent's location
    def set_location(self,x,y):
        self.x = x
        self.y = y
        return (self.x,self.y)
    #Function to increase or decrease energy consumption
    def energy(self,energy):
        self.energy_consumed += energy
        return self.energy_consumed
    
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

    #A function that implements the agent's actions
    def act(self,action):
        #For this first agent, the movement will be random and cleaning will be random as well
        #moving costs 1 energy, idling 0 , cleaning 2
        if action == "move_up":
            self.energy(1)
        elif action == "move_down":
            self.energy(1)
        elif action == "move_left":
            self.energy(1)
        elif action == "move_right":
            self.energy(1)
        elif action == "clean":
            self.energy(2)
        elif action == "idle":
            self.energy(0)
        return action
