class ShadowPal(object):
    def __init__(self):
        self.name = "Blince"
        self.sleep = 0
        self.pace = 1

    def decideNeed(self):
        if self.sleep == 1:
            return self.sleep
        else:
            return self.pace
    