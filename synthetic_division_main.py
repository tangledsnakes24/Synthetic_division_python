import math
#first gather the user input of the polynomial 
poly_unproc = input("Enter the polynomial you wish to find the zeros of: ")

#strip out the numbers to factor for possible divisors
def strip_divisors(poly_unprotec:str):
    if poly_unproc[0] == "-":
        first_num_unproc = poly_unproc[0:2]
    else: 
        first_num_unproc = poly_unproc[0]
        

    last_num_unproc = poly_unproc[-2:]
    return(first_num_unproc, last_num_unproc)

def get_factors(n):
    factors = set()
    # Only iterate up to the square root of n
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)       # Add the small factor
            factors.add(n // i)  # Add its matching large pair
            
    return sorted(list(factors))
#get a list of factors for the first and last number
factors_first = get_factors(first_num_unproc)
factors_last = get_factors(last_num_unproc)