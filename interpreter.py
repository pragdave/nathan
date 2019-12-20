class Interpreter:

    def __init__(self, logger):
        self.logger = logger
        self.x = 0
        self.y = 0
        self.direction = [1, 0]
        self.holding = []

    def evaluate_block(self, commands):
        for cmd in commands:
            cmd.accept(self)

    def evaluate_command(self, command):
        command.accept(self)

    def evaluate_forward(self):
        self.x += self.direction[0]
        self.y += self.direction[1]
        self.trace("F")

    def evaluate_turn(self, direction):
        x, y = self.direction
        if direction == "R":
            x, y = y, -x
        else:
            x, y = -y, x

        self.direction = [x, y]
        self.trace(direction)

    def trace(self, action):
        self.logger(
          action,
          [self.x, self.y],
          self.direction,
          self.holding
        )
