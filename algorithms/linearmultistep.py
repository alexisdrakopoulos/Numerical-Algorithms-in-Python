import re
import matplotlib.pyplot as plt
import numpy as np

# Equation parser

# examples of equations
equ1 = 'y\' = y'
equ2 = 'y\' = 5y'
equ3 = 'y\' = 17y'
equ4 = 'y\' = 17y + x'
equ5 = 'y\' = 29y + xy'
equ6 = 'y\' = 38y + 4xy - 7x'

# function attempt at parsing

def equ_parser(equation):

    # Check that equation is valid
    if '=' not in equation:
        raise ValueError('Your equation does not seem to have an = sign')

    # Get left and right parts of the equation
    left, right = equation.replace(' ', '').split('=')

    # Check order of the equation
    equ_order = left.count('\'')

    if equ_order == 0:
        raise ValueError('Your equation is not a differential, use \' to indicate order')

    if right.count('\'') == equ_order:
        raise ValueError('Left and right equations order is the same')

    # Get the function variable name chosen
    function_variable = left[left.find('\'')-1]

    # We have to detect exp() and trig functions now, will use np to eval

    # create a list with separated mathematical symbols
    symbols_detected = re.findall(r"pi|sin\([^)]*\)|exp\([^)]*\)|cos\([^)]*\)|tan\([^)]*\)|[+/-]|\*+|\d+\.?\d*|\w", right)


    maths_symbols = ['+', '-', '/', '*', '**']

    new_list = []
    
    variable = 'x'

    for prv, nxt in zip(symbols_detected, symbols_detected[1:]):
        new_list.append(prv)
        if nxt not in maths_symbols and prv not in maths_symbols:
            new_list.append('*')
    new_list.append(symbols_detected[-1])

    for idx, el in enumerate(new_list):
        if len(el) == 1:
            if el.isalpha() and el != 'y':
                variable = el
                new_list[idx] = 'x'
        temp_inner = ''
        if 'pi' in el:
            new_list[idx] = new_list[idx].replace('pi', 'np.pi')
        elif 'sin' in el:
            inner_variables = re.findall(r"\b(?!sin)\b\S+", new_list[idx])[0][1:-1]
            if len(inner_variables) >= 2:
                for i in inner_variables:
                    if i in maths_symbols:
                        temp_inner += i
                    else:
                        if i.isalpha() and i != 'y':
                            variable = i
                            temp_inner += 'x'
                        else:
                            temp_inner += i
                        temp_inner += '*'
                new_list[idx] = new_list[idx].replace(inner_variables, temp_inner[:-1])
            new_list[idx] = new_list[idx].replace('sin', 'np.sin')
        elif 'cos' in el:
            inner_variables = re.findall(r"\b(?!cos)\b\S+", new_list[idx])[0][1:-1]
            if len(inner_variables) >= 2:
                for i in inner_variables:
                    if i in maths_symbols:
                        temp_inner += i
                    else:
                        if i.isalpha() and i != 'y':
                            variable = i
                            temp_inner += 'x'
                        else:
                            temp_inner += i
                        temp_inner += '*'
                new_list[idx] = new_list[idx].replace(inner_variables, temp_inner[:-1])
            new_list[idx] = new_list[idx].replace('cos', 'np.cos')
        elif 'tan' in el:
            inner_variables = re.findall(r"\b(?!tan)\b\S+", new_list[idx])[0][1:-1]
            if len(inner_variables) >= 2:
                for i in inner_variables:
                    if i in maths_symbols:
                        temp_inner += i
                    else:
                        if i.isalpha() and i != 'y':
                            variable = i
                            temp_inner += 'x'
                        else:
                            temp_inner += i
                        temp_inner += '*'
                new_list[idx] = new_list[idx].replace(inner_variables, temp_inner[:-1])
            new_list[idx] = new_list[idx].replace('tan', 'np.tan')
        elif 'exp' in el:
            inner_variables = re.findall(r"\b(?!exp)\b\S+", new_list[idx])[0][1:-1]
            if len(inner_variables) >= 2:
                for i in inner_variables:
                    if i in maths_symbols:
                        temp_inner += i
                    else:
                        if i.isalpha() and i != 'y':
                            variable = i
                            temp_inner += 'x'
                        else:
                            temp_inner += i
                        temp_inner += '*'
                new_list[idx] = new_list[idx].replace(inner_variables, temp_inner[:-1])
            new_list[idx] = new_list[idx].replace('exp', 'np.exp')

    final_dict = {'main_var': function_variable,
                  'second_var': variable,
                  'equ_order': equ_order,
                  'formula': new_list}

    return final_dict

