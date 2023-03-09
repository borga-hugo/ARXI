import Helper.general as helper

class Exercise5():

    def runTest(self, test):

        TESTS = {
            1 : TestExercise5("The sunset sets at twelve o'clock.", '20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11'),
            #add more test
        }

        #test parameterization
        input=TESTS[test].text

        #execution of the function with the parameters of test
        result = Exercise5().run(input)

        valid = True if TESTS[test].result == result else False

        print('EXERCISE 05 - TEST ',test,' => PASSED [', valid,']', 'text:', TESTS[test].text, ' => ', result)
        

    def run(self, input):
        englishAlphabet=helper.Helper().englishAlphabet

        standardformat = input
        standardformat = list(map(lambda x: x.lower(), standardformat))
        auxStandardformat = list(standardformat)

        auxx = ''
        for itAuxStandardformat in auxStandardformat:
            try:
                #replace every letter in a given string with its position in the alphabet
                #For example, the letter "a" should be replaced with "1"
                a = englishAlphabet.index(itAuxStandardformat[0])+1
                auxx+= str(a) + ' '
            except:
                #If the string contains any non-letter characters, ignore them and do not include them in the output
                continue
        auxx = auxx[:-1]
        result = auxx
        return result


class TestExercise5:
    
    def __init__(self, text, result):
        self.text = text
        self.result = result
    

