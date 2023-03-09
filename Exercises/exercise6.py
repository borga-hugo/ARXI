class Exercise6():

    def runTest(self, test):

        TESTS = {
            1 : TestExercise6("din", '((('),
            2 : TestExercise6("recede", '()()()'),
            3 : TestExercise6("Success", ')())())'),
            4 : TestExercise6("(( @", '))((')
            #add more test
        }

        #test parameterization
        input=TESTS[test].text

        #execution of the function with the parameters of test
        result = Exercise6().run(input)

        valid = True if TESTS[test].result == result else False

        print('EXERCISE 06 - TEST ',test,' => PASSED [', valid,']', 'text:', TESTS[test].text, ' => ', result)
        

    def run(self, input):
        standardformat = input

        #The case of the characters should be ignored.
        standardformat = list(map(lambda x: x.lower(), standardformat))

        aux = {}
        for itInput in standardformat:
            if itInput not in aux:
                aux[itInput]=1
            else:
                aux[itInput] = aux[itInput]+1

        result = ''
        for itInput in list(standardformat):
            #represented by "(" if it appears only once 
            if aux[itInput] == 1:
                    result+='('
            #")" if it appears more than once
            else:
                result+=')'

        #The output string should contain only "(" and ")" characters.
        return result



class TestExercise6:
    
    def __init__(self, text, result):
        self.text = text
        self.result = result
    

