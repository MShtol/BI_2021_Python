# Maybe, I should've used argparse and optimize and compactize all checks.
# Using custom Class whole task could be written with much more elegance
import os


def main(input_fastq, output_file_prefix, gc_bounds=(0, 100),
         length_bounds=(0, 2 ** 32), quality_threshold=0,
         save_filtered=False):
    fastq_file = open(input_fastq, 'r')  # Not a good practice
    if save_filtered is False:
        out = open(output_file_prefix+'.fastq', 'w')
    else:
        out = open(output_file_prefix+'_passed.fastq', 'w')
        out2 = open(output_file_prefix+'_failed.fastq', 'w')
    while True:
        read = pull_read(fastq_file)
        if len(read[0]) == 0:
            break
        info, seq, _, qual = read
        read_gc = gc_count(seq)
        read_len = int(info.split('=')[-1])
        read_qual = mean_qual(qual)
        if ((gc_bounds[0] <= read_gc <= gc_bounds[1])
                & (length_bounds[0] <= read_len <= length_bounds[1])
                & (read_qual > quality_threshold)):
            [out.write(i+'\n') for i in read]
        elif save_filtered is True:
            [out2.write(i+'\n') for i in read]

    fastq_file.close()
    out.close()
    if save_filtered is True:
        out2.close()


# Count GC comtent for read
def gc_count(seq):
    """This function counts G and C in the given sequence
    :param str seq: striing of nucleic acid sequence
    :returns: percentage of G and C nucleotides
    :rtype: float
    """
    return (seq.count('G')+seq.count('C'))/len(seq)*100


# Read read from file
def pull_read(fastq_file):
    """This funtion reads one chunk of fastq file
    :param _io.TextIOWrapper fastq_file: file with fastq records
    :returns: list of 4 strings for 1 fastq record
    :rtype: list(str)
    """

    return [fastq_file.readline().strip() for i in range(4)]


# calculate mean  quality
def mean_qual(qual):
    """Calculates average quality of fastq record
    :param str qual: string with qualities of reading for corresponding nucleotides
    :returns: avearge quality of record
    :rtype: float
    """
    return sum([ord(i) for i in qual])/len(qual)-33


# Conditions for adding boundaries from input to kwargs
def add_gc_bound():
    """This function updates global dictionary of parameters with certain
    gc_bounds
    """
    global gc_bounds  # Not a good practice
    if len(gc_bounds) == 0:
        print('Default kept')
    elif len(gc_bounds) == 1:
        try:
            gc_bounds = [0, float(gc_bounds[0])]
            if 0 <= gc_bounds[1]:
                kwargs['gc_bounds'] = gc_bounds
            else:
                print("Very wrong numbers! Default kept")
        except Exception:
            print("Strange input, default kept")
    elif len(gc_bounds) == 2:
        try:
            gc_bounds = [float(i) for i in gc_bounds]
            if 0 <= gc_bounds[0] <= gc_bounds[1]:
                kwargs['gc_bounds'] = gc_bounds
            else:
                print("Very wrong numbers! Default kept")
        except Exception:
            print("Strange input, default kept")
    else:
        print("Strange input, default kept")


def add_len_bound():
    """This function adds lenght bounds to global dictionary of parameters"""
    global length_bounds  # Not a good practice
    if len(length_bounds) == 0:
        print('Default kept')
    elif len(length_bounds) == 1:
        try:
            length_bounds = [0, int(length_bounds[0])]
            if 0 <= length_bounds[1]:
                kwargs['length_bounds'] = length_bounds
            else:
                print("Very wrong numbers! Default kept")
        except Exception:
            print("Strange input, default kept")
    elif len(length_bounds) == 2:
        try:
            length_bounds = [int(i) for i in length_bounds]
            if 0 <= length_bounds[0] <= length_bounds[1]:
                kwargs['length_bounds'] = length_bounds
            else:
                print("Very wrong numbers! Default kept")
        except Exception:
            print("Strange input, default kept")
    else:
        print("Strange input, default kept")


def add_qual_threshhold():
    """This function adds quality threshold for reads to global
    dictionary of params
    """
    global quality_threshold
    try:
        kwargs['quality_threshold'] = int(quality_threshold)
    except Exception:
        print("Strange input, default kept")


if __name__ == '__main__':
    kwargs = {}
#     passing input path
    input_fastq = input('Enter path for input file:  ')
    assert os.path.exists(input_fastq), "No such file at, "+input_fastq
#     passing output path prefix
    output_file_prefix = input('Enter path prefix for output file:  ')
    path_dir = os.path.dirname(output_file_prefix)
    if len(path_dir) > 0:
        assert os.path.exists(path_dir), 'Wrong dirs for your output:  '+path_dir
# passing gc_bounds
    gc_bounds = input('Enter boundaries for GC-filtration:  ').split()
    add_gc_bound()
# passing length bounds
    length_bounds = input('Enter length boundaries for sequence:  ').split()
    add_len_bound()
# passing quality threshhold
    quality_threshold = input("Enter quality threshhold:  ").strip()
    add_qual_threshhold()
# Do we want to save filtered off?
    save_filtered = input('Save filtered off (y,n):  ').strip().lower()
    if save_filtered == 'y':
        kwargs['save_filtered'] = True
    else:
        print('Default False kept')
# Finaly, main!
    main(input_fastq, output_file_prefix, **kwargs)
