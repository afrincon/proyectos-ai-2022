from abc import ABC, abstractmethod


class Switchable(ABC):
    @abstractmethod
    def climb_up(self):
        pass

    @abstractmethod
    def climb_down(self):
        pass


class Escalators(Switchable):
    def climb_up(self):
        print("Stairs: Climb up...")

    def climb_down(self):
        print("Stairs: Climb down...")


class Elevator(Switchable):
    def climb_up(self):
        print("Elevator: up...")

    def climb_down(self):
        print("Levator: down...")


class EscalatorsSwitch:

    def __init__(self, c: Switchable):
        self.client = c
        self.on = False

    def press(self):
        if self.on:
            self.client.climb_down()
            self.on = False
        else:
            self.client.climb_up()
            self.on = True


l = Escalators()
e = Elevator()
switch = EscalatorsSwitch(l)
switch.press()
switch.press()