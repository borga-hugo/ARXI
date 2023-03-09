import math

class Exercise8():

    def runTest(self, test):

        TESTS = {
            1 : TestExercise8(-1, False),
            2 : TestExercise8(0, True),
            3 : TestExercise8(3, False),
            4 : TestExercise8(4, True),
            5 : TestExercise8(25, True),
            6 : TestExercise8(26, False)
        }

        #test parameterization
        integer=TESTS[test].integer

        #execution of the function with the parameters of test
        result = Exercise8().run(integer)

        valid = True if TESTS[test].result == result else False
   
        print('EXERCISE 08 - TEST ',test,' => PASSED [', valid,']', 'integer:', TESTS[test].integer, ' => ', result)
        

    def run(self, integer):
        n = integer
        if n < 0:
            return False
        else:
            sqrtN = int(math.sqrt(n))
            return ((sqrtN*sqrtN)==n)

class TestExercise8:
    
    def __init__(self, integer, result):
        self.integer = integer
        self.result = result
    

