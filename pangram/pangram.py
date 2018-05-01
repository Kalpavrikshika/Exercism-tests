def is_pangram(sentence):
    """Check whether 'str' contains ALL of the chars in set'"""
    set = 'abcdefghijklmnopqrstuvwxyz' 
    sentence = sentence.lower()
    for c in set:
        if c not in sentence:
            return False
            
    else:
        return True
is_pangram('')
is_pangram('abcdefghijklmnopqrstuvwxyz')
is_pangram('the_quick_brown_fox_jumps_over_the_lazy_dog')
is_pangram('a quick movement of the enemy will '
                       'jeopardize five gunboats')
is_pangram('five boxing wizards jump quickly at it')
is_pangram('the_quick_brown_fox_jumps_over_the_lazy_dog'),
is_pangram('the 1 quick brown fox jumps over the 2 lazy dogs')
is_pangram('7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog')
is_pangram('Five quacking Zephyrs jolt my wax bed')
is_pangram('the quick brown fox jumped over the lazy FX')



