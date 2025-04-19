#!/usr/bin/env python3

"""
DEPRECATED: Use rust-kart/vimod instead. Aside from the advantages of being
compiled (and thus not being reliant on a Python interpreter from PATH), the
Rust version (unlike this Python version) supports files whose names contain
whitespace.

Opens any modified files from the current Git working copy in ${EDITOR:-vi}.
"""

import os
import subprocess
import sys


def main():
    status: str = subprocess.run(
        ("git", "status"), capture_output=True, check=True, encoding="utf-8"
    ).stdout

    files: tuple[str, ...] = tuple(
        line.split(maxsplit=1)[1]
        for line in status.splitlines()
        if line.startswith("\tmodified:")
    )

    editor: str = os.environ.get("EDITOR", "vi")

    if files:
        sys.exit(subprocess.run((editor, *files)).returncode)

    print("no modified files", file=sys.stderr)


main()
