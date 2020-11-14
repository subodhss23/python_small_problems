'''Create a function that accepts the pricipal p, the term in years t, the interest 
    rate r, and the number of compounding periods per year n, The function returns the
    value at the end of term rounded to the nearest cent.'''

def compound_interest(p, t, r, n):
    n_t = n * t
    return round(p * ( 1 + r / n ) ** n_t, 2)


print(compound_interest(100, 1, 0.05, 1))
print(compound_interest(3500, 15, 0.1, 4))
print(compound_interest(100000, 20, 0.15, 365))