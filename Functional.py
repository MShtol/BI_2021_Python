def sequential_map(*args):
    """
    Returns list of values with sequential application of provided functions
    @ param values - list of needed values
    @ param funcs - tupple of applied functions
    @ return - processed list
    """    
    *funcs, values  = args
    func_chain()
    for func in funcs:
        values = [_ for _ in map(func,values)] 
    return values


def consensus_filter(*args):
    """
    Returns list of values with sequential filtrerion of provided  list by provided boolean functions
    @ param values - list of needed values
    @ param funcs - tupple of applied boolean functions
    @ return - filtered_list
    """ 
    *funcs, values  = args
    for func in funcs:
        values = [_ for _ in filter(func,values)] 
    return values


def conditional_reduce(bool_func,func,values):
    """
    Returns value calculated be reduce function analog from values that pass filter
    with multiple boolean functions.
    @ param bool_func - tupple of boolean functions
    @ param func - func to apply to list
    @ param values - list of values to be reduced
    @ return - result of reduction of filtered list
    """ 
    result, *values = [_ for _ in filter(bool_func,values)]
    for value in values:
        result = func(result, value)
    return result


def func_chain(*funcs):
    """
    Return function combined from a chain of multiple functions
    @ param funcs - tupple of functions
    @ return - combined function
    """ 
    def res_func(value):   
        for func in funcs:
            value = func(value)
        return value
    return res_func
