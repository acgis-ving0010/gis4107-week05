def mod_myvar(var):
    
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