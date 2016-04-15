# Gabriel Ehrlich
# Physics 91SI
# Spring 2015
# Lecture 9

class NewList(list):
    def __sub__(a, b):
        l = []
        for elem in a:
            if elem not in b: l.append(elem)

        return l
