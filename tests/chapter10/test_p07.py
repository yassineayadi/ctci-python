from chapter10.p07 import Reader, find_missing_int


def test_reader():
    large_integer_file = "chapter10/large_integer_file.txt"
    reader = Reader(large_integer_file)
    assert reader.read_chunk()[0] == '1'

def test_find_missing_int():
    large_integer_file = "chapter10/large_integer_file.txt"
    missing_int = find_missing_int(large_integer_file)
    assert missing_int == 17