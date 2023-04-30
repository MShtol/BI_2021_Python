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
    all_files = os.listdir(dir_path)
    if flag:
        return all_files
    else:
        return [file for file in all_files if not file.startswith('.')]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""List information about the FILEs (the current directory by default)""")
    parser.add_argument('-a', '--all', action='store_true', help='do not ignore .* files')
    parser.add_argument('dir_path', help="dir path/name", nargs='?', type=str,
                        default=os.getcwd())
    args = parser.parse_args()
    output = list_content(args.dir_path, args.all)
    sys.stdout.write('\n'.join(output))
