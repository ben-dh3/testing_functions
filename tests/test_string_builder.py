from lib.string_builder import *

def test_string_builder():
    string_builder = StringBuilder()
    string_builder.add("hello")
    size_result = string_builder.size()
    assert size_result == 5
    output_result = string_builder.output()
    assert output_result == "hello"