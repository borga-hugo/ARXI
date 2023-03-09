import Helper.general as helper

class Exercise11():

    def runTest(self, test):

        TESTS = {
            1 : TestExercise10('The quick brown fox jumps over the lazy dog', True),
            2 : TestExercise10('The quick brown fox jumps over the lazy cat', False)
            #add more test
        }

        #test parameterization
        input=TESTS[test].text

        #execution of the function with the parameters of test
        result = Exercise11().run(input)

        valid = True if TESTS[test].result == result else False

        print('EXERCISE 11 - TEST ',test,' => PASSED [', valid,']', 'text:', TESTS[test].text, ' => ', result)
        
    #that takes a string as input 
    #The input string will only contain letters from a-z and A-Z.
    def run(self, input):

        englishAlphabet=helper.Helper().englishAlphabet
        standardformat=input.lower()
        count=0
        aux=list(input)

        #returns a boolean (i return string bool to encapsulate on test structure)
        result=True
        for x in englishAlphabet:
            try:
                z = aux.index(x)

            #The function should ignore numbers, punctuation, and the case of the letters.
            except:
                #returns a boolean (i return string bool to encapsulate on test structure)
                return False
        return result



class TestExercise10:
    
    def __init__(self, text, result):
        self.text = text
        self.result = result
    

