#!/usr/bin/python
# encoding: utf-8

import sys
import os
import re
from workflow import Workflow3

log = None


def main(wf):

    arg = wf.args[0]
    wf.add_item(title = 'Complete', valid = True, arg = 'complete: ' + arg, icon='icons/todo_complete.png')
    wf.add_item(title = 'Delete', valid = True, arg = 'delete: ' + arg, icon='icons/todo_delete.png')
    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow3()
    # Assign Workflow logger to a global variable for convenience
    log = wf.logger
    sys.exit(wf.run(main))