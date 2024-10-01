def mod_myvar(var):
    """ Given a variable, determine which of the four conditions it meets, 
    and execute that condition's code.
    Condition 1: For a variable that has a remainder after division by two and the cubed value is not 27, add 4.
    Condition 2: For a variable that has a remainder after division by two and the cubed value is equal to 27, divide by 1.5.
    Condition 3: For a variable that does not have a remainder after division by two and is less than or equal to 10, multiply by 2. 
    Condition 4: For a variable that does not have a remainder after division by two and is more than 10, subtract 2. 
    """
    if var % 2:
        if var ** 3 != 27:
            var += 4           # Condition 1
        else:
            var /= 1.5         # Condition 2
    else:
        if var <= 10:
            var *= 2           # Condition 3
        else:
            var -= 2           # Condition 4
    return var