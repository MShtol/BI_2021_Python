#!/usr/bin/env python3
import argparse
import sys

def count_lines(file):
    '''
    Function returns number of lines in file.
    Differs from vanilla wc which returns number of \n, apparently.
    '''
    return str(len(file.split('\n')))


def count_words(file):
    '''
    Function counts number of words in file
    '''
    return str(len(file.split()))


def count_bytes(file):
    '''
    Function returns bytesize of a string
    '''
    return str(len(file.encode('utf-8')))


def main(file, flags):
    '''
    Main function which checks flags and executes appropriate functions.
    Order of functions in return - count_lines, count_words, count_bytes.
    '''
    results = []
    if True in flags.values():
        for key, value in flags.items():
            if value:
                results.append(key(file))
    else:
        results = count_lines(file), count_words(file), count_bytes(file)
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enter requiered options for word, byte or line count")
    parser.add_argument('-l', '--lines', action='store_true', help='print the newline counts')
    parser.add_argument('-w', '--words', action='store_true', help='print the word counts')
    parser.add_argument('-c', '--bytes', action='store_true', help='print the byte counts')
    parser.add_argument('file', help="file name", type=argparse.FileType('r', encoding='UTF-8'),
                        default=sys.stdin)
    args = parser.parse_args()
    flags = {count_lines: args.lines, count_words: args.words, count_bytes: args.bytes}
    file = args.file.read()
    output = main(file, flags)
    sys.stdout.write("\t".join(output))
