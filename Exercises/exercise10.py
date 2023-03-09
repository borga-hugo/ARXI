class Exercise10():

    def runTest(self, test):

        TESTS = {
            1 : TestExercise10('abcd', 'A-Bb-Ccc-Dddd'),
            2 : TestExercise10('RqaEzty', 'R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy'),
            3 : TestExercise10('cwAt','C-Ww-Aaa-Tttt')
            #add more test
        }

        #test parameterization
        input=TESTS[test].text
        
        #execution of the function with the parameters of test
        result = Exercise10().run(input)

        valid = True if TESTS[test].result == result else False

        print('EXERCISE 10 - TEST ',test,' => PASSED [', valid,']', 'text:', TESTS[test].text, ' => ', result)
        
    #takes a string as input 
    def run(self, input):
        standardformat=input.lower()

        #each character is repeated
        aux = {}
        for itInput in list(standardformat):
            if itInput not in aux:
                aux[itInput]=1
            else:
                aux[itInput] = aux[itInput]+1

        #The number of repetitions of a character should be equal to its position in the input string
        result = ''
        index = 0
        for itInput in list(standardformat):
            
            #The characters in the output string should be capitalized.
            result+=itInput.upper()
                
            i=1  
            while i <= index and index > 0:
                result+=itInput
                i+=1
            
            #separated by a hyphen (-). 
            result+='-'
            index+=1

        result=result[:-1]

        return result



class TestExercise10:
    
    def __init__(self, text, result):
        self.text = text
        self.result = result
    

