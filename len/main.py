#!/usr/bin/env python3
#
# Prints the lengths of all lines in a file.  For example:
#
#
#   $ len -s $(fd -t f) |tail -1
#   78:     Returns a lazy generator of lines without trailing newline characters from
#
# The length of a line is the number of codepoints, not bytes or grapheme
# clusters.  For example, len('á') == 1, but len('á') == 2.
#
# TODO
# - Traverse directories recursively
# - Recognize and exclude binary files
# - Prefix output with file names

from argparse import ArgumentParser
from sys import stdin

def chomp_file(file):
    with open(file) as istream:
        for line in chomp_lines(istream):
            yield line
        

def chomp_files(files):
    for file in files:
        for line in chomp_file(file):
            yield line


def chomp_lines(istream):
    """
    Returns a lazy generator of lines without trailing newline characters from
    the specified input stream.
    """
    return (line.rstrip('\n\r') for line in istream)


def main():
    args = parse_args()
    lines = chomp_files(args.files) if args.files else chomp_lines(stdin)
    if args.s:
        lines = sorted(lines, key=len)
    print_lines(lines)


def parse_args():
    parser = ArgumentParser(
            description='Print line lengths.',
            usage='%(prog)s [-h] [-s] [FILE...]')
    parser.add_argument(
            '-s',
            action='store_true',
            help='sort lines by increasing length')
    parser.add_argument(
            'files',
            help='file(s) to parse instead of stdin',
            metavar='FILE',
            nargs='*')
    return parser.parse_args()


def print_lines(lines):
    for line in lines:
        print(len(line), line, sep=': ')


if __name__ == '__main__':
    main()
