import modvar as mv

def test_modvar_condition1():
    var = 1 
    expected = 5
    actual = mv.mod_myvar(var)
    assert expected == actual

def test_modvar_condition2():
    var = 3
    expected = 2
    actual = mv.mod_myvar(var)
    assert expected == actual

def test_modvar_condition3():
    var = 2
    expected = 4
    actual = mv.mod_myvar(var)
    assert expected == actual

def test_modvar_condition4():
    var = 12
    expected = 10
    actual = mv.mod_myvar(var)
    assert expected == actual