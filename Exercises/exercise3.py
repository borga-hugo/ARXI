import Helper.general as helper

class Exercise3():

    def runTest(self, test):

        TESTS = {
            1 : TestExercise3([0, 0, 0, 1], 1),
            2 : TestExercise3([0, 0, 1, 0], 2),
            3 : TestExercise3([0, 1, 0, 1], 5),
            4 : TestExercise3([1, 0, 0, 1], 9),
            5 : TestExercise3([0, 0, 1, 0], 2),
            6 : TestExercise3([0, 1, 1, 0], 6),
            7 : TestExercise3([1, 1, 1, 1], 15),
            8 : TestExercise3([1, 0, 1, 1], 11)
            #add more test
        }

        #test parameterization
        binaryString=TESTS[test].integers
        
        #execution of the function with the parameters of test
        result = Exercise3().run(binaryString)

        valid = True if TESTS[test].result == result else False

        print('EXERCISE 03 - TEST ',test,' => PASSED [', valid,']', 'binary array:', TESTS[test].integers, ' => ', result)
        
    #Write a function that takes in an array of ones and zeroes
    def run(self, binaryString):

        #takes in an array of ones and zeroes
        if not helper.Helper().validBinaryArray(binaryString):
            raise Exception("Just ones and zeroes")

        #The input array can have varying lengths, not just limited to 4
        #and converts the equivalent binary value to an integer
        binaryString.reverse()
        aux = []
        for index, item in enumerate(binaryString):
            aux.append(item*pow(2, index))

        result = sum(aux)
        return result


class TestExercise3:
    
    def __init__(self, integers, result):
        self.integers = integers
        self.result = result
    
