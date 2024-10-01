import excel_utils as eu

def test_excel():
    """Testing create_cell_refs function.
    """
    columns = "A B"
    rows = "1 2"
    expected = "A1,A2,B1,B2"
    actual = eu.create_cell_refs(columns, rows)
    assert expected == actual