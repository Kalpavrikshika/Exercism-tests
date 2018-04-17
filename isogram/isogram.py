def is_isogram(string):
    '''if the length of the string if the same as the
    unique elements in the string(set(string)
    is an isogram'''
    if type(string) != str:
        raise TypeError ('Argument not a string')
    elif string == "":
        return True
    elif (string, str) and len(string) != 0:
        string = string.lower()
        if "-" in string:
            string_new=string.replace('-', '')
            if len(string_new) == len(set(string_new)): 
                return True
            else:
                 return False
            
            
        elif ' ' in string:
            string_new = string.replace(" ", "")
            if len(string_new) == len(set(string_new)):
                return True
            else:
                return False
                

        elif len(string) == len(set(string)):
            return True
        else:
            return False  
is_isogram("")   #true 
is_isogram("isogram") #true
is_isogram("eleven") #false
is_isogram("subdermatoglyphic") #true
is_isogram("Alphabet") #false'''
is_isogram("thumbscrew-japingly") #true
is_isogram("six-year-old")
is_isogram("Emily Jung Schwartzkopf") #true
is_isogram("accentor") #false
is_isogram("Aleph Bot Chap") #false '''

