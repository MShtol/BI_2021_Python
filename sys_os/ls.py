#!/usr/bin/env python3
import argparse
import sys
import os


def list_content(dir_path, flag):
    '''
    This function returns all files and directories in specified directory.
    @params dir_path - directory of interest
    @params flag - flag which determins if include hidden files
    '''
    os.chdir(dir_path)
    all_files = os.listdir()
    if flag:
        return all_files
    else:
        return [i for i in all_files if not i.startswith('.')]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""List information about the FILEs (the current directory by default)""")
    parser.add_argument('-a', '--all', action='store_true', help='do not ignore .* files')
    parser.add_argument('dir_path', help="dir path/name", nargs='?', type=str,
                        default=os.getcwd())
    args = parser.parse_args()
    output = list_content(args.dir_path, args.all)
    sys.stdout.write(' '.join(output))
