#!/usr/bin/env python3

from dataclasses import dataclass

import sys
from typing import Set

DEFAULT_MIN_LENGTH = 4
DEFAULT_WORDS_FILE = "/usr/share/dict/words"


@dataclass
class Command:
    mandatory_letter: str
    available_letters: Set[str]
    words_file: str


def parse_args(args) -> Command:
    if len(args) not in (1, 2):
        print("Usage: pangram <letters> [words-file]", file=sys.stderr)
        sys.exit(1)
    letters = args[0]
    return Command(
        mandatory_letter=letters[0],
        available_letters=set(letters),
        words_file=args[1] if len(args) == 2 else DEFAULT_WORDS_FILE,
    )


def make_validator(mandatory_letter, available_letters):
    def is_valid_char(c) -> bool:
        return c in available_letters or not c.isalpha()

    def is_valid_word(word) -> bool:
        return (
            len(word) >= DEFAULT_MIN_LENGTH
            and mandatory_letter in word
            and all(map(is_valid_char, word))
        )

    return is_valid_word


def main():
    command = parse_args(sys.argv[1:])
    with open(command.words_file) as lines:
        words = tuple(line.strip() for line in lines)

    is_valid_word = make_validator(
        command.mandatory_letter, command.available_letters
    )

    valid_words = sorted(filter(is_valid_word, words), key=len)

    for word in valid_words:
        if all(c in word for c in command.available_letters):
            print(' *', word)
        else:
            print('  ', word)


if __name__ == "__main__":
    main()
