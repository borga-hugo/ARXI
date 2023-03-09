import Helper.general as helper

class Exercise2():

    def runTest(self, test):

        TESTS = {
            1 : TestExercise2([1,2,3,4,3,2,1], 3),
            2 : TestExercise2([1,100,50,-51,1,1], 1),
            3 : TestExercise2([20, 10, -80, 10, 10, 15, 35], 0)
            #add more test
        }

        #test parameterization
        integers=TESTS[test].integers

        #execution of the function with the parameters of test
        result = Exercise2().run(integers)

        valid = True if TESTS[test].result == result else False

        print('EXERCISE 02 - TEST ',test,' => PASSED [', valid,']', 'integers:', TESTS[test].integers, ' => ', result)
        

    #Write a function that takes in an array of integers 
    def run(self, integers):

        #The input array may have length 0 < arr < 1000 and may contain any integer values, positive or negative.
        if not helper.Helper().validArraySize(integers, 0, 1000):
            raise Exception("The input array may have length 0 < arr < 1000")

        #If no such index exists, the function should return -1
        n=-1
        for pointer in range((len(integers)-1)):
            auxinput = integers.copy()
            del auxinput[pointer]

            #left of N
            left=auxinput[:pointer]
            #right of N
            right=auxinput[pointer:]

            #sum of the integers
            sumLeft = sum(left)
            sumRight = sum(right)
            
            #such that the sum of the integers to the left of N 
            #is equal to the sum of the integers to the right of N
            #The function should return the lowest index in case of multiple valid answers (first find fisrt return)
            if sumLeft == sumRight:
                n = pointer
                break

        return n


class TestExercise2:
    
    def __init__(self, integers, result):
        self.integers = integers
        self.result = result
    

