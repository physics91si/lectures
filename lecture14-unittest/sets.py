class Set(list):

    #creates a Set with the given list of values
    def __init__(self, input_list):
        data_list = []
        for num in input_list:
            if num not in data_list:
                data_list.append(num)
        self.data = data_list

    #prints the data in the set in a list format 
    def __str__(self):
        return "%s" %self.data
        
    #returns True is the set contains the given number    
    def contains(self, num):
        return num in self.data
    
    #adds a new element num to a set if it is not already in the set
    def add(self, num):
        if num not in self.data:
            self.data.append(num)
            
    #removes the given num from the set if it is present
    #it not, throws an exception
    def remove(self, num):
        try: 
            self.data.remove(num)
        except ValueError as e:
            print(e.args)
    
    #returns the size of the set         
    def size(self):
        return len(self.data)
    
    #returns a Set that is a union of the set with another set
    def __or__(self, other):
        union = []
        for num in self.data:
            if num not in union:
                union.append(num)
        for num in other.data:
            if num not in union:
                union.append(num)
        return Set(union)

    #returns a Set that is the intersection of the set with another set
    def __and__(self, other):
        intersection = []
        for num in self.data:
            if num in other.data and num not in intersection:
                intersection.append(num)
        return Set(intersection)
    
    #returns a Set of elements in the first set but not the second
    def __sub__(self, other):
        difference = self.data
        for num in difference:
            if num in other.data:
                difference.remove(num)
        return Set(difference)
    