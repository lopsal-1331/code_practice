'''
First challenge
'''

# imports
import numpy as np 

def jacobian(f, x): 
    '''
    f - vectorial function that recieves an array of size n and returns
        an array of size m 
    
    x - evaluation point (array of size n)

    RETURNS - a jacobian matrix m · n 
    '''
    epsilon = 1e-5
    x = np.array(x,dtype=float) # aseguramos array numpy

    f0 = f(x) 
    m = len(f0)
    n = len(x)

    J = np.zeros((m,n))

    for j in range(n): # recorremos cada una de las variable s
        x_forward = x.copy()
        x_backward = x.copy()

        x_forward[j] += epsilon 
        x_backward[j] -= epsilon 

        f_forward = f(x_forward)
        f_backward = f(x_backward)

        # realizamos la derivada parcial para cada componente de f respecto a x_j 
        J[:,j] = (f_forward-f_backward) / (2*epsilon)

    return J 


def f(state): 
    '''
    recieves an array of size n and returns an array of size m 
    '''
    x = state[0]
    y = state[1]

    return np.array(
        [x**2 + y, np.sin(x)+y**3]
    )

state = np.array([1.0, 2.0])
result = f(state)
J = jacobian(f=f, x=state)
print(J)