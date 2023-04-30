#!/usr/bin/env python3
import argparse
import sys
import os
import shutil


def rm(path, recursive):
    """Deletes files and folders if recursive option is used
    :param str path: path to file/dir
    :param bool recursive: flag for recursive deletion
    """
    if recursive:
        shutil.rmtree(path)
    elif os.path.isdir(path):
        sys.stdout.write(f'rm: cannot remove "{path}": Is a directory')
    else:
        os.remove(path)
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="""List files to remove. Optional -r for recursive""")
    parser.add_argument('-r', '--recursive', action='store_true', help='remove recursively')
    parser.add_argument('paths', nargs='+', help="files names", type=str, default=None) 
    args = parser.parse_args()
    for path in args.paths:
        rm(path, args.recursive)