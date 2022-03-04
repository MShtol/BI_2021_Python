### seq_magic
Script commands are passed on the Do step
exit — exit script
transcribe — transcribe sequence. If it's reverse transcription, corresponding message will be printed
reverse — return reverse sequense
complement — print complement sequense
reverse complement — print reversed compliment sequense

On a Seq step input your sequense

### fastq-filtrator
It's a script to filter read from fastq files by length, quality and GC content
input_fastq - path for the input file

output_file_prefix - prefix for the output file. If save_filtered is False, will create prefix + '.fastq' postfix file. Otherwise will create two files with '_passed.fastq' and '_failed.fastq' postfixes.

gc_bounds - upper or both boundaries for GC-filtration. Pass single value, two values separated by space or no values to keep default.

length_bounds - upper or both boundaries for sequence length. Pass single value, two values separated by space or no values to keep default.

quality_threshold - read with thi value or above will be kept

save_filtered - y/n if you want to have file with filtrated off values

### Functional.py
Some function to explore functional programming in Python.
Contains example of use of map(), filter() in form of their custom modifications

