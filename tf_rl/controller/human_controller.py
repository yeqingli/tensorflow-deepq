from tf_rl.utils.getch import getch
from redis import StrictRedis



class HumanController(object):
    def __init__(self, mapping):
        self.mapping = mapping
        self.r = StrictRedis()
        self.experience = []

    def action(self, o):
        c = self.r.get("action")
        if c not in self.mapping:
            return 0  # FIXME: for unknown action always take default
        return self.mapping[c]

    def store(self, observation, action, reward, newobservation):
        pass

    def training_step(self):
        pass



def control_me():
    r = StrictRedis()
    print("Human controller started. Press 'q' to exit ... ")
    while True:
        c = getch()
        if c == 'q':
            return
        r.set("action", c)


if __name__ == '__main__':
    control_me()
