from gym import spaces
import numpy as np
import random
from itertools import groupby
from itertools import product

class TicTacToe():

    def __init__(self):
        
        self.position = np.random.choice(['0','1','2','3','4','5','6','7','8'])
        self.pick = np.random.choice([1,3,5,7,9])
        self.state = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0}

        self.all_possible_numbers = [1,2,3,4,5,6,7,8,9]
        
        self.reset()


    def is_winning(self, curr_state):
        lines = [('0','1','2'),('3','4','5'),('6','7','8'),('0','3','6'),('1','4','7'),('2','5','8'),('0','4','8'),('2','4','6')]
        winner = None
        for line in lines:
            line_state = curr_state[line[0]] + curr_state[line[1]] + curr_state[line[2]]
            if line_state == 15:
                winner = line
        if winner == None:
            return None
        else:
            return winner
        """Takes state as an input and returns whether any row, column or diagonal has winning sum"""

    def is_terminal(self, curr_state):
        """Takes state as an input and returns whether it is win/tie state"""
        if self.is_winning(curr_state) != None:
            return 'win'
        if self.allowed_positions(curr_state) == None:
            return 'tie'
        
        return None

    def allowed_positions(self, curr_state):
        """Takes state as an input and returns all indexes that are blank"""
        index_list = []
        for key,value in curr_state.items():
            if value == 0:
                index_list.append(key)
        if index_list == []:
            return None
        else:
            return index_list
               
    def allowed_values(self, curr_state):
        """Takes the current state as input and returns all possible (unused) values that can be placed on the board"""
        allowed_values = [1,2,3,4,5,6,7,8,9]
        used_values =[]
        for key,value in curr_state.items():
            if value in [1,2,3,4,5,6,7,8,9]:
                used_values.append(value)
        allowed_values = [x for x in allowed_values if x not in used_values]
        if allowed_values == []:
             return None
        else:
             return allowed_values

    def action_space(self, curr_state):
        """Takes the current state as input and returns all possible actions, i.e, all combinations of allowed positions and allowed values"""
        allowed_position = self.allowed_positions(curr_state)
        allowed_val = self.allowed_values(curr_state)
        all_combination = list(product(allowed_position,allowed_val))
        if all_combination == []:
            return None
        else:
            return all_combination
        


    def initial_step(self, curr_state):
        """This functions will be used only if environment is playing with the odd numbers, i.e., the environment has to make first move"""
        obs = curr_state
        allowed_posn = self.allowed_positions(obs)
        allowed_val = self.allowed_values(obs)
        allowed_env_val = [x for x in allowed_val if x%2 != 0]
        if allowed_env_val==[]:
            reward = -1
            return obs,reward
        env_position = str(np.random.choice(allowed_posn))
        env_action = int(np.random.choice(allowed_env_val))
        env_move = (env_position,env_action)
        obs2 = self.state_transition(obs,env_move)
        return obs2
        

    def state_transition(self, curr_state, curr_action):
        """Takes current state and action and returns the board position just after agent's move."""
        curr_state.update({curr_action[0]:curr_action[1]})

        return curr_state
    
        
        
        
        


    def step(self, curr_state, curr_action):
        """Takes current state and action and returns the next state and reward. Hint: First, check the board position after
        agent's move, whether the game is won/loss/tied. Then incorporate environment's move and again check the board status."""
        
        curr_state=self.state_transition(curr_state,curr_action)
        agentwintie = self.is_terminal(curr_state)
        if agentwintie == 'win':
              reward = 10
              return curr_state,reward
        if agentwintie == 'tie':
              reward = 0
              return curr_state,reward

        obs = curr_state
        allowed_posn = self.allowed_positions(obs)
        allowed_val = self.allowed_values(obs)
        allowed_env_val = [x for x in allowed_val if x%2 == 0]
        if allowed_env_val==[]:
            reward = -1
            return obs,reward
            
        env_position = str(np.random.choice(allowed_posn))
        env_action = int(np.random.choice(allowed_env_val))
        env_move = (env_position,env_action)

        obs2 = self.state_transition(obs,env_move)
        env_win_tie = self.is_terminal(obs2)
        if env_win_tie == 'win':
            reward = -10
            return obs2, reward
        if env_win_tie == 'tie':
            reward = 0
            return obs2, reward
        reward = -1
        return obs2, reward
               
    def reset(self):
        return self.state       
            
                    
            
            
        
        



