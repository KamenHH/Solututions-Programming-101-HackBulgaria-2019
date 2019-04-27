def build_fraction(nominator, denominator):
    if denominator == 0:
        raise ZeroDivisionError("Error, denominator cannot be zero!")
    elif not isinstance(nominator, int) or not isinstance(denominator, int):
        raise ValueError('Error, denominator and numerator must be integers!')
    elif nominator == denominator:
        return (1, 1)
    else:
        return (nominator, denominator)


def GCD(nominator, denominator):
    dividend = nominator if nominator > denominator else denominator
    divisor = denominator if dividend == nominator else nominator
    while divisor != 0:
        temp = divisor
        divisor = dividend % divisor
        dividend = temp
    return dividend


def simplify_fraction(fraction):
    nominator, denominator = fraction
    gcd = GCD(nominator, denominator)
    if gcd != 1:
        return (nominator//gcd, denominator//gcd)
    else: 
        return fraction
 

def add_fractions(frac1, frac2):
    nom1, denom1 = frac1
    nom2, denom2 = frac2
    result_num = nom1*denom2 + nom2*denom1
    result_denom = denom1*denom2
    return simplify_fraction((result_num, result_denom))


def collect_fractions(fractions):
    from copy import deepcopy
    fract_copy = deepcopy(fractions)
    result = add_fractions(fract_copy.pop(0), fract_copy.pop(0))
    while fract_copy:
        result = add_fractions(result, fract_copy.pop(0))
    return result

def fraction_into_float(fraction):
    return fraction[0]/fraction[1]

def sort_fractions(fractions):
    # or use fraction_into_float
    return sorted(fractions, key=lambda result: result[0]/result[1])