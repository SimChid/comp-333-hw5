"""
COMP-333
Unit tests for given functions from unit_testing_sample_code.py
Simon Chidley & Aaron Foote
"""
## The following functions come from unit_testing_sample_code.py provided in the assignment
# COMP 333 Software Engineering
# Wesleyan University
# Alex Kaplan (akaplan01@wesleyan.edu) and Sebastian Zimmeck (szimmeck@wesleyan.edu)

"""
Capitalizes the first and last character of a string.
"""
def string_capitalizer(tobecapitalized):
    if tobecapitalized == "":
        return tobecapitalized
    i = 0
    try:
        tbclist = [*tobecapitalized]
        while i < (len(tbclist)):
            if i == 0 or i == (len(tbclist) - 1):
                tbclist[i] = tbclist[i].upper()
            i = i + 1
        tobecapitalized = ''.join(tbclist)
        return tobecapitalized
    except:
        # If failure, return the input as is.
        return tobecapitalized

"""
Capitalizes the first and last character of a string in a list of strings.
"""
def capitalize_list(slist):
    i = 0
    while i < len(slist):
        current_string = slist[i]
        slist[i] = string_capitalizer(current_string)
        i = i + 1
    return slist

"""
Squares, doubles, and then floor divides (by 3) an integer, in that order.
"""
def integer_manipulator(n):
    try:
        n = ((n*n)*2)//3
        return n
    except:
        # If failure, return the input as is.
        return n

"""
Squares, doubles, and then floor divides (by 3) an integer, in that order, in a
list of integers.
"""
def manipulate_list(intlist):
    i = 0
    while i < len(intlist):
        intlist[i] = integer_manipulator(intlist[i])
        i = i + 1
    return intlist

## The following functions are test functions to the above functions.

# Testing string functions
# n: string, s: string, tst: string --> None
def test_string(n,s,tst):
    if s == tst:
        print("Test {} passed! '{}' matches '{}'.".format(n,tst,s))
    else:
        print("Test {} failed. Expected:'{}'. got:'{}'.".format(n,s,tst))

# Testing string list functions
# n: string, sl: string list, tstl: string list --> None
def test_strlist(n,sl,tstl):
    print("Test {}:".format(n))
    for i in range(len(sl)):
        if sl[i] == tstl[i]:
            print("Test {} passed! '{}' matches '{}'.".format(i,tstl[i],sl[i]))
        else:
            print("Test {} failed. Expected: '{}'. Got '{}'.".format(i,sl[i],tstl[i]))

# Testing int functions 
# n: string, num: int, tst: int --> None
def test_int(n,num,tst):
    if num == tst:
        print("Test {} passed! '{}' matches '{}'.".format(n,tst,num))
    else:
        print("Test {} failed. Expected: '{}'. Got: '{}'.".format(n,num,tst))

# Testing int list function
# n: string, numl: int list, tstl: int list --> None
def test_intlist(n,numl,tstl):
    print("Test {}:".format(n))
    for i in range(len(numl)):
        if numl[i] == tstl[i]:
            print("Test {} passed! '{}' matches '{}'.".format(n,tstl[i],numl[i]))
        else:
            print("Test {} failed. Expected: '{}'. Got: '{}'.".format(n,numl[i],tstl[i]))

#Run all tests with 'python3 unit_testing.py' in command line.
print("\nString Capitalizer Tests:")
test_string("0", "TwO", string_capitalizer("two"))
test_string("1", "C", string_capitalizer("c"))
test_string("2", "FouR", string_capitalizer(4))
test_string("3", "", string_capitalizer(""))

print("\nList Capitalizer Tests:")
test_strlist("0", ["TwO","C","FouR",""], capitalize_list(["two","c",4,""]))

print("\nInteger Manipulator Tests:")
test_int("0", 66, integer_manipulator(10))
test_int("1", 2, integer_manipulator(2))
test_int("2", 6, integer_manipulator(3))
test_int("3", 0, integer_manipulator(0))
test_int("4", 1, integer_manipulator("three"))

print("\nManipulate List Tests:")
test_intlist("0", [66,2,6,0,1], manipulate_list([10,2,3,0,"three"]))
