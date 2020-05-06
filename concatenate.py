"""
package for concatenate text files
"""

from pathlib import Path
from typing import Iterable, Generator

import click

__version__ = '0.9.2'

EXCEPT_HEAD = ['[', '「', '（', '　', '\n', '…']

def concat(base_str: str, add_strs: Iterable[str]) -> str:
    """concat string and return new string
    """
    return base_str + "".join(add_strs)


def preprocess(strs: Iterable[str]) -> Generator[str, None, None]:
    """全角の挿入
    """
    for string in strs:
        try:
            if string[0] in EXCEPT_HEAD:
                yield string
            else:
                yield '　' + string
        except StopIteration:
            return

def insert_newpage(string: str) -> str:
    return string + '[newpage]\n'

def trim_end_newpage(string: str) -> str:
    if not string.endswith('[newpage]\n'):
        return string
    return string[:-10]



@click.command()
@click.argument("target")
@click.version_option(__version__, prog_name='concatenate')
def main(target):
    """ターゲットディレクトリ配下のテキストファイルに適当な前処理を施してファイルを連結する
    """
    targets = Path(target).glob("*.txt")
    text = ""
    for file in sorted(targets):
        abs_path = file.absolute()
        with open(abs_path) as f:
            lines = f.readlines()
            process_lines = preprocess(lines)
            text = concat(text, process_lines)
            text = insert_newpage(text)
    print(trim_end_newpage(text))


if __name__ == "__main__":
    main()
