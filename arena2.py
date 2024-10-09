from environment import Environment
from QAgent import QLearningAgent
import time
#Intantiate the environment
my_env=Environment()
my_env.load_env()
my_agent = QLearningAgent()
time_steps = 1000

for i in range(time_steps):
    current_state = my_agent.get_state(my_env)
    agent_action = my_agent.think(my_env)
    response = my_env.accept_agent_action(agent_action)
    # Reward system
    if agent_action == "clean":
        reward = 10  # Positive reward for cleaning
    elif response is False:  # Bumped into a wall
        reward = -5
    else:
        reward = -1  # Small penalty for each move to encourage efficient exploration
    my_agent.sense(my_env, agent_action, reward)
    # Print and animate environment as before
    my_env.print_env()
    print(f"Agent Action: {agent_action}")
    print(f"Step: {i}")
    time.sleep(0.01)

# Final summary
print(f'Sum of dirt_squared: {my_env.dirt_sos()}')
print(f'{my_env.stacks_cleaned} stacks cleaned')
