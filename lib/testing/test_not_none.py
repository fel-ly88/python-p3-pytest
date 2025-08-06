#!/usr/bin/env python3

from not_none_functions import return_not_none

# def test_return_not_none():
#     '''in not_none_functions, function "return_not_none" returns a value that is not None.'''
#     assert False

def test_function_returns_not_none():
    '''Your function should return a value that is not None.'''
    assert your_function_name() is not None
    
def your_function_name():
    return "something"