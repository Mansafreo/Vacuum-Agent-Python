# This is the file that houses a given agent , it's functions and how it interacts with the environment
# The agent is a simple agent that can move around the environment and clean the dirt in the environment
class Agent:
    def __init__(self):
        #The agent has a location in the environment but it doesn't know yet
        self.x = None
        self.y = None
        #The agent has a record of how much energy it uses
        self.energy_consumed=0
        #Also some memory about the cell it is currently in 
        self.current_cell="-"
        self.map={}
    
    #Function to set the agent's location
    def set_location(self,x,y):
        self.x = x
        self.y = y
        return (self.x,self.y)
    #Function to get the agent's current location
    def get_location(self):
        return (self.x,self.y)
    
    #Function to increase or decrease energy consumption
    def energy(self,energy):
        self.energy_consumed += energy
        return self.energy_consumed
    
    #The perceive function that will contain most of the robot's logic
    def think(self):
        pass

    #A function that implements hypothetical sensors that the agent uses to perceive the environment
    def perceive():
        pass

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
    
    def dirt_sense(self):
        return self.current_cell != "-"
    
    def map_lookup(self, location):
        x, y = location
        #Check if a location exists and get the value, otherwise return Unexplored
        return self.map.get((x, y), "Unexplored")
