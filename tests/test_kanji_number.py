from io import StringIO
from contextlib import redirect_stdout
from kanji_number_sequence import special_number_sequence

def test_special_number_sequence():
    expected_output = """1
2
三
4
5
六
7
8
九
10
11
十二
13
十四
十五
16
17
十八
19
二十
二十一
二十二
二十三
二十四
二十五
二十六
二十七
二十八
二十九
三十
三十一
三十二
三十三
三十四
三十五
三十六
三十七
三十八
三十九"""

    captured_output = StringIO()
    with redirect_stdout(captured_output):
        special_number_sequence()

    print("Captured Output:")
    print(captured_output.getvalue())

    print("Expected Output:")
    print(expected_output)


    assert captured_output.getvalue().strip() == expected_output.strip()

