#!/usr/bin/python
# Simple as a hell - writing current seconds to the file
import sys,time,os
from os.path import expanduser

workspace_name = os.environ.get("XcodeWorkspace", "No workspace")
filename = "~/.timecheck/start_time" + "_" + workspace_name
seconds = int(round(time.time()))
with open (expanduser(filename), 'w') as f: f.write (str(seconds))
