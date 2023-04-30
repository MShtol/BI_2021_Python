# Reverse engineering of basic UNIX utilities

Here you can find reproduction of UNIX utilities in python with use of libraries sys, argparse 


## Download and usage
If you have cloned whole repo with
`git clone git@github.com:MShtol/BI_2021_Python.git`
dont forgey to make all .py files executale
`chmod +x *.py`
To rin script you need to enter path to it. For example:
` ./wc.py <file> <options>`

## List of utilities
* wc  - count lines, words, bytes in file(s) or piped input. with -l, -w and -c options available
* ls  - list files in given path (cwd by deafult). -a option available
* sort - sort lines from file(s) or pipline. No options implemented
* rm - remove file and dirs with -r (recursive) option
* cat - display content of file(s). No options implemented


## Requirements
* Python 3.8
* Linux 20.04
