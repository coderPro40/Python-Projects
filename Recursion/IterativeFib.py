"""
Name: ThankGod Ofurum
Function: compute values in fibonacci secquence using
iterative loop
"""
def fib(n):
    #Instance variables
    a = 0
    b = 1
    #iterative loop
    for i in range(0, n):
        current = a
        a = b
        b = current + b
    return a

        
