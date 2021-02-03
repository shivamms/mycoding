import functions as func#

print(func.argstodic(name="subbu",age=50))

print(func.concatlist([1,2,3],[4,5,6],[7,8,9]))

print(func.firstlast([14,2,4]))

print(func.double_the_args("subbu", 87, 74, "maya"))

#assume inputs are numbers and may be more than one
print(func.two_times_all_args(1,4,7,8))

print(func.args_to_list("rt", 9, 3,"sf"))

print(func.kwargs_to_dic(a=933, b="jdhfd", c=90, l=3323))

print(func.is_there_empty_list([1,2,3,4],[],[234]))

print(func.func2())
func3 = func.func2()
print(func3())

print(func.list_to_tuple([1,2,3,4,5]))

# here built-in object is being passed
print(func.name_of_object(object))

func.print_decimals(0,10,0.1,1)

