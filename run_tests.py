#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This script gets every .py unittest module from ./unittests directory and runs
it individually one by one.

Shell script is run inside of python in order to do not waste time with .sh
file permissions management.
"""

import os

os.system(
    """
    for MODULE in `grep -Rl '' unittests/*.py | awk -F'[/.]' '{print $2}'`;
    do python -m unittest -v unittests.$MODULE;
    done
    # python -m unittest -v discover unittests
    """
    )
