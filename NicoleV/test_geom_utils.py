import geom_utils as gu

XMIN = 2
XMAX = 4
YMIN = 2
YMAX = 4

def test_is_point_in_box_left_of_box():
    x = 1
    y = 3
    expected = False
    actual = gu.is_point_in_box(x, y, XMIN, YMIN, XMAX, YMAX)
    assert expected == actual

def test_is_point_in_box_on_left_edge():
    x=2
    y=3
    expected = False
    actual = gu.is_point_in_box(x, y, XMIN, YMIN, XMAX, YMAX)
    assert expected == actual

def test_is_point_in_box_above_box():
    x=3
    y=5
    expected = False
    actual = gu.is_point_in_box(x, y, XMIN, YMIN, XMAX, YMAX)
    assert expected == actual

def test_is_point_in_box_on_top_edge():
    x=3
    y=4
    expected = False
    actual = gu.is_point_in_box(x, y, XMIN, YMIN, XMAX, YMAX)
    assert expected == actual

def test_is_point_in_box_right_of_box():
    x=5
    y=3
    expected = False
    actual = gu.is_point_in_box(x, y, XMIN, YMIN, XMAX, YMAX)
    assert expected == actual

def test_is_point_in_box_on_right_edge():
    x=4
    y=3
    expected = False
    actual = gu.is_point_in_box(x, y, XMIN, YMIN, XMAX, YMAX)
    assert expected == actual

def test_is_point_in_box_below_box():
    x=3
    y=1
    expected = False
    actual = gu.is_point_in_box(x, y, XMIN, YMIN, XMAX, YMAX)
    assert expected == actual

def test_is_point_in_box_on_bottom_edge():
    x=3
    y=2
    expected = False
    actual = gu.is_point_in_box(x, y, XMIN, YMIN, XMAX, YMAX)
    assert expected == actual

def test_is_point_in_box_in_box():
    x=3
    y=3
    expected = True
    actual = gu.is_point_in_box(x, y, XMIN, YMIN, XMAX, YMAX)
    assert expected == actual

