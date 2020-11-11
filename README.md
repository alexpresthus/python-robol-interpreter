## Python Robol Interpreter

### About the project
This is a solution to an assignment asking for an interpreter for a custom language 'Robol' - a language giving a robot instructions on how to move on a grid.


### How to run

Run a set of test codes by running the main.py as a script:
```
python main.py <program>

<program>: 1 | 2 | 3 | 4 | all
  * Which test program to run.
```
where the parameter is the id of the test to run.


### The interpreter
Behaves like an AST, evaluating the given syntax based on the language grammar (See section The assignment -> ROBOL Grammar).
Located in ```Robol.py```

Non-terminals are classified as separate Python classes, with naming similar to the ROBOL Grammar notation specified in the assignment documentation. Similar non-terminals that share attributes and purpose (e.g. different types of expressions (number, identifier, Boolean etc.) all evaluate to some value), are divided into subclasses of a common super class (e.g. Exp is the parent class of NumberExp and BooleanExp).

Terminals are identified as symbols; Strings as a string in quotes; Symbols as a symbol in quotes; Numbers as an integer; Boolean values as a Boolean True or False.


### Test code

The test code defines a class TestCode which has methods for running some test programs. Each method has a set of commands. The commands simulate “parsed” commands, and calls relevant parts of the interpreter to instantiate the AST, then calls the interpret() method of the instance of the Program Class to start interpreting the AST.

### The abstract

Program is the top-level of the AST. Program is instantiated with an instance of Robot and Grid. Robot is instantiated with an instance of Start, a list of instances of Statements and a list of instances of Bindings.
The initial call on Program.interpret() starts the interpretation of the AST-instance, initializing a recursive descent:
Program.interpret() calls Robot.interpret(grid), which attempts to call the interpret-methods on Start, the bindings in the bindings-list, and the statements in the statement-list. Furthermore, bindings and statements are interpreted until non-terminal expressions are interpreted and evaluated, and actions are executed or errors are raised.

### Entry file (main.py

Checks that the given command is correct and executes relevant test code, or displays usage guidelines if command is invalid.


## The assignment:

<img src="./images/image--002.png" align="right">

# Mandatory Exercise 1 - IN3040

In this exercise, you are going to write a small interpreter for a simple language for controlling a robot on a 2-dimensional grid.
The language is called *ROBOL*, a clever acronym for *ROBOT LANGUAGE*, and its grammar is defined below.

The grid on which the robot can move about is defined by its x and y bounds, for instance:

![](./images/grid.png)

The grid above is defined by the bound (7, 6), and the robot is currently located at position (3, 3).
Moving the robot 1 step north would put it at (3, 4).
Moving it one step eastwould put it at (4, 3), etc.

## Assignment

Make an interpreter for the *ROBOL* language in your object-oriented language of choice.
The interpreter shall operate on an *abstract syntax tree (AST)* representing a *ROBOL* program.
You **do not** need to write a parser for the language (however, if you want to rise to the challenge, feel free!).
You can design the classes for the AST as you like, but they should provide a somewhat faithful representation of the grammar listed below.
The outermost element program from the grammar should be represented by a class `Program` that provides an `interpret` method which will interpret the entire program.

### Approved Languages
- Java
- C#
- Python
- Kotlin
- Scala
- JavaScript
- TypeScript
- C++

If you want to choose another language, please ask the *gruppelaerer*.

## Requirements
- The interpreter must check that the poor robot does not fall off the edge of the world (i.e., moves beyond the bounds of the grid).
- You can display the state of the program in any form you like during execution, but at minimum, the program should, upon termination, print its state in the form of the current location of the robot.
- There are some example programs below. You should check that your implementation returns the correct result after running these programs, and include instructions on how to run their AST representations with your implementation.
- Write a design document that explains how you have implemented the interpreter, and why you have done it in this way.
 Furthermore, the document should explain how to run your program from the Linux command line.
- It should be possible to use the program from the command line like this: `<ProgramName> 1|2|3|4|all`  
  **Example**: A Java program with the main method in a class called *Oblig1*  
  `java Oblig1 2` should run test code 2 and print the results.  
  `java Oblig1 all` should run all the 4 programs and print the results.  
  There is an implementation of this provided in the program sketch.

## Deliverables
- The entire programand the design document should be placed in a single `.zip` file
- The name of the file should be **IN3040_Mandatory1_\<username>.zip**
- The submission is done through Devilry: https://devilry.ifi.uio.no/
- **Deadline:** `24-09-20 23:59`

![](./images/image--004.png)

## ROBOL Grammar

Words in angle brackets (e.g. `<expression>`) denotes non-terminals, while symbols in quotes (e.g. `"+"`) denotes terminals in the grammar.

