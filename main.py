#!/usr/bin/python
# encoding: utf-8

import sys
import os
import re
from workflow import Workflow3

log = None


def main(wf):


    # Add an item to Alfred feedback
    wf.add_item(title='Add a new todo', subtitle='task description', valid=True, arg='new: ', icon='icons/todo_new.png')
    lines = []
    filename = '/Users/king/todolist.md'
    if os.path.isfile(filename):
        with open(filename) as fin:
            lines = fin.readlines()
    lines = [line.strip() for line in lines]
    # todos = [line.strip().split('@') for line in lines]
    # todos = [todo.append(lines[i]) for i, todo in enumerate(todos)]
    for line in lines:
        wf.add_item(title=line, valid=True, arg=line, icon='icons/todo.png')
    # Send output to Alfred
    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow3()
    # Assign Workflow logger to a global variable for convenience
    log = wf.logger
    sys.exit(wf.run(main))