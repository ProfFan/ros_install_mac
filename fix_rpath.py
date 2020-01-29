#!/usr/bin/env python3
import lief, argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("file", help="The library to patch")
parser.add_argument("--rpath", help="The rpath to add", default="/opt/ros/melodic/lib")
args = parser.parse_args()
print("Processing: ", args.file)

mach=lief.parse(args.file)
subprocess.run(f"install_name_tool -add_rpath \"{args.rpath}\" \"{args.file}\"", shell=True)
for i in mach.libraries:
  if not "/" in i.name:
    print(i.name)
    subprocess.run(f"install_name_tool -change \"{i.name}\" \"@rpath/{i.name}\" \"{args.file}\"", shell=True)