```ebnf
(* a program consists of a robot, and a grid on which it can move around *)
<program> ::= <grid> <robot> ;

(* size of the grid given as a bound for the x axis and the y axis.
   both axes start at 0, <number> is a positive integer. *)
<grid> ::= "size" "(" <number> "*" <number> ")" ;

(* the robot has a list of variable bindings, a starting point, and a
   a set of statements that control its movement *)
<robot> ::= <binding>* <start> <stmt>* ;

(* a variable binding consists of a name and an initial value *)
<binding> ::= "let" <identifier> "=" <exp> ;

(* statements control the robot's movement *)
<stmt> ::= <stop>
         | <move> <exp>
         | <assignment>
         | <loop> ;

(* start gives the initial position for the robot *)
<start> ::= "start" "(" <exp> "," <exp> ")" ;
<stop>  ::= "stop" ;

(* on the grid, moving north means up along the y axis, east means to the right
   along the x axis, etc. *)
<move> ::= "north" | "south" | "east" | "west" ;

<assignment> ::= <identifier> "++" | <identifier> "--" ;

(* a loop will keep executing statements until a condition is met *)
<loop>  ::= "do" "{" <stmt>* "}" <until> ;
<until> ::= "until" <boolean_exp> ;

(* expressions; number is an integer, identifier is a string of
   letters and numbers, starting with a letter *)
<exp> ::= <identifier>
        | <number>
        | "(" <exp> ")"
        | <arithmetic_exp>
        | <boolean_exp> ;

<boolean_exp>    ::= "(" <boolean_op> <exp> <exp> ")" ;
<boolean_op>     ::= "<" | ">" | "=" ;
<arithmetic_exp> ::= "(" <arithmetic_op> <args> ")" ;
<arithmetic_op>  ::= "+" | "-" | "*" ;

(* at least 2 arguments, but could be more *)
<args> ::= <exp> <exp>+ ;
```

### Hints:
- You may assume that expressions are type-correct (so you do not have to implement a type checker). You can assume that no
  one writes programs that tries to add booleans and numbers, for instance.
- It might simplify things if all expressions can calculate an integer value. Boolean expressions can, for instance, return 1 for true and 0 for false.
- The robot probably needs to have a reference to the grid, and the statements probably need to have a reference to the robot. This can be achieved in many ways, choose one that fits with your overall design.

## Example programs:

#### Testing Code 1: Simple Example

```c
size(64*64)
start(23,30)
west 15
south 15
east (+ 2 3)
north (+ 17 20)
stop
```

The result is (13,52)

#### Testing Code 2: Example with variables

```c
size(64*64)
let i = 5
let j = 3
start(23,6)
north (* 3 i)
east 15       
south (- 12 i j)       
west (+ (* 2 i) (* 3 j) 1)
stop
```
The result is (18,17)

#### Testing Code 3: Example with loop and assignment
```c
size(64*64)
let i = 5
let j = 3
start(23,6)
north (* 3 i)
west 15
east 4
do {
    south j
    j--
} until (< j 1)
stop
```

The result is (12, 15)

#### Testing Code 4: Example with movement over the edge

```c
size(64*64)
let i = 8
start(1,1)
do {
    north i
} until (> i 100)
stop
```

The result should be an error saying that the bounds of the grid have been overstepped.

## Program sketch
Below is a Java sketch of an implementation of the interpreter. You can use this as a starting point for your own implementation, if you like. You may also change all of these definitions if you think that is necessary.

```java
class Oblig1 {
    public static void main(String[] args) {
        TestCode testCode = new TestCode();
        switch (args.length > 0 ? args[0] : "") {
            case "1":
                testCode.runProgram1();
                return;
            case "2":
                testCode.runProgram2();
                return;
            case "3":
                testCode.runProgram3();
                return;
            case "4":
                testCode.runProgram4();
                return;
            case "all":
                testCode.runAll();
                return;
            default:
                System.out.println("USAGE: java Oblig1 1|2|3|4|all");
                return;
        }
    }
}
```

```java
class TestCode {

    // Create the AST based on testing code 1
    // This code is just to help you understand how to create an AST
    void runProgram1() {
        Grid grid = new Grid(new NumberExp(64), new NumberExp(64));
        Start start = new Start(new NumberExp(23), new NumberExp(30))
        statements.add(new Move(Direction.west, new NumberExp(15)));
        statements.add(new Move(Direction.south, new NumberExp(15)));
        Program program;
        // Fill in rest of the code

        // Run the interpreter
        program.interpret();
    }

    // same as runProgram1 but with the AST based on the other example programs
    void runProgram2() {}
    void runProgram3() {}
    void runProgram4() {}
    void runAll() {
        runProgram1();
        runProgram2();
        runProgram3();
        runProgram4();
    }
}
```

```java
interface Robol {
    void interpret();
}

class Program implements Robol {
    Grid grid;
    Robot robot;
    public Program(Grid grid, Robot robot) {
        this.grid = grid;
        this.robot = robot;
    }
    public void interpret() {
        robot.interpret();
    }
}

class Robot implements Robol {
    public void interpret() {
        // write interpreter code for the robot here
    }
}

abstract class Statement implements Robol {
    public abstract void interpret();
}

class Assignment extends Statement {
    public void interpret() {
        // write interpreter code here
    }
}

class Loop extends Statement {
    List<Statement> statements;
    BoolExp condition;
    public void interpret() {
        // write interpreter code here
    }
}

abstract class Expression { ... }

abstract class BoolExp extends Expression {
    protected Expression left;
    protected Expression right;
    ...
}
```

# Closing Notes

If you find any mistakes in this assignment, or you have any questions, please post an issue on https://github.uio.no/IN3040/H20/issues.

Good luck!
