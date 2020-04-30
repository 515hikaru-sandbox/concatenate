"""
package for concatenate text files
"""

from pathlib import Path
from typing import Iterable, Generator

import click

EXCEPT_HEAD = ['[', '「', '（', '　']

def concat(base_str: str, add_strs: Iterable[str]) -> str:
    """concat string and return new string
    """
    return base_str + "".join(add_strs)


def preprocess(strs: Iterable[str]) -> Generator[str, None, None]:
    """全角の挿入
    """
    for string in strs:
        try:
            if len(string) == 0:
                yield string
            if string[0] in EXCEPT_HEAD:
                yield string
            else:
                yield '　' + string
        except StopIteration:
            return


@click.command()
@click.argument("target")
def main(target):
    """main"""
    targets = Path(target).glob("*.txt")
    text = ""
    for file in sorted(targets):
        abs_path = file.absolute()
        with open(abs_path) as f:
            lines = f.readlines()
            process_lines = preprocess(lines)
            text = concat(text, process_lines)
            text += '[newpage]'
    print(text[:-10])


if __name__ == "__main__":
    main()
