#!/usr/bin/env python3
#
# Prints line lengths from stdin or specified files.

from argparse import ArgumentParser
from itertools import islice
from os import walk
from os.path import isdir, join
from sys import stderr, stdin

def chomp_dir(dir):
    for d, _, fs in walk(dir):
        yield from chomp_files(join(d, f) for f in fs)


# TODO: Inject warning log, or return monads.
def chomp_file(file):
    with open(file) as istream:
        try:
            for line in chomp_lines(istream):
                yield line
        except UnicodeDecodeError:
            print('warning:', file + ':', 'binary file', file=stderr)
        

def chomp_files(files):
    for file in files:
        yield from chomp_dir(file) if isdir(file) else chomp_file(file)


def chomp_lines(istream):
    """
    Returns a lazy generator of lines without trailing newline characters from
    the specified input stream.
    """
    return (line.rstrip('\n\r') for line in istream)


def main():
    args = parse_args()
    lines = chomp_files(args.files) if args.files else chomp_lines(stdin)

    # Never do a full sort if we only want one line.
    if args.__dict__['1']:
        if args.r:
            lines = (max(lines, default=None, key=len),)
        elif args.s:
            lines = (min(lines, default=None, key=len),)
        else:
            lines = islice(lines, 1)

    elif args.r:
        lines = sorted(lines, key=len, reverse=True)
    elif args.s:
        lines = sorted(lines, key=len)

    print_lines(lines)


def parse_args():
    parser = ArgumentParser(
            description='Print line lengths.',
            usage='%(prog)s [-h] [-1rs] [FILE...]')
    parser.add_argument(
            '-1',
            action='store_true',
            help='print only the first line of output')
    parser.add_argument(
            '-r',
            action='store_true',
            help='sort lines by decreasing length')
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
        print(len(line), line, sep=':')


if __name__ == '__main__':
    main()
