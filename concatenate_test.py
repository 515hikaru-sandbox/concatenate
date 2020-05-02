"""
testing
"""

import pytest

from concatenate import concat, preprocess


def test_concat_string():
    base = ""
    strings = ["foo\n", "bar\n"]
    expected = "foo\nbar\n"
    actual = concat(base, strings)
    assert actual == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [(["foo\n"], ["　foo\n"]), (["bar\n", "boo\n", "\n", "boo\n"], ["　bar\n", "　boo\n", "\n", "　boo\n"])]
)
def test_preprocess(test_input, expected):
    results = preprocess(test_input)
    for result, exp in zip(results, expected):
        assert result == exp
