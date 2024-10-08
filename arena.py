#This is the file where the agent will interact with the environment
from agent import Agent
from environment import Environment
import time
#Intantiate the environment
my_env=Environment()
my_env.load_env()

#Instantiate the agent
my_agent=Agent()
my_env.place_agent((5,5))
time_steps=1000
for i in range(time_steps):
    agent_action=my_agent.think()
    my_env.accept_agent_action(agent_action)
    #Print the environment and pause the script for a fraction of a second to animate the environment movement
    my_env.print_env()
    print(f"Agent Cell->{my_env.agent_cell}")
    print(f"Agent Location->{my_env.get_agent_location()}")
    print(f"Agent Action->{agent_action}")
    print(f'step: {i}')
    time.sleep(0.01)
    #Build up dirt 
    my_env.random_dirt_build(probability=0.05)


#The agent will move around the environment and clean the dirt in the environment
#The agent will move randomly and clean randomly
#The agent will be placed in the center of the environment
#The agent will move around for 1000 time steps

#Print the sum of squares of dirt in the envrionment
print(f'sum of dirt_squared: {my_env.dirt_sos()}')
print(f"Energy Consumed->{my_agent.energy_consumed}")
print(f"{my_env.stacks_cleaned} stacks cleaned")
    