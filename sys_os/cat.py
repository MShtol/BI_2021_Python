#!/usr/bin/env python3
import argparse
import sys

def cat(text):
    """Writes file text to stdout
    :param str text: text of file or stdin
    """
    sys.stdout.write(text)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="""List files for reading.""")
    parser.add_argument('files', nargs='*', help="files names",
                        type=argparse.FileType('r'), default=sys.stdin)
    args = parser.parse_args()
    if not isinstance(args.files, list):
        args.files = [args.files]
    for file in args.files:
        cat(file.read())