#!/bin/bash
# create a list of files to clear
# use the truncate command to clear the files if they exist.
files="app.log const.log enum.log exception.log interface.log linkproc.log mod.log service.log singleton.log struct.log typedef.log"
for file in $files
do
  if [ -f $file ]; then
    truncate -s 0 $file
    printf "File $file has been cleared\n"
  fi
done
