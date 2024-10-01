def create_cell_refs(columns, rows):
    """Given lists of space-delimited column and row identifiers,
    generate a comma-delimited list of Excel cell references by column.

    Args:
        columns (string): A space-delimited list of column identifiers, 
        in capital letters. For example, "A B". 
        rows (string): A space-delimited list of row identifiers, in 
        numbers. For example, "1 2"

    Returns:
        string: A comma-delimited list of Excel cell references by column.
    """
    ref_list = []
    for c in columns.split():
        for r in rows.split():
            cell_ref = f'{c}{r}'
            ref_list.append(cell_ref)
    ref_comma_dl = ','.join(e for e in ref_list)
    return ref_comma_dl