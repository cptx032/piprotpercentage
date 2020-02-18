#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function, unicode_literals

import sys
import os

OUTDATED_COMMAND = "pip list -o --disable-pip-version-check --no-color"


def get_requirements_libs(filepath):
    with open(filepath) as req_file:
        return [
            i.split("==")[0]
            for i in req_file.read().split("\n")
            if i and ("#" not in i)
        ]


def get_rotten_libs():
    # the first two lines are the headers markers
    output = os.popen(OUTDATED_COMMAND).read()
    return [
        i.split()[0]
        for i in output.split("\n")[2:]
        if i
    ]


def get_rotten_percentage(requirements_path):
    req_libs = set(get_requirements_libs(requirements_path))
    rotten_libs = req_libs.intersection(set(get_rotten_libs()))
    # import ipdb; ipdb.set_trace(context=10)
    return int((len(rotten_libs) / float(len(req_libs))) * 100)

if __name__ == "__main__":
    print(get_rotten_percentage(sys.argv[1]))
