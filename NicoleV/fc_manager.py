def get_feature_type(feature_code):
    """ Given a feature code, return the feature type.
    """
    if feature_code == 1:
        return "point"
    elif feature_code == 2:
        return "polyline"
    elif feature_code ==3:
        return "polygon"
    else:
        return None
