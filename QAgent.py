import numpy as np
import random

class QLearningAgent:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.q_table = {}  # Q-table to store state-action values
        self.actions = ["move_up", "move_down", "move_left", "move_right", "clean", "idle"]
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount factor
        self.epsilon = epsilon  # Exploration rate
    
    def get_state(self, env):
        # Define state as the agent's location and the dirt status around
        agent_location = env.get_agent_location()
        surroundings = [env.get_location(agent_location[0] + dx, agent_location[1] + dy) 
                        for dx in [-1, 0, 1] for dy in [-1, 0, 1]]  # Look around the agent
        return (agent_location, tuple(surroundings))
    
    def choose_action(self, state):
        if state not in self.q_table:
            self.q_table[state] = {action: 0 for action in self.actions}
        # Epsilon-greedy strategy for exploration-exploitation
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(self.actions)  # Explore
        else:
            return max(self.q_table[state], key=self.q_table[state].get)  # Exploit

    def learn(self, state, action, reward, next_state):
        if next_state not in self.q_table:
            self.q_table[next_state] = {action: 0 for action in self.actions}
        # Q-learning formula
        current_q = self.q_table[state][action]
        max_future_q = max(self.q_table[next_state].values())
        new_q = current_q + self.alpha * (reward + self.gamma * max_future_q - current_q)
        self.q_table[state][action] = new_q
    
    def think(self, env):
        state = self.get_state(env)
        action = self.choose_action(state)
        return action

    def sense(self, env, action, reward):
        state = self.get_state(env)
        new_state = self.get_state(env)
        self.learn(state, action, reward, new_state)

