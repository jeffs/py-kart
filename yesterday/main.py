#!/usr/bin/env python3
#
# Prints yesterday's date, formatted for use as a filesystem relative path.

from datetime import date, timedelta

yesterday = date.today() - timedelta(days=1)
print(yesterday.strftime('%Y/%m/%d'))
