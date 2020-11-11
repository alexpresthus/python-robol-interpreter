# Robol.py
import sys

class Program:
    def __init__(self, grid, robot):
        self.grid = grid
        self.robot = robot

    def interpret(self):
        self.robot.interpret(self.grid)

class Grid:
    def __init__(self, numberExpX, numberExpY):
        self.x = numberExpX.value
        self.y = numberExpY.value

class Robot:
    def __init__(self, bindings, start, statements):
        self.bindings = bindings
        self.start = start
        self.statements = statements

    def interpret(self, grid):
        try:
            self.start.interpret(self, grid)
        except Exception as e:
            print(f'ERROR: {e}')

        self.position = Position(self.start, grid)

        try:
            for binding in self.bindings:
                binding.interpret(self)
        except Exception as e:
            print(f'ERROR: {e}')

        try:
            for stmt in self.statements:
                stmt.interpret(self, grid)
        except Exception as e:
            print(f'ERROR: {e}')

class Position:
    def __init__(self, start, grid):
        self.x = start.x
        self.y = start.y
        self.grid = grid

        print(f'Grid: {grid.x}*{grid.y}\nStart: ({self.x} {self.y})')

    def move(self, direction):
        if (direction == "north"):
            self.moveUp()
        elif (direction == "south"):
            self.moveDown()
        elif (direction == "east"):
            self.moveRight()
        elif (direction == "west"):
            self.moveLeft()
        else:
            raise ValueError(f'Invalid direction: {direction}')

    def moveUp(self):
        if (self.y + 1 > self.grid.y):
            raise ValueError(f'Invalid move: Out of range (Attempted direction: north). Robots position can not exceed grid. \nFinal position: ({self.x},{self.y}) \nExiting...\n')
        else:
            self.y += 1

    def moveDown(self):
        if (self.y - 1 < 0):
            raise ValueError(f'Invalid move: Out of range (Attempted direction: south). Robots position can not exceed grid. \nFinal position: ({self.x},{self.y}) \nExiting...\n')
        else:
            self.y -= 1

    def moveRight(self):
        if (self.x + 1 > self.grid.x):
            raise ValueError(f'Invalid move: Out of range (Attempted direction: east). Robots position can not exceed grid. \nFinal position: ({self.x},{self.y}) \nExiting...\n')
        else:
            self.x += 1

    def moveLeft(self):
        if (self.x - 1 < 0):
            raise ValueError(f'Invalid move: Out of range (Attempted direction: west). Robots position can not exceed grid. \nFinal position: ({self.x},{self.y}) \nExiting...\n')
        else:
            self.x -= 1

class Binding:
    def __init__(self, identifier, exp):
        self.identifier = identifier.value
        self.exp = exp

    def interpret(self, robot):
        try:
            self.exp.interpret(robot)
        except Exception as e:
            print(f'ERROR: {e}')

        self.value = self.exp.value

    def assign(self, operator):
        if (operator == "++"):
            self.value += 1
        elif (operator == "--"):
            self.value -= 1
        else:
            pass

class Identifier:
    def __init__(self, string):
        self.value = string


class Statement:
    def __init__(self):
        pass

    def interpret(self, robot, grid):
        pass

class Start:
    def __init__(self, expX, expY):
        self.expX = expX
        self.expY = expY

    def interpret(self, robot, grid):
        try:
            self.expX.interpret(robot)
            self.expY.interpret(robot)
        except Exception as e:
            print(f'ERROR: {e}')

        self.x = self.expX.value
        self.y = self.expY.value

        if ( self.x < 0 or self.x > grid.x or self.y < 0 or self.y > grid.y ):
            raise ValueError(f'start {self.x} {self.y}: Start position must be within grid')

class Stop(Statement):
    def __init__(self):
        pass

    def interpret(self, robot, grid):
        print(f'The position is ({robot.position.x},{robot.position.y})')

