import Helper.general as helper

class Exercise7():

    def runTest(self, test):

        TESTS = {
            1 : TestExercise7(89,1,1),
            2 : TestExercise7(92,1,-1),
            3 : TestExercise7(695,2,2),
            4 : TestExercise7(46288,3,51)
            #add more test
        }

        #test parameterization
        n=TESTS[test].n
        p=TESTS[test].p

        #execution of the function with the parameters of test
        result = Exercise7().run(n,p)

        valid = True if TESTS[test].result == result else False

        print('EXERCISE 07 - TEST ',test,' => PASSED [', valid,']', 'n:', TESTS[test].n, 'p:', TESTS[test].p, ' => ', result)
        

    def run(self, n,p):
        
        #default value (error)
        result = -1

        #The input integers n and p will always be strictly positive.
        if not helper.Helper().intPositive(n) or not helper.Helper().intPositive(p):
            raise Exception("The input integers n and p will always be strictly positive.")
            
        auxN=str(n)
        auxN = list(map(lambda x: int(x), auxN))

        #the sum of the digits of a given positive integer n, taken to successive powers of p
        aux = []
        for it in auxN:
            aux.append(pow(it, p))
            p+=1
        sumPow = sum(aux)

        #is equal to k times n.
        k = 0
        x = n*k
        while x <= sumPow:
            k += 1
            x = n*k
            if sumPow == x:
                result = k

        return result


class TestExercise7:
    
    def __init__(self, n, p, result):
        self.n = n
        self.p = p
        self.result = result
    

