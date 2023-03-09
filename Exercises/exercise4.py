import sys
import Helper.general as helper

class Exercise4():

    def runTest(self, test):

        TESTS = {
            1 : TestExercise4(['a', 'b', 'c', 'd', 'f'], 'e'),
            2 : TestExercise4(['O', 'Q', 'R', 'S'] , 'P'),
            3 : TestExercise4(["a", "b", "c", "d", "f"] , 'e'),
            4 : TestExercise4(["O", "Q", "R", "S"] , 'P')
            #add more test
        }

        #test parameterization
        input=TESTS[test].letters

        #execution of the function with the parameters of test
        result = Exercise4().run(input)

        valid = True if TESTS[test].result == result else False

        print('EXERCISE 04 - TEST ',test,' => PASSED [', valid,']', 'letters:', TESTS[test].letters, ' => ', result)
        
    #Write a method that takes an array of consecutive (increasing) letters as input 
    def run(self, input):

        if not helper.Helper().validArraySize(input, 2, sys.maxsize):
            raise Exception("The length of the array will always be at least 2")

        englishAlphabet=helper.Helper().englishAlphabet

        standardformat = input.copy()
        #[standardformat.lower() for x in standardformat]
        standardformat = list(map(lambda x: x.lower(), standardformat))
        startIndex = englishAlphabet.index(standardformat[0])

        aux = -1
        #You will always receive a valid array and it will always be missing exactly one letter. 
        #The length of the array will always be at least 2
        for index, itEnglishAlphabet in enumerate(englishAlphabet[startIndex:]):
            if itEnglishAlphabet!=standardformat[index]:
                aux = itEnglishAlphabet
                break
        
        #The array will always contain letters in only one case.
        aux = aux if input[0].islower() else aux.upper()
        result=aux

        #returns the missing letter in the array
        return result


class TestExercise4:
    
    def __init__(self, letters, result):
        self.letters = letters
        self.result = result
    

