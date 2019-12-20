class BlockNode:
    def __init__(self, count, commands):
        self.count = count
        self.commands = commands

    def accept(self, visitor):
        visitor.evaluate_block(self.count, self.commands)


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
    def __init__(self, count, commands):
        self.count = count
        self.commands = commands

    def accept(self, visitor):
        visitor.evaluate_command(self.commands, self.count)

class ObjManipNode:
    def __init__(self, manip):
        self.manip = manip

    def accept(self, visitor):
        visitor.evaluate_objmanip(self.manip)
