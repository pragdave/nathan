class BlockNode:
    def __init__(self, commands):
        self.commands = commands

    def accept(self, visitor):
        visitor.evaluate_block(self.commands)


class ForwardNode:
    def __init__(self):
        pass

    def accept(self, visitor):
        visitor.evaluate_forward()


class TurnNode:
    def __init__(self, direction):
        self.direction = direction

    def accept(self, visitor):
        visitor.evaluate_turn(self.direction)


class CommandNode:
    def __init__(self, command):
        self.command = command

    def accept(self, visitor):
        visitor.evaluate_command(self.command)

class ObjManipNode:
    def __init__(self, manip):
        self.manip = manip

    def accept(self, visitor):
        visitor.evaluate_objmanip(self.manip)
