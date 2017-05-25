"""
Name: ThankGod Ofurum
Function: compute values in fibonacci secquence using
recursive loop
"""
def rfib(n):
    #base case
    if n <= 1:
        return n
    #Recursive case
    else:
        return rfib(n-1) + rfib(n-2)
