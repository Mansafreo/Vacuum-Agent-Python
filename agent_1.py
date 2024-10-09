#This is a relatively smarter agent that the first one which chose actions randomly
"""
This agent has memory and keeps track of where it has explored or not and whether it has encountered obstacles
The decisions are still random but this one will try to explore unexplored locations first and avoids obstacles that it has encountered before
It is much more efficient than the first one
"""
from agent import Agent
from random import choice
#create a class that inherits from the Agent class
class Agent_1(Agent):
    def __init__(self):
        #The agent has a location in the environment but it doesn't know yet
        self.x = 0
        self.y = 0
        #The agent has a record of how much energy it uses
        self.energy_consumed=0
        #Initialize a 2D array of co-ordinates so that the bot can map its surroundings
        self.map={}
        self.map[0,0]=1
        #To remember what it had done last
        self.last_action=""
        self.current_cell="-"

    #The perceive function that will contain most of the robot's logic
    def think(self):
       if self.dirt_sense() is True:
            return self.act("clean")
       #Get it's current location
       x,y=self.get_location()
       perception=self.perceive()
       #Loop through the perception and see if one of them is unexplored
       unexplored=[]
       explorable=[]
       for loc in perception:
            status=perception[loc]
            if(status=="Unexplored"):
                unexplored.append(loc)
            elif(status==1):
                explorable.append(loc)
            elif(status==0):
                continue
            else:
                Exception("Invalid location status")
       #If there are unexplored locations, choose one at random
       if len(unexplored)>0:
            move=choice(unexplored)
            return self.act("move_"+move)
       #If there are no unexplored locations, choose a random action
       else:
            #Make a choice between being idle and moving
            options=["idle","move"]
            decision=choice(options)
            if decision=="move":
                move=choice(explorable)
                return self.act("move_"+move)
            else:
                return self.act("idle")

    #Function to allow the robot to look up a location in the map
    def map_lookup(self, location):
        x, y = location
        #Check if a location exists and get the value, otherwise return false
        return self.map.get((x, y), "Unexplored")

    #A function that allows the agent to sort of reason about the environment it's in
    def perceive(self):
        #Get it's current location
        x,y=self.get_location()
        #Get the hypothetical locations around it
        left=[x-1,y]
        right=[x+1,y]
        up=[x,y-1]
        down=[x,y+1]
        #Map the locations
        left=self.map_lookup(left)
        right=self.map_lookup(right)
        up=self.map_lookup(up)
        down=self.map_lookup(down)
        #To give the think function the environment it knows
        data={
            "left":left,
            "right":right,
            "up":up,
            "down":down
        }
        print(data)
        return data

    def dirt_sense(self):
        #check if it's current cell is clean
        if self.current_cell!="-":
            return True
        
    def sense(self,stimuli):
        x,y=self.get_location()
        if stimuli is True:
            #This means that the area is movable and probably should be mapped if ot doesn't exist
            #check what the last move was so it can be added to the map correctly
            if self.last_action=="up":
                self.map[x,y-1]=1
                #Update it's current location
                self.y-=1
            elif self.last_action=="down":
                self.map[x,y+1]=1
                self.y+=1
            elif self.last_action=="left":
                self.map[x-1,y]=1
                self.x-=1
            elif self.last_action=="right":
                self.map[x+1,y]=1
                self.x+=1
        elif stimuli is False:
            #Must have been a bump
            if self.last_action=="up":
                self.map[x,y-1]=0
            elif self.last_action=="down":
                self.map[x,y+1]=0
            elif self.last_action=="left":
                self.map[x-1,y]=0
            elif self.last_action=="right":
                self.map[x+1,y]=0


    #A function that implements the agent's actions
    def act(self,action):
        #For this first agent, the movement will be random and cleaning will be random as well
        #moving costs 1 energy, idling 0 , cleaning 2
        if action == "move_up":
            self.last_action="up"
            self.energy(1)
        elif action == "move_down":
            self.last_action="down"
            self.energy(1)
        elif action == "move_left":
            self.last_action="left"
            self.energy(1)
        elif action == "move_right":
            self.last_action="right"
            self.energy(1)
        elif action == "clean":
            self.last_action=5
            self.energy(2)
        elif action == "idle":
            self.last_action=6
            self.energy(0)
        return action
    
if __name__=="__main__":
    agent=Agent_1()
    print(agent.map)