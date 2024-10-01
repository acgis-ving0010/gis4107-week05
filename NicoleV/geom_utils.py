def is_point_in_box(x, y, xmin, ymin, xmax, ymax):
    """ Given a point x,y and the dimensions of a box xmin, ymin, xmax, ymax, 
    determine if point is inside the box. 
    """
    if (xmin < x < xmax) and (ymin < y < ymax):
        return True
    else:
        return False
    