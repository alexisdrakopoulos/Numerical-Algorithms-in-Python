# Numerical Algorithms in Python

Numerical Algorithms written in Python3 (Interactivity/readability above functionality/efficiency)

These algorithms were written in order to be played with and for fun. Some are messier than others and some are unfinished. I think interactive algorithms can be very fun to both see how they operate and to see features such as convergence rates.

## Algorithms in this repository
- Newton's Method (With square root example)

  <a href="http://www.codecogs.com/eqnedit.php?latex=x_{n&plus;1}&space;=&space;x_n&space;&plus;&space;\frac{f(x_n)}{f'(x_n)}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?x_{n&plus;1}&space;=&space;x_n&space;&plus;&space;\frac{f(x_n)}{f'(x_n)}" title="x_{n+1} = x_n + \frac{f(x_n)}{f'(x_n)}" /></a>
- Forward Euler's Method (under linearmultistep) 

  <a href="http://www.codecogs.com/eqnedit.php?latex=y_{n&plus;1}&space;=&space;y_n&space;&plus;&space;hf(t_n,&space;y_n)" target="_blank"><img src="http://latex.codecogs.com/gif.latex?y_{n&plus;1}&space;=&space;y_n&space;&plus;&space;hf(t_n,&space;y_n)" title="y_{n+1} = y_n + hf(t_n, y_n)" /></a>
- Adam Bashforth 2-step Method (under linearmultistep)

  <a href="http://www.codecogs.com/eqnedit.php?latex=y_{n&plus;2}&space;=&space;y_{n&plus;1}&space;&plus;&space;\frac{3}{2}hf(t_{n&plus;1},&space;y_{n&plus;1})&space;-&space;\frac{1}{2}hf(t_n,&space;y_n)" target="_blank"><img src="http://latex.codecogs.com/gif.latex?y_{n&plus;2}&space;=&space;y_{n&plus;1}&space;&plus;&space;\frac{3}{2}hf(t_{n&plus;1},&space;y_{n&plus;1})&space;-&space;\frac{1}{2}hf(t_n,&space;y_n)" title="y_{n+2} = y_{n+1} + \frac{3}{2}hf(t_{n+1}, y_{n+1}) - \frac{1}{2}hf(t_n, y_n)" /></a>



The linearmultistep.py comes with a custom written parser for 1st order differential equations. You can feed it equations as inputs when running the script. The methods then use eval() to evaluate the output from the parser.

### Linear Multistep with Equation Parser

The file linearmultistep.py contains a parser that can parse equations of the form <a href="http://www.codecogs.com/eqnedit.php?latex=y&space;=&space;y'" target="_blank"><img src="http://latex.codecogs.com/gif.latex?y&space;=&space;y'" title="y = y'" /></a>, you have to have an equal sign, and the parser will use the right-hand side of the equation to perform the linear multistep methods.

![Linear Multistep Gif](https://github.com/alexisdrakopoulos/Numerical-Algorithms-in-Python/blob/master/gifs/linear_multistep.gif)

### Dependencies
Dependencies are fairly simple, these were written in python3.6. Check the imports for a proper list of dependencies.

### To Do List
- Re-write the linear methods and make a general structure for writing the Adam-Bashforth methods, also add Adam-Moulton
