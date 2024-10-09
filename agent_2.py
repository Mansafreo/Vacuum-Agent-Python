from agent import Agent
from random import choice
"""
An improvement from agent_1 with backtracking -> It's a better explorer but more energy intensive
"""
class Agent_2(Agent):
    def __init__(self):
        # Initialize agent's location, memory, energy usage, and action history
        self.x, self.y = 0, 0
        self.energy_consumed = 0
        self.map={}
        self.map[0,0]= 1  # 1 represents explored and passable
        self.visited = {(0, 0): True}  # Keep track of visited cells
        self.stack = [(0, 0)]  # Stack to store the path for backtracking
        self.last_action = ""
        self.current_cell = "-"
    
    # Modified think function to prioritize unexplored cells and implement backtracking
    def think(self):
        # If there's dirt in the current cell, clean it
        if self.dirt_sense():
            return self.act("clean")
        
        # Get current location and perception of surrounding cells
        perception = self.perceive()
        unexplored, explorable = [], []
        
        # Classify surrounding cells as unexplored or explorable
        for direction, status in perception.items():
            if status == "Unexplored":
                unexplored.append(direction)
            elif status == 1 and not self.visited.get(self.get_new_location(direction), False):
                explorable.append(direction)
        
        # Prioritize moving to unexplored cells
        if unexplored:
            move = choice(unexplored)
            self.stack.append(self.get_location())  # Add current location to stack for backtracking
            return self.act(f"move_{move}")
        
        # If no unexplored cells, move to an explorable cell or backtrack
        elif explorable:
            actions=["idle","move"]
            decision=choice(actions)
            if decision=="idle":
                self.act("idle")
            else:
                move = choice(explorable)
                self.stack.append(self.get_location())
                return self.act(f"move_{move}")
     
        # If stuck (no explorable cells), backtrack using the stack
        elif self.stack:
            previous_location = self.stack.pop()  # Backtrack to the previous location
            return self.move_to_previous(previous_location)
        
        # If nothing to do, stay idle
        return self.act("idle")
    
    # Function to calculate the new location based on a move direction
    def get_new_location(self, direction):
        x, y = self.get_location()
        if direction == "up":
            return (x, y - 1)
        elif direction == "down":
            return (x, y + 1)
        elif direction == "left":
            return (x - 1, y)
        elif direction == "right":
            return (x + 1, y)
    
    # Perceive the status of surrounding cells
    def perceive(self):
        x, y = self.get_location()
        perception = {
            "left": self.map_lookup((x - 1, y)),
            "right": self.map_lookup((x + 1, y)),
            "up": self.map_lookup((x, y - 1)),
            "down": self.map_lookup((x, y + 1)),
        }
        return perception
    
    # Move to a previous location during backtracking
    def move_to_previous(self, previous_location):
        prev_x, prev_y = previous_location
        curr_x, curr_y = self.get_location()
        if prev_x < curr_x:
            return self.act("move_left")
        elif prev_x > curr_x:
            return self.act("move_right")
        elif prev_y < curr_y:
            return self.act("move_up")
        elif prev_y > curr_y:
            return self.act("move_down")
    
    def dirt_sense(self):
        return self.current_cell != "-"
    
    def map_lookup(self, location):
        x, y = location
        #Check if a location exists and get the value, otherwise return false
        return self.map.get((x, y), "Unexplored")
    
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

    
    # Function to implement actions and update energy consumption
    def act(self, action):
        if action == "move_up":
            self.last_action = "up"
            self.energy(1)
        elif action == "move_down":
            self.last_action = "down"
            self.energy(1)
        elif action == "move_left":
            self.last_action = "left"
            self.energy(1)
        elif action == "move_right":
            self.last_action = "right"
            self.energy(1)
        elif action == "clean":
            self.last_action = "clean"
            self.energy(2)
        elif action == "idle":
            self.last_action = "idle"
            self.energy(0)
        return action

    def get_location(self):
        return self.x, self.y

    def energy(self, amount):
        self.energy_consumed += amount

if __name__ == "__main__":
    agent = ImprovedAgent()
    print(agent.map)
