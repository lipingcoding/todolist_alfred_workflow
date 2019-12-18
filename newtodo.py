#!/usr/bin/python
# encoding: utf-8

import sys
import os
import re
from workflow import Workflow3

log = None


def main(wf):
    # The Workflow instance will be passed to the function
    # you call from `Workflow.run`

    # Your imports here if you want to catch import errors
    

    # Get args from Workflow as normalized Unicode

    # if len(wf.args):
		# try:
		# 	arg = re.findall(r'new: (.*)', ''.join(wf.args))[0]
    #   arg = 
		# except IndexError:
		# 	arg = arg if arg != None else ''
    # else:
		# arg = ''
    arg = re.findall(r'new: (.*)', ''.join(wf.args))[0]
    arg = arg + ' @ '
    

    # Do stuff here ...


    # Add an item to Alfred feedback
    wf.add_item(title='Add a new todo', subtitle='task description', valid=True, arg = arg)

    # Send output to Alfred
    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow3()
    # Assign Workflow logger to a global variable for convenience
    log = wf.logger
    sys.exit(wf.run(main))