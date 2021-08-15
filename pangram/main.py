#!/usr/bin/env python3

from dataclasses import dataclass

import argparse
import sys
from typing import Callable, Set

DEFAULT_MIN_LENGTH = 4
DEFAULT_WORDS_FILE = "/usr/share/dict/words"


@dataclass
class Command:
    mandatory_letters: Set[str]
    available_letters: Set[str]
    min_length: int
    words_file: str


def parse_args() -> Command:
    parser = argparse.ArgumentParser(description="Find Spelling Bee answers.")
    parser.add_argument(
        "-m",
        "--min-length",
        default=DEFAULT_MIN_LENGTH,
        help="omit words shorter than N characters",
        metavar="N",
        type=int,
    )
    parser.add_argument(
        "letters",
        help="available letters, capitalized if manadatory",
        type=str,
    )
    parser.add_argument(
        "words_file",
        default=DEFAULT_WORDS_FILE,
        help="available words, one per line",
        metavar="words-file",
        nargs="?",
        type=str,
    )
    args = parser.parse_args()
    return Command(
        mandatory_letters=set(c.lower() for c in args.letters if c.isupper()),
        available_letters=set(args.letters.lower()),
        min_length=args.min_length,
        words_file=args.words_file,
    )


def make_validator(command: Command) -> Callable[[str], bool]:
    def is_valid_char(c: str) -> bool:
        return c in command.available_letters or not c.isalpha()

    def is_valid_word(word: str) -> bool:
        return (
            len(word) >= command.min_length
            and all(c in word for c in command.mandatory_letters)
            and all(map(is_valid_char, word))
        )

    return is_valid_word


def main() -> None:
    command = parse_args()
    with open(command.words_file) as lines:
        words = tuple(line.strip() for line in lines)

    is_valid_word = make_validator(command)
    valid_words = sorted(filter(is_valid_word, words), key=len)
    for word in valid_words:
        is_pangram = all(c in word for c in command.available_letters)
        prefix = " *" if is_pangram else "  "
        print(prefix, word)


if __name__ == "__main__":
    main()
