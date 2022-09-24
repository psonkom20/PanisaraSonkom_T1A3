#!/bin/bash
python3 main.py $1


python3 -m pip install cowsay

if ! [[ -x "$ (command -v python)"]]
then
    python_version = "$(python -v 2>&1)"
    if [[python_version == "Python 3"* ]]
    then
        python3 main.py
    else
    echo "Error: Your running an older version of python.
     Please update to a newer version; https://www.python.org/downloads/ " >&2``
    fi
else
    echo 'Error:
    This program runs on Python, but its look like Python is not currently installed.
    to install Python, please refer to https//installpython3.com' >&2
    exit 1
fi

