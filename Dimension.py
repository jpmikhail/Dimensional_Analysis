import numpy as np
import copy

class Dimension:
    '''
        'values' is a vector of powers for each associated dimension. The
        identity of each dimension is left general. The length of 'values'
        depends on the number of dimensions being used. Powers can be any real
        number. E.g., [1, 1, 0] for Mass*Length and [0, 0, 1] for Time.
    '''
    def __init__(self, values):
        self.values = values
        
    def __str__(self): # print the values array
        return str(self.values)
        
    '''
    Boolean check for whether multiple Dimension instances have consistent
    dimensions, meaning their 'values' vectors are identical.
    
    e.g., Pressure and Stress have consistent dimensions.
    '''
    def consistent(*dims):
        result = True
        for i in range(1, len(dims)):
            if not np.array_equal(dims[0].values, dims[i].values):
                result = False
                break            
        return result

    '''
    Multiply multiple Dimension instances together, adding their powers for
    each dimension.
    
    e.g., Force = Mass*Acceleration
    '''
    def multiply(*dims):
        values = dims[0].values.copy()
        for i in range(1, len(dims)):
            values += dims[i].values
        return Dimension(values)
    
    '''
    Divide multiple Dimension instances, subtracting from the first instance
    the sum of powers for all subsequent instances.
    
    e.g., Acceleration = Length/Time/Time
    '''
    def divide(*dims): # dims[0]/dims[1]/dims[2]/...
        values = dims[0].values.copy()
        for i in range(1, len(dims)):
            values -= dims[i].values
        return Dimension(values)
    
    '''
    Add multiple Dimension instances together if they are consistent, not
    changing their powers and returning a copy of the first instance if
    successful.
    
    e.g., Length = Length + Length
    '''
    def add(*dims):
        if Dimension.consistent(*dims):
            return copy.deepcopy(dims[0])
        else:
            raise ValueError('Dimensions cannot be added.')
            
    def subtract(*dims):
        return Dimension.add(*dims) # same operation
    
    '''
    Raise a Dimension instance to a power by multiplying its 'values' vector
    by the given power.
    
    e.g., Area = Length**2
    '''
    def power(dim, n):
        return Dimension(dim.values * n)
    
    ## Operator overloading
    def __mul__(dim1, dim2):
        return dim1.multiply(dim2)
    
    def __truediv__(dim1, dim2):
        return dim1.divide(dim2)
    
    def __add__(dim1, dim2):
        return dim1.add(dim2)
    
    def __sub__(dim1, dim2):
        return dim1.subtract(dim2)
    
    def __pow__(dim, n):
        return dim.power(n)
    
    ## Comparison overloading
    def __eq__(dim1, dim2):
        return dim1.consistent(dim2)
    
    def __ne__(dim1, dim2):
        return not dim1.consistent(dim2)