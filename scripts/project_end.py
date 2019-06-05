#!/usr/bin/python
# Simly calling pyton to finish the task
import sys,time,os
from os.path import expanduser

workspace_name = os.environ.get("XcodeWorkspace", "No workspace")
filename = "~/.timecheck/start_time" + "_" + workspace_name

line = ""
with open (expanduser(filename), 'r') as f: line = f.readline()
start_time = int(line)
end_time = int(round(time.time()))
diff = end_time - start_time

workspace_name = os.environ.get("XcodeWorkspace", "No workspace")
project_name = os.environ.get("XcodeProjectName", "No project")
activity = os.environ.get("IDEAlertMessage", "No message")
user_name = os.environ.get("USER", "No user")

def shell(command):
	return os.popen(command).read()

model = shell('sysctl -n hw.model').replace(',', '_').replace('\n', '')
cpu_model = shell('sysctl -n machdep.cpu.brand_string').replace('\n', '')

xcode_directory = os.environ.get("XcodeDeveloperDirectory")
xcode_version = shell(xcode_directory + "/usr/bin/xcodebuild -version").replace('\n', ' ')

macos_version = shell("defaults read loginwindow SystemVersionStampAsString").replace('\n', '')

with open (expanduser("~/.timecheck/results.csv"), 'a') as f:
	f.write(
	 workspace_name
	 + "," + project_name
	 + "," + user_name
	 + "," + str(start_time)
	 + "," + str(end_time)
	 + "," + str(diff)
	 + "," + activity
	 + "," + cpu_model
	 + "," + model
	 + "," + xcode_version
	 + "," + macos_version
	 + "\n")

# Upload the results somewhere
