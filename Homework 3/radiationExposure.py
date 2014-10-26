def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    # FILL IN YOUR CODE HERE...
    values= []
    i = start
    while abs(i - stop) > 1e-6:
        values.append(i)
        i+=step 
    areas = map(lambda x: f(x)*step, values)
    return reduce(lambda x, y: x + y, areas, 0)
    
def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)   