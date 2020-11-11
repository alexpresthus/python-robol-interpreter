import sys
from testCode import TestCode

if len(sys.argv) != 2:
    raise ArgumentError('Invalid number of arguments. USAGE: python main.py 1 | 2 | 3 | 4 | all')

testCode = TestCode()
program = sys.argv[1]

if (program == "1"):
    testCode.runProgram1()
elif (program == "2"):
    testCode.runProgram2()
elif (program == "3"):
    testCode.runProgram3()
elif (program == "4"):
    testCode.runProgram4()
elif (program == "all"):
    testCode.runAll()
else:
    raise ValueError('USAGE: python Oblig1.py 1 | 2 | 3 | 4 | all')
