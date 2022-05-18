# Constructing Classes in Python

This a homework on Python Classes construction in Institute of Bioinformatics.
All scripts are provided in jupyter notebook format

### Table of content
1. [Create class with constructor and couple of methods](#t1)
2. [Create class RNA with transcription and translation methods](#t2)
3. [Class derived from set()](#t3)
4. [Create Class for stats calculation of fasata files](#t4)

<a name="t1"></a>
### Create class with constructor and couple of methods

Here we create class VideoGame which enhances ancient russian meme abot gane development.
By altering different parameters of wished game you can compose message that briefly describes it.

Object is initialyzed with game name and (optionaly) its genre as two str parameters.

Methods:
* `concept()` - prints final message
* `evaluation()` - prediction of commercial succes of the game
* `set_caravan()` - add caravan robing
* `set_char(characterss)` - sets playable characters (str, list)
* `set_dev(developer)` - sets developer name (str)
* `set_dim(dim_num)` - sets number of dimensions (int, float)
* `set_vill()`- sets villians (str, list)


<a name="t2"></a>
### Create class RNA with transcription and translation methods
Here we create class RNA, which contains rna-sequnce itsekf and can perform translation and reverse transcription.

Object is initialyzed with sequence string.

Methods:
* `translate()` - translates sequence into protein
* `rev_transcript()` - transcrobes sequence into DNA

<a name="t3"></a>
### Class derived from set()
Modification of class `set()` which is initialyzed only with positive numbers from list and only postive numbers are added.

Object is initialyzed with a list of elements. Anything other then positive numbers is dropped. 

Methods:
* `add(element)` - add one element if it's positive number, otherwise - discard.


<a name="t4"></a>
### Create Class for stats calculation of fasta files
Class StatoFasta can calculate a number of stats for fasta file.

Object is initialyzed with a path to the fasta file.

Methods:
* `calc_stat` - calculate  all implemented stats and prints them
* `count_seq` - counts sequnces
* `gc_count` - calculates GC-content
* `len_calc` - calculates length for every sequnce
* `plot_len_dist` - plots distriburion if lengths
* `tetra_distr` - plots tetramer frequencies
* `which_nuc` - determines if sequences are DNA, RNA or somerhing else

