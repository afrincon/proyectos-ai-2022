class Escalators:
    def climb_up(self):
        print("Stairs: Slimb up...")

    def climb_down(self):
        print("Stairs: Climb down...")


class EscalatorsSwitch:

    def __init__(self, l: Escalators):
        self.escalators = l
        self.on = False

    def press(self):
        if self.on:
            self.escalators.climb_down()
            self.on = False
        else:
            self.escalators.climb_up()
            self.on = True


l = Escalators()
switch = EscalatorsSwitch(l)
switch.press()
switch.press()