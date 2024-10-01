import seqmod as sm
TESTSEQ = 'ABCD'

def test_mod_sequence_noskip_notrunc():
    expected = 'ABCD'
    actual = sm.mod_sequence(TESTSEQ)
    assert expected == actual

def test_mod_sequence_skip0_notrunc():
    expected = 'BCD'
    actual = sm.mod_sequence(TESTSEQ, 0)
    assert expected == actual

def test_mod_sequence_skip1_notrunc():
    expected = 'ACD'
    actual = sm.mod_sequence(TESTSEQ, 1)
    assert expected == actual

def test_mod_sequence_skip1_trunc2():
    expected = 'A'
    actual = sm.mod_sequence(TESTSEQ, 1, 2)
    assert expected == actual

def test_mod_sequence_skip2_trunc2():
    expected = 'AB'
    actual = sm.mod_sequence(TESTSEQ, 2, 2)
    assert expected == actual

def test_mod_sequence_skip3_trunc2():
    expected = 'AB'
    actual = sm.mod_sequence(TESTSEQ, 3, 2)
    assert expected == actual

def test_mod_sequence_skip4_notrunc():
    expected = 'ABCD'
    actual = sm.mod_sequence(TESTSEQ, 4)
    assert expected == actual

def test_mod_sequence_noskip_trunc4():
    expected = 'ABCD'
    actual = sm.mod_sequence(TESTSEQ, truncate_index=4)
    assert expected == actual

def test_mod_sequence_skip1_trunc4():
    expected = 'ACD'
    actual = sm.mod_sequence(TESTSEQ, 1, 4)
    assert expected == actual