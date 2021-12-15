#!/usr/bin/env python3

"""This script opens (in Vim) any modified files in the current Git working copy."""

import subprocess as _subprocess, sys as _sys


def main():
    status = _subprocess.run(
        ("git", "status"), capture_output=True, check=True, encoding="utf-8"
    ).stdout

    files = tuple(
        line.split(maxsplit=1)[1]
        for line in status.splitlines()
        if line.startswith("\tmodified:")
    )

    if files:
        _sys.exit(_subprocess.run(("vim", *files)).returncode)

    print("no modified files", file=_sys.stderr)


if __name__ == "__main__":
    main()
