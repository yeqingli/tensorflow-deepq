import random
import numpy as np

class GreedyController(object):
    def __init__(self, mapping, num_observation_lines):
        self.mapping = mapping
        self.num_actions = len(self.mapping)
        self.num_observation_lines = num_observation_lines
        self.num_obs_per_line = 5
        self.region_size = 8*5#self.num_observation_lines/self.num_actions

    def score(self, observe):
        """
        observe is 5 dimension numpy vector
        3 = (f, e, w), 2 = (speed y, speed y)
        """
        ret = 0 
        ret += 1 - observe[0]
        ret -= 1 - observe[1]
        ret -= 0.1*(1 - observe[2]) # Hate the wall a little bit
        return ret

    def action(self, o):
        # Zero degree means straight right, rotation clock-wise 
        # observation = double[(3+2)*#lines+2+2]
        # 3 = (f, e, w), 2 = (speed y, speed y)
        # {"up": 3, "right": 0, "down": 1,"left": 2,}
        region_size = self.region_size
        gain = np.zeros(self.num_actions)
        reward = np.zeros(self.num_actions)
        for i in xrange(0, region_size, self.num_obs_per_line):
            gain[0] += self.score(o[i:i+self.num_obs_per_line])
        for i in xrange(region_size, 2*region_size, self.num_obs_per_line):
            gain[1] += self.score(o[i:i+self.num_obs_per_line])
        for i in xrange(2*region_size, 3*region_size, self.num_obs_per_line):
            gain[2] += self.score(o[i:i+self.num_obs_per_line])
        for i in xrange(3*region_size, 4*region_size, self.num_obs_per_line):
            gain[3] += self.score(o[i:i+self.num_obs_per_line])
        reward[0] = gain[3] + gain[0]
        reward[1] = gain[0] + gain[1]
        reward[2] = gain[1] + gain[2]
        reward[3] = gain[2] + gain[3]
        
        maxi = reward.argmax()
        mini = reward.argmin()    
        if reward[maxi] > reward[mini]:
            #print(reward, maxi, mini)
            return maxi 
        # Use random walk if all directions are the same
        return random.randint(0, self.num_actions - 1)

    def store(self, observation, action, reward, newobservation):
        pass

    def training_step(self):
        pass
        