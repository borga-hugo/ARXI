class Exercise9():

    def runTest(self, test):

        TESTS = {
            1 : TestExercise9([1, 1, 1], 5, [1, 1, 1, 3, 5]),
            2 : TestExercise9([0, 0, 1], 5,[0, 0, 1, 1, 2])
            #add more test
        }

        #test parameterization
        signature=TESTS[test].signature
        n=TESTS[test].n

        #execution of the function with the parameters of test
        result = Exercise9().run(signature,n)

        valid = True if TESTS[test].result == result else False

        print('EXERCISE 09 - TEST ',test,' => PASSED [', valid,']', 'signature:', TESTS[test].signature, 'n:', TESTS[test].n, ' => ', result)
        

    def run(self, signature, n):

        #The input signature will always contain 3 integers. (no validation needed)
        #The input n will always be a non-negative integer. (no validation needed)

        #If n is 0, the function should return an empty array 
        if n==0:
            return[]

        aux = signature

        #control var because signature will always contain 3 integers
        i=3

        while i<n:
            value = aux[-1]+ aux[-2] + aux[-3]
            aux.append(value)
            i+=1
        result = aux
        return result


class TestExercise9:
    
    def __init__(self, signature, n, result):
        self.signature = signature
        self.n = n
        self.result = result
    

