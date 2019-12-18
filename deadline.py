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
		# 	arg = re.findall(r'(.*)', ''.join(wf.args))[0]
		# except IndexError:
		# 	arg = arg if arg != None else ''
    # else:
		# arg = ''
    arg = wf.args[0]

    # Do stuff here ...


    # Add an item to Alfred feedback
    wf.add_item(title='Deadline', subtitle='day month year, seperated by space', valid=True, arg = arg, icon='icons/deadline.png')

    # Send output to Alfred
    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow3()
    # Assign Workflow logger to a global variable for convenience
    log = wf.logger
    sys.exit(wf.run(main))