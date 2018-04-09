def is_leap_year(year):
    while (year % 4 == 0):
        if (year % 100 != 0):
            #print ('True')
            return True
        elif (year % 400 != 0):
            #print ('False')
            return False
        elif (year % 400 == 0):
            #print ('True')
            return True
        break
    return False
