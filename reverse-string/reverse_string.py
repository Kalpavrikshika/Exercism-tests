
def reverse(input):
    
    #reverse as string
    return input[::-1]

#An alternative approach I wass using - string to list
    '''myinput = input
    mylist = list(myinput)
    #print (mylist)
    mylist.reverse()
    return (mylist)'''

    '''while True:
        if input == None:
            print (None)
            break
        else:
    #find length of list
    l=len(mylist)-1
    #while loop to reverse
    while l >= 0:
        print (mylist[l])
        l -= 1
#actual reverse function happens here
    
    #return(mylist)
    #not working: '' input and '' puctuated sentence.'''

reverse(input = 'robot')
reverse(input = 'Ramen')
reverse(input = 'I\'m hungry!')
reverse(input = 'racecar')



