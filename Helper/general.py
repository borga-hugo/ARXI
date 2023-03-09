class Helper():

    englishAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def onlyLettersFromaToz(self, string):

        ENGLISHALPHABETATOZLOWERCASESTRING='abcdefghijklmnopqrstuvwxyz'

        for x in list(string):
            #find function is case sensitive
            #index function is not case sensitive
            index=ENGLISHALPHABETATOZLOWERCASESTRING.find(x)
            if index==-1:
                return False
        return True

    def validArraySize(self, array, min, max):
        size = len(array)
        if min < size and size < max:
            return True
        return False
    
    def validBinaryArray(self, array):
        VALID_NUMBERS=[0,1]
        for x in array:
            try:
                index=VALID_NUMBERS.index(x)
            except:
                return False
        return True
    
    def intPositive(self, value):
        if type(value) == int and value > 0:
            return True
        return False