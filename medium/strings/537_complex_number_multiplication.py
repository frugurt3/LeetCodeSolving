def complex_number_multiply(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    Note: a and b input in form 'a+bi', output - the same.
    """
    # Split numbers to real and imagine parts without "i".
    ra, ia = a[:-1].split("+")
    rb, ib = b[:-1].split("+")

    # Convert all parts to integer.
    ra, rb = int(ra), int(rb)
    ia, ib = int(ia), int(ib)

    # Return result with formula of multiply for complex numbers.
    return "{}+{}i".format((ra * rb) - (ia * ib), (ra * ib) + (ia * rb))
