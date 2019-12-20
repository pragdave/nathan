class Interpreter:

    def __init__(self, logger):
        self.logger = logger
        self.x = 0
        self.y = 0
        self.direction = [1, 0]
        self.holding = []

    def evaluate_block(self, count, commands):
        #using this count, interate through each command in "commands" list
        #ie: 3[FR] calls the sequence "FR" three times
        for cmdcountiter in range(0, int(count)):
            for cmd in commands:
                cmd.accept(self)

    def evaluate_command(self, command, count):
        #using this count, iterate through the command "count" number of times
        #ie: 3F calls "F" three times
        for cmdcountiter in range(0, int(count)):
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

    def evaluate_objmanip(self, manip):
        #get current X/Y position
        currentX, currentY = self.x, self.y
        #pick up/drop off object based on given command at this X/Y position
        action = manip
        if action == "P":
            self.holding.append([currentX, currentY])
        elif action == "D":
            self.holding.pop()

        self.trace(manip)   


    #function that uses the logger to print values that he wrote- do not touch
    def trace(self, action):
        self.logger(
          action,
          [self.x, self.y],
          self.direction,
          self.holding
        )
