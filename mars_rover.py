class Marsrover:

    def __init__(self, xcoor, ycoor, facing):
        self.x = xcoor
        self.y = ycoor
        self.facing = facing

    def return_coordinates(self):
        return [self.x, self.y, self.facing]

    def movement(self, commands):
        for i in commands:
            if (i == 'f'):
                self.move_forward()
            elif (i == 'b'):
                self.move_backward()

    def move_forward(self):
        if self.facing == 'N':
            self.y += 1
        elif self.facing == 'S':
            self.y -= 1
        elif self.facing == 'E':
            self.x += 1
        elif self.facing == 'W':
            self.x -= 1

    def move_backward(self):
        if self.facing == 'N':
            self.y -= 1
        elif self.facing == 'S':
            self.y += 1
        elif self.facing == 'E':
            self.x -= 1
        elif self.facing == 'W':
            self.x += 1
