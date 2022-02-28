"""
A collection of simple math operations

Methods define here
-------------------
simple_add(...)


simple_sub(...)


simple_mult(...)


simple_div(...)


simple_div(...)


poly_first(...)

    
def poly_second(...)

       
"""
 


def simple_add(a,b):
    '''
    simple_add(a,b)
    
    Parameters
    ----------
    a,b : float optional
    int,float or array_like int,float
    
    Returns 
    ------- 
    the sum of the input a,b 
    
    Examples
    --------
    >>> simple_math.simple_add(5,10)
    >>> 15
    
    '''
      
    return a+b

def simple_sub(a,b):
    '''    

    simple_sub(a,b) 
    
    Parameters
    ----------
    a,b : float optional
    int,float or array_like int,float
    
    Returns 
    ------- 
    the Substraction of the input a,b 

    Examples
    --------
    >>> simple_math.simple_sub(5,10)
    >>> -5

    '''
    
    return a-b

def simple_mult(a,b):
    '''
    simple_mult(a,b)  
    
    Parameters
    ----------
    a,b : float optional
    int,float or array_like int,float
    if a,b are array_like variables, the size should match
    
    Returns 
    ------- 
    the Multiplacation of the input a,b 
    
    Examples
    --------
    >>> simple_math.simple_mult(5,10)
    >>> 50
    
    '''
    
    return a*b

def simple_div(a,b):
    '''
    simple_div(a,b)   

    Parameters
    ----------
    a,b : float optional
    int,float or array_like int,float
    if a,b are array_like variables, the size should match
    
    Returns 
    ------- 
    the Division of the input a,b 
    
    Examples
    --------
    >>> simple_math.simple_div(5,10)
    >>> 0.5

    '''
    
    return a/b

def poly_first(x, a0, a1):
    '''
    poly_first(x, a0, a1)
    retuen the value of a1*x + a0  

    Parameters
    ----------
    a1,a0 : int,float optional
    x: int,float or array_like int,float
    Returns 
    ------- 
    the vlaue of linear polynominal a1*x + a0  
    Examples
    --------
    >>> simple_math.poly_first(5,10,15)
    >>> 85

    '''
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    '''
    poly_second(x, a0, a1, a2)

    retuen the value of a2*x**2 + a1*x + a0
    
    Parameters
    ----------
    a1,a1,a0 : int,float optional
    x: int,float or array_like int,float
    Returns 
    ------- 
    the vlaue of quadratic polynominal a2*x**2 + a1*x + a0 
    Examples
    --------
    >>> simple_math.poly_second(5,10,15,10)
    >>> 335

    '''
    
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