def eulers_method():
    """
    (Forward) Euler's method (Adam-bashforth 1)

    Args:
        initial_value: an initial guess y0
        formula: F(x,y) for Euler's method to compute
        step_size: the step size h
        steps: the number of steps the program will run

    Returns:
        a list of root estimates from step 1 -> step specified

    Raises:
        have not yet added errors this is for testing

    """
    
    print("""  Welcome to Adam-Bashforth Methods 1 and 2 in Python
            
          Tips:
              - use y' to denote derivative
              - keep left hand side simplified
              - tan, cos, sin, exp will only compute what is within brackets ()
              
          Enter VALUE of x not steps. So if you want x [0, 4] for y' = y you 
          would enter x = 4, step-size you like and the program computes the rest for you.
          
          Enjoy.
    
    """)
    
    
    
    while True:
        try:
            formula_raw = input('Write down your differential equation: ')
            formula_dict = equ_parser(formula_raw)
        except ValueError as inst:
            print(inst)
            continue
        break

    formula_list = formula_dict['formula']
    formula_str = ''.join(formula_list)

    while True:
        try:
            step_size_raw = input('Write down your step size h: ')
            step_size = float(step_size_raw)
        except ValueError:
            print('Not a valid step size')
            continue
        break
    while True:
        try:
            initial_value_raw = input('Write down your initial value y(0): ')
            y = float(initial_value_raw)
        except ValueError:
            print('Your initial value has to be a real number')
            continue
        break
    while True:
        try:
            steps_raw = input('Until what value of x: ')
            steps = int(float(steps_raw)/step_size)
        except ValueError:
            print('Steps has to be an integer number')
            continue
        break

    print('\n')
    print('Formula: ', str(formula_raw))
    print('I will run for', str(steps), 'steps at step size', str(step_size))
    confirmation_message = input('\nType yes to confirm, no to end program: ')
    
    if confirmation_message.lower() in ('no', 'n', 'stop', 'exit'):
        return print('You have selected to halt the program')
    
    method_choice = input('Type 1 for Euler\'s Method 1-step, or type 2 for Adam-Bashforth 2 step: ')
        
    x = 0
    
    try:
        number_of_decimals = len(str(step_size).split('.')[1])
    except IndexError:
        number_of_decimals = 0

    print('\n')
    print('Eulers Method Values:')
    print(str(round(y, 4)), 'for step 0 at x =', x)

    y_values = [y]
    x_values = [step_size*i for i in range(steps+int(method_choice))]
    
    if method_choice in '1':
        for i in range(steps):
            function = eval(formula_str)
            y = y + step_size * function
            x += step_size
            curr_step = str(i+1)
            print(str(round(y, 4)), 'for step', curr_step, 'at x =', round(x, number_of_decimals))
            y_values.append(y)
    
    elif method_choice in '2':
        print('Using Euler\'s Method for second initial value')
        function1 = eval(formula_str)
        y = y + step_size * function1
        x += step_size
        print(str(round(y, 4)), 'for step 1 at x =', round(x, number_of_decimals))
        y_values.append(y)
        
        for i in range(steps):
            function2 = eval(formula_str)
            y = y + 3/2 * step_size * function2 - 1/2 * step_size * function1
            function1 = function2
            x += step_size
            curr_step = str(i+2)
            print(str(round(y, 4)), 'for step', curr_step, 'at x =', round(x, number_of_decimals))
            y_values.append(y)
                        

    plt.plot(x_values, y_values)
    plt.ylabel('Estimates for y')
    plt.xlabel('x-values')
    plot_title = "Euler's Formula for " + str(formula_raw)
    plt.title(plot_title)
    plt.show()



eulers_method()
print('\n')
repeat_program_choice = input('Press enter to quit, or type again to go again: ')

if repeat_program_choice.lower() == 'again':
    eulers_method()
    print('\n')
    repeat_program_choice = input('Press enter to quit, or type again to go again: ')
