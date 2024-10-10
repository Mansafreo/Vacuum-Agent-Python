#Open the environment file 
import random
#The environment is a 10 x 10 grid to represent the edited vaccum cleaner environment
class Environment:
    def __init__(self):
       #To keep track of what the status of the current agent cell is so that if the 
       #agent moves without cleaning, we can restore the cell as it was
       self.agent_cell=""
       self.stacks_cleaned=0
    #The load_env method reads the environment file and loads the environment data into a list
    def load_env(self,filename="./maps/env.map"):
        file = open(filename, "r")#open the file in read mode
        env_data = []#create an empty list
        #read the file line by line
        for line in file:
            #check if the line is a comment denoted by a //
            if not line.startswith("//"):
                #remove the newline character
                line = line.strip()
                #split the line by the spaces
                row = line.split(" ")
                #append the row to the env_data list
                env_data.append(row)
        #close the file
        file.close()
        #set the environment data to the env_data list
        self.env_data = env_data
        return env_data
    
    def print_env(self):
        for row in self.env_data:
            print(" ".join(row))
        print("\n")

    #For the environment, there needs to be a co-ordinate system to represent the location of the agent so that 
    #it can learn to navigate the environment. The co-ordinate system is represented by the x and y co-ordinates
    #The x co-ordinate represents the row and the y co-ordinate represents the column
    def get_location(self, x, y):
        return self.env_data[x][y]
       
    #Function to make a certain cell dirty periodically 
    def dirt_build(self,location):
        x,y=location
        #Get all the non-wall cells
        #Walls are represented by the character "O"
        if self.get_location(x,y) != "O" and self.get_location(x,y) != "A":
            #Add a dirt stack, starting with 1 upwards,if it's clean , i.e "-", put it as one
            if self.env_data[x][y] == "-":
                self.env_data[x][y] = "1"
            else:
                #If the cell is already dirty, increment the dirt stack
                #Max dirt is 9
                if int(self.env_data[x][y]) < 9:
                    self.env_data[x][y] = str(int(self.env_data[x][y]) + 1)
        return self.env_data[x][y]
    
    #Function to clean a cell
    # Function to clean a cell
    def clean_cell(self):
        # check the agent_cell
        if self.agent_cell != "-":
            # Check if agent_cell can be converted to an integer
            try:
                current_dirt = int(self.agent_cell)
                if current_dirt > 1:
                    self.agent_cell = str(current_dirt - 1)
                    self.stacks_cleaned += 1
                else:
                    # If the dirt stack is 1, clean the cell
                    self.agent_cell = "-"
                    self.stacks_cleaned += 1  # Increment cleaned count if it was cleaned
            except ValueError:
                print(f"Warning: Unable to convert agent_cell '{self.agent_cell}' to an integer.")

    
    #Function to randomly build up dirt in random rooms at a given probability
    def random_dirt_build(self,probability):
        #The probability is a number between 0 and 1
        for x in range(1,10):
            for y in range(1,10):
                if random.random() < probability:
                    self.dirt_build((x,y))
        return self.env_data

    #Function to change the location of the agent
    def move_agent(self,location):
        x,y=location
        self.env_data[x][y] = "A"
        return self.env_data[x][y]
    
    #Function to remove the agent from a location
    def remove_agent(self,location):
        x,y=location
        self.env_data[x][y] = "-"
        return self.env_data[x][y]
    
    #Function to place the agent in a given location
    def place_agent(self,location):
        x,y=location
        #If the cell is not a wall, place the agent in the cell and record what was in the cell so it can be restored when the agent moves
        if self.env_data[x][y] != "O":
            self.agent_cell=self.get_location(x,y)
            self.env_data[x][y] = "A"
            return self.env_data[x][y]
        else:
            Exception("Can't place agent in a wall")
    #function to get the agent's location
    def get_agent_location(self):
        for x in range(1,10):
            for y in range(1,10):
                if self.env_data[x][y] == "A":
                    return (x,y)

    #To accept agent actions
    def accept_agent_action(self,action):
        x,y=self.get_agent_location()
        if action == "move_up":
            if self.env_data[x-1][y] != "O":
                #Restore the cell to it's original state
                self.env_data[x][y] = self.agent_cell
                #Update the agent cell
                self.agent_cell=self.get_location(x-1,y)
                #Move the agent
                self.move_agent((x-1,y))
                return True
            else:
                #Meaning there was a bump
                return False
        elif action == "move_down":
            if self.env_data[x+1][y] != "O":
                self.env_data[x][y] = self.agent_cell
                self.agent_cell=self.get_location(x+1,y)
                self.move_agent((x+1,y))   
                return True 
            else:
                return False
        elif action == "move_left":
            if self.env_data[x][y-1] != "O":
                self.env_data[x][y] = self.agent_cell 
                self.agent_cell=self.get_location(x,y-1)
                self.move_agent((x,y-1))  
                return True
            else:
                return False 
        elif action == "move_right":
            if self.env_data[x][y+1] != "O":
                self.env_data[x][y] = self.agent_cell
                self.agent_cell=self.get_location(x,y+1)
                self.move_agent((x,y+1))
                return True 
            else:
                return False
        elif action == "clean":
            self.clean_cell()
            return None
        elif action == "idle":
            return None
    
    #function to print the environment to the terminal
    def print_env(self):
        #First clear the terminal for each frame
        print("\033c")
        for row in self.env_data:
            print(" ".join(row))
        print("\n")
    #Get the sum of squares of dirt in the environment
    def dirt_sos(self):
        sos=0
        for x in range(1,10):
            for y in range(1,10):
                if self.env_data[x][y] != "O" and self.env_data[x][y] != "A" and self.env_data[x][y] != "-":
                    sos += int(self.env_data[x][y])**2
        return sos


if __name__=="__main__":
    my_env=Environment()
    my_env.load_env()
    test_location=my_env.get_location(2,1)
    print(test_location)