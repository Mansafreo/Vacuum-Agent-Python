# Vacuum Cleaner Agent in a maze world
## Introduction
This project is a simple implementation of a vacuum cleaner agent in a maze world. The agent is able to move in the maze world and clean the dirty cells. The agent is able to move in four directions: up, down, left, and right. The agent is able to sense the environment and determine whether a cell(room) is dirty or not. The agent is able to clean the dirty cells. The agent also has a bump sensor so it can detect if it hits a wall as it moves.

The aim of this project is to demonstrate agent designs and implementations in a simple environment. The project is implemented in Python. It is largely based on the problem found [here](https://web.ntnu.edu.tw/~tcchiang/ai/Vacuum%20Cleaner%20World.htm).

## Prior Knowledge
The "environment" the agent will be interacting with is a 10 x 10 2D grid that either has cells(rooms) represnted by - in the map files and walls represented by O in the map files found in the `./maps/` directory

The agent cannot move through the walls and the walls are always assumed to be clean. The agent has no prior knowledge of the environment and doesn't have a location sensor. The agent can only sense the current cell it is in and determine if it is dirty or not. The agent can also determine if it has hit a wall as it moves.

The agent uses 2 energy for cleaning. Each movement costs 1 energy. The agent can also stay idle costing 0 energy. At each time step each room has a chance of increasing dirt by one unit

## Performance measure
The performance measure is based on the sum of dirt squared in all the rooms and the energy used by the agent. The goal is to minimise the sum of dirt squared in all the rooms and cost the least amount of energy after a given time period T.

## Project structure
The project is structured as follows:
- `agent.py`: Contains the agent class that implements the agent logic
- `environment.py`: Contains the environment class that implements the environment logic
- `arena.py`: Contains the code that allows a given agent to interact with a given environment
- `maps/`: Contains the map files that represent the environment
- `bogo_agent.py`: Contains a simple agent that moves randomly in the environment
- Numbered agents e.g `agent1.py`, `agent2.py`, `agent3.py`: Contains the different agents that can be used in the environment
  
## The Environment Class

The `Environment` class is responsible for creating and managing the environment in which the agents operate. It handles the initialization of the environment from a map file, updates the environment based on the agent's actions, and provides methods for the agent to interact with the environment.

### Sample Methods

- `__init__(self, map_file)`: 
  - **Description**: Constructor that initializes the environment from a given map file.
  - **Parameters**: 
    - `map_file` (str): The path to the map file that represents the environment.
  - **Example**:
    ```python
    env = Environment("maps/map1.txt")
    ```

- `get_agent_location(self)`:
  - **Description**: Returns the current location of the agent in the environment.
  - **Returns**: 
    - `(int, int)`: A tuple representing the (x, y) coordinates of the agent's location.
  - **Example**:
    ```python
    location = env.get_agent_location()
    ```

- `move_agent(self, location)`:
  - **Description**: Moves the agent to a new location in the environment.
  - **Parameters**: 
    - `location` (tuple): A tuple representing the (x, y) coordinates of the new location.
  - **Example**:
    ```python
    env.move_agent((2, 3))
    ```

- `clean_cell(self, location)`:
  - **Description**: Cleans the cell at the given location.
  - **Parameters**: 
    - `location` (tuple): A tuple representing the (x, y) coordinates of the cell to be cleaned.
  - **Example**:
    ```python
    env.clean_cell((1, 1))
    ```

- `accept_agent_action(self, action)`:
  - **Description**: Accepts an action from the agent and updates the environment accordingly.
  - **Parameters**: 
    - `action` (str): The action to be performed by the agent (e.g., "move_up", "move_down", "clean").
  - **Returns**: 
    - `str`: The result of the action (e.g., the new state of the cell).
  - **Example**:
    ```python
    result = env.accept_agent_action("move_up")

### Example Usage

Here is an example of how to use the `Environment` class:

```python
from environment import Environment

# Initialize the environment with a map file
env = Environment("maps/env1.map")

# Get the agent's current location
location = env.get_agent_location()
print(f"Agent's current location: {location}")

# Move the agent to a new location
env.move_agent((2, 3))

# Clean a specific cell
env.clean_cell((1, 1))

# Accept an action from the agent
result = env.accept_agent_action("move_up")
print(f"Result of the action: {result}")

```
## The Agent Class

The `Agent` class is responsible for defining the behavior and actions of the agent within the environment. It includes methods for the agent to perceive its surroundings, decide on actions, and interact with the environment.

### Sample Methods

- `__init__(self)`:
  - **Description**: Constructor that initializes the agent's state, including its location, memory, and energy usage.
  - **Example**:
    ```python
    agent = Agent()
    ```

- `get_location(self)`:
  - **Description**: Returns the current location of the agent.
  - **Returns**: 
    - `(int, int)`: A tuple representing the (x, y) coordinates of the agent's location.
  - **Example**:
    ```python
    location = agent.get_location()
    ```

- `perceive(self)`:
  - **Description**: Allows the agent to perceive its surroundings and returns the status of adjacent cells.
  - **Returns**: 
    - `dict`: A dictionary with keys as directions ("up", "down", "left", "right") and values as the status of the corresponding cells.
  - **Example**:
    ```python
    perception = agent.perceive()
    ```

- `act(self, action)`:
  - **Description**: Performs the given action and updates the agent's state accordingly.
  - **Parameters**: 
    - `action` (str): The action to be performed by the agent (e.g., "move_up", "move_down", "clean").
  - **Returns**: 
    - `str`: The result of the action.
  - **Example**:
    ```python
    result = agent.act("move_up")
    ```

- `think(self)`:
  - **Description**: Decides on the next action for the agent based on its current state and surroundings.
  - **Returns**: 
    - `str`: The next action to be performed by the agent.
  - **Example**:
    ```python
    next_action = agent.think()
    ```

### Example Usage

Here is an example of how to use the `Agent` class:

```python
from agent import Agent

# Initialize the agent
agent = Agent()

# Get the agent's current location
location = agent.get_location()
print(f"Agent's current location: {location}")

# Perceive the surroundings
perception = agent.perceive()
print(f"Perception of surroundings: {perception}")

# Decide on the next action
next_action = agent.think()
print(f"Next action: {next_action}")

# Perform an action
result = agent.act(next_action)
print(f"Result of the action: {result}")

```

## The Arena 
This `arena.py` script sets up the environment and places the agent inside it to interact with the surroundings. The agent moves around the environment, cleans dirt, and maps the area for a set number of time steps. The simulation animates the agent's movement and tracks its performance metrics such as energy consumption, number of cleaned stacks, and mapping coverage.
### Key Components:
Agent Interaction with Environment:
>The agent interacts with an environment represented as a 2D grid.
The environment has cells that may contain dirt (which the agent can clean) or walls (which the agent must avoid).
Agent Behavior:

>The agent moves around the environment for 2000 time steps, performing actions such as moving and cleaning dirt.
At each step, the agent perceives the environment and takes an action (move, clean, or idle).
The agent updates its internal map as it moves, marking cells as "explored."
Metrics and Reporting:

After the simulation, various performance metrics are printed:

<b>Dirt SOS</b>: Sum of squares of dirt remaining, indicating how much dirt is left in the environment.

<b>Energy Consumed</b>: How much energy the agent has used during its movement and cleaning actions.

<b>Stacks Cleaned</b>: How many dirt piles the agent successfully cleaned.

<b>Efficiency</b>: The number of stacks cleaned per unit of energy.
Mapping Coverage: Percentage of the environment that the agent has explored and mapped.

### Example Usage
Here is an example of how to use the `Arena` class:

```python
from bogo_agent import Bogo_Agent
from environment import Environment
import time
#Intantiate the environment
my_env=Environment()
my_env.load_env()
#Instantiate the agent
my_agent=Bogo_agent()
my_env.place_agent((1,1))
time_steps=2000
for i in range(time_steps):
    #Print the environment and pause the script for a fraction of a second to animate the environment movement
    my_env.print_env()
    my_agent.current_cell=my_env.agent_cell
    agent_action=my_agent.think()
    response=my_env.accept_agent_action(agent_action)
    my_agent.sense(response)
    time.sleep(0.01)
    #Build up dirt 
    my_env.random_dirt_build(probability=0.01)

#Print the sum of squares of dirt in the envrionment
print(f'sum of dirt_squared: {my_env.dirt_sos()}')
print(f"Energy Consumed->{my_agent.energy_consumed}")
print(f"{my_env.stacks_cleaned} stacks cleaned")
print(f"Efficiency ->{my_env.stacks_cleaned/my_agent.energy_consumed}")
#Get the percentage of mapped areas
mapped=0
for i in my_agent.map.values():
    if i==1 or i==0:
        mapped+=1
print(f"Percentage of mapped areas->{(mapped/100)*100}%")

```

## Installation
To run the project, you need to have Python installed on your system. You can download Python from the official website: https://www.python.org/

This project has no external dependencies

Clone the repo:
```bash
git clone <https://github.com/Mansafreo/Vacuum-Agent-Python/>
```

## Test
- Navigate to the `arena.py` file directory level
- Run in by using the command `py arena.py`

### Sample output
"A" represents the location of the agent

"-" represents a clean cell

A number (0-9) represents a dirty cell

"O" represents a wall
```bash
O O O O O O O O O O
O 9 9 9 9 9 9 9 9 O
O 9 O O O O O O 9 O
O 9 O 1 - 1 - - 9 O
O 9 O - - 1 - O 9 O
O 9 O - 1 - 1 O 9 O
O 9 O - - 2 - O 9 O
O 9 O O - O O O 9 O
O 9 9 9 A 7 8 9 9 O
O O O O O O O O O O


Agent Cell->2
Agent Location->(8, 4)
Agent Action->clean
Response->None
Map->{(0, 0): 1, (0, 1): 1, (1, 1): 0, (0, 2): 1, (0, 3): 1, (-1, 3): 0, (0, 4): 1, (0, 5): 1, (-1, 5): 0, (0, 6): 1, (1, 6): 0, (0, 7): 1, (0, 8): 0, (-1, 7): 0, (1, 7): 1, (1, 8): 0, (2, 7): 1, (3, 7): 1, (4, 7): 1, (5, 7): 1, (6, 7): 1, (6, 8): 0, (7, 7): 1, (7, 6): 1, (7, 5): 1, (7, 4): 1, (6, 4): 0, (8, 4): 0, (7, 3): 1, (6, 3): 0, (7, 2): 1, (7, 1): 1, (6, 1): 0, (8, 1): 0, (7, 0): 1, (6, 0): 1, (6, -1): 0, (5, 0): 1, (5, 1): 0, (4, 0): 1, (3, 0): 1, (2, 0): 1, (1, 0): 1, (1, -1): 0, (0, -1): 0, (-1, 0): 0, (-1, 1): 0, (-1, 2): 0, (1, 2): 0, (1, 3): 0, (-1, 4): 0, (1, 4): 0, (1, 5): 0, (-1, 6): 0, (2, 6): 0, (2, 8): 0, (3, 6): 1, (3, 5): 1, (3, 4): 1, (2, 4): 1, (2, 3): 1, (2, 2): 1, (2, 1): 0, (3, 2): 1, (4, 2): 1, (4, 3): 1, (3, 3): 1, (5, 3): 1, (5, 2): 1, (6, 2): 1, (8, 2): 0, (8, 3): 0, (6, 5): 0, (8, 5): 0, (8, 6): 0, (6, 6): 0, (7, 8): 0, (8, 7): 0, (5, 6): 0, (5, 8): 0, (4, 6): 0, (4, 8): 0, (3, 8): 0, (8, 0): 0, (7, -1): 0, (5, -1): 0, (4, 1): 0, (4, -1): 0, (2, 5): 1, (4, 4): 1, (4, 5): 1, (5, 5): 1, (5, 4): 1, (3, 1): 0}
step: 1999
sum of dirt_squared: 2147
Energy Consumed->1718
448 stacks cleaned
Efficiency ->0.2607683352735739
Percentage of mapped areas->94.0%

```


    