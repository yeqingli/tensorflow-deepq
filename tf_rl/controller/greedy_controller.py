import random

class GreedyController(object):
    def __init__(self, mapping):
        self.mapping = mapping

    def action(self, o):
        return random.randint(0, self.num_actions - 1)

    def store(self, observation, action, reward, newobservation):
        pass

    def training_step(self):
        pass
