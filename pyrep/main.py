#!/usr/bin/env python
#
# TODO: Factor logging config into pykart-wide package.

"""Runs a Python REPL, in a Poetry environment if available."""

import logging
import os
import subprocess

LOGGING_LEVEL_VAR = "PYKART_LOGGING_LEVEL"
LOGGING_LEVEL_NAMES = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

if level := os.environ.get(LOGGING_LEVEL_VAR):
    if level in LOGGING_LEVEL_NAMES:
        logging.basicConfig(level=getattr(logging, level))
    else:
        try:
            logging.basicConfig(level=int(level))
        except ValueError:
            valid = ", ".join(LOGGING_LEVEL_NAMES + ["or an integer"])
            logging.warning(f"{level}: bad {LOGGING_LEVEL_VAR}; want {valid}")

if subprocess.run(["poetry", "run", "python"]):
    logging.info("venv not found; running system python")
    subprocess.run(["python"])
