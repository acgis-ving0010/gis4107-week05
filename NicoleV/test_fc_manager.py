import fc_manager as fcman

def test_get_feature_type_point():
    point = 1
    expected = "point"
    actual = fcman.get_feature_type(point)
    assert expected == actual

def test_get_feature_type_polyline():
    polyline = 2
    expected = "polyline"
    actual = fcman.get_feature_type(polyline)
    assert expected == actual

def test_get_feature_type_polygon():
    polygon = 3
    expected = "polygon"
    actual = fcman.get_feature_type(polygon)
    assert expected == actual

def test_get_feature_type_none():
    other = 123
    expected = None
    actual = fcman.get_feature_type(other)
    assert expected == actual