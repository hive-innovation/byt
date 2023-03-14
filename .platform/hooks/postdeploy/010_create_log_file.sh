#!/bin/bash

if test -f "$DJANGO_LOG_FILE_PATH";
then
  echo "$DJANGO_LOG_FILE_PATH exists"
else
  # create log file
  touch $DJANGO_LOG_FILE_PATH
fi

# set log file owner (we are currently "root", but the app runs as "byt")
chown byt:byt $DJANGO_LOG_FILE_PATH
