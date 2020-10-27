# len

Prints line lengths from stdin or specified files.

## Examples

Find the longest line in any of several files:

    $ len -1r *.py
    78:    Returns a lazy generator of lines without trailing newline characters from

Find the longest line in any file under the current directory:

  $ len -1r .
  169:You just won't believe how vastly hugely mind-bogglingly big it is. I mean, you may think it's a long way down the road to the chemist, but that's just peanuts to space.

Find the shortest line in any file under the current directory:

  $ len -1s .
  0:

## Bugs

The length of a line is the number of code points, which don't necessarily map
to terminal columns.  For example, len('á') == 1, but len('á') == 2.
