#!/usr/bin/env python3
#
# Replaces ordinary quotation marks with smart quotes.
#
# ## Quality
# TODO: Add formal test suite
# TODO: Rewrite in Rust
#
# ### Bugs
# TODO: Correctly support quote followed by punctuation (')' or '—')
#
# ## Features
# TODO: Support -i flag to process files in-place.

import re
import sys

# The look-behind for single close quotes lets us use them as apostrophes.
SINGLE_CLOSE = re.compile(r"(?<=\S)'|'(?=\s|$)")
SINGLE_OPEN = re.compile(r"'(?=\S)")

DOUBLE_CLOSE = re.compile(r'"(?=\s|$)')
DOUBLE_OPEN = re.compile(r'"(?=\S)')

def smarten(line):
    line = SINGLE_OPEN.sub('‘', SINGLE_CLOSE.sub('’', line))
    line = DOUBLE_OPEN.sub('“', DOUBLE_CLOSE.sub('”', line))
    return line

def print_smart(lines):
    for line in lines:
        print(smarten(line), end='')


def main():
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            with open(arg) as lines:
                print_smart(lines)
    else:
        print_smart(sys.stdin)


if __name__ == '__main__':
    main()
