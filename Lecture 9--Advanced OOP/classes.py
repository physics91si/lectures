# Gabriel Ehrlich
# Physics 91SI
# Spring 2015
# Lecture 9

class adder(object):
    def __init__(self, d):
        self.d = d
    def __repr__(self):
        return str(self.d)
    def __add__(self, other):
        print "You told me to add %r and %r!" % (self.d, other)
        return self.d + other

class slicer(object):
    def __getitem__(self, key):
        return key
