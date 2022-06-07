from chapter10.p08 import find_duplicates
from io import StringIO


def test_find_duplicates():
    stream = StringIO("1\n2\n3\n4\n3\n4\n5\n")
    find_duplicates(stream)

