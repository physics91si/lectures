# coding: utf-8

# Gabriel Ehrlich
# Physics 91SI
# Spring 2015
# Lecture 9

# This looked like:
#
#     In [1]: cd ph91si
#
#     In [2]: cd lecture 9
#
#     In [3]: ls
#
# In other words, you can do a bunch of UNIX stuff straight in IPython.
get_ipython().magic(u'cd ph91si')
get_ipython().magic(u'cd lecture9')
get_ipython().system(u'ls -F --color ')

# Example of advanced OOP at use in a builtin!
# 'True' is a 'bool' object; 'bool' is sublassed from 'int'
True + 5

# Warm-up: coding bee. Here's the answer
class Weight:
    def __init__(self, mass):
        self.mass = mass
    def weight(self):
        return self.mass*9.8

# OPERATOR OVERLOADING
# Here the '+' operator is overloaded
l = []
m = [4]
l + m

# Using '+' essentially calls this
l.__add__(m)

# This module defines a class 'adder' that overloads __add__
import classes
a = classes.adder(57)
print "Value of a: %r" % a.d
print "What happens when we add a + 5:"
a + 5

# Another special method name we can overload: __str__
# Note how str objects overload the __mod__ special method
reload(classes)
print "Here is my object: %s" % a
str(a)

# We can use special method names to expose useful Python infrastructure
# Example: __getitem__ and slices. Define a 'slicer' classes that does
# nothing but return whatever was passed inside the brackets
l = classes.slicer()
l[3]
l["hi there"]
l[3:4]
l[::]
l[..., ...]

# INHERITANCE
# You can add lists together
l = [3,4,5]
m = [4,5]
l + m
# But you can't subtract them!
l - m

# So let's make a version of a list that's the same except you can also
# subract.
import newlist
l = newlist.NewList([3,4,5])
m = [4,5]
l - m

# Can still do everything else that lists do!
l + m

# AT LAST... a final example of infrastructure that IPython's tab completion
# can reveal: variables are stored in dicts. Modules, classes,  instances,
# and functions all have these.
newlist.__dict__
