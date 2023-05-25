def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """

    if a > b:
        print("first number is greater")
    elif a < b:
        print("second number is greater"):
    else:
        print("numbers are equal")
    
    
        