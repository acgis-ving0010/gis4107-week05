import countdown as c

def test_get_countdown_for_no_arg():
    expected = "10 9 8 7 6 5 4 3 2 1 0"
    actual = c.get_countdown_as_text_using_for()
    assert expected == actual

def test_get_countdown_for_arg():
    var = 5
    expected = "5 4 3 2 1 0"
    actual = c.get_countdown_as_text_using_for(5)
    assert expected == actual

def test_get_countdown_while_no_arg():
    expected = "10 9 8 7 6 5 4 3 2 1 0"
    actual = c.get_countdown_as_text_using_while()
    assert expected == actual

def test_get_countdown_while_arg():
    var = 5
    expected = "5 4 3 2 1 0"
    actual = c.get_countdown_as_text_using_while(5)
    assert expected == actual