class Move(Statement):
    def __init__(self, direction, exp):
        self.direction = direction.value
        self.exp = exp

    def interpret(self, robot, grid):
        try:
            self.exp.interpret(robot)
        except Exception as e:
            print(f'ERROR: {e}')

        self.value = self.exp.value

        for i in range(self.value):
            try:
                robot.position.move(self.direction)
            except Exception as e:
                print(f'ERROR: {e}')
                sys.exit()

class Direction:
    def __init__(self, str):
        if (str != "north" and str != "east" and str != "south" and str != "west") :
            raise ValueError(f'ERROR: {str} is not a valid direction. Must be "north, "east", "south" or "west"')
        self.value = str

class Assignment(Statement):
    def __init__(self, identifier, operation):
        self.identifier = identifier
        self.operation = operation

    def interpret(self, robot, grid):
        for binding in robot.bindings:
            if (self.identifier == binding.identifier):
                self.value = "assigned"
                if (self.operation == "++"):
                    binding.value += 1
                elif (self.operation == "--"):
                    binding.value -= 1
                else:
                    pass
        if (type(self.value) != str):
            raise NameError(f'{self.identifier} not found.')


class Loop(Statement):
    def __init__(self, until, *statements):
        self.statements = statements
        self.condition = until

    def interpret(self, robot, grid):
        try:
            self.condition.interpret(robot)
        except Exception as e:
            print(f'ERROR: {e}')

        try:
            while (self.condition.value == False):
                try:
                    for stmt in self.statements:
                        stmt.interpret(robot, grid)
                except Exception as e:
                        print(f'ERROR: {e}')
                        return
                try:
                    self.condition.interpret(robot)
                except Exception as e:
                    print(f'ERROR: {e}')
                    return
        except Exception as e:
            print(f'ERROR: {e}')


class Until:
    def __init__(self, booleanExp):
        self.booleanExp = booleanExp

    def interpret(self, robot):
        try:
            self.booleanExp.interpret(robot)
        except Exception as e:
            print(f'ERROR: {e}')

        self.value = self.booleanExp.value

class Exp:
    def __init__(self):
        pass

    def interpret(self, robot):
        pass

class IdExp(Exp):
    def __init__(self, identifier):
        self.identifier = identifier

    def interpret(self, robot):
        for binding in robot.bindings:
            if (self.identifier == binding.identifier):
                self.value = binding.value
                return
        if (type(self.value) != str):
            raise NameError(f'{self.identifier} not found.')

class NumberExp(Exp):
    def __init__(self, value):
        self.value = value

class BooleanExp(Exp):
    def __init__(self, operator, exp1, exp2):
        self.operator = operator
        self.exp1 = exp1
        self.exp2 = exp2

    def interpret(self, robot):
        try:
            self.exp1.interpret(robot)
            self.exp2.interpret(robot)
        except Exception as e:
            print(f'ERROR: {e}')

        if (self.operator.value == '<'):
            self.value = (self.exp1.value < self.exp2.value)
        elif (self.operator.value == '>'):
            self.value = (self.exp1.value > self.exp2.value)
        else:
            self.value = (self.exp1.value == self.exp2.value)

class BooleanOp:
    def __init__(self, operator):
        self.value = operator

class ArithmeticExp(Exp):
    def __init__(self, operator, args):
        self.operator = operator
        self.args = args

    def interpret(self, robot):
        self.args.interpret(robot)

        if (self.operator.value == '+'):
            self.value = 0
            for exp in self.args.exps:
                self.value += exp.value
        elif (self.operator.value == '-'):
            self.value = self.args.exps[0].value
            for exp in self.args.exps:
                if (exp != self.args.exps[0]):
                    self.value -= exp.value
        else:
            self.value = 1
            for exp in self.args.exps:
                self.value *= exp.value

class ArithmeticOp:
    def __init__(self, operator):
        self.value = operator

class Args:
    def __init__(self, *args):
        self.exps = args

    def interpret(self, robot):
        for exp in self.exps:
            try:
                exp.interpret(robot)
            except Exception as e:
                print(f'ERROR: {e}')
