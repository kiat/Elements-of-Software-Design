

# Move Data operations into Numpy


# Use builtin functions and libraries

newlist = []
for word in oldlist:
    newlist.append(word.upper())


newlist = map(str.upper, oldlist)  # wiki cites map as a for loop moved into C code


# Reduce Memory Footprints

# # slow
#  inefficient because a new string gets created
msg = 'hello ' + my_var + ' world'

# faster
msg = 'hello %s world' % my_var

# or better:
msg = 'hello {} world'.format(my_var)



# Do only necessary things inside a loop

myfunc = myObj.func
fcor i in range(n):
    myfunc(i) # faster than myObj.func(i)


# List Comprehensive
# It is more about python style. It is not so much improving the performance.
newlist = []
for word in wordlist:
    newlist.append(word.upper())
A better way to write this code is:
newlist = list(map(str.upper, wordlist))




# Check your profile

# You can use a profiler, for example:

# python -m cProfile [-o output_file] [-s sort_order] myscript.py
#
