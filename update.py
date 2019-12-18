#!/usr/bin/python
# encoding: utf-8

import sys
import os
import re

def update(todo):
    filename = '/Users/king/todolist.md'
    with open(filename) as fin:
        lines = fin.readlines()
    lines = [line.strip() for line in lines]
    if todo[:9] == 'complete:':
        todo = todo[10:]
    elif todo[:7] == 'delete:':
        todo = todo[8:]
    else:
        return
    lines.remove(todo)
    with open(filename, 'w') as fin:
        for line in lines:
            fin.write(line + '\n')