"""
COMP-333
Unit tests for given frunctions with use of pytest
Simon Chidley & Aaron Foote
"""

import pytest

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

## Run all tests with 'pytest' in the terminal. More instructions in the README.md

def test_cap_0():
    assert "TwO" == string_capitalizer("two")
def test_cap_1():
    assert "C" == string_capitalizer("c")
def test_cap_2():
    assert "FouR" == string_capitalizer(4)
def test_cap_3():
    assert "" == string_capitalizer("")

def test_cap_list():
    str_l = ["TwO","C","FouR",""]
    tst_l = capitalize_list(["two","c",4,""])
    for i in range(4):
        assert str_l[i] == tst_l[i]

def test_int_manip_0():
    assert 66 == integer_manipulator(10)
def test_int_manip_1():
    assert 2 == integer_manipulator(2)
def test_int_manip_2():
    assert 6 == integer_manipulator(3)
def test_int_manip_3():
    assert 0 == integer_manipulator(0)
def test_int_manip_4():
    assert 1 == integer_manipulator("three")

def test_int_manip_list():
    assert [66,2,6,0,1] == manipulate_list([10,2,3,0,"three"])