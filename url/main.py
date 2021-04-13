#!/usr/bin/env python3
#
# This script %-encodes or %-decodes a given URL.  Inspired by:
# https://unix.stackexchange.com/a/159254/49952

from sys import argv, exit, stderr
from urllib.parse import quote_plus, unquote_plus

if len(argv) != 3 or argv[1] not in ['encode', 'decode']:
    print('usage: url {encode|decode} <url>', file=stderr)
    exit(2)

command, url = argv[1:]
op = quote_plus if command == 'encode' else unquote_plus

print(op(url))
