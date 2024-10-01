
def get_countdown_as_text_using_for(start_value=10):
    """Given a start_value, default is 10, return a space delimited string
       containing numbers descending from start_value to 0 using a for loop
    """
    countdown_list = []
    for i in range(start_value+1):
        value = start_value - i
        countdown_list.append(value)
    countdown_string = ' '.join(str(v) for v in countdown_list)
    return countdown_string

def get_countdown_as_text_using_while(start_value=10):
    """Given a start_value, default is 10, return a space delimited string
       containing numbers descending from start_value to 0 using a while loop
    """
    countdown_list = []
    i = start_value
    while i >= 0:
        countdown_list.append(i)
        i -= 1
    countdown_string = ' '.join(str(v) for v in countdown_list)
    return countdown_string