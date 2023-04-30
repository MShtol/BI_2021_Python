#!/usr/bin/env python3
import argparse
import sys


def count_lines(file):
    '''
    Function returns number of lines in file.
    Differs from vanilla wc which returns number of \n, apparently.
    :param str file: text from analyzed file
    :returns: number of lines
    :rtype: int
    '''
    return len(file.split('\n'))


def count_words(file):
    '''
    Function counts number of words in file
    :param str file: text from analyzed file
    :returns: number of words
    :rtype: int
    '''
    return len(file.split())


def count_bytes(file):
    '''
    Function returns bytesize of a string
    :param str file: text from analyzed file
    :returns: number of bytes
    :rtype: int
    '''
    return len(file.encode('utf-8'))


def main(file, flags):
    '''
    Main function which checks flags and executes appropriate functions.
    Order of functions in return - count_lines, count_words, count_bytes.
    :param IOWrapper file: analyzed file or stdin
    :param dict flags: dictionary of booleans for functions to compute
    :returns: list of results
    :rtype: list
    '''
    results = []
    name, text = file.name, file.read()
    if True in flags.values():
        for key, value in flags.items():
            if value:
                results.append(key(text))
    else:
        results = [count_lines(text), count_words(text), count_bytes(text)]
    if name != '<stdin>':
        results.append(name)
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enter requiered options for word, byte or line count")
    parser.add_argument('-l', '--lines', action='store_true', help='print the newline counts')
    parser.add_argument('-w', '--words', action='store_true', help='print the word counts')
    parser.add_argument('-c', '--bytes', action='store_true', help='print the byte counts')
    parser.add_argument('files', nargs='*', help="files names", type=argparse.FileType('r'),
                        default=sys.stdin)  
        
    args = parser.parse_args()
    if not isinstance(args.files, list):
        args.files = [args.files]
    flags = {count_lines: args.lines, count_words: args.words, count_bytes: args.bytes}
    outputs =[main(file, flags) for file in args.files]
    if len(outputs) > 1:
        outputs.append([sum(i) for i in list(zip(*outputs))[:-1]] + ['total'])
    for output in outputs:
        sys.stdout.write("\t".join([str(i) for i in output])+'\n')
