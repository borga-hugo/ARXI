import Helper.general as helper

class Exercise1():

    def runTest(self, test):

        TESTS = {
            1 : TestExercise1('xyaabbbccccdefww', 'xxxxyyyyabklmopq', 'abcdefklmopqwxy'),
            2 : TestExercise1('abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz')
            #add more test
        }

        #test parameterization
        s1=TESTS[test].s1
        s2=TESTS[test].s2

        #execution of the function with the parameters of test
        result = Exercise1().run(s1,s2)

        valid = True if TESTS[test].result == result else False

        print('EXERCISE 01 - TEST ',test,' => PASSED [', valid,']', 's1:', TESTS[test].s1, ' s2', TESTS[test].s2, ' => ', result)
        
    #that takes in two strings, s1 and s2
    def run(self, s1, s2):
        
        auxString=s1+s2

        #containing only letters from 'a' to 'z'
        if not helper.Helper().onlyLettersFromaToz(auxString):
            raise Exception("Only Letters from 'a' to 'z'")

        #other away but is in this case dont validate case
        #if not auxString.isalpha():
            #raise Exception("Only Letters from 'a' to 'z'")

        #containing distinct letters
        lst = []
        for letter in auxString:
            if letter not in lst: lst.append(letter)

        #alphabetical order 
        lst.sort()
        result = ''.join([str(elem) for elem in lst])

        #return a new string
        return result


class TestExercise1:
    
    def __init__(self, s1, s2, result):
        self.s1 = s1
        self.s2 = s2
        self.result = result
