#!/bin/bash
python3 main.py $1


if ! [[ -x "$ (command -v python)"]]
then

    echo 'Error:
    This program runs on Python, but its look like Python is not currently installed.
    to install Python, please refer to https//installpython3.com' >&2
    exit 1
fi

