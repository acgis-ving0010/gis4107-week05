def is_point_in_box(x, y, xmin, ymin, xmax, ymax):
    if (xmin < x < xmax) and (ymin < y < ymax):
        return True
    else:
        return False
    