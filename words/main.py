#!/usr/bin/env python3
#
# Prints the number of alphanumeric words in stdin or specified files.
# Markdown links are heuristically recognized and removed automatically.

import re
import sys

from typing import Iterable

# We care only about links that include whitespace, thus affecting word count.
# Such links are generally either inline:   [text]( http://... )
# Or on separate lines, like footnotes:     [tag]: http://...
LINK_RE = re.compile('(?:]\([^)]*)|(?:^\[.*]:.*)')


def is_word(s: str) -> bool:
    """Return true if s contains any alphanumeric characters."""
    return any(c.isalnum() for c in s)


def count_words(line: str) -> int:
    """Return the number of words in the specified line. """
    return sum(1 for s in line.split() if is_word(s))


def count_markdown_words(lines: Iterable[str]) -> int:
    """
    Return the total number of words on all of the specified lines, excluding
    (most) Markdown links.
    """
    # Python's re.sub method, unlike equivalent functions in other mainstream
    # languages, and unlike Python's own str.replace, expects the replacement
    # text before the subject text. 🤦  The type system can't catch incorrect
    # ordering, even at runtime, because both parameters are strings.
    return sum(count_words(LINK_RE.sub('', line)) for line in lines)


def main():
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            with open(arg) as lines:
                total = count_markdown_words(lines)
            print('{:8}        {}'.format(total, arg))
    else:
        print(count_markdown_words(sys.stdin))


if __name__ == '__main__':
    main()
