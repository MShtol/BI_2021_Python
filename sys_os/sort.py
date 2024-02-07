#!/usr/bin/env python3
import argparse
import sys

def sort_lines(text):
    """This function sorts stripped input strings
    :param list text: list of strings to sort
    :returns: sorted list of strings
    :rtype: list
    """
    return sorted(text, key=lambda x: x.strip())

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="""List information about the FILEs to sort""")
    parser.add_argument('files', nargs='*', help="files names", type=argparse.FileType('r'),
                        default=sys.stdin) 
    args = parser.parse_args()
    if not isinstance(args.files, list):
        args.files = [args.files]
    text = []
    for file in args.files:
        text.extend(file.readlines())
    output = sort_lines(text)
    sys.stdout.write(''.join(output))