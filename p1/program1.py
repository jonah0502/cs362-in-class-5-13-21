def isPal(myString):
    # Program to check if a string is palindrome or not
    my_str = myString

    # make it suitable for caseless comparison
    my_str = my_str.lower()

    # reverse the string
    rev_str = reversed(my_str)

    # check if the string is equal to its reverse
    if list(my_str) == list(rev_str):
        return True
    else:
        return False


