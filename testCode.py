from Robol import *

class TestCode:
    def __init__(self):
        pass

    def runProgram1(self):
        grid = Grid(NumberExp(64), NumberExp(64))
        bindings = []
        start = Start(NumberExp(23), NumberExp(30))
        statements = []
        statements.append(Move(Direction("west"), NumberExp(15)))
        statements.append(Move(Direction("south"), NumberExp(15)))
        statements.append(Move(Direction("east"), ArithmeticExp(ArithmeticOp("+"), Args(NumberExp(2), NumberExp(3)))))
        statements.append(Move(Direction("north"), ArithmeticExp(ArithmeticOp("+"), Args(NumberExp(17), NumberExp(20)))))
        statements.append(Stop())

        robot = Robot(bindings, start, statements)
        program = Program(grid, robot)

        print('\n*** Program 1 ***\nSTART\n')
        program.interpret()
        print('\nEND\n')

    def runProgram2(self):
        grid = Grid(NumberExp(64), NumberExp(64))
        bindings = []
        bindings.append(Binding(Identifier("i"), NumberExp(5)))
        bindings.append(Binding(Identifier("j"), NumberExp(3)))
        start = Start(NumberExp(23), NumberExp(6))
        statements = []
        statements.append(Move(Direction("north"), ArithmeticExp(ArithmeticOp("*"), Args(NumberExp(3), IdExp("i")))))
        statements.append(Move(Direction("east"), NumberExp(15)))
        statements.append(Move(Direction("south"), ArithmeticExp(ArithmeticOp("-"), Args(NumberExp(12), IdExp("i"), IdExp("j")))))
        statements.append(Move(Direction("west"), ArithmeticExp(ArithmeticOp("+"), Args( ArithmeticExp(ArithmeticOp("*"), Args(NumberExp(2), IdExp("i"))), ArithmeticExp(ArithmeticOp("*"), Args(NumberExp(3), IdExp("j"))), NumberExp(1)))))
        statements.append(Stop())

        robot = Robot(bindings, start, statements)
        program = Program(grid, robot)

        print('\n*** Program 2 ***\nSTART\n')
        program.interpret()
        print('\nEND\n')

    def runProgram3(self):
        grid = Grid(NumberExp(64), NumberExp(64))
        bindings = []
        bindings.append(Binding(Identifier("i"), NumberExp(5)))
        bindings.append(Binding(Identifier("j"), NumberExp(3)))
        start = Start(NumberExp(23), NumberExp(6))
        statements = []
        statements.append(Move(Direction("north"), ArithmeticExp(ArithmeticOp("*"), Args(NumberExp(3), IdExp("i")))))
        statements.append(Move(Direction("west"), NumberExp(15)))
        statements.append(Move(Direction("east"), NumberExp(4)))
        statements.append(Loop(Until(BooleanExp(BooleanOp("<"), IdExp("j"), NumberExp(1))), Move(Direction("south"), IdExp("j")), Assignment("j", "--")))
        statements.append(Stop())

        robot = Robot(bindings, start, statements)
        program = Program(grid, robot)

        print('\n*** Program 3 ***\nSTART\n')
        program.interpret()
        print('\nEND\n')

    def runProgram4(self):
        grid = Grid(NumberExp(64), NumberExp(64))
        bindings = []
        bindings.append(Binding(Identifier("i"), NumberExp(8)))
        start = Start(NumberExp(1), NumberExp(1))
        statements = []
        statements.append(Loop(Until(BooleanExp(BooleanOp(">"), IdExp("i"), NumberExp(100))), Move(Direction("north"), IdExp("i"))))
        statements.append(Stop())

        robot = Robot(bindings, start, statements)
        program = Program(grid, robot)

        print('\n*** Program 4 ***\nSTART\n')
        program.interpret()
        print('\nEND\n')

    def runAll(self):
        self.runProgram1()
        self.runProgram2()
        self.runProgram3()
        self.runProgram4()
