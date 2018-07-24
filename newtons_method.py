# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 17:23:10 2018

@author: alexi
"""

def function(x):
    """
    Write down your function for Newton's method, such as f(x) = x**2 - 16
    """
    return x**2 - 125
    
def derivative(x):
    """
    Write down your derivative for Newton's method, such as f'(x) = 2x
    """
    return 2*x


def newtons_method(function, derivative, initial_value):
    """
    This is the function that performs Newton's Method
    
    Return:
        No real return, prints values at each step for interactivity. 
        Can easily be changed to return a single value and remove the last print statement.
    """
    
    guess = initial_value
    
    # Use this to define how accurate our value will be
    epsilon = 0.001
    
    # Record steps:
    step = 0
    
    # Record dictionary, you could return the dictionary if you like and make some plots.
    step_dict = {}
    
    while True:
        new_guess = guess - function(guess)/derivative(guess)
        step += 1
        
        # Recording in steps
        step_dict[step] = new_guess
        
        
        if abs(new_guess-guess) < epsilon:
            return print(f'At step {step} your value is {round(new_guess,len(str(epsilon)))}')
        guess = new_guess

        print(f'At step {step} your value is {round(new_guess,len(str(epsilon)))}')



