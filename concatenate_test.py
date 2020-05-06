"""
testing
"""

import pytest

from concatenate import concat, preprocess, insert_newpage, trim_end_newpage


def test_concat_string():
    """文字列と文字列の配列を連結する
    """
    base = ""
    strings = ["foo\n", "bar\n"]
    expected = "foo\nbar\n"
    actual = concat(base, strings)
    assert actual == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (["foo\n"], ["　foo\n"]),
        (["bar\n", "boo\n", "\n", "boo\n"], ["　bar\n", "　boo\n", "\n", "　boo\n"]),
        (["「こんにちは」\n"], ["「こんにちは」\n"]),
        (["……それはない\n"], ["……それはない\n"]),
    ]
)
def test_preprocess(test_input, expected):
    """全角空けのテスト
    """
    results = preprocess(test_input)
    for result, exp in zip(results, expected):
        assert result == exp


def test_insert_newpage():
    """newpage トークンの挿入
    """
    test_input = "foo\n"
    result = insert_newpage(test_input)
    expected = 'foo\n[newpage]\n'
    assert result == expected

@pytest.mark.parametrize(
    "test_input,expected",
    [("　foo\n[newpage]\n", "　foo\n"), ("foo\n", "foo\n")]
)
def test_trim_end_newpage(test_input, expected):
    result = trim_end_newpage(test_input)
    assert result == expected
