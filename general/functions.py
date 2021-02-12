def argstodic(**kwargs):
    return {x:y for x,y in kwargs.items()}

def concatlist(*args):
    outlist = []
    for arg in args:
        outlist = outlist+arg 
    return outlist

def nonemptylist(*args):
    for arg in args:
        if not len(arg):
            return False
    return True

def firstlast(lst):
  return lst[0], lst[-1]

def double_the_args(*args):
  return args * 2

#assume inputs are numbers and may be more than one
def two_times_all_args(*args):
  return [x*2 for x in args]

# the parameters in *args are passed as tuple
def args_to_list(*args):
  return list(args)

# the key=value arguments in **kwargs are stored in dictionary
def kwargs_to_dic(**kwargs):
  return kwargs

# take unknown number of lists as argument and return True if there is no empty list otherwise return False
def is_there_empty_list(*args):
  return all(args)

#returning a function which is already defined
def func1():
  return "inside func1"

def func2():
  return func1

def list_to_tuple(lst):
  return tuple(lst)

def name_of_object(object):
  return object.__name__

# print decimal numbers with desired number of places
def print_decimals(start,end,interval, places):
  while(start <= end):
    print(round(start,places))
    start += interval

def def is_square(n):  
    if n >= 0 and (n ** (1/2)).is_integer():
        return True
    return False